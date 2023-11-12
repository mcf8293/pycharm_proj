import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download(url):
    resp= requests.get(url)
    homepage=BeautifulSoup(resp.text,"html.parser")
    hrefs=homepage.find("div",class_="list list-squared list-condensed clearfix").find_all("a")
    for a in hrefs:
        with open("a.txt","a",encoding="utf-8") as f:
            f.write(a.text)

if __name__ == '__main__':

    url="https://search.xhsd.com/search?frontCategoryId=41&sort=11"
    with ThreadPoolExecutor(50) as t:
        for i in range(1,100):
          t.submit(download,f"https://search.xhsd.com/search?frontCategoryId=41&sort=11&pageNo={i}")
    print("Download!!!")

