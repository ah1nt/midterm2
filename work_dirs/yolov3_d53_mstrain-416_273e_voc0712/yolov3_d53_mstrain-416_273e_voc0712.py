auto_scale_lr = dict(base_batch_size=16, enable=False)
backend_args = None
data_root = '/Localize/lc/homework/work3/data/VOCdevkit/'
dataset_type = 'VOCDataset'
default_hooks = dict(
    checkpoint=dict(interval=1, type='CheckpointHook'),
    logger=dict(interval=50, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'),
    visualization=dict(type='DetVisualizationHook'))
default_scope = 'mmdet'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
img_norm_cfg = dict(
    mean=[
        123.675,
        116.28,
        103.53,
    ],
    std=[
        58.395,
        57.12,
        57.375,
    ],
    to_rgb=True)
launcher = 'none'
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=True, type='LogProcessor', window_size=50)
model = dict(
    backbone=dict(
        depth=53,
        init_cfg=dict(checkpoint='open-mmlab://darknet53', type='Pretrained'),
        out_indices=(
            3,
            4,
            5,
        ),
        type='Darknet'),
    bbox_head=dict(
        anchor_generator=dict(
            base_sizes=[
                [
                    (
                        116,
                        90,
                    ),
                    (
                        156,
                        198,
                    ),
                    (
                        373,
                        326,
                    ),
                ],
                [
                    (
                        30,
                        61,
                    ),
                    (
                        62,
                        45,
                    ),
                    (
                        59,
                        119,
                    ),
                ],
                [
                    (
                        10,
                        13,
                    ),
                    (
                        16,
                        30,
                    ),
                    (
                        33,
                        23,
                    ),
                ],
            ],
            strides=[
                32,
                16,
                8,
            ],
            type='YOLOAnchorGenerator'),
        bbox_coder=dict(type='YOLOBBoxCoder'),
        featmap_strides=[
            32,
            16,
            8,
        ],
        in_channels=[
            512,
            256,
            128,
        ],
        loss_cls=dict(
            loss_weight=1.0, type='CrossEntropyLoss', use_sigmoid=True),
        loss_conf=dict(
            loss_weight=1.0, type='CrossEntropyLoss', use_sigmoid=True),
        loss_wh=dict(loss_weight=2.0, type='MSELoss'),
        loss_xy=dict(
            loss_weight=2.0, type='CrossEntropyLoss', use_sigmoid=True),
        num_classes=20,
        out_channels=[
            1024,
            512,
            256,
        ],
        type='YOLOV3Head'),
    neck=dict(
        in_channels=[
            1024,
            512,
            256,
        ],
        num_scales=3,
        out_channels=[
            512,
            256,
            128,
        ],
        type='YOLOV3Neck'),
    type='YOLOV3')
optim_wrapper = dict(
    optimizer=dict(lr=0.02, momentum=0.9, type='SGD', weight_decay=0.0001),
    type='OptimWrapper')
param_scheduler = [
    dict(
        begin=0, by_epoch=False, end=500, start_factor=0.001, type='LinearLR'),
    dict(
        begin=0,
        by_epoch=True,
        end=20,
        gamma=0.1,
        milestones=[
            16,
            19,
        ],
        type='MultiStepLR'),
]
resume = False
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='VOC2007/ImageSets/Main/test.txt',
        data_prefix=dict(sub_data_root='VOC2007/'),
        data_root='/Localize/lc/homework/work3/data/VOCdevkit/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1000,
                600,
            ), type='Resize'),
            dict(
                mean=[
                    123.675,
                    116.28,
                    103.53,
                ],
                std=[
                    58.395,
                    57.12,
                    57.375,
                ],
                to_rgb=True,
                type='Normalize'),
            dict(size_divisor=32, type='Pad'),
            dict(type='PackDetInputs'),
        ],
        test_mode=True,
        type='VOCDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = dict(eval_mode='11points', metric='mAP', type='VOCMetric')
test_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(keep_ratio=True, scale=(
        1000,
        600,
    ), type='Resize'),
    dict(
        mean=[
            123.675,
            116.28,
            103.53,
        ],
        std=[
            58.395,
            57.12,
            57.375,
        ],
        to_rgb=True,
        type='Normalize'),
    dict(size_divisor=32, type='Pad'),
    dict(type='PackDetInputs'),
]
train_cfg = dict(max_epochs=20, type='EpochBasedTrainLoop', val_interval=1)
train_dataloader = dict(
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    batch_size=2,
    dataset=dict(
        dataset=dict(
            ann_file='VOC2007/ImageSets/Main/trainval.txt',
            backend_args=None,
            data_prefix=dict(sub_data_root='VOC2007/'),
            data_root='/Localize/lc/homework/work3/data/VOCdevkit/',
            filter_cfg=dict(
                bbox_min_size=32, filter_empty_gt=True, min_size=32),
            pipeline=[
                dict(backend_args=None, type='LoadImageFromFile'),
                dict(type='LoadAnnotations', with_bbox=True),
                dict(keep_ratio=True, scale=(
                    1000,
                    600,
                ), type='Resize'),
                dict(prob=0.5, type='RandomFlip'),
                dict(type='PackDetInputs'),
            ],
            type='VOCDataset'),
        times=3,
        type='RepeatDataset'),
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(backend_args=None, type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(keep_ratio=True, scale=(
        1000,
        600,
    ), type='Resize'),
    dict(prob=0.5, type='RandomFlip'),
    dict(type='PackDetInputs'),
]
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=1,
    dataset=dict(
        ann_file='VOC2007/ImageSets/Main/test.txt',
        data_prefix=dict(sub_data_root='VOC2007/'),
        data_root='/Localize/lc/homework/work3/data/VOCdevkit/',
        pipeline=[
            dict(backend_args=None, type='LoadImageFromFile'),
            dict(keep_ratio=True, scale=(
                1000,
                600,
            ), type='Resize'),
            dict(
                mean=[
                    123.675,
                    116.28,
                    103.53,
                ],
                std=[
                    58.395,
                    57.12,
                    57.375,
                ],
                to_rgb=True,
                type='Normalize'),
            dict(size_divisor=32, type='Pad'),
            dict(type='PackDetInputs'),
        ],
        test_mode=True,
        type='VOCDataset'),
    drop_last=False,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = dict(eval_mode='11points', metric='mAP', type='VOCMetric')
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='DetLocalVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work_dirs/yolov3_d53_mstrain-416_273e_voc0712'
