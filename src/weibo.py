# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel

from src import tree


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 600)
        Form.setMinimumSize(QtCore.QSize(875, 600))
        Form.setMaximumSize(QtCore.QSize(875, 600))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 875, 595))
        self.tabWidget.setMinimumSize(QtCore.QSize(875, 595))
        self.tabWidget.setMaximumSize(QtCore.QSize(875, 600))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setStyleSheet('background-image: url("../resource/wel.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 'background-color: transparent;')
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(150, 240, 571, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('color: red;'
                                   'background-color: transparent;'
                                   'background-clip: padding-box')
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet('background-image: url("../resource/back.jpg");'
                               'background-repeat: no-repeat;'
                               'background-position: center;'
                               'background-size:cover;'
                               )
        self.view_rs_button = QtWidgets.QPushButton(self.tab)
        self.view_rs_button.setGeometry(QtCore.QRect(280, 510, 75, 23))
        self.view_rs_button.setObjectName("view_rs_button")
        self.clear_rs_button = QtWidgets.QPushButton(self.tab)
        self.clear_rs_button.setGeometry(QtCore.QRect(480, 510, 75, 23))
        self.clear_rs_button.setObjectName("clear_rs_button")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 861, 421))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 859, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hot_search = tree.MyTreeView(self.scrollAreaWidgetContents)
        self.hot_search.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.hot_search.setUniformRowHeights(True)
        self.hot_search.setObjectName("hot_search")
        self.verticalLayout.addWidget(self.hot_search)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 10, 761, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(26)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet('background-image: url("../resource/back.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.show_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.show_textBrowser.setGeometry(QtCore.QRect(10, 200, 491, 351))
        self.show_textBrowser.setObjectName("show_textBrowser")
        self.analyze_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.analyze_textBrowser.setGeometry(QtCore.QRect(510, 200, 351, 161))
        self.analyze_textBrowser.setObjectName("analyze_textBrowser")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(530, 60, 151, 21))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.analyze_button = QtWidgets.QPushButton(self.tab_2)
        self.analyze_button.setGeometry(QtCore.QRect(640, 130, 75, 23))
        self.analyze_button.setObjectName("analyze_button")
        self.clear_button = QtWidgets.QPushButton(self.tab_2)
        self.clear_button.setGeometry(QtCore.QRect(730, 130, 75, 23))
        self.clear_button.setObjectName("clear_button")
        self.show_button = QtWidgets.QPushButton(self.tab_2)
        self.show_button.setGeometry(QtCore.QRect(550, 130, 75, 23))
        self.show_button.setObjectName("show_button")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(700, 60, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.user_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.user_textBrowser.setGeometry(QtCore.QRect(10, 20, 491, 171))
        self.user_textBrowser.setObjectName("user_textBrowser")
        self.pic_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.pic_textBrowser.setGeometry(QtCore.QRect(510, 370, 351, 181))
        self.pic_textBrowser.setObjectName("pic_textBrowser")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 871, 573))
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tab_8.setStyleSheet('background-image: url("../resource/warn.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.label_10 = QtWidgets.QLabel(self.tab_8)
        self.label_10.setGeometry(QtCore.QRect(280, 120, 311, 101))
        font = QtGui.QFont()
        font.setFamily("HGDY_CNKI")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet('color: red;'
                                    'background-color: transparent;'
                                    'background-clip: padding-box')
        self.label_11 = QtWidgets.QLabel(self.tab_8)
        self.label_11.setGeometry(QtCore.QRect(40, 240, 791, 131))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet('color: red;'
                                    'background-color: transparent;'
                                    'background-clip: padding-box')
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tab_5.setStyleSheet('background-image: url("../resource/re.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.clear_report_pushButton = QtWidgets.QPushButton(self.tab_5)
        self.clear_report_pushButton.setGeometry(QtCore.QRect(530, 330, 75, 23))
        self.clear_report_pushButton.setObjectName("clear_report_pushButton")
        self.report_pushButton = QtWidgets.QPushButton(self.tab_5)
        self.report_pushButton.setGeometry(QtCore.QRect(250, 330, 75, 23))
        self.report_pushButton.setObjectName("report_pushButton")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(150, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.report_lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.report_lineEdit.setGeometry(QtCore.QRect(340, 160, 351, 21))
        self.report_lineEdit.setObjectName("report_lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(150, 220, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.report_comboBox = QtWidgets.QComboBox(self.tab_5)
        self.report_comboBox.setGeometry(QtCore.QRect(340, 220, 201, 21))
        self.report_comboBox.setObjectName("report_comboBox")
        self.report_comboBox.addItem("")
        self.report_comboBox.addItem("")
        self.report_comboBox.addItem("")
        self.report_comboBox.addItem("")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tab_6.setStyleSheet('background-image: url("../resource/re.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(200, 150, 201, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comment_id_lineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.comment_id_lineEdit.setGeometry(QtCore.QRect(410, 170, 201, 20))
        self.comment_id_lineEdit.setObjectName("comment_id_lineEdit")
        self.comment_pushButton = QtWidgets.QPushButton(self.tab_6)
        self.comment_pushButton.setGeometry(QtCore.QRect(370, 260, 75, 23))
        self.comment_pushButton.setObjectName("comment_pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(210, 320, 471, 51))
        font = QtGui.QFont()
        font.setFamily("华光行楷_CNKI")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tab_7.setStyleSheet('background-image: url("../resource/re.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.label_7 = QtWidgets.QLabel(self.tab_7)
        self.label_7.setGeometry(QtCore.QRect(210, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.topic_lineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.topic_lineEdit.setGeometry(QtCore.QRect(430, 200, 191, 20))
        self.topic_lineEdit.setObjectName("topic_lineEdit")
        self.topic_pushButton = QtWidgets.QPushButton(self.tab_7)
        self.topic_pushButton.setGeometry(QtCore.QRect(370, 360, 75, 23))
        self.topic_pushButton.setObjectName("topic_pushButton")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tab_9.setStyleSheet('background-image: url("../resource/back.jpg");'
                                 'background-repeat: no-repeat;'
                                 'background-position: center;'
                                 'background-size:cover;'
                                 )
        self.cloud_lineEdit = QtWidgets.QLineEdit(self.tab_9)
        self.cloud_lineEdit.setGeometry(QtCore.QRect(330, 230, 351, 21))
        self.cloud_lineEdit.setObjectName("cloud_lineEdit")
        self.label_12 = QtWidgets.QLabel(self.tab_9)
        self.label_12.setGeometry(QtCore.QRect(70, 220, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.cloud_pushButton = QtWidgets.QPushButton(self.tab_9)
        self.cloud_pushButton.setGeometry(QtCore.QRect(390, 360, 75, 23))
        self.cloud_pushButton.setObjectName("cloud_pushButton")
        self.tabWidget.addTab(self.tab_9, "")
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎来到微博管控系统"))
        self.label_2.setText(_translate("Form", "欢迎进入微博内容识别与管控系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "欢迎页面"))
        self.view_rs_button.setText(_translate("Form", "查看热搜"))
        self.clear_rs_button.setText(_translate("Form", "清除热搜"))
        self.label_14.setText(_translate("Form", "欢迎来到实时热搜查询界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "查看热搜"))
        self.show_textBrowser.setPlaceholderText(_translate("Form", "在这里可以查看用户所发日志："))
        self.analyze_textBrowser.setPlaceholderText(_translate("Form", "在这里展示分析博客的结果："))
        self.label.setText(_translate("Form", "待查询用户id："))
        self.analyze_button.setText(_translate("Form", "分析"))
        self.clear_button.setText(_translate("Form", "清空"))
        self.show_button.setText(_translate("Form", "展示"))
        self.user_textBrowser.setPlaceholderText(_translate("Form", "在这里可以查看该用户个人信息："))
        self.pic_textBrowser.setPlaceholderText(_translate("Form", "在这里展示分析图片的结果："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "查看用户"))
        self.label_10.setText(_translate("Form", "WARNING！"))
        self.label_11.setText(_translate("Form", "这里可进行微博举报、评论区管控、ID管控，所有操作均会生效，请慎重！"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "管控提醒"))
        self.clear_report_pushButton.setText(_translate("Form", "取消"))
        self.report_pushButton.setText(_translate("Form", "提交"))
        self.label_3.setText(_translate("Form", "输入需要举报的微博url："))
        self.label_4.setText(_translate("Form", "请选择你想要举报的类型："))
        self.report_comboBox.setItemText(0, _translate("Form", "人身攻击"))
        self.report_comboBox.setItemText(1, _translate("Form", "涉黄信息"))
        self.report_comboBox.setItemText(2, _translate("Form", "有害信息"))
        self.report_comboBox.setItemText(3, _translate("Form", "不良价值导向"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "举报微博"))
        self.label_8.setText(_translate("Form", "输入需要管控的博客地址："))
        self.comment_pushButton.setText(_translate("Form", "提交"))
        self.label_5.setText(_translate("Form", "注：此处发表的评论均为正能量评论！"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "评论区管控"))
        self.label_7.setText(_translate("Form", "输入需要管控的话题："))
        self.topic_pushButton.setText(_translate("Form", "提交"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "话题管控"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "管控页面"))
        self.label_12.setText(_translate("Form", "输入需要生成词云的url："))
        self.cloud_pushButton.setText(_translate("Form", "确认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Form", "词云"))
