# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   Get_sentiment.py
 
@Time    :   2019-12-11 11:43
 
@Desc    :   获取domain预测的结果
 
'''

import tensorflow as tf
from Base_model.sentiment.sentiment_classifier_v2 import SentimentCLS   # Domain 分类

dc = SentimentCLS()
dc.set_mode(tf.estimator.ModeKeys.PREDICT)


def get_sentiment_res(msg):
    '''

    :param msg:
    :return:
    '''
    resul = {
        'sentiment': ''
         }

    sentiment_result = dc.predict(msg)
    resul['sentiment'] = sentiment_result

    return resul


