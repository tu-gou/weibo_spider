from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()


class SpiderJD(object):

    def __init__(self, url, type):
        self.url = url
        self.items = []

        options = webdriver.ChromeOptions()

        # 处理SSL证书错误问题
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        # 忽略无用的日志
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[1]/div/a[1]').click()
        time.sleep(10)
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[2]/div[2]/div[2]/main/div/div/div[2]/article/div[1]/div/div[2]/div/div/span/div/i').click()
        # print('点击箭头\n')
        time.sleep(1)
        # //*[@id="app"]/div[1]/div[2]/div[2]/main/div/div/div[2]/article/div[2]/div/div[2]/div/div/div/div/div[6]
        driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[2]/div[2]/div[2]/main/div/div/div[2]/article/div[2]/div/div[2]/div/div/div/div/div[6]').click()
        # print('点击投诉\n')
        # //*[@id="pl_report_complaint"]/div[1]/div[1]/div[4]/ul/li[3]/a
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        if type == 1:
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[4]/ul/li[1]/a').click()
            # print('点击涉黄信息\n')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[6]/ul/li[1]/a').click()
            # print('点击色情导流\n')
            time.sleep(1)
        elif type == 0:  # 人身攻击
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[4]/ul/li[4]/a').click()
            # print('点击人身攻击\n')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[6]/ul/li[15]/a').click()
            # print('点击不友善言论\n')
            time.sleep(1)
        elif type == 2:  # 有害
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[4]/ul/li[2]/a').click()
            # print('点击有害信息\n')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[6]/ul/li[8]/a').click()
            # print('点击恐暴血腥\n')
            time.sleep(1)
        elif type == 3:  # 不良价值导向
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[4]/ul/li[10]/a').click()
            # print('点击不良价值导向\n')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[1]/div[6]/ul/li[42]/a').click()
            # print('点击不良价值导向\n')
            time.sleep(1)
        else:
            print('错误的type输入！')
            return 0
        driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[2]/p[3]/label/input').click()
        # print('点击同意\n')
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="pl_report_complaint"]/div[1]/div[2]/a').click()
        # print('点击提交\n')
        time.sleep(5)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.quit()


def spider(url, type):
    # test_url = 'https://weibo.com/7843334475/N3MsQ9bc0'
    # 0:涉黄 1:人身攻击 2:暴力信息 3:不良价值导向
    SpiderJD(url, type)  # url为要举报的微博地址，type为举报类型
