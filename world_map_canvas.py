# -*- coding: utf-8 -*-
"""
@author: mcreng
"""

import itertools
import cartopy
import cartopy.io.shapereader as shpreader
from matplotlib.figure import Figure
from shapely.geometry import Point
from matplotlib.backends.qt_compat import QtWidgets, is_pyqt5
from util import timeit

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

class WorldMapCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=6, dpi=150):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(1, 1, 1, projection=cartopy.crs.PlateCarree())
        self.ax.stock_img()
        self.ax.add_feature(cartopy.feature.LAND, zorder=1)
        self.ax.add_feature(cartopy.feature.BORDERS, zorder=2)
        self.ax.add_feature(cartopy.feature.COASTLINE, zorder=2)
        fig.tight_layout()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    
        self.land = cartopy.feature.LAND
        self.countries = shpreader.Reader(shpreader.natural_earth(resolution='110m',
                                                                  category='cultural',
                                                                  name='admin_0_countries')).records()

    @timeit   
    def on_click(self, event):
        local_countries, self.countries = itertools.tee(self.countries)
        point = Point(event.xdata, event.ydata)
        country = next(itertools.filterfalse(lambda country: not country.geometry.intersects(point), local_countries))
        print(country.attributes['NAME_LONG'])
        self.fill_country(country)

    @timeit    
    def fill_country(self, country):
        self.ax.clear()
        geom = country.geometry
        self.ax.stock_img()
        self.land = self.land.geometries()
        self.land = (l.difference(geom) for l in self.land)
        self.land = cartopy.feature.ShapelyFeature(self.land, cartopy.crs.PlateCarree(), facecolor=cartopy.feature.COLORS['land'])
        self.ax.add_feature(self.land, zorder=1)
        self.ax.add_feature(cartopy.feature.BORDERS, zorder=2)
        self.ax.add_feature(cartopy.feature.COASTLINE, zorder=2)
        self.draw()
        self.flush_events()