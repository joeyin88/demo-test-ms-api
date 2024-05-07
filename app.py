from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['f0YKBrmFBhTmYWNmDFG0/V/yJUClHKCzM5qwP00oRVPRMZ63I7IQBgp3gLNCYcemsq+3hVG2prLGkwWqut7/wC9Nqa6aU9ULNzDInI0Ft7YWdFtaIFZerzhKog8yJTrgKoeLoCncnuBHL4J9XiM+mAdB04t89/1O/w1cDnyilFU=CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['422a4f0ca756ea2bc4bafac72f10ec74T'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)