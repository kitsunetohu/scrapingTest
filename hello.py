from bs4 import BeautifulSoup
import requests
import bs4

url = 'http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2018.html'
r = requests.get(url)

r.encoding = r.apparent_encoding  # 转换编码，不然中文会显示乱码，也可以r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')  # 获取爬取网页的BeautifulSoup对象

for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
        td = tr('td')
        print(td)
        t = [td[0].string, td[1].string, td[2].string, td[3].string]  # 把每个学校解析出的数据各自装到一个列表中
        print(t)