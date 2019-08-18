from bs4 import BeautifulSoup
import requests
import bs4

url="http://www.pythonscraping.com/pages/warandpeace.html"
r = requests.get(url)

r.encoding = r.apparent_encoding  # 转换编码，不然中文会显示乱码，也可以r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')  # 获取爬取网页的BeautifulSoup对象

l=soup.find_all('span',{'class':'green'})
for name in l:
    print(name.get_text())
