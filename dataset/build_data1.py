import os

import cv2
from mmocr.apis import MMOCRInferencer

# 初始化MMOCRInferencer模型
ocr = MMOCRInferencer(det='DBNet', rec='SAR')

# 指定输入目录和输出目录
input_dir = '/dwc/集装箱数据分类/imagesgaoyao/0.8_0.9/'
output_dir = '/dwc/01_CTD/01_train_data/'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 遍历输入目录中的所有图片文件
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 检查文件扩展名
            img_path = os.path.join(root, file)
            print(f"Processing image: {img_path}")

            # 尝试加载图像并打印其形状
            img = cv2.imread(img_path)
            if img is None:
                print(f"Failed to load image: {img_path}")
            else:
                print(f"Image shape: {img.shape}")

                # 尝试进行缩放操作
                try:
                    resized_img = cv2.resize(img, (640, 480))
                    print(f"Resized image shape: {resized_img.shape}")
                except Exception as e:
                    print(f"Failed to resize image: {img_path}, error: {e}")

                # 进行推理并保存结果
                ocr(img_path, out_dir=output_dir, save_pred=True, save_vis=True)
