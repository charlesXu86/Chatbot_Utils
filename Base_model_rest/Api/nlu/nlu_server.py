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

from Base_model_rest.Api.nlu.get_nlu_result import get_nlu
from Base_model_rest.Api.utils.LogUtils import Logger    # 打印日志

logger = logging.getLogger(__name__)


def nlu_server(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            msg = jsonData["text"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            result = get_nlu(msg)
            dic = {
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(result,
                                json_dumps_params={'ensure_ascii':False})
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)