---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import json
import matplotlib.pyplot as plt

%matplotlib inline
```

```python
f = "data/continents.geojson"
with open(f, 'r') as infile:
    g = json.load(infile)

from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
                plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
```

```python
plt.rcParams['figure.figsize'] = [10, 5] # set figure size

```

```python
f = "data/continents.geojson"
with open(f, 'r') as infile:
    g = json.load(infile)

from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
                plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
```

```python
import pandas as pd
participants2018 = pd.read_csv('data/participants2018.csv', encoding='latin-1')
```

```python
participants2018
```

```python
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^')
```

```python
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^')     
    
```

```python
sanantonio = ( -98.4936, 29.4241)

```

```python
import pyproj
```

```python
pyproj.Geod?
```

```python
geod = pyproj.Geod(ellps='WGS84')
```

```python
gcd = geod.inv(sanantonio[0], sanantonio[1], 27.9977, -26.1836)
gcd
```

```python
gcd[-1] * 0.000621371
```

```python
waypoints = geod.npts(sanantonio[0], sanantonio[1], 27.9977, -26.1836, 20)
```

```python
waypoints
```

```python
#route = [minn]
route = [sanantonio]
route.extend(waypoints)
route.append((27.9977, -26.1836))
```

```python
import numpy as np
route = np.array(route)
```

```python
plt.plot(route[:,0], route[:,1])
```

```python
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^')     

plt.plot(route[:,0], route[:,1])
```

## On your own

1. Calculate and plot the great circle routes bringing our participants to the workshop.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

# Solution

```python
import pandas as pd
participants2018 = pd.read_csv('data/participants2018.csv', encoding='latin-1')
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^', markerfacecolor='r', markeredgecolor='r')     


for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    plt.plot(route[:,0], route[:,1], color='r')
```

### Break the line

```python
import pandas as pd
participants2018 = pd.read_csv('data/participants2018.csv',encoding='latin-1')
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^', markerfacecolor='r', markeredgecolor='r')     

for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        plt.plot(route[:min_index,0], route[:min_index,1], color='r')
        plt.plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    plt.plot(route[:,0], route[:,1], color='r')
plt.plot(sanantonio[0],sanantonio[1],  '*', markerfacecolor='y', markeredgecolor='r', markersize=12)
```

```python
import pandas as pd
participants2018 = pd.read_csv('data/participants2018.csv',encoding='latin-1')
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^', markerfacecolor='r', markeredgecolor='r')     

for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        plt.plot(route[:min_index,0], route[:min_index,1], color='r')
        plt.plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    plt.plot(route[:,0], route[:,1], color='r')
plt.plot(sanantonio[0],sanantonio[1],  '*', markerfacecolor='y', markeredgecolor='r', markersize=12)
```

```python
import pandas as pd
participants2018 = pd.read_csv('data/participants2018.csv',encoding='latin-1')
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2018.iterrows():
    plt.plot(p['lon'], p['lat'], '^', markerfacecolor='r', markeredgecolor='r')     

for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        plt.plot(route[:min_index,0], route[:min_index,1], color='r')
        plt.plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    plt.plot(route[:,0], route[:,1], color='r')
plt.plot(sanantonio[0],sanantonio[1],  '*', markerfacecolor='y', markeredgecolor='r', markersize=12)
plt.savefig(fname='../figs/readmefigs/routes18.png')
```

### Plot the great circle routes bringing our participants to the workshop in 2016

```python
import pandas as pd
participants2016 = pd.read_csv('data/participants2016.csv',encoding='latin-1')
minn = (-93.2550, 44.9778)
from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2016.iterrows():
    plt.plot(p['lon'], p['lat'], 'o', markerfacecolor='b', markeredgecolor='b')     


for idx, p in participants2016.iterrows():
    waypoints = geod.npts(minn[0], minn[1], p['lon'], p['lat'], 20)
    route = [minn]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    plt.plot(route[:,0], route[:,1], color='b')
plt.plot(minn[0],minn[1],  '*', markerfacecolor='y', markeredgecolor='b', markersize=12)
```

## Plot 2017 Participant Travel

```python
import pandas as pd
participants2017 = pd.read_csv('data/participants2017.csv',encoding='latin-1')
vancouver = (-123.1207, 49.2827)


from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2017.iterrows():
    plt.plot(p['lon'], p['lat'], 'o', markerfacecolor='r', markeredgecolor='r')     


for idx, p in participants2017.iterrows():
    waypoints = geod.npts(vancouver[0], vancouver[1], p['lon'], p['lat'], 20)
    route = [vancouver]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        plt.plot(route[:min_index,0], route[:min_index,1], color='r')
        plt.plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    plt.plot(route[:,0], route[:,1], color='r')
plt.plot(vancouver[0],vancouver[1],  '*', markerfacecolor='y', markeredgecolor='r', markersize=12)
```

```python
import pandas as pd
participants2017 = pd.read_csv('data/participants2017.csv',encoding='latin-1')
vancouver = (-123.1207, 49.2827)


from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
           plt.plot(*geom.exterior.xy, color='grey')
    else:
        plt.plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2017.iterrows():
    plt.plot(p['lon'], p['lat'], 'o', markerfacecolor='r', markeredgecolor='r')     


for idx, p in participants2017.iterrows():
    waypoints = geod.npts(vancouver[0], vancouver[1], p['lon'], p['lat'], 20)
    route = [vancouver]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        plt.plot(route[:min_index,0], route[:min_index,1], color='r')
        plt.plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    plt.plot(route[:,0], route[:,1], color='r')
plt.plot(vancouver[0],vancouver[1],  '*', markerfacecolor='y', markeredgecolor='r', markersize=12)
```

## Subplots

```python
fig, axes = plt.subplots(2, 2)
#axes[0, 0].plot(x, y)
#axes[1, 1].scatter(x, y)
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            axes[0,0].plot(*geom.exterior.xy, color='grey')
    else:
        axes[0,0].plot(*sf.exterior.xy, color='grey')
participants2016 = pd.read_csv('data/participants2016.csv',encoding='latin-1')
    
for idx, p in participants2016.iterrows():
    axes[0,0].plot(p['lon'], p['lat'], 'o', markerfacecolor='b', markeredgecolor='b')     
    
for idx, p in participants2016.iterrows():
    waypoints = geod.npts(minn[0], minn[1], p['lon'], p['lat'], 20)
    route = [minn]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    axes[0,0].plot(route[:,0], route[:,1], color='b')
    axes[0,0].title.set_text('2016')


axes[0,0].axis('off')

# 2017

participants2017 = pd.read_csv('data/participants2017.csv', encoding='latin-1')

vancouver = (-123.1207, 49.2827)


from shapely.geometry import shape
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            axes[0,1].plot(*geom.exterior.xy, color='grey')
    else:
        axes[0,1].plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2017.iterrows():
    axes[0,1].plot(p['lon'], p['lat'], 'o', markerfacecolor='r', markeredgecolor='r')     


for idx, p in participants2017.iterrows():
    waypoints = geod.npts(vancouver[0], vancouver[1], p['lon'], p['lat'], 20)
    route = [vancouver]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        axes[0,1].plot(route[:min_index,0], route[:min_index,1], color='r')
        axes[0,1].plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    axes[0,1].plot(route[:,0], route[:,1], color='r')
    axes[0,1].title.set_text('2017')
    axes[0,1].axis('off')


# 2018

for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            axes[1,0].plot(*geom.exterior.xy, color='grey')
    else:
        axes[1,0].plot(*sf.exterior.xy, color='grey')

for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        axes[1,0].plot(route[:min_index,0], route[:min_index,1], color='g')
        axes[1,0].plot(route[min_index:,0], route[min_index:,1], color='g')
        continue
    axes[1,0].plot(route[:,0], route[:,1], color='g')   
    axes[1,0].title.set_text('2018')

for idx, p in participants2018.iterrows():
    axes[1,0].plot(p['lon'], p['lat'], 'o', markerfacecolor='g', markeredgecolor='g')     
axes[1,0].axis('off')


# all three years
for feature in g['features']:
    sf = shape(feature['geometry'])
    if feature['geometry']['type'] == 'MultiPolygon':
        for geom in sf.geoms:
            axes[1,1].plot(*geom.exterior.xy, color='grey')
    else:
        axes[1,1].plot(*sf.exterior.xy, color='grey')
    
for idx, p in participants2016.iterrows():
    axes[1,1].plot(p['lon'], p['lat'], 'o', markerfacecolor='b', markeredgecolor='b')     
    
for idx, p in participants2016.iterrows():
    waypoints = geod.npts(minn[0], minn[1], p['lon'], p['lat'], 20)
    route = [minn]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    axes[1,1].plot(route[:,0], route[:,1], color='b')

    

for idx, p in participants2017.iterrows():
    axes[1,1].plot(p['lon'], p['lat'], 'o', markerfacecolor='r', markeredgecolor='r')     


for idx, p in participants2017.iterrows():
    waypoints = geod.npts(vancouver[0], vancouver[1], p['lon'], p['lat'], 20)
    route = [vancouver]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        axes[1,1].plot(route[:min_index,0], route[:min_index,1], color='r')
        axes[1,1].plot(route[min_index:,0], route[min_index:,1], color='r')
        continue
    axes[1,1].plot(route[:,0], route[:,1], color='r')   
    

    
 
for idx, p in participants2018.iterrows():
    waypoints = geod.npts(sanantonio[0], sanantonio[1], p['lon'], p['lat'], 20)
    route = [sanantonio]
    route.extend(waypoints)
    route.append((p['lon'], p['lat']))
    route = np.array(route)
    if (route[:,0].max()-route[:,0].min())>180:
        min_index = route[:,0].argmin()+1
        axes[1,1].plot(route[:min_index,0], route[:min_index,1], color='g')
        axes[1,1].plot(route[min_index:,0], route[min_index:,1], color='g')
        continue
    axes[1,1].plot(route[:,0], route[:,1], color='g')   
    
for idx, p in participants2018.iterrows():
    axes[1,1].plot(p['lon'], p['lat'], 'o', markerfacecolor='g', markeredgecolor='g')   
axes[1,1].title.set_text('2016-2018')

axes[1,1].axis('off')




fig.set_size_inches(18.5, 10.5, forward=True)
plt.savefig(fname='quad.png')
```

```python

```
