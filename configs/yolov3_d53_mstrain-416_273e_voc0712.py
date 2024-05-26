_base_ = [
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/models/yolov3_d53_mstrain-416.py',
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/datasets/voc0712_1.py',
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/schedules/schedule_273e.py', '/Localize/lc/homework/work3/mmdetection/configs/_base_/default_runtime.py'
]
model = dict(
    bbox_head=dict(
        num_classes=20))
# use PASCAL VOC pre-trained model
# load_from = 'http://download.openmmlab.com/mmdetection/v2.0/voc/yolov3_d53_mstrain-416_273e_voc0712_20201023-556553a8.pth'
