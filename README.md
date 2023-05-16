# gptRobotPro
一个基于调用chatGPT API的聊天机器人
#### **一、Django服务端接口**

运行这个项目首先需要在chatPro\chat\myapp\api.py文件中的openai_secret_key中输入自己的API key。

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/1.png)

这个程序使用requests.post()方法向OpenAI API发出POST请求，并将响应结果以JSON格式解析成Python对象。程序从响应数据中提取出聊天机器人的回复消息，并将其封装到Response对象中返回给客户端。

urls.py中的设置如下

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/2.png)

在终端输入python manage.py runserver开启服务，输入参数msg="hello"，可以看到openai返回了"Hello! How may I assist you today?"

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/3.png)

#### **二、noneBot机器人逻辑**

终端输入nb create创建nonebot项目，选择插件开发者，进行如下操作

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/4.png)

python解释器运行入口文件为bot.py程序运行，代码如下

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/5.png)

在nbpro\env.dev配置监听主机的IP地址与端口等信息

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/6.png)

项目的核心逻辑代码在nbpro\src\plugins\chat\__init__.py中，用户发送以 "chatgpt小助手" 开头的消息，程序会将 "chatgpt小助手" 后面的内容作为参数传给 requestApi 函数，然后获取返回结果并输出到聊天窗口中。

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/7.png)

主要流程如下：使用 Python 的 re 模块进行字符串匹配和提取，即 pattern 变量，用于匹配以 "chatgpt小助手" 开头的字符串，并获取后面的内容。通过 on_command 函数定义了一个名为 chatgpt 的命令。在 handle_function 函数中，首先通过 event.get_plaintext() 获取用户发送的文本消息，然后利用 re 模块中的 match 函数对其进行正则匹配，提取出需要查询的内容。如果匹配失败，则输出错误信息，结束命令处理；如果匹配成功，则调用 requestApi 函数获取数据，并通过 await chatgpt.finish(text) 将结果输出到聊天窗口中。requestApi 函数的作用是向另一个 URL 发送 GET 请求，请求参数为 msg，服务器返回的结果是一个 JSON 格式的字符串，从中提取出 text 字段的值并返回。

终端输入python bot.py运行机器人，可以得到下面的结果

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/8.png)



#### **三、go-http登录QQ账号，监听账号的所有输入，反向代理nonoBot**

命令行直接运行go-cqhttp，得到下面的结果

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/9.png)

修改config.yml文件中的QQ号码，不用输入密码，直接扫码登录即可

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/10.png)
这边的universal的配置改成 ws://127.0.0.1:51736/onebot/v11/，与前面noneBot中的配置主机号、端口号以及协议相匹配，反向代理noneBot

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/11.png)

最后就可以实现qq聊天机器人啦

![Alt text](https://github.com/AlanAluuu/gptRobotPro/blob/main/ScreenShots/12.png)
