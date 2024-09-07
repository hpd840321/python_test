import os
import json
import shutil
import logging

# 设置日志配置
logging.basicConfig(filename='move_image.log', level=logging.INFO)


def load_image_paths(search_path):
    """加载指定路径下所有图像文件的路径到内存"""
    image_paths = {}
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):  # 可根据需要添加其他图像格式
                image_name = os.path.splitext(file)[0]
                image_paths[image_name] = os.path.join(root, file)
    return image_paths


def move_images_based_on_jsons(json_dir, search_path):
    # 加载所有图像文件路径
    image_paths = load_image_paths(search_path)

    # 获取指定目录下所有 JSON 文件
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    # 输出 JSON 文件清单
    logging.info(f"找到以下 JSON 文件: {json_files}")
    print(f"找到以下 JSON 文件: {json_files}")

    for json_file in json_files:
        json_path = os.path.join(json_dir, json_file)

        # 读取 JSON 文件
        with open(json_path, 'r') as f:
            data = json.load(f)

        # 获取 JSON 文件名（不带扩展名）
        json_file_name = os.path.splitext(json_file)[0]

        logging.info(f"开始查找与 JSON 文件 '{json_file}' 相关的图像文件。")

        # 检查内存中是否存在对应的图像文件
        if json_file_name in image_paths:
            source_path = image_paths[json_file_name]
            destination_path = os.path.join(json_dir, os.path.basename(source_path))
            try:
                shutil.move(source_path, destination_path)
                log_message = f"移动文件: {source_path} 到 {destination_path}"
                print(log_message)
                logging.info(log_message)  # 记录完整的移动路径日志
            except Exception as e:
                error_message = f"无法移动文件 {source_path} 到 {json_dir}: {e}"
                logging.error(error_message)
                print(f"错误: {error_message}")
        else:
            logging.info(f"未找到与 JSON 文件 '{json_file}' 相关的图像文件。")

# 示例调用
# source_dir = r"E:\\OCR训练数据集副本"
# target_dir = r"E:\\OCR训练数据集副本_digit_new"
move_images_based_on_jsons('/dwc/ocr_data/OCR训练数据集副本_digit_new/', '/dwc/ocr_data/OCR训练数据集副本')
