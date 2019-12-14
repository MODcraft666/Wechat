from wxpy import *


logger = logging.getLogger('itchat')


def load_config_to_bot(bot):
    """加载配置项"""
    bot_status = '机器人登录成功！！！'
    print(bot_status)
    """机器人配置状态"""
    groups = bot.groups().search('测试群')[0]
    bot_config_status = '启用接龙的群：'
    d = bot_config_status + str(groups)
    print(d)
    