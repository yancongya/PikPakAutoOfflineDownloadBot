# TG机器人的令牌，tg找@BotFather创建机器人即可获取
TOKEN = '8071161435:AAGCHB796q49t1QHLmvJdRp2KqnKvntKTBU'
# TG用户ID，限制发送消息的用户
ADMIN_IDS = ['icongya']
# pikpak账号，可以为手机号、邮箱，支持任意多账号
USER = ["2655283737@qq.com"]
# 账号对应的密码，注意与账号顺序对应！！！
PASSWORD = ["3b4kms7k5YPytn"]
# 自动删除配置，未配置默认开启自动删除，留空即可
AUTO_DELETE = {}
# 以下分别为aria2 RPC的协议（http/https）、host、端口、密钥
ARIA2_HTTPS = False
ARIA2_HOST = "e192.168.31.105"
ARIA2_PORT = "6800"
ARIA2_SECRET = "haoyong"
# aria2下载根目录
ARIA2_DOWNLOAD_PATH = "/mnt/sda1/aria2/pikpak"
# 可以自定义TG API，也可以保持默认
TG_API_URL = 'https://api.telegram.org'

# 自定义Pikpak离线下载路径
PIKPAK_OFFLINE_PATH = "download"