import requests
from bs4 import BeautifulSoup


def translate_leg_name():  # 英雄中英字典
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
    }
    url = f"https://home.gamer.com.tw/artwork.php?sn=3330001"  # 巴哈 英雄聯盟角色資料表
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
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
