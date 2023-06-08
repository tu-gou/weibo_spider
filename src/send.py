from certifi import contents
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

'''
自动发布微博
content：发送内容
username：微博账号
password：微博密码
'''


def post_weibo(content):
    chrome_options = webdriver.ChromeOptions()
    # 把允许提示这个弹窗关闭
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # 设置页面最大化，避免元素被隐藏

    # print('# get打开微博主页')
    # url = 'http://weibo.com/u/7796024506'
    url = 'http://weibo.com/'
    driver.get(url)  # get打开微博主页
    time.sleep(6)  # 页面加载完全

    # driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[1]/div/a[1]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/main/div[2]/div/div/div[2]/div[1]/div/button').click()

    time.sleep(10)
    # 登录后 默认到首页，有微博发送框
    for con in content:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[2]/button').click()
        # print('# 找到文本输入框 输入内容 //*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea')
        weibo_content = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[1]/div[1]/div[2]/div[1]/div/textarea')
        weibo_content.send_keys(con)
        time.sleep(1)
        # print('# 点击发送按钮 //*[@id="homeWrap"]/div[1]/div/div[4]/div/button')
        driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div[1]/div[1]/div[2]/div[4]/div/div[4]/button').click()
        time.sleep(3)

    driver.close()  # 关闭浏览器


def run(topic):
    con = []
    # 自动发微博
    for line in open("send.txt", "r", encoding='utf-8'):
        content = topic + ' ' + line
        # print(content[:-1])
        con.append(content)
    post_weibo(con)

# if __name__ == '__main__':
#     topic = '#乘风破浪#'
#     run(topic)
