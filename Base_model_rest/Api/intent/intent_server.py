# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   payback_class_controller.py

@Time    :   2019-06-10 14:44

@Desc    :  还款意愿分类接口封装

'''

from django.http import JsonResponse
import json
import logging
import datetime

from Base_model_rest.Api.intent.get_intent_result import get_intention
from Base_model_rest.Api.utils.LogUtils import Logger    # 打印日志

logger = logging.getLogger(__name__)


def intent_server(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            msg = jsonData["msg"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            result = get_intention(msg)
            dic = {
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic,
                                json_dumps_params={'ensure_ascii':False})
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)