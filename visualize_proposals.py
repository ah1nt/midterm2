import mmcv
import numpy as np
import torch
from mmengine import Config
from mmdet.apis import init_detector, inference_detector  ,show_result_pyplot

import cv2
import matplotlib.pyplot as plt
from mmdet.registry import VISUALIZERS

# 配置文件和检查点文件路径
config_file = '/Localize/lc/homework/work3/work_dirs/faster_rcnn_r50_fpn_1x_voc0712/faster_rcnn_r50_fpn_1x_voc0712.py'
checkpoint_file = './work_dirs/faster_rcnn_r50_fpn_1x_voc0712/epoch_12.pth'
cfg = Config.fromfile(config_file)
model = init_detector(cfg, checkpoint_file, device='cuda:0')

img_file ='005192.jpg'
img_path = '/Localize/lc/homework/work3/images/'
img = mmcv.imread(img_path+img_file)
out_file=img_path+'result_'+img_file

result = inference_detector(model, img)
# show_result_pyplot(model, img, result, out_file=out_file)

visualizer = VISUALIZERS.build(model.cfg.visualizer)
visualizer.dataset_meta = model.dataset_meta

visualizer.add_datasample(
    'result',
    img,
    data_sample=result,
    draw_gt=False,
    wait_time=0,
    out_file=out_file
)
visualizer.show()
