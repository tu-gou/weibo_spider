from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()


# 保存爬取的数据

class Item(object):
    include = None


class SpiderJD(object):

    def __init__(self, url):
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
        time.sleep(2)
        time.sleep(4)
        count = 0
        while count < 1:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            count += 1
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[3]/div[1]/div/a[1]').click()
        time.sleep(10)
        fileName = 'recommend.txt'
        fo = open(fileName, 'a', encoding='utf8')
        fo.truncate(0)
        fo.close()
        count = 0
        while count < 1:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            count += 1
        comment_div_list = driver.find_elements(By.XPATH, '//*[@id="scroller"]/div[1]/div')
        count = 0
        while count < 1:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            count += 1
        # comment_div_list=comment_div_list+(driver.find_elements(By.XPATH,'//*[@id="scroller"]/div[1]/div'))

        # print('length:', len(comment_div_list))
        for sp in comment_div_list:
            # print("sss")
            item = Item()
            item.include = sp.find_element(By.XPATH, './div/div/div/div[1]/div[2]/div[1]/span').text
            # print('评论：' + item.include)
            self.pipeLineTxt(item)
            # self.pipeLineMysql(item)
        # self.SearchInclude(self.items)
        driver.close()
        driver.quit()

    def pipeLineTxt(self, item):

        item.include = item.include.replace('了', '')
        item.include = item.include.replace('的', '')
        # print(item.include)
        fileName = 'recommend.txt'
        fo = open(fileName, 'a', encoding='utf8')
        fo.write('%s\n' % item.include)
        fo.flush()
        fo.close()
        # print('TXT文件保存成功！')


if __name__ == '__main__':
    url = 'https://weibo.com/7295508424/N3IR9sh8i'
    SpiderJD(url)
