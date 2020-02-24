import os


def scan_directory(directory, source_format={'java'}):
    """
    扫描文件夹下所有文件并返回符合source_format格式的文件
    :param directory:
    :param source_format:
    :return:
    """
    res = []
    for relative_path in os.listdir(directory):
        absolute_path = directory + "\\" +relative_path
        if relative_path.startswith("."):
            print("忽略文件夹/文件：", directory + "\\" + relative_path)
            continue
        if os.path.isfile(absolute_path):
            filename, format = relative_path.split('.')
            if format in source_format:
                res.append(absolute_path)
        if os.path.isdir(absolute_path):
            sub_res = scan_directory(absolute_path)
            if len(sub_res) is not 0:
                res.append(sub_res)
    return res


if __name__ == "__main__":
    list = scan_directory(r"C:\Users\17326\Desktop\source\learning\spring-framework-master")
    for file in list:
        print(file)