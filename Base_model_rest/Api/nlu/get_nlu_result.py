# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   get_nlu_result.py
 
@Time    :   2020/8/3 2:35 下午
 
@Desc    :   组装nlu结果
 
"""
from copy import deepcopy
from Base_model.cluener.predict_sequence_label import NER_model
from Base_model.utils.time_utils import get_time
import tensorflow as tf
from Base_model.intention.intent_classifier import IntentionCLS

intent = IntentionCLS()

intent.set_mode(tf.estimator.ModeKeys.PREDICT)

ner = NER_model()


def get_nlu(msg):
    """

    :param msg:
    :return:
    """
    result = {
        'intent': {},
        'entities': '',
        'intent_ranking': '',
        'text': ''
    }
    first_intent = {}
    ner_result = {
        "entity": '',
        "value": '',
        "start": '',
        "end": ''
    }
    intent_result = []
    res_ = []
    ner_model_result = ner.predict(msg)
    for k1, v1 in ner_model_result.items():  # k为实体的属性，v为该属性下对应的实体信息，v同时为一个字典，存在同一属性对应多个实体
        ner_result['entity'] = k1

        for k2, v2 in v1.items():
            ner_result['value'] = k2
            ner_result['start'] = v2[0][0]
            ner_result['end'] = v2[0][1]
            res_.append(deepcopy(ner_result))

    time = get_time(msg)
    if time['key']:
        ner_result['entity'] = 'date-time'
        ner_result['value'] = time['key']
        ner_result['date'] = time['date']

        res_.append(deepcopy(ner_result))

    intent_model_result = sorted(intent.predict(msg).items(), key=lambda x: x[1], reverse=True)
    for one in intent_model_result:
        tmp = {'name': one[0], 'confidence': one[1]}
        intent_result.append(tmp)

    result['intent'] = intent_result[0]
    result['entities'] = res_
    result['intent_ranking'] = intent_result
    result['text'] = msg

    return result

