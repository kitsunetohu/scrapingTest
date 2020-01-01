from bs4 import BeautifulSoup
import requests
import pprint
import bs4
url="https://play.google.com/store/apps/details?id=com.netease.onmyoji.na&showAllReviews=true"
r = requests.get(url)

r.encoding = r.apparent_encoding  # 转换编码，不然中文会显示乱码，也可以r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')  # 获取爬取网页的BeautifulSoup对象
pprint.pprint(html)
reviews_elms = soup.find_all('div', {'class': 'd15Mdf bAhLNe'})

for x in reviews_elms:
    name=x.find('span',{'class':'X43Kjb'})
    pprint.pprint(name.__dict__)
