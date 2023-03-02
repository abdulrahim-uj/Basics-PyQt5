from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

import sys


'''
QApplication: where we can place window & widgets
QMainWindow: like a container, holds all widgets
'''
def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) # set window --> x, y positions and width, height
    win.setWindowTitle("Basic PyQt5 App") # set window title

    # Add label
    lbl_hello = QLabel(win)
    lbl_hello.setText("Basic PyQt5 App First Label")
    lbl_hello.resize(200,20) # set width, height
    lbl_hello.move(50, 50) # set x, y position to place the label from top-left corner
    lbl_hello.setStyleSheet("border: 1px solid red;") # set border style

    # Add button
    btn_click = QPushButton(win)
    btn_click.setText("Click here")
    btn_click.move(75, 75)
    # connect to button click func
    btn_click.clicked.connect(button_clicked)


    # show the window
    win.show()
    
    # for exit call 
    sys.exit(app.exec_())

# button click func
def button_clicked():
    print("button clicked!")

# call main func
main()
