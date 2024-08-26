# 编码: utf-8
"""
@作者:  xingyu liao
@联系: sherlockliao01@gmail.com
"""

import argparse
import logging
import sys

import numpy as np
import torch
import tqdm
from torch.backends import cudnn

sys.path.append('.')

from fastreid.evaluation.rank import evaluate_rank
from fastreid.config import get_cfg
from fastreid.utils.logger import setup_logger
from fastreid.data import build_reid_test_loader
from predictor import FeatureExtractionDemo
from fastreid.utils.visualizer import Visualizer

# 导入项目中添加的一些模块
# 例如，像下面这样添加部分ReID
# sys.path.append("projects/PartialReID")
# from partialreid import *

# 启用cudnn的基准模式来提升训练性能
cudnn.benchmark = True
# 设置fastreid的日志记录器
setup_logger(name="fastreid")

# 获取日志记录器实例
logger = logging.getLogger('fastreid.visualize_result')


def setup_cfg(args):
    # 从文件和命令行参数中加载配置
    cfg = get_cfg()
    # 添加部分ReID配置 (如果有的话)
    # add_partialreid_config(cfg)
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    return cfg


def get_parser():
    # 定义命令行参数解析器
    parser = argparse.ArgumentParser(description="使用ReID模型提取特征")
    parser.add_argument(
        "--config-file",
        metavar="FILE",
        help="配置文件的路径",
    )
    parser.add_argument(
        '--parallel',
        action='store_true',
        help='是否使用多进程进行特征提取'
    )
    parser.add_argument(
        "--dataset-name",
        help="用于可视化排名列表的测试数据集名称"
    )
    parser.add_argument(
        "--output",
        default="./vis_rank_list",
        help="保存排名列表结果的文件或目录",

    )
    parser.add_argument(
        "--vis-label",
        action='store_true',
        help="是否可视化查询实例的标签"
    )
    parser.add_argument(
        "--num-vis",
        default=1,
        help="要可视化的查询图像数量",
    )
    parser.add_argument(
        "--rank-sort",
        default="ascending",
        help="按AP指标对可视化图像进行排序的顺序",
    )
    parser.add_argument(
        "--label-sort",
        default="ascending",
        help="按余弦相似性指标对可视化图像进行排序的顺序",
    )
    parser.add_argument(
        "--max-rank",
        default=10,
        help="要可视化的最大排名列表数",
    )
    parser.add_argument(
        "--opts",
        help="使用命令行'KEY VALUE'对来修改配置选项",
        default=[],
        nargs=argparse.REMAINDER,
    )
    return parser


if __name__ == '__main__':
    # 解析命令行参数
    args = get_parser().parse_args()
    # 设置配置
    cfg = setup_cfg(args)
    # 构建ReID测试数据加载器
    test_loader, num_query = build_reid_test_loader(cfg, dataset_name=args.dataset_name)

    print (" num_query ========> ",num_query)

    # 创建特征提取示例对象
    demo = FeatureExtractionDemo(cfg, parallel=args.parallel)

    logger.info("开始提取图像特征")
    feats = []
    pids = []
    camids = []

    # 使用进度条对加载器中的图像进行特征提取
    for (feat, pid, camid) in tqdm.tqdm(demo.run_on_loader(test_loader), total=len(test_loader)):
        feats.append(feat)
        pids.extend(pid)
        camids.extend(camid)

    # 将特征拼接为一个大的特征矩阵
    feats = torch.cat(feats, dim=0)
    
    q_feat = feats[:num_query]  # 查询图像的特征
    g_feat = feats[num_query:]  # 画廊图像的特征
    q_pids = np.asarray(pids[:num_query])  # 查询图像的身份ID
    g_pids = np.asarray(pids[num_query:])  # 画廊图像的身份ID
    q_camids = np.asarray(camids[:num_query])  # 查询图像的摄像头ID
    g_camids = np.asarray(camids[num_query:])  # 画廊图像的摄像头ID

    # 计算余弦距离矩阵
    distmat = 1 - torch.mm(q_feat, g_feat.t())
    distmat = distmat.numpy()

    logger.info("正在为所有查询图像计算AP ...")
    # 评估排名结果
    cmc, all_ap, all_inp = evaluate_rank(distmat, q_pids, g_pids, q_camids, g_camids)
    logger.info("完成所有查询图像的AP计算！")

    # 初始化可视化工具
    visualizer = Visualizer(test_loader.dataset)
    # 获取模型输出的可视化结果
    visualizer.get_model_output(all_ap, distmat, q_pids, g_pids, q_camids, g_camids)

    logger.info("开始保存ROC曲线 ...")
    # 可视化ROC曲线并保存
    fpr, tpr, pos, neg = visualizer.vis_roc_curve(args.output)
    visualizer.save_roc_info(args.output, fpr, tpr, pos, neg)
    logger.info("完成ROC曲线的保存！")

    logger.info("正在保存排名列表结果 ...")
    # 可视化排名列表并保存
    query_indices = visualizer.vis_rank_list(args.output, args.vis_label, args.num_vis,
                                             args.rank_sort, args.label_sort, args.max_rank)
    logger.info("完成排名列表结果的保存！")
