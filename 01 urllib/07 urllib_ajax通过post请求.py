import urllib.parse
import urllib.request


def create_request(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf8')
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf8")
    return content


def download(content, page):
    with open("kfc" + str(page) + ".json", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(content, page)
