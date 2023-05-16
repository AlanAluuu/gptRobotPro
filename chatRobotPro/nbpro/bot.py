import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


# 调用 nonebot.init() 函数进行初始化。
nonebot.init()


# 调用 driver.register_adapter() 函数注册适配器
# 指定与用户交互的具体协议，这里为OneBot v11 协议
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)


# 加载内置插件与自定义插件
nonebot.load_builtin_plugins("echo")  # 内置插件
nonebot.load_from_toml("pyproject.toml")


if __name__ == "__main__":
    nonebot.run()