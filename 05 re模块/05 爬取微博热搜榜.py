import re
import requests

global url
num = int(input("请输入序号选择:1-热搜榜，2-文娱榜，3-体育榜，4-游戏榜\n"))
if num == 1:
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
elif num == 2:
    url = 'https://s.weibo.com/top/summary?cate=entrank'
elif num == 3:
    url = 'https://s.weibo.com/top/summary?cate=sport'
elif num == 4:
    url = 'https://s.weibo.com/top/summary?cate=game'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie': 'SUB=_2AkMSQxkbf8NxqwFRmPkRyWLiZI9_zwDEieKkH-jAJRMxHRl-yT9kql1StRB6OcM39JFoIb2E70kxZyoN9M9bqd4umn9w; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5qC.zre9vur0ySHJgPzmA6; _s_tentry=passport.weibo.com; Apache=9653302155263.076.1696568882514; SINAGLOBAL=9653302155263.076.1696568882514; ULV=1696568882518:1:1:1:9653302155263.076.1696568882514:'
}
try:
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf8'
    homepage = response.text
    # 获取热搜 re.S不能缺少，因为可以忽略换行符（.匹配所有字符，但是不包括换行符）
    contents = re.findall('<td class="td-02">.*?<a.*?>(.*?)</a>', homepage, re.S)[1:]
    hots = re.findall('<td class="td-02">.*?<span>(.*?)</span>', homepage, re.S)
    weibos = []
    for content, hot in zip(contents, hots):
        sina = {
            "topic": content,
            "hot": hot
        }
        weibos.append(sina)
    print(weibos)
except NameError:
    print("URL输入错误")
except requests.exceptions.ConnectionError:
    print("网络连接出错")
