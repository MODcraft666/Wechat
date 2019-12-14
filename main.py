from wxpy import *
import load
import os

if os.path.isfile("接龙信息.txt") == False:
    file = open("接龙信息.txt",'w')
    file.write('') 
    file.close()
    print ('检测到无txt文件，已自动为您创建:接龙信息.txt')
# 微信机器人，缓存登录信息
# 如果你需要部署在服务器中，则在下面加入一个入参console_qr=True
# console_qr表示在控制台打出二维码，部署到服务器时需要加上
bot = Bot(cache_path=True)
# 加载配置信息到机器人
load.load_config_to_bot(bot)
"""群功能"""
group = bot.groups().search('测试群')[0]
@bot.register(group,msg_types=TEXT)
def group_msg(msg):
    """接收群消息"""
    msgs = msg.text
    text = msgs.replace('#','',1)
    if '#' in msgs and text!='' and text.isspace() == False :
        # 群接龙回复
        texts = text.strip()
        print('收到接龙，接龙信息：%s' % (texts))
        with open("接龙信息.txt", "a", encoding='utf-8') as f:
            f.write('\n'+str(texts))
            f.close()
        msg.reply('接龙成功')
    elif text == ''or text.isspace():
        msg.reply('接龙信息不能为空')
    else:
        pass

# 堵塞进程，直到结束消息监听 (例如，机器人被登出时)
# embed() 互交模式阻塞，电脑休眠或关闭互交窗口则退出程序
bot.join()