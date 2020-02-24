# -*- coding: utf-8 -*-
import html
import  re


def before_trans(waiting_trans):
    """
    在翻译之前将没必要注释符（/**, * , */）删除
    :param waiting_trans: 待翻译队列
    :return:
    """
    no_annotation = waiting_trans.strip().replace('/*', ' ').replace('*/', ' ').\
        replace('*', ' ').replace("\n", ' ').replace("\t", ' ')
    res = ""
    # before 如果为0，则为不可见字符（回车，制表符，空格等），为1则为可见字符
    last = ''
    for char in no_annotation:
        if char == ' ':
            if last == ' ':
                continue
            elif last == '.' or last == ',' or last == ';':
                res += ' '
                last = ' '
            else:
                res += char
                last = char
        else:
            res += char
            last = char
    # HTML 转义字符处理，Google翻译遇到转义字符会报错
    return html.unescape(res)


def after(trans_res, space_content):
    """
    在翻译之后将注释加上必要的注释符（/**, * , */）
    :param trans_res:
    :param space_content:
    :return:
    """
    res = space_content + "/** \n" + space_content + " * " + trans_res
    res = res.replace('，', '，\n' + space_content + ' * ')
    res = res.replace('。', '。 \n' + space_content + ' * ')
    res = res.replace('！', '！ \n' + space_content + ' * ')
    res = res.replace('；', '； \n' + space_content + ' * ')
    # res = head_line
    # for row in re.split('[，。！；]', trans_res):
    #     index = trans_res.rfind(row) + len(row)
    #     res = res + space_content + " * " + row + trans_res[index] +  '\n'
    res = res + space_content + ' */\n'
    return res