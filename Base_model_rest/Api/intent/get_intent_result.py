# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   get_sentiment_result.py
 
@Time    :   2020-01-13 11:19
 
@Desc    :
 
'''
import tensorflow as tf
from copy import deepcopy
from Base_model.intention.intent_classifier import IntentionCLS
from Base_model.utils.time_utils import get_time

intent = IntentionCLS()

intent.set_mode(tf.estimator.ModeKeys.PREDICT)


def get_intention(msg):
    """
    获取ner的结果并做简单处理
    :param msg:
    :return:
    """
    result = []

    model_result = sorted(intent.predict(msg).items(), key=lambda  x:x[1], reverse=True)
    for one in model_result:
        tmp = {'name': one[0], 'confidence': one[1]}
        result.append(tmp)

    return result