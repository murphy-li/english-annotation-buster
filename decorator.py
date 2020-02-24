def before_trans(waiting_trans):
    """
    在翻译之前将没必要注释符（/**, * , */）删除
    :param waiting_trans: 待翻译队列
    :return:
    """
    return waiting_trans.replace('/*', ' ').replace('*/', ' ').replace('*', ' ')


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