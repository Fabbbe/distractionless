#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Utilities used by distractionless application
'''

from PyQt5.QtGui import QFontDatabase, QFont

def get_monospaced_font(size):
    '''
    Takes a size and finds a monospaced font from system fonts,
    sets the font size and then returns it
    '''
    monospace_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    monospace_font.setPointSize(size)
    return monospace_font
