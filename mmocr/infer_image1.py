from pathlib import Path

from PIL import Image
from mmocr.apis import TextDetInferencer, TextRecInferencer


def process_images(image_folder):
    # 创建一个列表来保存所有的图像路径
    image_paths = [str(p) for p in Path(image_folder).rglob('*.*') if p.is_file()]

    # 读取文本检测模型
    det_inferencer = TextDetInferencer(model='DBNet')

    # 读取文本识别模型
    rec_inferencer = TextRecInferencer(model='CRNN')

    ocr = MMOCRInferencer(det='DBNet', rec='SAR')

    # 遍历图像路径并进行推理
    for image_path in image_paths:
        # 文本检测
        det_results = det_inferencer(image_path)

        # 检查是否有 'predictions' 字段，这是新的输出结构的一部分
        if 'predictions' in det_results:
            predictions = det_results['predictions']
        else:
            raise KeyError("Expected 'predictions' field in detection results.")

        # 提取每个框中的文本区域
        cropped_images = []
        for prediction in predictions:
            box = prediction['bbox']
            x1, y1, x2, y2 = box
            cropped_image = Image.open(image_path).crop((x1, y1, x2, y2))
            cropped_images.append(cropped_image)

        # 文本识别
        rec_results = rec_inferencer(cropped_images)

        # 输出结果
        print(f"Results for {image_path}:")
        for i, text in enumerate(rec_results['predictions']):
            print(f"Box {i + 1}: {text}")


# 指定图像文件夹路径
image_folder = '/dwc/集装箱数据分类/imagesgaoyao/0.8_0.9/'

# 调用函数
process_images(image_folder)
