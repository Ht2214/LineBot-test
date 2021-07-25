from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Di5NEO41V35Jh3N8ZMSrF2Y2t09TpTty6ZY1Yv6ek46HoYMXwaB4UF22lZmpl5GRVabCDIcgK2LULYTPorImGFJTa3TFMxu9NG3auNe0+TkXLZGcP73aJNoM6WMLpoUQy+KtSCmOKJ5gO0eodM046QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('aca9d853dba10ea8706483170ca87f91')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
