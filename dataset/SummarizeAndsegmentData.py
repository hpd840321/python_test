import os
import shutil

def move_files(src_dir, dest_dir, trash_dir):
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
    # 确保目标和废弃目录存在
    os.makedirs(dest_dir, exist_ok=True)
    os.makedirs(trash_dir, exist_ok=True)
    # 移动文件
    for image in image_files:
        json_file = image.replace('.png', '.json').replace('.jpg', '.json').replace('.jpeg', '.json')  # 根据需要修改扩展名
        if json_file in json_files:
            shutil.move(image, os.path.join(dest_dir, os.path.basename(image)))  # 移动图像
            shutil.move(json_file, os.path.join(dest_dir, os.path.basename(json_file)))  # 移动 JSON
        else:
            shutil.move(image, os.path.join(trash_dir, os.path.basename(image)))  # 移动到废弃目录

# 调用函数
if __name__ == "__main__":
    src_directory = "/dwc/ocr_data/OCR训练数据集副本"  # 替换为实际源目录路径
    dest_directory = "/dwc/ocr_data/OCR训练数据集副本zhengshi"  # 替换为实际目标目录路径
    trash_directory = "/dwc/ocr_data/OCR训练数据集副本feiqi"  # 替换为实际废弃目录路径
    move_files(src_directory, dest_directory, trash_directory)
