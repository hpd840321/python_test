import os
import shutil
import random
from PIL import Image

def split_dataset(src_dir, dest_dir, train_folder='train', val_folder='val', test_folder='test', train_ratio=0.7, val_ratio=0.2):
    image_files = []
    json_files = []

    # 加载图像文件和 JSON 文件名称
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):  # 根据需要添加图像格式
                image_files.append(os.path.join(root, file))  # 存储全路径
            elif file.endswith('.json'):
                json_files.append(os.path.join(root, file))  # 存储全路径

    # 输出图像和 JSON 文件信息
    print("图像文件:", image_files)
    print("JSON 文件:", json_files)

    # 确保目标目录存在
    os.makedirs(dest_dir, exist_ok=True)

    # 移动文件并划分数据集
    for image in image_files:
        json_file = image.replace('.png', '.json').replace('.jpg', '.json').replace('.jpeg', '.json')  # 根据需要修改扩展名
        if json_file in json_files:
            rand_val = random.random()
            if rand_val < train_ratio:  # 70% 训练集
                target_dir = os.path.join(dest_dir, train_folder)
            elif rand_val < train_ratio + val_ratio:  # 20% 验证集
                target_dir = os.path.join(dest_dir, val_folder)
            else:  # 剩余部分为测试集
                target_dir = os.path.join(dest_dir, test_folder)

            os.makedirs(target_dir, exist_ok=True)  # 确保目标目录存在
            shutil.move(image, os.path.join(target_dir, os.path.basename(image)))  # 移动图像
            shutil.move(json_file, os.path.join(target_dir, os.path.basename(json_file)))  # 移动 JSON
        else:
            print(f"未找到对应的 JSON 文件: {json_file}")

if __name__ == "__main__":
    src_directory = "/dwc/ocr_data/OCR训练数据集副本zhengshi"  # 替换为实际源目录路径
    dest_directory = "/dwc/ocr_data/OCR_DataSet_BASE"  # 替换为实际目标目录路径
    split_dataset(src_directory, dest_directory)