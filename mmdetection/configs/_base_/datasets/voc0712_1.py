
# voc0712.py
dataset_type = 'VOCDataset'
# data_root = 'data/VOCdevkit/'
data_root = '/Localize/lc/homework/work3/data/VOCdevkit/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

# 数据处理流水线
backend_args = None

# train_pipeline = [
#     dict(type='LoadImageFromFile', backend_args=backend_args),
#     dict(type='LoadAnnotations', with_bbox=True),
#     dict(type='Resize', scale=(1000, 600), keep_ratio=True),
#     dict(type='RandomFlip', prob=0.5),
#     dict(type='PackDetInputs')
# ]

# test_pipeline = [
#     dict(type='LoadImageFromFile', backend_args=backend_args),
#     dict(type='Resize', scale=(1000, 600), keep_ratio=True),
#     # avoid bboxes being resized
#     dict(type='LoadAnnotations', with_bbox=True),
#     dict(
#         type='PackDetInputs',
#         meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
#                    'scale_factor'))
# ]

train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(1000, 600), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    # dict(type='Normalize', **img_norm_cfg),
    # dict(type='Pad', size_divisor=32),
    dict(type='PackDetInputs')
]

test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(1000, 600), keep_ratio=True),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='PackDetInputs')
]

train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type='RepeatDataset',
        times=3,
        dataset=dict(
            type=dataset_type,
            data_root=data_root,
            ann_file='VOC2007/ImageSets/Main/trainval.txt',
            data_prefix=dict(sub_data_root='VOC2007/'),
            filter_cfg=dict(
                filter_empty_gt=True, min_size=32, bbox_min_size=32),
            pipeline=train_pipeline,
            backend_args=backend_args)
    )
)

val_dataloader = dict(
    batch_size=8,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='VOC2007/ImageSets/Main/test.txt',
        data_prefix=dict(sub_data_root='VOC2007/'),

        test_mode=True,
        pipeline=test_pipeline)
)

test_dataloader = val_dataloader

# train_dataloader = dict(
#     batch_size=2,
#     num_workers=2,
#     persistent_workers=True,
#     sampler=dict(type='DefaultSampler', shuffle=True),
#     batch_sampler=dict(type='AspectRatioBatchSampler'),
#     dataset=dict(
#         type='RepeatDataset',
#         times=3,
#         dataset=dict(
#             type='ConcatDataset',

#             ignore_keys=['dataset_type'],
#             datasets=[
#                 # dict(
#                 #     type=dataset_type,
#                 #     data_root=data_root,
#                 #     ann_file='VOC2007/ImageSets/Main/trainval.txt',
#                 #     data_prefix=dict(sub_data_root='VOC2007/'),
#                 #     filter_cfg=dict(
#                 #         filter_empty_gt=True, min_size=32, bbox_min_size=32),
#                 #     pipeline=train_pipeline,
#                 #     backend_args=backend_args),
#                 dict(
#                     type=dataset_type,
#                     data_root=data_root,
#                     ann_file='VOC2007/ImageSets/Main/trainval.txt',
#                     data_prefix=dict(sub_data_root='VOC2007/'),
#                     filter_cfg=dict(
#                         filter_empty_gt=True, min_size=32, bbox_min_size=32),
#                     pipeline=train_pipeline,
#                     backend_args=backend_args)
#             ])))

# val_dataloader = dict(
#     batch_size=1,
#     num_workers=2,
#     persistent_workers=True,
#     drop_last=False,
#     sampler=dict(type='DefaultSampler', shuffle=False),
#     dataset=dict(
#         type=dataset_type,
#         data_root=data_root,
#         ann_file='VOC2007/ImageSets/Main/test.txt',
#         data_prefix=dict(sub_data_root='VOC2007/'),
#         test_mode=True,
#         pipeline=test_pipeline,
#         backend_args=backend_args))
# test_dataloader = val_dataloader

# Pascal VOC2007 uses `11points` as default evaluate mode, while PASCAL
# VOC2012 defaults to use 'area'.
val_evaluator = dict(type='VOCMetric', metric='mAP', eval_mode='11points')
test_evaluator = val_evaluator
