# -*- coding: utf-8 -*-
"""
@author: mcreng
"""

import sys
from matplotlib.backends.qt_compat import QtWidgets, is_pyqt5
from util import timeit
from world_map_canvas import WorldMapCanvas

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        self.canvas = WorldMapCanvas()
        layout.addWidget(self.canvas)
        self.addToolBar(NavigationToolbar(self.canvas, self))        
        self.canvas.mpl_connect('button_press_event', self.on_click)
    @timeit   
    def on_click(self, event):
        self.canvas.on_click(event)


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        qapp = QtWidgets.QApplication(sys.argv)
    else:
        qapp = QtWidgets.QApplication.instance() 
    app = ApplicationWindow()
    app.show()
    qapp.exec_()