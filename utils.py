import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
channel_access_token = "JewQVuSc9Ii4Rq5Zt5bAHG+GMYHziTEQExy52cEMx1o1uwTUkj2DQjZBsZ4jxf0I31cHeF2mn4VmWFM4+7bW4TEVQFDqhv5z7QU3J+ML2UyEAGN+ShbqKvVytGVlwUSVDv0P6SDmBdas+mWgoX2uWgdB04t89/1O/w1cDnyilFU="

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
