一、Chatbot_Utils
==========================

1、Chatbot_Utils是一个Chatbot_CN的一个辅助工程，主要为对话系统服务，同时也可以为其他业务所用。他将对话系统中的基本算法模型包装，并且提
供通用接口，供外部工程调用。

这个工程代替了之前Chatbot_CN下的Chatbot_Model功能，Chatbot_Utils提供的功能有：

    1、拼音汉字互转

    2、文本纠错

    3、NER

    4、句法分析

    5、nlu，nlu部分包括意图识别、

2、该项目结构主要分为三大块：

    *  Chatbot_Utils：项目全局配置

    *  Base_model：主要是模型文件和预测文件

    *  Base_model_rest：接口文件


二、使用
============




三、接口使用示例
======================

1、拼音汉字转换

.. code:: python


详情请参考：`Dingtalk_README <https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst>`_

2、wetalk

.. code:: python



四、Update News
======================

    * 2020.1.7  完成基于Bert fine-tune的有监督的ner识别

    * 2020.1.9  接入微信





五、Resources
======================

.. _`Dingtalk_README`: https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst
