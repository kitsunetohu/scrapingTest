from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text  # 服务器返回响应

soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""

print(soup.prettify())  # 使用prettify()格式化显示输出

print(soup.title)  # 获取html的title标签的信息
print(soup.a)  # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
print(soup.a.name)   # 获取a标签的名字
print(soup.a.parent.name)   # a标签的父标签(上一级标签)的名字
print(soup.a.parent.parent.name)  # a标签的父标签的父标签的名字

print('所有a标签的内容：', soup.find_all('a'))

for x in soup.find_all('a'):
    print(x.string)