import requests
from bs4 import BeautifulSoup
import datetime
import telegram

present = str(datetime.datetime.now())
day = present[:4] + present[5:7] + present[8:10]
req = requests.get("http://maegok.ms.kr/maegok-m/M01030802/list?ymd="+day)
soup = BeautifulSoup(req.text,"html.parser")
tag = soup.find("a",href="/maegok-m/M01030802/list?ymd=" + day)
li = tag.find_all('li')

school_lunch = ""
for i in li:
    school_lunch = school_lunch + i.text + "\n"

Token = "Token"
bot = telegram.Bot(token=Token)

# for i in bot.getUpdates():
#     print(i.message)          ID Check 

bot.send_message(ID,school_lunch)





