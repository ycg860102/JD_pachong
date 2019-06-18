# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:21:58 2019

@author: yangchg
"""

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time,datetime
import os
from pyquery import PyQuery as pq
#from config import settings as SET
import re

#browser_for_login为正常浏览器，用于登录
#browser_for_login = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#无头模式
#browser = webdriver.Chrome(chrome_options=chrome_options)
browser2 = webdriver.Chrome(options=chrome_options)

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)


choice_list=[]
ban_list=[]

browser.get('https://passport.jd.com/new/login.aspx')
while browser.current_url!='https://www.jd.com/':
    print(browser.current_url)
    time.sleep(2)

cookies = browser.get_cookies()
#browser.close()
browser2.get('https://www.jd.com/index-1000002668.html')
for cookie in cookies:
    browser2.add_cookie(cookie)

browser.get('https://mall.jd.com/index-1000002668.html')
clickarea = browser.find_element_by_xpath('//*[@class="J_LayoutWrap d-layout-wrap layout-auto  d-enable "]/div/div/div/div/div/div/div/map/area[4]')

#方法1 直接点解区域
clickarea.click() 

#方法2 发送链接地址
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
href = clickarea.get_attribute('href') 
browser.get(href)

dateLine = datetime.datetime.strptime('20190618 195959','%Y%m%d %H%M%S')


while True :
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if datetime.datetime.now() >= dateLine:
        clickarea.click()
        #browser.get(clickarea.get_attribute('href') )
        
    runtime = (datetime.datetime.now() - dateLine)     
    if runtime.days>=0 and runtime.seconds >10 :
        break
    
    time.sleep(0.1)
    print(now)
    


