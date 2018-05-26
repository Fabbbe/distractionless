#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
A distractionless writer made using
PyQt5
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit, QHBoxLayout, QFrame, QMenu
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

WINDOW_TITLE = 'Distraction Less'
FONT_SIZE = 14
BACKGROUND_COLOR = '#f3f3e0'

class App(QMainWindow):
    '''
    The main Qt application for the writer.
    '''
    def __init__(self):
        super().__init__()
        
        self.InitUI()
        
    def InitUI(self):

        # Set up window & settings
        self.setMinimumSize(300, 200)
        self.resize(800, 600)
        self.move(400, 100)
        self.setWindowTitle(WINDOW_TITLE)

        # Create the central widget

        self.widget = QWidget(self)
        self.widget.setStyleSheet('background-color:'+ BACKGROUND_COLOR +';')

        # Create default text font
        self.input_font = QFont("Mono")
        self.input_font.setPointSize(FONT_SIZE)

        # Create text feild
        self.center_text = QPlainTextEdit(self.widget)
        self.center_text.setMaximumWidth(980)
        self.center_text.setFont(self.input_font)

        # Disable frame style
        self.center_text.setFrameStyle(QFrame.NoFrame)

        # Text feild custom context menu
        self.center_text.setContextMenuPolicy(Qt.CustomContextMenu)


        # Create HBox and set it as layout
        self.widget.setLayout(QHBoxLayout())

        # Layout settings
        self.widget.layout().addWidget(self.center_text)
        self.widget.layout().setContentsMargins(0,0,0,0) 
        self.widget.layout().setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.widget)

    def save_text(self):
        '''
        Saves the written text to a file
        
        TODO: Make it work
        '''
        text_to_save = self.center_text.toPlainText()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())
    
