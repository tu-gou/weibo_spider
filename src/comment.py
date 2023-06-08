from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def post_weibo(content, wb_id):
    chrome_options = webdriver.ChromeOptions()
    # 把允许提示这个弹窗关闭
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # 设置页面最大化，避免元素被隐藏

    # print('# get打开微博主页')
    url = 'http://weibo.com/' + wb_id
    driver.get(url)  # get打开微博主页
    time.sleep(6)  # 页面加载完全
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[1]/div/a[1]').click()
    time.sleep(10)

    for con in content:
        # print('# 找到文本输入框')
        weibo_content = driver.find_element(By.XPATH, '//*[@id="composerEle"]/div[2]/div/div[1]/div/textarea')
        weibo_content.send_keys(con)
        # print('# 点击发送按钮')
        driver.find_element(By.XPATH, '//*[@id="composerEle"]/div[2]/div/div[3]/div/button').click()
        time.sleep(5)

    driver.close()  # 关闭浏览器


def run(wb_id):
    con = []
    for line in open("comment.txt", "r", encoding='utf-8'):
        content = line
        # print(content[:-1])
        con.append(content)
    post_weibo(con, wb_id)

# if __name__ == '__main__':
#     wb_id= '7295508424/N3IR9sh8i'
#     run(wb_id)
