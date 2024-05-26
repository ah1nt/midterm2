import mmcv
import matplotlib.pyplot as plt
from PIL import Image
from mmdet.apis import init_detector, inference_detector, show_result_pyplot

# 定义要检测的图片路径
non_voc_images = ['./image1.jpg', './image2.jpg', './image3.jpg']

# 初始化Faster R-CNN模型
config_file_faster_rcnn = './mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_voc0712.py'
checkpoint_file_faster_rcnn = './work_dirs/faster_rcnn_r50_fpn_1x_voc0712/latest.pth'
model_faster_rcnn = init_detector(config_file_faster_rcnn, checkpoint_file_faster_rcnn, device='cuda:0')

# 初始化YOLO V3模型
config_file_yolo = './mmdetection/configs/yolo/yolov3_d53_mstrain-416_273e_voc0712.py'
checkpoint_file_yolo = './work_dirs/yolov3_d53_mstrain-416_273e_voc0712/latest.pth'
model_yolo = init



# import mmcv
# import matplotlib.pyplot as plt
# from PIL import Image
# from mmdet.apis import init_detector, inference_detector, show_result_pyplot

# # 定义要检测的图片路径
# non_voc_images = ['../non_voc_images/image1.jpg', '../non_voc_images/image2.jpg', '../non_voc_images/image3.jpg']

# # 初始化Faster R-CNN模型
# config_file_faster_rcnn = '../mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_voc0712.py'
# checkpoint_file_faster_rcnn = '../mmdetection/work_dirs/faster_rcnn_r50_fpn_1x_voc0712/latest.pth'
# model_faster_rcnn = init_detector(config_file_faster_rcnn, checkpoint_file_faster_rcnn, device='cuda:0')

# # 初始化YOLO V3模型
# config_file_yolo = '../mmdetection/configs/yolo/yolov3_d53_mstrain-416_273e_voc0712.py'
# checkpoint_file_yolo = '../mmdetection/work_dirs/yolov3_d53_mstrain-416_273e_voc0712/latest.pth'
# model_yolo = init_detector(config_file_yolo, checkpoint_file_yolo, device='cuda:0')

# # 可视化比较
# for img_path in non_voc_images:
#     img = mmcv.imread(img_path)

#     # Faster R-CNN 结果
#     result_faster_rcnn = inference_detector(model_faster_rcnn, img)
#     show_result_pyplot(model_faster_rcnn, img, result_faster_rcnn, out_file=f'faster_rcnn_{img_path}.jpg')

#     # YOLO V3 结果
#     result_yolo = inference_detector(model_yolo, img)
#     show_result_pyplot(model_yolo, img, result_yolo, out_file=f'yolo_{img_path}.jpg')

#     # 展示结果
#     fig, axes = plt.subplots(1, 2, figsize=(20, 10))
#     axes[0].imshow(Image.open(f'faster_rcnn_{img_path}.jpg'))
#     axes[0].set_title('Faster R-CNN')

#     axes[1].imshow(Image.open(f'yolo_{img_path}.jpg'))
#     axes[1].set_title('YOLO V3')

#     plt.show()
