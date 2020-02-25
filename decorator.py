# -*- coding: utf-8 -*-
import html


def before(waiting_trans):
    """
    在翻译之前将没必要注释符（/**, * , */）删除
    :param waiting_trans: 待翻译队列
    :return: 将注释代码处理为正常语句
    """
    # 写暴力一点他不香吗？？
    # 保留回车符，去掉/*，*，*/，制表符，两个、三个、四个空字符转换为一个
    res = waiting_trans.strip().replace('/*', ' ').replace('*/', ' '). \
        replace('*', ' ').replace("\t", ' ').replace("    ", ' ').replace("   ", ' ').replace("  ", ' ').replace("&#64;", '@').replace("&#064;", '@')
    # HTML 转义字符处理，Google翻译遇到转义字符会报错
    return html.unescape(res)


def after(trans_result, indent):
    """
    在翻译之后将注释加上必要的注释符（/**, * , */）
    :param trans_result: 翻译结果
    :param indent: 缩进
    :return: 处理翻译结果之后的注释代码
    """
    trans_result = trans_result.replace('@ ', '@')
    res = indent + '/**\n'
    for line in trans_result.split('\n'):
        res = res + indent + ' * ' + line + '\n'
    res = res + indent + ' */\n'
    res = res.replace("批注", "注解")
    return res
