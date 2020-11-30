import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import sqlite3
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.params = {}
        self.headers = ['ID', 'Название сорта', 'Степень обжарки', 'Цена', 
                        'Описание вкуса', 'Объем упаковки', 'Молотый(1)/в зернах(2)']
        self.con = sqlite3.connect('coffee.sqlite')
        cur = self.con.cursor()
        self.result = cur.execute("SELECT * FROM main").fetchall()
        self.table(self.result)
    
    def table(self, result):
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())