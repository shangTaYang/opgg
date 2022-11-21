# 當爬取的網頁為 JavaScript 網頁前端（非伺服器端）生成，需引入 selenium 套件來模擬瀏覽器載入網頁並跑完 JavaScript 程式才能取得資料
# 引入套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time


def translate_leg_name():  # 英雄中英字典
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
    }
    r = "https://home.gamer.com.tw/artwork.php?sn=3330001"
    # r = requests.get(url)
    # soup11 = BeautifulSoup(r.text,'html.parser')
    # a = soup11.find("div","class_=BH-lbox_MSG-list8")
    # print(a.find("div","class_=MSG-list8C"))

    # legal = input("想找誰(英文):")

    # ./chromedriver.exe 為 chrome 瀏覽器驅動引擎檔案位置（注意 MacOS/Linux 沒有 .exe 副檔名），也可以使用絕對路徑，例如： C:\downloads\chromedriver.exe
    driver = webdriver.Chrome('./chromedriver.exe')
    # 發出網路請求
    driver.get(r)

    page_content = driver.page_source

    # 將 HTML 內容轉換成 BeautifulSoup 物件，html.parser 為使用的解析器
    soup = BeautifulSoup(page_content, 'html.parser')

    # 透過 select 使用 CSS 選擇器 選取我們要選的 html 內容
    name = soup.select(
        "tr")
    eng = []
    chi = []
    leg_dic = {}
    for i in name:
        a = i.select("td:nth-child(1) > div > font")
        for eng_name in a:
            eng.append(eng_name.text)

        c = i.select("td:nth-child(2) > div > font")
        for chi_name in c:
            chi.append(chi_name.text)

    chi.pop(17)
    chi.insert(17, "布郎姆")
    chi.pop(14)
    chi.insert(14, "貝爾薇斯")
    for i, e in enumerate(chi):
        leg_dic[e] = eng[i]
    leg_dic.update({"凱莎": "KaiSa", "努努和威朗普": "nunu", "卡力斯": "khazix", "嘉文四世": "jarvaniv",
                    "好運姐": "missfortune", "威寇茲": "velkoz", "寇格魔": "kogmaw", "悟空": "monkeyking",
                    "易大師": "masteryi", "李星": "leesin", "睿娜妲．格萊斯克": "renata", "科加斯": "chogath",
                    "翱銳龍獸": "aurelionsol", "蒙多醫生": "drmundo", "貝爾薇斯": "belveth", "貪啃奇": "tahmkench", "趙信": "xinzhao",
                    "達瑞文": "draven", "雷珂煞": "reksai"})
    return leg_dic
