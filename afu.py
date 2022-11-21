import tkinter as tk

import requests
from bs4 import BeautifulSoup

from excel_translate_name import translate_leg_name


def plus():  # 主呼叫程式，輸入並按下BUTTON後執行
    leg_name = []
    leg = translate_leg_name()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37', 'Accept-Language': 'zh-TW'
    }
    url = f"https://tw.op.gg/modes/urf"
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    leg_chi_name = soup.select(".css-ds3kc ")
    for i in leg_chi_name:
        leg_name.append(i.select("strong")[0].text)  # 中文名
    # leg_name = 英雄list
    input_leg_name = name.get()  # 輸入的值
    t = 0
    for i in leg_name:
        if input_leg_name in i:  # 如果輸入的值有在完整英雄明裡
            # print(i, leg[i])  # 印出完整英雄中文名，對應到的英文名
            tis = tk.Entry(window)
            tis.place(x=38, y=70+t,
                      width=120,
                      height=30)
            tis.insert(2, i)
            t += 30
            get_inf(leg[i])  # 利用英文名進行爬蟲
            # print("")


def cls():
    name.delete(0, 'end')


def get_inf(name):  # 利用英文名進行爬蟲，回傳貼上福文
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37', 'Accept-Language': 'zh-TW'
    }
    url = f"https://www.op.gg/modes/urf/{name}/build"
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    row_data = []

    big_con = soup.select(
        ".item_mark img")[0]["alt"]  # 左主1

    small_con1 = soup.select(".css-1kvgh2t img")[0]["alt"]  # 左主2
    row_data.append("------主符文------")
    row_data.append(big_con)
    row_data.append(small_con1)

    small_con2 = soup.select(".css-1x2xypo img")  # [0]["alt"]  #左下3
    bra = 0
    for i in small_con2:
        if bra < 3:
            small_con2 = i["alt"]
            row_data.append(small_con2)
            bra += 1
        elif bra == 3:
            row_data.append("------副符文------")
            big_con2 = soup.select(
                ".item_mark img")[1]["alt"]  # 中上
            row_data.append(big_con2)
            small_con2 = i["alt"]
            row_data.append(small_con2)
            bra += 1
        else:
            small_con2 = i["alt"]
            row_data.append(small_con2)
    row_data.append("------附加------")
    for i in range(2, 5):  # 右3
        small_con3 = soup.select(
            f"#content-container > main > div.css-1qtfvu5.e1fry64k0 > div:nth-child(2) > div > div > div > div > div > div.css-1ooi192.e1gtrici3 > div:nth-child({i}) >div")
        for i, e in enumerate(small_con3):
            if e.select(".css-1tnxdkh"):
                small_con3_3_1 = i+1
                row_data.append(small_con3_3_1)
    fuwon = {"精準": "1_精準", "強攻": "1_強攻", "致命節奏": "2_致命節奏",
             "瞬疾步法": "3_瞬疾步法", "征服者": "4_征服者", "超量治癒": "1_超量治癒", "凱旋": "2_凱旋", "氣定神閒": "3_氣定神閒",
             "傳奇：敏捷": "1_傳奇：敏捷", "傳奇：韌性": "2_傳奇：韌性", "傳奇：血脈": "3_傳奇：血脈", "致命一擊": "1_致命一擊",
             "斬殺": "2_斬殺", "背水一戰": "3_背水一戰",

             "征服": "2_征服", "死亡電刑": "1_死亡電刑", "掠食者": "2_掠食者",
             "靈魂收割": "3_靈魂收割", "刀鋒之雹": "4_刀鋒之雹", "凌虐": "1_凌虐", "血噬": "2_血噬", "即刻衝擊": "3_即刻衝擊",
             "殭屍守衛": "1_殭屍守衛", "幽靈普羅": "2_幽靈普羅", "眼球收集器": "3_眼球收集器", "寶藏獵人": "1_寶藏獵人",
             "狡詐獵人": "2_狡詐獵人", "殘虐獵人": "3_殘虐獵人", "終焉獵人": "4_終焉獵人",

             "巫術": "3_巫術", "召喚艾莉": "1_召喚艾莉", "奧術彗星": "2_奧術彗星",
             "相位衝擊": "3_相位衝擊", "除魔晶球": "1_除魔晶球", "附魔之帶": "2_附魔之帶", "光輝披風": "3_光輝披風",
             "卓越": "1_卓越", "迅捷": "2_迅捷", "絕對專注": "3_絕對專注", "焦灼": "1_焦灼",
             "水行者": "2_水行者", "暴風凝聚": "3_暴風凝聚",

             "意志": "4_意志", "不死之握": "1_不死之握", "神聖守護": "3_神聖守護",
             "裂地衝擊": "2_裂地衝擊", "盾擊": "3_盾擊", "爆破": "1_爆破", "生命之泉": "2_生命之泉",
             "骨甲": "3_骨甲", "堅毅": "3_堅毅", "調節": "1_調節", "過度生長": "1_過度生長",
             "甦醒": "2_甦醒", "回春": "2_回春",

             "啟示": "5_啟示", "冰川增幅": "1_冰川增幅", "啟封法書": "2_啟封法書",
             "先發制人": "3_先發制人", "海克斯充能閃現": "1_海克斯充能閃現", "魔法靈靴": "2_魔法靈靴", "完美計時": "3_完美計時",
             "乾糧快遞": "3_乾糧快遞", "未來市集": "1_未來市集", "小兵去質器": "2_小兵去質器", "銀河視界": "1_銀河視界",
             "斗轉星移": "2_斗轉星移", "時間扭曲藥水": "3_時間扭曲藥水", 1: 1, 2: 2, 3: 3, "------副符文------": "------副符文------",
             "------主符文------": "------主符文------", "------附加------": "------附加------"}
    c = []
    for i in row_data:
        if i in fuwon:
            c.append(fuwon[i])
    # print(c)
    for i, e in enumerate(c):
        tk.Label(window, text=e, font=('Arial', 12, 'bold')).place(
            x=200, y=i*25)  # font=('Arial', 12, 'bold'),fg='#f00'

        # print(end)


    # print(row_data)
window = tk.Tk()
window.title("OPGG速查器")
window.geometry("350x350")
window.resizable(False, False)  # 是否可調整視窗

# 文本
label1 = tk.Label(window,
                  text='副符文為3選2\n\n再請留意\n\n如有重複名稱\n\n符文顯示為\n\n最後一位英雄', font=('Arial', 12, 'bold'))  # font=('Arial', 12, 'bold'),fg='#f00'
label1.place(x=42, y=130)


# 輸入處
name = tk.Entry(window)
name.insert(2, "輸入英雄名稱")
name.place(x=38, y=0,
           width=120,
           height=40)


# 按鈕
search = tk.Button(window, text="查詢", command=plus)
search.place(x=50, y=40,
             width=50,
             height=40)

back = tk.Button(window, text="清空", command=cls)
back.place(x=100, y=40,
           width=50,
           height=40)

window.mainloop()
