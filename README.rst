一、Chatbot_Utils介绍
==========================

    Chatbot_Utils是一个Chatbot_CN的一个辅助工程，主要为对话系统服务，同时也可以为其他业务所用。他将对话系统中的基本算法模型包装，并且提
供通用接口，供外部工程调用。

    这个工程代替了之前Chatbot_CN下的Chatbot_Model功能，Chatbot_Utils提供的功能有：

        1、拼音汉字互转

        2、文本纠错

        3、NER

        4、句法分析


二、使用
============




三、接口使用示例
======================

1、dingtalk

.. code:: python

    import chatbot_help as ch
    from chatbot_help import DingtalkChatbot

    print(ch.__version__)                # 打印版本信息
    dtalk = DingtalkChatbot(webhook)     # 你设置群机器人的时候生成的webhook

详情请参考：`Dingtalk_README <https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst>`_

2、wetalk

.. code:: python



四、Update News
======================

    * 2020.1.7  接入钉钉群，支持主动推送消息、outgoing交互

    * 2020.1.9  接入微信





五、Resources
======================

.. _`Dingtalk_README`: https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst
