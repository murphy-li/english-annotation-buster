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
        replace('*', ' ').replace('\t', ' ').replace('\n', ' ').replace('    ', ' ').\
        replace('  ', ' ').replace("&#64;", '@').replace("&#064;", '@')
    # HTML 转义字符处理，Google翻译遇到转义字符会报错
    return encode_at(html.unescape(res))


def after(trans_result, indent):
    """
    在翻译之后将注释加上必要的注释符（/**, * , */）
    :param trans_result: 翻译结果
    :param indent: 缩进
    :return: 处理翻译结果之后的注释代码
    """
    res = decode_at(trans_result)
    res = indent + '/**\n' + indent + " * " + res
    # res = trans_result.replace('，', '，\n' + indent + ' * ')
    res = res.replace('。', '。 \n' + indent + ' * ')
    res = res.replace('！', '！ \n' + indent + ' * ')
    res = res.replace('；', '； \n' + indent + ' * ')
    res = res.replace('“', '"')
    res = res.replace('”', '"')
    res = res.replace('" ', '"')
    res = res.replace("批注", "注解")
    res = res.replace("@ ", "@")
    for value in enter_set:
        res = res.replace(value, "\n" + indent + " * " + value)
    if not res.endswith('\n'):
        res = res + "\n"
    res = res + indent + ' */\n'
    return res


# 应该不翻译的集合，或许加引号无效
at_set = ['@author', '@see', '@return', '@code', '@link', '@version', '@throws']
# 应该换行的集合
enter_set = ['@return', '@see', '@throws']
def encode_at(string):
    """
    对部分@注解加引号，不让谷歌翻译尝试翻译
    :param string:
    :return:
    """
    for value in at_set:
        string = string.replace(value, '<' + value + '>')
    return string


def decode_at(string):
    """
    以上的反操作
    :param string:
    :return:
    """
    for value in at_set:
        string = string.replace('<' + value + '>',  value + ' ')
        string = string.replace('< ' + value + '>',  value + " ")
    return string
