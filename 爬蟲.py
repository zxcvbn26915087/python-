# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:41:15 2021

@author: admin
"""

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import 爬蟲_module as m

pres={
      'profile.default_content_setting_values' : 
          {
              'notifications' : 2
          }
}

opt =webdriver.ChromeOptions()
opt.add_experimental_option('prefs',pres)

browser = webdriver.Chrome(options = opt)

sleep_time = 10
range_start = 80 
range_end = 110

#建立資料夾
m.create_KM_file()

#抓取第一類的網址
list1 = []
list1 = m.get_url('url_km1.txt')

#抓取第二類的網址
list2 = []
list2 = m.get_url('url_km2.txt')

#存入csv之清單
list5 = []

#獲取資料料存取路徑
path_list1,path_list2 = m.get_pathlist()

j=0
header1 = '網址'
for h in range(len(list1)):
    ck = h%3
    for year in range(range_start,range_end) : 
        list3 = []
        if year < 100:
            browser.get(list1[h]+'?SELECT_YEAR=0%d'%year)
        else:
            browser.get(list1[h]+'?SELECT_YEAR=%d'%year)
        bs = BeautifulSoup(browser.page_source,'html.parser')
        if ck == 0:
            try:
                k = bs.find('table').find_all('a')
                for i in range(len(k)):
                    st = k[i]['href']
                    st = header1 + st[2:len(k[i]['href'])]
                    list3.append(st)
                print(h,year,list3)
            except BaseException as error:
                j+=1
                continue
            sleep(sleep_time)
        elif ck == 1:
            try:
               s = bs.find_all('table')
               k = s[1].find_all('a')
               for i in range(len(k)):
                   st = k[i]['href']
                   st = header1 + st[2:len(k[i]['href'])]
                   list3.append(st)
               print(h,year,list3)
            except BaseException as error:
                j+=1
                continue
            sleep(sleep_time)
        else:
            try:
                k = bs.find('table').find_all('a')
                for i in range(len(k)):
                    st = k[i]['href']
                    st = header1 + st[2:len(k[i]['href'])]
                    list3.append(st)
                print(h,year,list3)
            except BaseException as error:
                j+=1
                continue
            sleep(sleep_time)
        
        for item in range(len(list3)):
            m.save_to_folder(list3[item], path_list1[j])
            if m.save_to_folder(list3[item], path_list1[j]) != None:
                list5.append(m.save_to_folder(list3[item], path_list1[j])) 
            sleep(sleep_time)    
        j+=1

j=0
#header可換
header2 = '網址'
for i in range(len(list2)):
    #爬取的網址
    list4 = []
    browser.get(list2[i])
    bs = BeautifulSoup(browser.page_source,'html.parser')
    try:
        s = bs.find_all('table')
        k = s[1].find_all('a')
        for i in range(len(k)):
            st = k[i]['href']
            if st.startswith('java'):
                continue
            else:
                st = header2 + st[5:len(k[i]['href'])]
                list4.append(st)
        print(i,list4)
    except BaseException as error:
        j+=1
        continue
    sleep(sleep_time)
    for item in range(len(list4)):
        m.save_to_folder(list4[item], path_list2[j])
        if m.save_to_folder(list4[item], path_list2[j]) != None:
            list5.append(m.save_to_folder(list4[item], path_list2[j])) 
        sleep(sleep_time)  
    j+=1
    
m.create_csv(list5)
m.del_KM_emp_dir()

