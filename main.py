from translater import translate
from file_scanner import scan_directory
import decorator
import file_util


def trans(lines):
    """
    读取和翻译文件
    :param file_name: 文件名
    :return:
    """
    trans_result = ""
    # TODO 字符串是否是不可改变的？
    waiting_trans = ""
    string = ""
    for line in lines:
        string += line
    for line in lines:
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


def i_am_buster(source_dir):
    # TODO 错误恢复，翻译到一半挂了恢复
    # TODO 文件太多，多进程翻译（貌似python多线程就是个渣渣）
    """

    :param source_dir: 项目文件夹
    :return:
    """
    files = scan_directory(source_dir)
    for file_name in files:
        print("开始翻译：" + file_name)
        lines = file_util.read_file(file_name)
        trans_result = trans(lines)
        file_util.write_back(trans_result, file_name)
        print("完成对 " + file_name + " 的翻译")


if __name__ == "__main__":
    i_am_buster(r"C:\Users\17326\Desktop\source\learning\spring-framework-master")
