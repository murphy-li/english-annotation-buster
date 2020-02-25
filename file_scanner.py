# -*- coding: utf-8 -*-
import os


def scan_directory(directory, logging=False, source_format={'java'}):
    """
    扫描文件夹下所有文件并返回符合source_format格式的文件
    :param directory:
    :param logging: 是否打印日志
    :param source_format:
    :return:
    """
    res = []
    for relative_path in os.listdir(directory):
        absolute_path = directory + "\\" + relative_path
        # 忽略隐藏文件
        if relative_path.startswith("."):
            if logging:
                print("忽略文件夹/文件：", directory + "\\" + relative_path)
            continue
        # 忽略测试文件
        if "\\src\\test\\" in absolute_path:
            if logging:
                print("忽略文件夹/文件：", directory + "\\" + relative_path)
            continue
        if os.path.isfile(absolute_path):
            try:
                filename, file_format = relative_path.split('.')
                if file_format in source_format:
                    res.append(absolute_path)
            except ValueError:
                pass
        if os.path.isdir(absolute_path):
            sub_res = scan_directory(absolute_path, source_format=source_format)
            if len(sub_res) is not 0:
                for file in sub_res:
                    res.append(file)
    return res


if __name__ == "__main__":
    list = scan_directory(r"C:\Users\17326\Desktop\source\learning\spring-framework-master")
    for file in list:
        print(file)