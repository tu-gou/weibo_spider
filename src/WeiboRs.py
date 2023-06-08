# -*- coding: utf-8 -*-

import pymysql
from selenium.webdriver.common.by import By


from selenium import webdriver

import time


from MysqlByWbrs import save_rs, save_context

options = webdriver.ChromeOptions()

# 保存爬取的数据

class Item(object):
    rank = None
    title = None
    search = None
    link = None


class SpiderJD(object):

    def __init__(self, url):
        self.url = url
        self.items = []

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        time.sleep(3)
        splists = driver.find_elements(by=By.XPATH, value="//div[@id='pl_top_realtimehot']//tr")

        for sp in splists[2:]:
            item = Item()

            item.rank = sp.find_element(By.XPATH,'.//td[contains(@class,"ranktop")]').text
            item.title = sp.find_element(By.XPATH,'.//td[@class="td-02"]/a').text
            item.search = sp.find_element(By.XPATH,'.//td[@class="td-02"]/span').text
            item.link = sp.find_element(By.XPATH,'.//td[@class="td-02"]/a').get_attribute("href")

            print('排名：' + item.rank + '   标题：' + item.title + '   搜索量：' + item.search + '  链接' + item.link)

            if item.rank != '•':
                self.items.append( item )
                self.pipeLineTxt(item)
                self.pipeLineMysql(item)

        self.SearchInclude(self.items)
        driver.close()
        driver.quit()

    def SearchInclude(self, items):
        self.introductions = []
        for i in range(50):
            item = items[i]
            options = webdriver.ChromeOptions()

            # 处理SSL证书错误问题
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')

            # 忽略无用的日志
            options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            driver2 = webdriver.Chrome()
            driver2.maximize_window()
            driver2.get(item.link)
            time.sleep(2)
            time.sleep(3)
            it = Item()
            # /html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/p[2]
            # html/body/div[1]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/p[2]
            it.introduction = driver2.find_element(By.XPATH,"//p[@node-type='feed_list_content']").text
            it.title = item.title
            print('标题：' + it.title + ' ' + it.introduction)
            self.introductions.append(it)
            filename = 'include.txt'
            fo = open(filename, 'a', encoding='utf8')
            fo.write('排名:%s\t   标题：%s\t 内容：%s\t\n' %
                     (item.rank, item.title, it.introduction.strip().replace(' ', '').replace('\n', '')))
            fo.flush()
            fo.close()
            print('TXT文件保存成功！')
            self.pipeContextMysql((item.rank, item.title, it.introduction.strip().replace(' ', '').replace('\n', '')))
            driver2.close()
            driver2.quit()

    def pipeLineTxt(self, item):
        fileName = 'rs.txt'
        fo = open(fileName, 'a', encoding='utf8')
        fo.write('排名:%s\t   标题：%s\t   搜索量：%s\t 链接%s\t\n' %
                 (item.rank, item.title, item.search, item.link))
        fo.flush()
        fo.close()
        print('TXT文件保存成功！')

    def pipeLineMysql(self, item):
        save_rs(db, item)

    def pipeContextMysql(self, item):
        save_context(db, item)


# 打开数据库连接
db = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="wb",
    charset='utf8mb4'
)


def spider():
    url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
    SpiderJD(url)
    db.close()
