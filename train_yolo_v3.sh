#!/bin/bash

# 安装MMDetection和依赖
# pip install openmim
# mim install mmdet

# 训练YOLO V3
mim train mmdet ./mmdetection/configs/yolo/yolov3_d53_mstrain-416_273e_voc0712.py --gpus 4
