#!/bin/bash

# 安装MMDetection和依赖
# pip install openmim
# mim install mmdet


mim train mmdet ./mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_voc0712.py --gpus 4
