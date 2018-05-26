#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A distractionless writer made using
PyQt5
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit, QVBoxLayout, QFrame, QMenu, QFileDialog, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

WINDOW_TITLE = 'Distraction Less'
FONT_SIZE = 14
INFO_FONT_SIZE = 11
MAXIMUM_WIDTH = 980
BACKGROUND_COLOR = '#f3f3e0'

class App(QMainWindow):
    '''
    The main Qt application for the writer.
    '''
    def __init__(self):
        super().__init__()
        
        self.working_file_name = ''

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
        self.input_font = QFont('Mono')
        self.input_font.setPointSize(FONT_SIZE)

        # Create info bar font
        self.info_font = QFont('Mono')
        self.info_font.setPointSize(INFO_FONT_SIZE)

        # Create LineEdit for the top info bar
        # This bar is for displaying info about
        # the current file
        self.top_info_bar = QLineEdit(self.widget)
        self.top_info_bar.setReadOnly(True) 
        self.top_info_bar.setMaximumWidth(MAXIMUM_WIDTH)

        # Set font and style
        self.top_info_bar.setStyleSheet('qproperty-alignment: AlignCenter;')
        self.top_info_bar.setFont(self.info_font)
        self.top_info_bar.setFrame(QFrame.NoFrame)
        self.update_top_info_bar()

        # Create text feild
        self.center_text = QPlainTextEdit(self.widget)
        self.center_text.setMaximumWidth(MAXIMUM_WIDTH)
        self.center_text.setFont(self.input_font)

        # Disable frame style
        self.center_text.setFrameStyle(QFrame.NoFrame)

        # Text feild custom context menu
        self.center_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.center_text.customContextMenuRequested.connect(self.context_menu_event)

        # Create HBox and set it as layout
        self.widget.setLayout(QVBoxLayout())

        # Layout settings
        self.widget.layout().addWidget(self.top_info_bar)
        self.widget.layout().addWidget(self.center_text)
        self.widget.layout().setContentsMargins(0,0,0,0) 
        self.widget.layout().setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.widget)

    def save_text_file(self):
        '''
        Saves the written text to a file
        '''
        text_to_save = self.center_text.toPlainText()
        name = QFileDialog.getSaveFileName(self,'Save as...','','All Files (*);;Text Files (*.txt)')[0]

        with open(name, 'w') as save_file:
            save_file.write(text_to_save)

        # Show the new file path
        self.working_file_name = name

        # Update info bar
        self.update_top_info_bar()

    def open_text_file(self):
        ''' Opens a file and '''
        name = QFileDialog.getOpenFileName(self,'Open a File','','All Files (*);;Text Files (*.txt)')[0]

        with open(name, 'r') as new_file:
            new_text = new_file.read()

        self.center_text.setPlainText(new_text)
        
        # Set current file name to the opened one.
        self.working_file_name = name
        
        # Update info bar
        self.update_top_info_bar()


    def context_menu_event(self, event):
        '''
        This function defines the context menu that
        appears on right-click. 

        '''

        context_menu = QMenu(self)

        copy_action = context_menu.addAction('Copy') # Copy to clipboard
        paste_action = context_menu.addAction('Paste') # Paste clipboard

        # Save file as...
        save_as_action = context_menu.addAction('Save as...') 
        # Open file
        open_action = context_menu.addAction('Open file')

        action = context_menu.exec_(self.center_text.mapToGlobal(event))

        # Copy and paste actions
        if action == copy_action:
            self.center_text.copy()
        elif action == paste_action:
            self.center_text.paste()

        # File managment actions 
        elif action == save_as_action:
            self.save_text_file()
        elif action == open_action:
            self.open_text_file()

    def update_top_info_bar(self):
        if self.working_file_name != '':
            self.top_info_bar.setText(self.working_file_name)
        else:
            self.top_info_bar.setText('New File')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())
    
