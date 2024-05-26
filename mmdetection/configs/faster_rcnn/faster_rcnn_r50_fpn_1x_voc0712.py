_base_ = [
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/schedules/schedule_1x.py', '/Localize/lc/homework/work3/mmdetection/configs/_base_/default_runtime.py',
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/datasets/voc0712_0.py',
    '/Localize/lc/homework/work3/mmdetection/configs/_base_/models/faster-rcnn_r50_fpn.py'

]


model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=20)))
# use PASCAL VOC pre-trained model
# load_from = 'http://download.openmmlab.com/mmdetection/v2.0/voc/faster_rcnn_r50_fpn_1x_voc0712_20201017-38b2e6ce.pth'
