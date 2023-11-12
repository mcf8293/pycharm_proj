import urllib.request
from lxml import etree

def create_request(page):
  if page==1:
     url='https://sc.chinaz.com/tupian/qinglvtupian.html'
  else:
     url='https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
  }
  request=urllib.request.Request(url=url, headers=headers)
  return request


def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    # print(content)
    return content


def download(content):
    tree=etree.HTML(content)
    imgs=tree.xpath("/html/body/div[3]/div[2]//img")
    for img in imgs:
        # 列表取出数据需要使用下标
        name=img.xpath("./@alt")[0]
        url="https:"+img.xpath("./@data-original")[0]
        # 下载图片
        urllib.request.urlretrieve(url=url,filename='./pic/'+name+'.jpg')

if __name__ == '__main__':
   start_page=int(input("请输入起始页码:"))
   end_page=int(input("请输入结束页码:"))
   for page in range(start_page, end_page+1):
      # 请求对象的定制
      request=create_request(page)
      # 获取响应内容
      content=get_content(request)
      # 下载
      download(content)

