import json
import os

def convert_folder_to_mmocr_format(input_folder, output_json_path):
    mmocr_data = {
        "metainfo": {
            "dataset_type": "TextRecogDataset",  # 修改为 TextRecogDataset
            "task_name": "textrecog",  # 修改为 textrecog
            "category": [{"id": 0, "name": "text"}]
        },
        "data_list": []
    }

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as f:
                data = json.load(f)

            for item in data['images']:
                mmocr_item = {
                    "img_path": item['file_name'],
                    "height": item['height'],
                    "width": item['width'],
                    "instances": []
                }

                for annotation in item['annotations']:
                    instance = {
                        "bbox": annotation['bbox'],
                        "bbox_label": 0,
                        "polygon": annotation['polygon'],
                        "text": annotation['text'],
                        "ignore": False
                    }
                    mmocr_item["instances"].append(instance)

                mmocr_data["data_list"].append(mmocr_item)

    with open(output_json_path, 'w') as f:
        json.dump(mmocr_data, f, indent=4)

# 示例调用
convert_folder_to_mmocr_format('Z:\\ocr_data\\OCR_DataSet_BASE\\train', 'Z:\\ocr_data\\OCR_DataSet_BASE\\train_annotations.json')
