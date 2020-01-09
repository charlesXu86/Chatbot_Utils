# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   dingtalkTest.py
 
@Time    :   2019-12-30 11:30
 
@Desc    :
 
'''

from chatbot_help import DingtalkChatbot


# https://oapi.dingtalk.com/robot/send?access_token=255ad4462d1ac10157494e1ac476b2d328bf40afe849befb193f3909805aae01
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=255ad4462d1ac10157494e1ac476b2d328bf40afe849befb193f3909805aae01'

webhook_xiaoben = 'https://oapi.dingtalk.com/robot/send?access_token=f1c01af6f011e3418719344f21e5d82d2a1674b06e1e254d81ba756848b3caaf'


mobile = ['15869035214']
def sendtxtmsg(msg):
    '''
    发送文本消息
    :param msg:
    :return:
    '''
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=876f817aadf8b4a22a94e6ce63fcb41bcfc36274748847512eaa61ad9e2d0454'

    # 初始化
    dtalk = DingtalkChatbot(webhook_xiaoben)
    dtalk.send_text(msg=msg)

# if __name__ == '__main__':
#     msg = '我是小笨，小笨就是我'
#     sendtxtmsg(msg)