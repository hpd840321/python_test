import MMOCRInferencer


# 读取模型
inferencer = MMOCRInferencer(det='DBNet', rec='SAR')
# 进行推理并可视化结果
inferencer('Z:\\01_CTD\\01_train_data\\01_sanrong')


