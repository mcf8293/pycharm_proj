from lxml import etree
import requests
from pprint import pprint
url='https://s.weibo.com/top/summary'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Cookie':'SUB=_2AkMSQxkbf8NxqwFRmPkRyWLiZI9_zwDEieKkH-jAJRMxHRl-yT9kql1StRB6OcM39JFoIb2E70kxZyoN9M9bqd4umn9w; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5qC.zre9vur0ySHJgPzmA6; _s_tentry=passport.weibo.com; Apache=9653302155263.076.1696568882514; SINAGLOBAL=9653302155263.076.1696568882514; ULV=1696568882518:1:1:1:9653302155263.076.1696568882514:'
}
response=requests.get(url=url,headers=headers)
response.encoding='utf8'
homepage=response.text
tree=etree.HTML(homepage)
trs=tree.xpath('//tr[position()>1]')
topics=[]
for tr in trs:
    title=tr.xpath('.//a/text()')[0]
    hot=tr.xpath('.//span/text()')[0]

    content={
      "title":title,
      "hot":hot
    }
    topics.append(content)
pprint(topics)


