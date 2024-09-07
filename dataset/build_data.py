import os

import mmocr

# 加载预训练模型
model = mmocr.models.build_detector(
    config_file='/dwc/01_CTD/02_mmocr_model/configs/textrecog/abinet/abinet_20e_st-an_mj.py',
    checkpoint_file='/dwc/01_CTD/02_mmocr_model/abinet_20e_st-an_mj_20221005_012617-ead8c139.pth'
)
model = mmocr.m

# 指定输入路径
input_path = '/dwc/集装箱数据分类/imagesgaoyao'

# 遍历输入路径下的所有子路径和文件
for root, dirs, files in os.walk(input_path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 检查文件扩展名
            img_path = os.path.join(root, file)
            print(f"Processing image: {img_path}")

            # 进行推理
            result = model.inference(img_path)

            # 显示结果
            mmocr.visualization.show_result(img_path, result, score_thr=0.3)
