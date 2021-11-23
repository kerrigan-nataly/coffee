import sys

import sqlite3

from PyQt5 import uic
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUi()

    def initUi(self):
        #self.coffee_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.coffee_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.show_coffee()
        

    def show_coffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        result = cur.execute('SELECT * FROM coffee').fetchall()
            
        self.coffee_table.setRowCount(len(result))
        for i in range(len(result)):
            for j, elem in enumerate(result[i]):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
    ex.connection.close()  
