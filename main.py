from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
from requests import get, post
import os
import random

time1 = datetime.now().strftime('%H:%M')

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = ["oYnjO6uwFCUxabv1khTNgb2-j5g8"]

template_id = ["7RvPipGrMGGeqHSG69vAACZP1xcApiHacKl7oP_xy0k"]


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)
data = {"today": {"value": time1}, "words": {"value": get_words(), "color": get_random_color()}}
res = wm.send_template(user_id[0], template_id[0], data)
print(res)
