from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as  pd
import  numpy as np
import time
driver = webdriver.Chrome()
driver.get('https://anime.nicovideo.jp/ranking/access-weekly.html?from=nanime_rank-access-daily_rank')
time.sleep(4)

pageSourse=driver.page_source
bs=BeautifulSoup(pageSourse,'html.parser')
l=bs.find_all('div',{'class':'rk-top__item__detail-title'})
result=[]

for name in l:
    result.append(name.get_text())
o=bs.find_all('div',{'class':'rk-other__item__detail-title'})

for name in o:
    result.append(name.get_text())

np_data=np.array(result)
save = pd.DataFrame(np_data,columns=['title'])
save.to_csv('D:\\python\\a_modified.csv')
