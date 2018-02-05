# coding: utf-8
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re

#メンションされた時
@respond_to('こんにちは')
def mention_func(message):
    message.reply('こんにちは')

#出席登録の発言があった時
@listen_to('^[出][席](?<![1-9,\.])[1-9](?![1-9,\.])')
def listen_func(message):
    text = message.body['text']
    match = re.findall(r'[0-9]',text)
    for m in match:
        text = m
    """
    ここに出席登録の処理
    """
    text = "出席番号"+text+"番で登録しました"
    message.send(text)
