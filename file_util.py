def write_back(text, file_name):
    """
    将翻译结果写回文件
    :param text: 翻译结果
    :param file: 文件路径
    :return:
    """
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(text)

def read_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    return file.readlines()