import sys
import pkgutil
import importlib

def list_submodules(package_name):
    package = importlib.import_module(package_name)
    # 获取包的路径
    package_path = package.__path__
    # 使用pkgutil.iter_modules获取子模块信息
    submodules = pkgutil.iter_modules(package_path)

    for submodule_info in submodules:
        # submodule_info是一个命名元组，包含了模块名、模块路径等信息
        submodule_name = submodule_info.name
        submodule_path = submodule_info.module_finder.find_spec(submodule_name).origin
        print(f"Submodule Name: {submodule_name}, Path: {submodule_path}")

# 替换这里的'package_name'为你想要查看的包的名字
list_submodules('mmocr')