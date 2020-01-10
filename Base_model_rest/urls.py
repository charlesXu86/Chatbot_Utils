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


urlpatterns = [

    path('chatbot', bot_server), # 多轮对话

]