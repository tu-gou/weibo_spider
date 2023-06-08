import os
import sys

import jieba
import pymysql
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory, QMessageBox, QLabel

from src import WeiboRs, WuMember, NaiveBayes, complain, spider_user, comment, send, recommend, cloud, image_recognition
from src.MysqlByWbrs import read_rs, read_rs_context
from weibo import Ui_Form


class Weibo(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Weibo, self).__init__(parent)
        self.setupUi(self)
        # 对TreeView进行model初始化
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['排名', '标题', '搜索量', '链接'])
        self.hot_search.setModel(model)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.init_ui()

    @pyqtSlot()
    def init_ui(self):
        self.view_rs_button.clicked.connect(self.show_hot_search)
        self.clear_rs_button.clicked.connect(self.clear_hot_search)
        self.show_button.clicked.connect(self.show_user)
        self.show_button.clicked.connect(self.show_blog)
        self.analyze_button.clicked.connect(self.analyze_blog)
        self.analyze_button.clicked.connect(self.analyze_pic)
        self.clear_button.clicked.connect(self.clear_blog)
        self.report_pushButton.clicked.connect(self.report)
        self.clear_report_pushButton.clicked.connect(self.clear_report)
        self.comment_pushButton.clicked.connect(self.comment)
        self.topic_pushButton.clicked.connect(self.topic)
        self.cloud_pushButton.clicked.connect(self.word_cloud)

    @pyqtSlot()
    def show_hot_search(self):
        # WeiboRs.spider()
        #   treeView的模型
        model = QStandardItemModel(self)
        #   模型的标题
        model.setHorizontalHeaderLabels(['排名', '标题', '搜索量', '链接'])
        # 添加条目,热搜榜共50条热搜
        for i in range(50):
            item = read_rs(db, i + 1)
            itemProject = QStandardItem(str(item[0]))
            model.appendRow(itemProject)
            model.setItem(i, 1, QStandardItem(item[1]))
            model.setItem(i, 2, QStandardItem(item[2]))
            model.setItem(i, 3, QStandardItem(item[3]))
            # 添加子条目
            itemChild = QStandardItem('详情')
            context = read_rs_context(db, i + 1)
            itemProject.appendRow(itemChild)
            itemProject.setChild(0, 1, QStandardItem(context[2]))

        self.hot_search.setModel(model)
        self.hot_search.setWordWrap(True)

        # 调整第一列的宽度
        self.hot_search.header().resizeSection(0, 80)
        self.hot_search.header().resizeSection(1, 300)
        # 设置成有虚线连接的方式
        self.hot_search.setStyle(QStyleFactory.create('windows'))

    @pyqtSlot()
    def clear_hot_search(self):
        empty_model = QStandardItemModel(self)
        empty_model.setHorizontalHeaderLabels(['排名', '标题', '搜索量', '链接'])
        self.hot_search.setModel(empty_model)

    @pyqtSlot()
    def show_user(self):
        if self.lineEdit_5.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入id！')
        else:
            user_id = self.lineEdit_5.text()
            spider_user.user_spider(user_id)
            path = user_id + 'info.txt'
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            self.user_textBrowser.setText(text)

    @pyqtSlot()
    def show_blog(self):
        if self.lineEdit_5.text() == '':
            pass
        else:
            user_id = self.lineEdit_5.text()
            path = user_id + 'blog.txt'
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            self.show_textBrowser.setText(text)

    @pyqtSlot()
    def analyze_blog(self):
        if self.lineEdit_5.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入id！')
        else:
            user_id = self.lineEdit_5.text()
            path = user_id + 'blog.txt'
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                word = jieba.lcut(text)
                test_data = WuMember.find_feature(word)
                NaiveBayes.naive_bayes(test_data)
            with open('classify.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                self.analyze_textBrowser.setText(text)

    @pyqtSlot()
    def analyze_pic(self):
        if self.lineEdit_5.text() == '':
            pass
        else:
            # 设置图片格式
            img_extensions = [".jpg"]
            # 设置文件夹路径
            dir_path = 'E:/pythonProject/weibo/src/pic'
            # 初始化计数器
            count = 0
            # 遍历文件夹中的所有文件
            for filename in os.listdir(dir_path):
                # 检查文件是否为图像文件
                if any(filename.lower().endswith(extension) for extension in img_extensions):
                    # 如果是图像文件，则计数器加 1
                    count += 1
            nude_pic = []
            for i in range(count):
                num = i + 1
                n = image_recognition.Nude('E:/pythonProject/weibo/src/pic/' + str(num) + '.jpg')
                n.resize(maxheight=800, maxwidth=600)
                n.parse()
                if n.result:
                    nude = str(num) + '.jpg'
                    nude_pic.append(nude)
            if not nude_pic:
                self.pic_textBrowser.setText("该用户所有博客中没有色情图片！")
            else:
                for pic in nude_pic:
                    self.pic_textBrowser.append(pic)

    @pyqtSlot()
    def clear_blog(self):
        self.show_textBrowser.clear()
        self.analyze_textBrowser.clear()
        self.lineEdit_5.clear()
        self.pic_textBrowser.clear()
        self.user_textBrowser.clear()

    @pyqtSlot()
    def report(self):
        if self.report_lineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入待举报url！')
        else:
            index = self.report_comboBox.currentIndex()
            url = self.report_lineEdit.text()
            complain.SpiderJD(url, index)
            messageBox = QMessageBox()
            messageBox.setWindowTitle('管控举报')
            messageBox.setText('您已成功举报该文章！')
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            messageBox.setDefaultButton(QMessageBox.Ok)
            messageBox.exec_()

    @pyqtSlot()
    def clear_report(self):
        self.report_lineEdit.clear()

    @pyqtSlot()
    def comment(self):
        if self.comment_id_lineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入待管控博客地址！')
        else:
            weibo_id = self.comment_id_lineEdit.text()
            comment.run(weibo_id)
            messageBox = QMessageBox()
            messageBox.setWindowTitle('管控博客')
            messageBox.setText('您已成功淹没该评论区！')
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            messageBox.setDefaultButton(QMessageBox.Ok)
            messageBox.exec_()

    @pyqtSlot()
    def topic(self):
        if self.topic_lineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入待管控话题！')
        else:
            weibo_id = self.topic_lineEdit.text()
            send.run(weibo_id)
            messageBox = QMessageBox()
            messageBox.setWindowTitle('管控话题')
            messageBox.setText('您已成功淹没该话题！')
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            messageBox.setDefaultButton(QMessageBox.Ok)
            messageBox.exec_()

    @pyqtSlot()
    def word_cloud(self):
        if self.cloud_lineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '请输入待生成词云url！')
        else:
            url = self.cloud_lineEdit.text()
            recommend.SpiderJD(url)
            cloud.run()
            messageBox = QMessageBox()
            messageBox.setWindowTitle('词云生成结果')
            pixmap = QPixmap('output.png')
            label = QLabel(self)
            label.setPixmap(pixmap)
            messageBox.layout().addWidget(label)
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            messageBox.setDefaultButton(QMessageBox.Ok)
            messageBox.exec_()


if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db="wb",
        charset='utf8'
    )
    app = QApplication(sys.argv)
    weibo = Weibo()
    weibo.show()
    sys.exit(app.exec_())
