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

<!-- #region -->

## Local Autocorrelation: Hot Spots, Cold Spots, and Spatial Outliers ##

In addition to the Global autocorrelation statistics, PySAL has many local
autocorrelation statistics. Let's compute a local Moran statistic for the same
dataset we used previously.



## Imports
<!-- #endregion -->

```python
import pandas as pd
import geopandas as gpd
import libpysal as lp
import matplotlib.pyplot as plt
import rasterio as rio
import numpy as np
import contextily as ctx
import shapely.geometry as geom
%matplotlib inline
```


```python
df = gpd.read_file("data/airbnb.shp")
np.random.seed(12345)
import esda
```

```python
wq = lp.weights.Queen.from_dataframe(df)
wq.transform = 'r'
lag_price = lp.weights.lag_spatial(wq, df['median_pri'])
y = df['median_pri']

```

```python
price = df['median_pri']
b, a = np.polyfit(price, lag_price, 1)
f, ax = plt.subplots(1, figsize=(9, 9))

plt.plot(price, lag_price, '.', color='firebrick')

 # dashed vert at mean of the price
plt.vlines(price.mean(), lag_price.min(), lag_price.max(), linestyle='--')
 # dashed horizontal at mean of lagged price 
plt.hlines(lag_price.mean(), price.min(), price.max(), linestyle='--')

# red line of best fit using global I as slope
plt.plot(price, a + b*price, 'r')
plt.title('Moran Scatterplot')
plt.ylabel('Spatial Lag of Price')
plt.xlabel('Price')
plt.show()

```

Now, instead of a single $I$ statistic, we have an *array* of local $I_i$
statistics, stored in the `.Is` attribute, and p-values from the simulation are
in `p_sim`.

```python
li = esda.moran.Moran_Local(y, wq)
```

```python
li.q
```

We can again test for local clustering using permutations, but here we use
conditional random permutations (different distributions for each focal location)

```python
(li.p_sim < 0.05).sum()
```

We can distinguish the specific type of local spatial association reflected in
the four quadrants of the Moran Scatterplot above:

```python
sig = li.p_sim < 0.05
hotspot = sig * li.q==1
coldspot = sig * li.q==3
doughnut = sig * li.q==2
diamond = sig * li.q==4
```

```python
spots = ['n.sig.', 'hot spot']
labels = [spots[i] for i in hotspot*1]
```

```python
df = df
from matplotlib import colors
hmap = colors.ListedColormap(['red', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True, \
        k=2, cmap=hmap, linewidth=0.1, ax=ax, \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
```

```python
spots = ['n.sig.', 'cold spot']
labels = [spots[i] for i in coldspot*1]
```

```python
df = df
from matplotlib import colors
hmap = colors.ListedColormap(['blue', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True, \
        k=2, cmap=hmap, linewidth=0.1, ax=ax, \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
```

```python
spots = ['n.sig.', 'doughnut']
labels = [spots[i] for i in doughnut*1]
```

```python
df = df
from matplotlib import colors
hmap = colors.ListedColormap(['lightblue', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True, \
        k=2, cmap=hmap, linewidth=0.1, ax=ax, \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
```

```python
spots = ['n.sig.', 'diamond']
labels = [spots[i] for i in diamond*1]
```

```python
df = df
from matplotlib import colors
hmap = colors.ListedColormap(['pink', 'lightgrey'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True, \
        k=2, cmap=hmap, linewidth=0.1, ax=ax, \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
```

```python
sig = 1 * (li.p_sim < 0.05)
hotspot = 1 * (sig * li.q==1)
coldspot = 3 * (sig * li.q==3)
doughnut = 2 * (sig * li.q==2)
diamond = 4 * (sig * li.q==4)
spots = hotspot + coldspot + doughnut + diamond
spots
```

```python
spot_labels = [ '0 ns', '1 hot spot', '2 doughnut', '3 cold spot', '4 diamond']
labels = [spot_labels[i] for i in spots]
```

```python

from matplotlib import colors
hmap = colors.ListedColormap([ 'lightgrey', 'red', 'lightblue', 'blue', 'pink'])
f, ax = plt.subplots(1, figsize=(9, 9))
df.assign(cl=labels).plot(column='cl', categorical=True, \
        k=2, cmap=hmap, linewidth=0.1, ax=ax, \
        edgecolor='white', legend=True)
ax.set_axis_off()
plt.show()
```

## Putting it all together

```python
from pysal.explore import esda
from pysal.viz.splot import esda as esdaplot
```

```python
lisa = esda.Moran_Local(df["median_pri"], wq)
```

```python
esdaplot.lisa_cluster(lisa, df);
```

```python
esdaplot.plot_local_autocorrelation(lisa, df, "median_pri");
```

## P-values revisited

```python
lisa = esda.Moran_Local(df["median_pri"], wq)
```

```python
f, axs = plt.subplots(1, 3, figsize=(16, 3))
for i, ax in zip([0.05, 0.01, 0.001], axs):
    esdaplot.lisa_cluster(lisa, df, p=i, ax=ax)
    ax.set_title(f"Significance level = {i}")
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Repeat the local analysis using rook contiguity and knn4. How do the results compare across different spatial weights?</div>

```python
# %load solutions/320_1.py
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Local Spatial Autocorrelation</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
