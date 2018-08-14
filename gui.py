import sys
import cartopy
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import itertools
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

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

        canvas = FigureCanvas(Figure(figsize=(10, 6)))
        layout.addWidget(canvas)
        self.addToolBar(NavigationToolbar(canvas, self))        

        ax = canvas.figure.add_subplot(1, 1, 1, projection=cartopy.crs.PlateCarree())
        ax.stock_img()
        ax.add_feature(cartopy.feature.LAND, zorder=1)
        ax.add_feature(cartopy.feature.BORDERS, zorder=2)
        ax.add_feature(cartopy.feature.COASTLINE, zorder=2)

        self.land = cartopy.feature.LAND
        self.countries = shpreader.Reader(shpreader.natural_earth(resolution='110m',
                                                                  category='cultural',
                                                                  name='admin_0_countries')).records()

        canvas.mpl_connect('button_press_event', self.on_click)
        
    def on_click(self, event):
        print('You pressed', event.button, event.xdata, event.ydata)

if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()