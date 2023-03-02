from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

import sys


'''
QApplication: where we can place window & widgets
QMainWindow: like a container, holds all widgets
'''

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.setGeometry(200, 200, 300, 300) # set window --> x, y positions and width, height
        self.setWindowTitle("Basic PyQt5 App") # set window title
        # All gui elements placed here in this func
        self.initUI()
    
    # initUI
    def initUI(self):
        # Add label
        self.lbl_hello = QLabel(self)
        self.lbl_hello.setText("Basic PyQt5 App First Label")
        self.lbl_hello.resize(200,20) # set width, height
        self.lbl_hello.move(50, 50) # set x, y position to place the label from top-left corner
        self.lbl_hello.setStyleSheet("border: 1px solid red;") # set border style

        # Add button
        self.btn_click = QPushButton(self)
        self.btn_click.setText("Click here")
        self.btn_click.move(75, 75)
        # connect to button click func
        self.btn_click.clicked.connect(self.button_clicked)

    # button click func that can change label text
    def button_clicked(self):
        if self.lbl_hello.text() == "Hey, you clicked":
            self.lbl_hello.setText("Basic PyQt5 App First Label")
        else:
            self.lbl_hello.setText("Hey, you clicked")
        # call update widgets size func
        self.update()

    # func uses to adjest size when change something on runtime
    def update(self):
        self.lbl_hello.adjustSize()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()

    # show the window
    win.show()
    
    # for exit call 
    sys.exit(app.exec_())


# call main func
main()
