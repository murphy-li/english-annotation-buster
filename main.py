# -*- coding: utf-8 -*-
from translater import translate
from file_scanner import scan_directory
import decorator
import file_util
import time
import sys
from tqdm import tqdm


def trans(lines):
    """
    翻译字符串
    :param lines: 文件内容
    :return:
    """
    # 翻译结果
    trans_result = ""
    # 待翻译字符串
    waiting_trans_string = ""
    # 状态为0说明在代码行， 状态为1 说明在注释行
    status = 0
    for line in lines:
        # TODO 改成正则匹配
        trans_result += line
        # /** xxxx */的形式 或者是 如果是*/结尾而且当前是注释行
        if (line.lstrip('/*') and line.rstrip().endswith('*/')) or line.rstrip().endswith('*/') and status == 1:
            waiting_trans_string += line
            status = 0
        # 如果是/*开头则说明是注释行或者是当前本身就是注释行
        if line.lstrip().startswith('/*') or status == 1:
            # 如果当前为注释首行
            waiting_trans_string += line
            status = 1
        # 如果当前不是注释行
        elif status == 0:
            # 如果待查询字符串不为空，查询翻译结果
            if len(waiting_trans_string.strip()) != 0:
                # 查看第一行注释缩进的索引
                space_index = waiting_trans_string.index('/')
                # 获得缩进，因为缩进可能是制表符，所以直接保存缩进字符
                space_content = waiting_trans_string[0:space_index]
                # 翻译修饰之后的字符串
                trans_res = translate(decorator.before(waiting_trans_string))
                # 添加修饰之后的翻译结果
                trans_result += decorator.after(trans_res, space_content)
            # 待翻译置为空
            waiting_trans_string = ""
        # 如果不处于以上状态则抛出异常
        else:
            print(status, line)
            raise SystemError("状态错误")
    return trans_result


# 使用此标题进行错误恢复
first_line = "/** Generated by english-annotation-buster, Powered by Google Translate.**/\n"


def buster_english(source_dir):
    # TODO 文件太多，多进程翻译（貌似python多线程就是个渣渣）
    """
    扫描source_dir下所有的文件，然后对这些源码文件进行翻译
    :param source_dir: 项目文件夹
    :return:
    """
    # 扫描文件夹下所有文件
    files = scan_directory(source_dir)
    progress_iter = tqdm(files)
    for file_name in progress_iter:
        # 获得项目内的相对路径
        relative_file_path = file_name.strip(source_dir)
        # 更新进度条
        progress_iter.set_description("正在处理文件{}".format(relative_file_path))
        # 读取文件
        lines = file_util.read_file(file_name)
        # 如果扫描到文件开头是headline，则直接跳过对该文件的处理
        if len(lines) != 0 and lines[0].startswith(first_line):
            continue
        # 获取翻译结果并加上加上头部
        trans_result = first_line + trans(lines)
        # 文件写回
        file_util.write_back(trans_result, file_name)
        # 休眠，谷歌有做限制，但是目前不知道频率是多少
        time.sleep(10)


def print_usage():
    """
    打印使用信息
    """
    print('Usage: python main.py [path to your java source folder]')
    print('\nExamples:')
    print('\tpython main.py C:\\path\\to\\your\\java\\source\\folder')
    print('\tpython main.py /home/user/path/to/your/java/source/folder')


if __name__ == "__main__":
    # 添加对命令行的解析，如果目前用不着可以先注释它
    if len(sys.argv) < 2:
        print_usage()
        exit(1)
    source_directory = sys.argv[1]
    buster_english(source_directory)