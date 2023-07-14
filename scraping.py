##### モジュールのインポート
from time import sleep
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urljoin

import pdb

session = requests.session()

#WebDriverのオプション設定

options = Options()
options.add_argument('--disable-gpu');
options.add_argument('"--disable-extensions://"');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');

#WebDriver(ブラウザ)の起動
DRIVER_PATH = '/Users\UserName\Desktop\Selenium\chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

# 要素が見つからないときの暗黙的な待機処理
driver.implicitly_wait(10)

sleep(3)
url = 'https://www.eventernote.com/login'
driver.get(url)

print(driver.current_url)

# [email or アカウント名] を入力するフォームであるnameタグ(email)を取得し、elem_usernameに代入する
elem_username = driver.find_element_by_name("email")
#インスタンスの確認
elem_username
#サイトのアカウント名入力フォームにメールアドレスを打ち込む処理
elem_username.send_keys('yourmail')
# passwordを入力するフォームであるnameタグ(password)を取得し、elem_passwordに代入する
elem_password = driver.find_element_by_name('password')
#サイトのパスワード入力フォームにパスワードを打ち込む処理
elem_password.send_keys('your_password')
# 「ログインする」と書いてあるボタンをクリックする準備のため、　class名(btn btn-primary) を取得し、elem_login_btnに代入

elem_login_btn = driver.find_element_by_css_selector('input.btn.btn-primary')
# click()メソッドを使用し、「ログインする」と書いてあるボタンをクリック
sleep(3)
elem_login_btn.click()
# イベント情報のxpath    /html/body/div[1]/div/div/div[3]/ul/li[2]/a
#ログインした後の画面の上部にあるイベント情報をクリックする処理
sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/ul/li[2]/a").click()
#広告を閉じる処理
#<link rel="prefetch" href="https://www.eventernote.com/events/">
sleep(3)
driver.get("https://www.eventernote.com/events/")
#<div id="ad_position_box">

#1/16
import numpy as np
import pdb
import copy

import datetime

#今日の日にち
today_date = datetime.datetime.now()
#wile文の中で日にちを加算していく用の日時  （※ to_datetimeで変換したオブジェクトを再代入させると1970年の年時(UNIX時間)になるので再び　datetime.datetime.now()) で今日の日にちを取得）
while_days = datetime.datetime.now()

# print(while_days)

total_data_list = []

while True:
    #今日の日付+x日までの日時を自動検索
    #　　ｘは　timedelta(days=x)　
    if while_days < today_date + datetime.timedelta(days=2):
        
#       print(while_days)

        #年id取得
        elem_year = driver.find_element_by_id('year')
        select_year = Select(elem_year)
        str_year =  str(while_days.year)
        #年入力
        select_year.select_by_value(str_year)
        
        #月id取得
        elem_month = driver.find_element_by_id('month')
        select_month = Select(elem_month)
        str_month =  str(while_days.month)
        #月入力
        select_month.select_by_value(str_month)

        #日id取得
        elem_day = driver.find_element_by_id('day')
        select_day = Select(elem_day)
        str_day =  str(while_days.day)
        
        #日入力
        select_day.select_by_value(str_day)

        #ボタン要素取得
        elem_event_search_btn = driver.find_element_by_css_selector('input.btn.btn-primary')

        #ボタンを押す
        sleep(3)
        elem_event_search_btn.click()
        
    else:
        break
        #page_クローリング＿start
    

    while True:


        html = '''
        <a href=driver.current_url></a>
        '''

        url = driver.current_url

        page = requests.get(url)

        soup = BeautifulSoup(page.text,"html.parser")


        events_all = soup.find_all('div', attrs={'class': 'event'})
        events_all
    
        sleep(3)

        for events in events_all:
            events_data = [x.text for x in events.select('.place')]
            events_data = [s.replace('\n', '') for s in events_data]
            events_data = [s.replace('            会場: ', '') for s in events_data]
            events_data = [s.replace('            会場: ', '') for s in events_data]

            total_data_list.extend(copy.deepcopy(events_data))
#                 pdb.set_trace()

        try:
            next_page_click = driver.find_element_by_class_name('next').find_element_by_tag_name("a")
            sleep(3)
            next_page_click.click()
            #pdb.set_trace()
            
            continue
        except:
            while_days+= datetime.timedelta(days=1)
            break


print(total_data_list)

