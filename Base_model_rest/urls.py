#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: urls.py 
@desc: 接口url
@time: 2019/05/10 
"""


# ===============
#
#   apis 下面的路由
#
# ===============

from django.urls import path

from Base_model_rest.Api.bot.Bot_server import bot_server

from Base_model_rest.Api.ner.NER_server import ner_server
from Base_model_rest.Api.sentiment.Sentiment_cls_server import sentiment_server


urlpatterns = [

    path('chatbot', bot_server), # 多轮对话

    path('cluener', ner_server),

    path('sentiment', sentiment_server)   # 情感分类

]