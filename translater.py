# -*- coding: utf-8 -*-
from googletrans import Translator


def translate(source, src='en', dest='zh-cn', service_urls=['translate.google.cn']):
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
    res = translate("Fuck you")
    print(res)