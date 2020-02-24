import html
def before_trans(waiting_trans):
    """
    在翻译之前将没必要注释符（/**, * , */）删除
    :param waiting_trans: 待翻译队列
    :return:
    """
    no_annotation = waiting_trans.replace('/*', ' ').replace('*/', ' ').replace('*', ' ')
    # HTML 转义字符处理，Google翻译遇到转义字符会报错
    return html.unescape(no_annotation)


def after(trans_res, space_content):
    """
    在翻译之后将注释加上必要的注释符（/**, * , */）
    :param trans_res:
    :param space_content:
    :return:
    """
    descorate_res = space_content + "/** \n"
    for index, row in enumerate(trans_res.split('\n')):
        descorate_res = descorate_res + space_content + " * " + row + '\n'
    descorate_res = descorate_res + space_content + ' */\n'
    return descorate_res