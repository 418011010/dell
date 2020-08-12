#-*-coding:utf-8-*-
import urllib.request
import re
import random
import datetime
#from dateutil.relativedelta import relativedelta
#import mysql.connector
import sys
from selenium import webdriver  # 导入selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import requests
from requests.cookies import RequestsCookieJar
from requests.auth import HTTPBasicAuth
import json
import os
from bs4 import BeautifulSoup as bs
from join import mixmp3
from MP3play import trans_mp3_to_wav,playwave

url1 = 'http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal'


headers1 = {
  'accept': 'text/plain, */*; q=0.01',
  'accept-encoding': 'gzip, deflate',
  'accept-language': 'zh-CN,zh;q=0.9',
  'content-length': '55',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'JSESSIONID=7DDCCFAB9CAC513A936B85E6149F74FA.tomcat_9005',
  'host': '113.57.169.227:8088',
  'origin': 'http://113.57.169.227:8088',
  'proxy-connection': 'keep-alive',
  'referer': 'http://113.57.169.227:8088/ccps/login.jsp',
  'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; HTC U11 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 YaBrowser/18.6.0.683.00 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}
headers2 = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'accept-encoding': 'gzip, deflate',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cache-control': 'max-age=0',
  'content-length': '38',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'JSESSIONID=7DDCCFAB9CAC513A936B85E6149F74FA.tomcat_9005',
  'host': '113.57.169.227:8088',
  'origin': 'http://113.57.169.227:8088',
  'proxy-connection': 'keep-alive',
  'referer': 'http://113.57.169.227:8088/ccps/login.jsp',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; HTC U11 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 YaBrowser/18.6.0.683.00 Mobile Safari/537.36'
}


# c_service = Service(r'd:\chromedriver.exe')
# c_service.command_line_args()
# c_service.start()


def getcook():
    loginurl = 'http://113.57.169.227:8088/ccps/login.jsp'  # 登录页面
    path = r'd:\chromedriver.exe'
    # 加载webdriver驱动，用于获取登录页面标签属性

    # driver = webdriver.Chrome(r'd:\chromedriver.exe')
    # option = webdriver.ChromeOptions()
    # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # option.add_argument('--headless') #增加无界面选项
    # option.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
    # option.add_experimental_option('excludeSwitches', ['enable-logging'])
    c_service = Service(path)
    c_service.command_line_args()
    c_service.start()

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(executable_path=path, options=chrome_options)
    driver.get(loginurl)  # 请求登录页面
    driver.find_element_by_id('wcode').clear()  # 获取用户名输入框，并先清空
    driver.find_element_by_id('wcode').send_keys(u'WHBK')  # 输入用户名
    driver.find_element_by_id('password').clear()  # 获取密码框，并清空
    driver.find_element_by_id('password').send_keys(u'')  # 输入密码

    #captcha = driver.find_element_by_id('captcha_image')  # 获取验证码标签
    #submit = driver.find_element_by_css_selector('a[name="登录"]')  # 获取提交按钮
    submit = driver.find_element_by_link_text("登录")
    # 判断是否需要验证码
    captcha = []
    if captcha:
        captcha_field = driver.find_element_by_id('captcha_field')  # 获取验证码输入框
        text = input("请输入验证码：")  # 控制栏输入验证码
        captcha_field.send_keys(text)  # 将输入的验证码传递给selenium打开的浏览器
        submit.click()  # 按钮提交并登录
    else:
        submit.click()  # 无验证码则直接登录提交

    cookies = driver.get_cookies()  # 获取COOK

    #driver.get('http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal')  # 请求其他页面
    time.sleep(1)
    driver.quit()
    c_service.stop()
    #print(cookies)
    return cookies  # 返回cookies 之后其他方法可以调用，这样不用每次请求都返回登录


def login():
    '''登录接口:/auth/login'''
    s=requests.Session()
    r=s.post(
      url='http://113.57.169.227:8088/ccps/validateStaff.action',headers=headers1,
      data="staff.wcode=WHBK&staff.alias=WHBK&staff.password=")
    time.sleep(1)
    q=s.post(
      url="http://113.57.169.227:8088/ccps/login.action",headers=headers2,
      data="staff.wcode=WHBK&staff.password=")
    #print(q.text)
    time.sleep(1)
    return s


def get_content(url, headers,second):
    '''
    @获取403禁止访问的网页
    '''
    randdom_header = random.choice(headers)

    req = urllib.request.Request(url)

    #req.add_header("Host", "blog.csdn.net")
    #req.add_header("Referer", "http://www.weather.com.cn/weather/101200101.shtml")
    req.add_header("Upgrade-Insecure-Requests", 1)
    req.add_header("User-Agent", randdom_header)
    req.add_header("GET", url)
    req.add_header("Cookie", 'JSESSIONID="007651E2115C20B55C0E913388334ABC.tomcat_9010"')
    content = urllib.request.urlopen(req,timeout=second).read()
    return content.decode(encoding="utf-8")


while True:
    os.system("cls")
    cook = getcook()
    headers1['cookie'] = 'JSESSIONID={}'.format(cook[0]['value'])
    headers2['cookie'] = 'JSESSIONID={}'.format(cook[0]['value'])

    #
    # #print(type(cook[0]))
    # cookie_jar = RequestsCookieJar()
    # cookie_jar.set(name=cook[0]['name'],value=cook[0]['value'],domain=cook[0]['domain'],path=cook[0]['path'],secure=False)
    # time.sleep(2)

    # 实例化session
    # session = requests.session()
    # session.cookies.set(name=cook[0]['name'],value=cook[0]['value'],domain=cook[0]['domain'],path=cook[0]['path'],secure=False)
    #requests.utils.add_dict_to_cookiejar(session.cookies,cook[0])

    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    #res = session.get("http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal",headers=req_header,cookies=login())
    #res = requests.get("http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal",auth=HTTPBasicAuth('WHBK','000000'))
    res = login().get("http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal")
    #res = login().get("http://113.57.169.227:8088/ccps//workorder/findWorkOrderSearchList.action?workOrder.range=sd")

    time.sleep(1)
    if res.status_code == 200:
        #print(res.content.decode('utf-8'))
        retxt = res.text
        #print(res.status_code)
        #print("ok")
        #time.sleep(2)
        soup = bs(retxt, 'lxml')
        #print(soup.tbody)
        #print(soup.select('tbody tr'))
        #print(soup.select('tbody.table_list'))
        tlist = soup.select('tbody.table_list tr td a[href^="javascript:workOrderView"]')

        if len(tlist):
            print("亲，你有{}条工单需要处理:".format(len(tlist)))
            for t in tlist:
                print(t.string)
            mixmp3(len(tlist))
            trans_mp3_to_wav('out.mp3', 'out.wav')
            playwave('out.wav')
        else:
            pass
        #driver.quit()
        #os.system('taskkill /im chromedriver.exe /F')
    else:
        print("网页打开失败，请检查网络。")
    time.sleep(600-13)


