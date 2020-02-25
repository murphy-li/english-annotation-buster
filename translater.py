# -*- coding: utf-8 -*-
from googletrans import Translator
import decorator
import re


def translate(string, indent=None):
    """
    对当前字符串进行翻译
    :param string: 待翻译的字符串
    :param indent: 指定缩进，用于递归
    :return:  翻译结果
    """
    # 如果待翻译为空，返回空
    if len(string.strip()) == 0:
        return ""
    # 查看第一行注释缩进的索引
    if indent is None:
        space_index = string.index('/')
        # 获得缩进，因为缩进可能是制表符，所以直接保存缩进字符
        indent = string[0:space_index]
    # 翻译修饰之后的字符串
    string_before_trans = decorator.before(string)
    if len(string_before_trans) > 5000:
        # 匹配到 5000字左右 + 空行，递归处理
        res = re.findall(r"([\s\S]{2000,4999})\n\s*?\n([\s\S]*)", string_before_trans)
        if len(res) == 1:
            return translate(res[0][0], indent=indent) + translate(res[0][1], indent=indent)
        else:
            print(len(res))
            raise SystemError("匹配结果错误")
    trans_res = __translate__(string_before_trans)
    # 添加修饰之后的翻译结果
    return decorator.after(trans_res, indent)


def __translate__(source, src='en', dest='zh-cn', service_urls=['translate.google.cn']):
    """
    翻译机
    :param source:
    :param src:
    :param dest:
    :param service_urls:
    :return:
    """
    translator = Translator(service_urls=service_urls)
    result = translator.translate(source, src=src, dest=dest)
    return result.text


if __name__ == '__main__':
    res = __translate__("Fuck you")
    print(res)