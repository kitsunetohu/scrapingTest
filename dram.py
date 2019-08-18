#!/usr/bin/env python
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import xlsxwriter
import os


def GetRoot():
    url = 'https://artv.info/'
    r = requests.get(url)
    r.encoding = r.apparent_encoding  # 转换编码，不然中文会显示乱码，也可以r.encoding = 'utf-8'
    html = r.text
    bs = BeautifulSoup(html, 'html.parser')

    tmpList = bs.find('a', {'href': './ar.html'}).parent.next_siblings
    for sibling in tmpList:
        if sibling.name=='a'and '視聴率' in sibling.string:
            title= sibling.string
            url=sibling.attrs['href']
            title=title[1:]
            print('现在的题目是:',title)
            print('现在的链接是:',url)
            print()

            GetAndSave('https://artv.info/'+url, title, path='./data')


def GetAndSave(url,fileName,path='/data'):
    r = requests.get(url)
    r.encoding = r.apparent_encoding  # 转换编码，不然中文会显示乱码，也可以r.encoding = 'utf-8'
    html = r.text
    bs = BeautifulSoup(html, 'html.parser')
    firstList=[sibling.string for sibling in bs.find('table', {'id': 'simpleArTbl'}).tr]
    print(firstList)
    path=os.path.join(path,fileName+'.xlsx')
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write_row('A1',firstList)
    i=1
    for tr in bs.find('table', {'id': 'simpleArTbl'}).tbody.find_all('tr'):
        i=i+1
        td=tr('td')
        list=[x.string for x in td]
        row='A'+str(i)
        worksheet.write_row(row, list)

        print(list)

    workbook.close()


GetRoot()

