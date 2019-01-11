# -*- coding: utf-8 -*-
"""
@author: mcreng
"""

import sys
from matplotlib.backends.qt_compat import QtGui, QtWidgets, is_pyqt5
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
        # Set window param
        super(ApplicationWindow, self).__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)
        self.setWindowTitle('Visited Countries World Map')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        # Initialize canvas
        self.canvas = WorldMapCanvas()
        layout.addWidget(self.canvas)
        # Add toolbar
        self.addToolBar(NavigationToolbar(self.canvas, self))
        # Set up event handlers
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_move)

    def on_click(self, event):
        """
        Refer on click handler to self.canvas
        """
        self.canvas.on_click(event)

    def on_move(self, event):
        """
        Refer on move handler to self.canvas
        """
        self.canvas.on_move(event)


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        qapp = QtWidgets.QApplication(sys.argv)
    else:
        qapp = QtWidgets.QApplication.instance()
    app = ApplicationWindow()
    app.show()
    qapp.exec_()
