from transitions.extensions import GraphMachine

import os 
import sys
import random

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction

from utils import send_text_message
import message_template

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

import urllib3
urllib3.disable_warnings()


load_dotenv()

channel_access_token = "JewQVuSc9Ii4Rq5Zt5bAHG+GMYHziTEQExy52cEMx1o1uwTUkj2DQjZBsZ4jxf0I31cHeF2mn4VmWFM4+7bW4TEVQFDqhv5z7QU3J+ML2UyEAGN+ShbqKvVytGVlwUSVDv0P6SDmBdas+mWgoX2uWgdB04t89/1O/w1cDnyilFU="

def macdonald(url):
    target_url = url
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = []
    for index, data in enumerate(soup.select('img')):
        if index == 20:
            return content

        link = 'https://www.mcdonalds.com' + data['src']
        content.append(link)
    return content

def louisa(url):
    target_url = url
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = []
    for index, data in enumerate(soup.select('div.container div.col-sm-6 img')):
        if index == 20:
            return content

        link = 'https://www.louisacoffee.co' + data['src']
        content.append(link)
    return content

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "menu"

    def is_going_to_class1(self, event):
        text = event.message.text
        return text == "麥當勞"

    def is_going_to_class2(self, event):
        text = event.message.text
        return text == "路易莎"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("open the menu", message)
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_class1(self,event):
        food_url    = 'https://www.mcdonalds.com/tw/zh-tw/full-menu/extra-value-meals.html'
        food_photo = macdonald(food_url)
        p1=random.sample(range(len(food_photo)),1)
        
        drink_url   = 'https://www.mcdonalds.com/tw/zh-tw/full-menu/beverages-and-snacks.html'
        drink_photo = macdonald(drink_url)
        p2=random.sample(range(len(drink_photo)),1)

        Image_Carousel = TemplateSendMessage(
        alt_text='Image_Carousel_Template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url=food_photo[p1[0]],
                action=URITemplateAction(
                    uri=food_url,
                    label="food"
                )
            ),
            ImageCarouselColumn(
                image_url=drink_photo[p2[0]],
                action=URITemplateAction(
                    uri=drink_url,
                    label="snack"
                )
            )
            ]))
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(event.reply_token,Image_Carousel)

    def on_enter_class2(self,event):
        food_url    = 'https://www.louisacoffee.co/products_list/13'
        food_photo = louisa(food_url)
        p1=random.sample(range(len(food_photo)),1)
        
        drink_url   = 'https://www.louisacoffee.co/products_list/12'
        drink_photo = louisa(drink_url)
        p2=random.sample(range(len(drink_photo)),1)

        Image_Carousel = TemplateSendMessage(
        alt_text='Image_Carousel_Template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url=food_photo[p1[0]],
                action=URITemplateAction(
                    uri=food_url,
                    label="food"
                )
            ),
            ImageCarouselColumn(
                image_url=drink_photo[p2[0]],
                action=URITemplateAction(
                    uri=drink_url,
                    label="drink"
                )
            )
            ]))
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(event.reply_token,Image_Carousel)
        
        