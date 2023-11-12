import re,requests
if __name__ == '__main__':
    url='http://36kr.com'
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    }
    response=requests.get(url=url, headers=headers)
    homepage=response.text
    href_list=re.findall(r'<a class="article-item-title weight-bold" href="([^"]+)"',homepage)
    title_list=re.findall(r'<a class="article-item-title weight-bold" href="/p/\d+" target="_blank" sensors_operation_list="page_flow">(.*?)</a>',homepage)
    for href in href_list:
        print(url+href)