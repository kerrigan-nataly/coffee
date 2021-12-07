import sys

import sqlite3

from PyQt5 import uic
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget


################### first window #####################
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUi()

    def initUi(self):
        #self.coffee_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.coffee_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.show_coffee()
        self.add_button.clicked.connect(self.open_AddFormWindow)
        

    def show_coffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        result = cur.execute('SELECT * FROM coffee').fetchall()
            
        self.coffee_table.setRowCount(len(result))
        for i in range(len(result)):
            for j, elem in enumerate(result[i]):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))

    def open_AddFormWindow(self):
        self.add_form_window = AddFormWindow()
        self.add_form_window.show()
        

################### second window #####################
class AddFormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUi()

    def initUi(self):
        self.buttonBox.accepted.connect(self.add_coffee)
        self.buttonBox.rejected.connect(self.close)

    def add_coffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
    ex.connection.close()  
