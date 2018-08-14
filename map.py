import cartopy
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import itertools

# =============================================================================
# import os
# source_proj = ccrs.PlateCarree()
# fname = os.path.join(config["repo_data_dir"],
#                      'raster', 'natural_earth',
#                      '50-natural-earth-1-downsampled.png')
# 
# return self.imshow(imread(fname), origin='upper',
#                    transform=source_proj,
#                    extent=[-180, 180, -90, 90])
# =============================================================================

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

def fill_country(country_names):
    global countries, land
    plt.cla()
    for country_name in country_names:
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

