from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtWidgets import QTreeView, QAbstractItemView, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MyTreeView(QTreeView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.doubleClicked.connect(self.show_full_text)

    @pyqtSlot(QModelIndex)
    def show_full_text(self, index):
        item = self.model().itemFromIndex(index)
        full_text = item.text()
        try:
            QMessageBox.information(self, '详情', full_text)
        except Exception as e:
            print(e)
