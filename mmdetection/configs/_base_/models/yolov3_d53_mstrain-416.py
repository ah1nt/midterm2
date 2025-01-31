
model = dict(
    type='YOLOV3',
    backbone=dict(
        type='Darknet',
        depth=53,
        out_indices=(3, 4, 5),
        init_cfg=dict(type='Pretrained', checkpoint='open-mmlab://darknet53')),
    neck=dict(
        type='YOLOV3Neck',
        num_scales=3,   # 确保与 out_indices 长度匹配
        in_channels=[1024, 512, 256],
        out_channels=[512, 256, 128]),
    bbox_head=dict(
        type='YOLOV3Head',
        num_classes=20,
        in_channels=[512, 256, 128],
        out_channels=[1024, 512, 256],
        anchor_generator=dict(
            type='YOLOAnchorGenerator',
            base_sizes=[[(116, 90), (156, 198), (373, 326)],
                        [(30, 61), (62, 45), (59, 119)],
                        [(10, 13), (16, 30), (33, 23)]],
            strides=[32, 16, 8]),
        bbox_coder=dict(type='YOLOBBoxCoder'),
        featmap_strides=[32, 16, 8],


        loss_cls=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0),
        loss_conf=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0),
        loss_xy=dict(type='CrossEntropyLoss', use_sigmoid=True, loss_weight=2.0),
        loss_wh=dict(type='MSELoss', loss_weight=2.0)))

# train_cfg = dict(
#     assigner=dict(
#         type='GridAssigner',
#         pos_iou_thr=0.5,
#         neg_iou_thr=0.5,
#         min_pos_iou=0))

# test_cfg = dict(
#     nms_pre=1000,
#     min_bbox_size=0,
#     score_thr=0.05,
#     conf_thr=0.005,
#     nms=dict(type='nms', iou_threshold=0.45),
#     max_per_img=100)

# dataset_type = 'CocoDataset'
# data_root = 'data/coco/'
# img_norm_cfg = dict(
#     mean=[0, 0, 0], std=[1, 1, 1], to_rgb=True)
# train_pipeline = [
#     dict(type='LoadImageFromFile'),
#     dict(type='LoadAnnotations', with_bbox=True),
#     dict(type='PhotoMetricDistortion'),
#     dict(type='Expand', mean=img_norm_cfg['mean']),
#     dict(type='MinIoURandomCrop'),
#     dict(type='Resize', img_scale=[(320, 320), (416, 416), (608, 608)], keep_ratio=True),
#     dict(type='RandomFlip', flip_ratio=0.5),
#     dict(type='Normalize', **img_norm_cfg),
#     dict(type='Pad', size_divisor=32),
#     dict(type='DefaultFormatBundle'),
#     dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
# ]
# test_pipeline = [
#     dict(type='LoadImageFromFile'),
#     dict(
#         type='MultiScaleFlipAug',
#         img_scale=(416, 416),
#         flip=False,
#         transforms=[
#             dict(type='Resize', keep_ratio=True),
#             dict(type='RandomFlip'),
#             dict(type='Normalize', **img_norm_cfg),
#             dict(type='Pad', size_divisor=32),
#             dict(type='ImageToTensor', keys=['img']),
#             dict(type='Collect', keys=['img']),
#         ])
# ]
# data = dict(
#     samples_per_gpu=8,
#     workers_per_gpu=4,
#     train=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_train2017.json',
#         img_prefix=data_root + 'train2017/',
#         pipeline=train_pipeline),
#     val=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_val2017.json',
#         img_prefix=data_root + 'val2017/',
#         pipeline=test_pipeline),
#     test=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_val2017.json',
#         img_prefix=data_root + 'val2017/',
#         pipeline=test_pipeline))
# evaluation = dict(interval=1, metric=['bbox'])

# optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0005)
# optimizer_config = dict(grad_clip=None)
# lr_config = dict(
#     policy='step',
#     warmup='linear',
#     warmup_iters=1000,
#     warmup_ratio=0.1,
#     step=[16, 22])
# runner = dict(type='EpochBasedRunner', max_epochs=24)
