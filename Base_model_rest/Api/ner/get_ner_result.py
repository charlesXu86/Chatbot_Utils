# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   get_sentiment_result.py
 
@Time    :   2020-01-13 11:19
 
@Desc    :
 
'''
from copy import deepcopy
from Base_model.cluener.predict_sequence_label import NER_model
from Base_model.utils.time_utils import get_time

ner = NER_model()


def get_ner(msg):
    '''
    获取ner的结果并做简单处理
    :param msg:
    :return:
    '''
    result = {
        "entity" : '',
        "value" : '',
        "start" : '',
        "end" : ''
    }
    res_ = []
    model_result = ner.predict(msg)
    for k1, v1 in model_result.items():      # k为实体的属性，v为该属性下对应的实体信息，v同时为一个字典，存在同一属性对应多个实体
        result['entity'] = k1

        for k2, v2 in v1.items():
            result['value'] = k2
            result['start'] = v2[0][0]
            result['end'] = v2[0][1]
            res_.append(deepcopy(result))

    time = get_time(msg)
    if time['key']:
        result['entity'] = 'date-time'
        result['value'] = time['key']
        result['date'] = time['date']

        res_.append(deepcopy(result))

    return res_