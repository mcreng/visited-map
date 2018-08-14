# Visited Map

This is an interactive Python3 app for showing a world map of visited countries. A PyQt5 GUI is planned to be implemented.

## Current Progress

The `map.py` is responsible to plot the world map. When the script is called, the following default world map is shown.

![default_world](C:\Users\mcreng\git\VisitedMap\docs\default_world.png)

The script supports the function `fill_countries(country_names)`. Upon inputting a list of country names, the countries are highlighted in the output world map.

```Python
>>> fill_countries(['China', 'Australia', 'Japan'])
```

![updated_world](C:\Users\mcreng\git\VisitedMap\docs\updated_world.png)