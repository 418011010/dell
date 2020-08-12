from selenium import webdriver  # 导入selenium
import time
driver = webdriver.Chrome(r'd:\chromedriver.exe')
option = webdriver.ChromeOptions()
option.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'


def loginZhihu():
    loginurl = 'http://113.57.169.227:8088/ccps/login.jsp'  # 登录页面
    # 加载webdriver驱动，用于获取登录页面标签属性
    #driver = webdriver.Chrome()
    driver.get(loginurl)  # 请求登录页面
    driver.find_element_by_id('wcode').clear()  # 获取用户名输入框，并先清空
    driver.find_element_by_id('wcode').send_keys(u'WHBK')  # 输入用户名
    driver.find_element_by_id('password').clear()  # 获取密码框，并清空
    driver.find_element_by_id('password').send_keys(u'000000')  # 输入密码

    #captcha = driver.find_element_by_id('captcha_image')  # 获取验证码标签
    #submit = driver.find_element_by_css_selector('a[name="登录"]')  # 获取提交按钮
    submit =driver.find_element_by_link_text("登录")
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
    time.sleep(2)
    driver.get('http://113.57.169.227:8088/ccps//workorder/findWorkOrderList.action?workOrder.range=yff&workOrder.standby3=order_deal')  # 请求其他页面
    return cookies  # 返回cookies 之后其他方法可以调用，这样不用每次请求都返回登录


print(loginZhihu())
