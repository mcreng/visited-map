import cartopy
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import itertools

countries_shp = shpreader.natural_earth(resolution='110m',
                                        category='cultural', name='admin_0_countries')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=cartopy.crs.PlateCarree())

countries = shpreader.Reader(countries_shp).records()

ax.stock_img()
ax.add_feature(cartopy.feature.LAND, zorder=1)
ax.add_feature(cartopy.feature.BORDERS, zorder=2)
ax.add_feature(cartopy.feature.COASTLINE, zorder=2)
land = cartopy.feature.LAND

def fill_country(country_name):
    global countries, land
    plt.cla()
    local_countries, countries = itertools.tee(countries)
    selected_countries = (country for country in local_countries if country.attributes['NAME_LONG'] == country_name)
    for country in selected_countries:
        geom = country.geometry
        ax.stock_img()
        land = land.geometries()
        land = (l.difference(geom) for l in land)
        land = cartopy.feature.ShapelyFeature(land, cartopy.crs.PlateCarree(), facecolor=cartopy.feature.COLORS['land'])
        ax.add_feature(land, zorder=1)
        ax.add_feature(cartopy.feature.BORDERS, zorder=2)
        ax.add_feature(cartopy.feature.COASTLINE, zorder=2)
        print(country.attributes['NAME_LONG'])
    fig.canvas.draw()
    fig.canvas.flush_events()

def fill_countries(country_names):
    for country_name in country_names:
        fill_country(country_name)
