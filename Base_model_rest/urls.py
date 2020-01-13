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


urlpatterns = [

    path('wechat_bot', bot_server), # 多轮对话

    path('cluener', ner_server)

]