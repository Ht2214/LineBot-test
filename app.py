from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import urllib.request as req
import bs4
import urllib.parse


app = Flask(__name__)

line_bot_api = LineBotApi('LqpT9ZRYCkihkthoMOE9EroQxrHkLzMd1akokISMcotRbwudTnKI+RzOAGjL61pD6CqXS3JoDU+CL+Eh4Vgh3/gZyWK6RXvAbYLJ/xwawqT7pNoOH2+C7ZZpDK6St+s9awNIBaI4dwEVezNOS70DqQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3cffb42cd89f2d190379032174907bfb')


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


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     if isinstance(event, MessageEvent):  # 如果有訊息事件
#         if event.message.text in ['桃園市', '桃園', '桃園縣',
#                                   'Taoyuan', 'taoyuan', 'Taoyuan City']:
#             area = "桃園市"
#         elif event.message.text in ['台北市', '台北', '臺北市', '臺北',
#                                     'Taipei', 'taipei', 'Taipei City']:
#             area = "台北市"
#         elif event.message.text in ['新北市', '新北']:
#             area = "新北市"
#         elif event.message.text in ['新竹市', '新竹', 'Hsinchu', 'hsinchu']:
#             area = "新竹市"
#         elif event.message.text in ['新竹縣']:
#             area = "新竹縣"
#         elif event.message.text in ['台中市', '台中', '臺中市', '臺中']:
#             area = "台中市"
#         elif event.message.text in ['台南市', '台南', '臺南市', '臺南']:
#             area = "台南市"
#         elif event.message.text in ['台東線', '台東', '臺東市', '臺東']:
#             area = "台東縣"
#         elif event.message.text in ['高雄市', '高雄']:
#             area = "高雄市"
#         elif event.message.text in ['基隆市', '基隆']:
#             area = "基隆市"
#         elif event.message.text in ['宜蘭縣', '宜蘭']:
#             area = "宜蘭縣"
#         elif event.message.text in ['苗栗縣', '苗栗']:
#             area = "苗栗縣"
#         elif event.message.text in ['彰化縣', '彰化']:
#             area = "彰化縣"
#         elif event.message.text in ['嘉義縣', '嘉義']:
#             area = "嘉義縣"
#         elif event.message.text in ['雲林縣', '雲林']:
#             area = "雲林縣"
#         elif event.message.text in ['嘉義市', '嘉義']:
#             area = "嘉義市"
#         elif event.message.text in ['屏東縣', '屏東']:
#             area = "屏東縣"
#         elif event.message.text in ['花蓮縣', '花蓮']:
#             area = "花蓮縣"
#         elif event.message.text in ['南投縣', '南投']:
#             area = "南投縣"
#         elif event.message.text in ['澎湖縣', '澎湖']:
#             area = "澎湖縣"
#         elif event.message.text in ['金門縣', '金門']:
#             area = "金門縣"
#         else:
#             line_bot_api.reply_message(
#                 event.reply_token,
#                 TextSendMessage(text="請輸入台灣縣市名稱，我才能推薦餐廳給你!"))
#         area = urllib.parse.quote(area)
#         url = "https://ifoodie.tw/explore/" + area + "/list?sortby=popular&opening=true"
#         # 建立request物件，附加headers資訊
#         requests = req.Request(url, headers={
#             "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
#                           " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
#                           "91.0.4472.124 Mobile Safari/537.36 Edg/91.0.864.67"
#         })
#         with req.urlopen(requests) as response:
#             data = response.read().decode("utf-8")
#         root = bs4.BeautifulSoup(data, "html.parser")
#
#         # 爬取前五筆餐廳卡片資料
#         cards = root.find_all("div", class_="jsx-3757653001 info-rows", limit=5)
#
#         content = ""
#         for card in cards:
#             name = card.find("a", class_="jsx-3757653001 title-text").getText()  # 餐廳名稱
#             rate = card.find("div", class_="jsx-1207467136 text").getText()  # 餐廳評價
#             address = card.find("div", class_="jsx-3757653001 address-row").getText()  # 餐廳地址
#             content += f"{name} \n{rate}顆星 \n{address} \n\n"
#             # 將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
#
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=content))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    TextSendMessage(text='分享地址讓我們為你推薦餐廳！',
                    quick_reply=QuickReply(items=[
                       QuickReplyButton(action=LocationAction(label="label", text="分享地點")),
                        QuickReplyButton(action=MessageAction(label="label", text="test"))
                   ]))
    # work as the user submit the location message
    if isinstance(event, MessageEvent):
        if event.message.type =="location":
            latitude = event.message.latitude
            longitude = event.message.lontitude
            content = latitude + longitude
            TextMessage(text=content)
        else:
            TextMessage(text="請輸入地址")


if __name__ == "__main__":
    app.run()
