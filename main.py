from translater import translate
from file_scanner import scan_directory
import decorator


def read_trans_file(file_name):
    """
    读取和翻译文件
    :param file_name: 文件名
    :return:
    """
    trans_result = ""
    file = open(file_name, 'r', encoding='utf-8')
    # TODO 字符串是否是不可改变的？
    waiting_trans = ""
    for line in file.readlines():
        # TODO 改成正则匹配
        if line.lstrip().startswith('*') or line.lstrip().startswith('/*') or line.lstrip().startswith('*/'):
            # 添加当前行
            trans_result += line
            waiting_trans += line
        else:
            # 查询翻译结果
            if len(waiting_trans) is not 0:
                # 查看第一行注释开头的空格数, 因为有可能是\t制表符
                space_index = waiting_trans.index('/')
                space_content = waiting_trans[0:space_index]
                deco = decorator.before_trans(waiting_trans)
                trans_res = translate(deco)
                # 添加翻译结果
                trans_result += decorator.after(trans_res, space_content)
            # 添加不用翻译的当前行
            trans_result += line
            # 待翻译置为空
            waiting_trans = ""
    return trans_result


def write_back(text, file_name):
    """
    将翻译结果写回文件
    :param text: 翻译结果
    :param file: 文件路径
    :return:
    """
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(text)


def i_am_buster(source_dir):
    files = scan_directory(source_dir)
    for file_name in files:
        trans_result = read_trans_file(file_name)
        print(trans_result)
        write_back(trans_result, file_name)


if __name__ == "__main__":
    i_am_buster(r"C:\Users\17326\Desktop\source\learning\spring-framework-master")
