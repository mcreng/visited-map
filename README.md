# Visited Map

This is an interactive Python3 app for showing a world map of visited countries. 

## Current Progress

The `world_map_canvas.py` is responsible to plot the world map. When the script is called, and the app has not run before, the following default world map is shown.

![default_world](https://raw.githubusercontent.com/mcreng/VisitedMap/master/docs/default_world.png)

Notice the geographical information listed in the upper right corner. Upon left clicking on the respective countries (in this example, China), they are highlighted.

![updated_world](https://raw.githubusercontent.com/mcreng/VisitedMap/master/docs/updated_world.png)

Upon right clicking on the countries, they are removed from highlighting.

The app saves the map data in a compressed (`gzip`) text files and they load back when the app is restarted.

This is the complete world map.

![complete_world](https://raw.githubusercontent.com/mcreng/VisitedMap/master/docs/complete_world.PNG)

## Work List

- [x] Generate world map
- [x] Highlight selected world map
- [x] Build a Qt app
- [ ] Find a method to compile app into any environment
- [x] Save/load data to resume progress for map
- [ ] Infinite scroll for map
- [ ] Allow resetting map at once