# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   Bot_server.py
 
@Time    :   2020-01-08 10:45
 
@Desc    :
 
'''
import requests
from django.http import JsonResponse
import json
from Base_model_rest.Api.bot.dingtalkServer import sendtxtmsg

url = 'http://172.16.19.74:5005/webhooks/rest/webhook'

app_sec = 'T6IGStQoOQQnndequiEz0ovv9ATthuOfeK36T3bRZYnC1uASuTJWIwI6YhPy3aAQ'

def bot_server(request):

    msg = {
        "sender":'',
        "message":''
    }

    if request.method == 'POST':

        for k, v in request.headers.items():       # 这里还需要加一个验证，防止垃圾信息
            print(k, v)

        req_body = request.body

        req_body = json.loads(req_body)

        robot_text = req_body['text']['content']
        conversationId = req_body['conversationId']

        msg['sender'] = conversationId
        msg['message'] = robot_text

        # 请求 Chatbot_RASA对话接口
        response = requests.post(url=url,
                                 json={
                                     "sender" : conversationId,
                                     "message": robot_text
                                 })
        result = json.loads(response.content)
        response_text = result[0]['text']     # 机器人回复的内容

        sendtxtmsg(response_text)
        res = '111'
        dic = {
            "result": res
        }
        return JsonResponse(dic)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)