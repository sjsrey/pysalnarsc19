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

# Spatial Weights: Case Study

- [Introduction](#Introduction)
- [Data](#Data)
- [TAZ Contiguity](#Construct-a-Rook-contiguity-weight)
- [Counties as sets](#Counties-as-sets)
- [Block weights](#Block-weights)
- [Intersection weights](#Intersection-weights)

## Introduction
This notebook illustrates the use of PySAL weights in preparing input to a
spatial optimization model. It makes use of the `set-theoretic` functionality
that the weights class affords.

The researcher is building an optimization model to partition traffic analysis
zones (TAZs) subject to contiguity constraints and a boundary condition, such
that flows between TAZs assigned to the same group are maximized, but flows
cannot cross specified boundaries. The problem facing the research is to develop
a representation of neighbor relations as input to the spatial optimization
model.


## Data
The data under consideration is a set of *Traffic Analysis Zones* (TAZs) in Southern California.
We first read these in and visualize the context:

```python
import numpy as np
import libpysal 
import random as rdm
import geopandas as gpd
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
%matplotlib inline
```

```python
shp = gpd.read_file(libpysal.examples.get_path("taz.shp"))
shp.head()
```

```python
shp.plot(figsize=(15,15),color='white', edgecolor='grey')
plt.axis('off')
```


### Construct a Rook contiguity weight
The researcher first needs to define the adjacency relations between the TAZs. Here the *rook* criterion is used:

```python
wrook = libpysal.weights.Rook.from_dataframe(shp)
```

```python
def w2line_graph(w, shp):
    segments = []
    centroids = shp.centroid.values
    for i in w.id2i:
        origin = np.array(centroids[i].coords)[0] 
        for j in w.neighbors[i]:
            dest = np.array(centroids[j].coords)[0]
            ij = [i,j]
            ij.sort()
            segments.append([origin, dest])

    return segments    
```

```python
segs = w2line_graph(wrook, shp)
fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal')
shp.plot(ax=ax, color='white', edgecolor='grey')
segs_plot = LineCollection(np.array(segs),colors="red")
segs_plot.set_linewidth(0.20)
ax.add_collection(segs_plot)
ax.set_axis_off()
```

We can zoom into a more dense area of the region by setting the view limits on the axis object:

```python
segs = w2line_graph(wrook, shp)
fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal')
shp.plot(ax=ax, color='white', edgecolor='grey')
segs_plot = LineCollection(np.array(segs),colors="red")
segs_plot.set_linewidth(0.20)
ax.add_collection(segs_plot)
_ = ax.set_xlim(360000, 400000)
_ = ax.set_ylim(3730000, 3780000)

#ax.set_axis_off()
```
Note that we have commented out the call to turn the axis off. 

## Counties as sets
The county boundaries are going to play the role of the sets. 

```python
shp["CNTY"].describe()
```

```python
fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal')
shp.plot(ax=ax,color='white', edgecolor='black')
shp.plot(column="CNTY", ax=ax, categorical=True,cmap="Pastel1",alpha=0.6)
ax.set_axis_off()
```
## Block weights

As we learned previously, block weights use a *regime variable* that partitions the observations into exhaustive and mutually exclusive groups. All members belonging to the same group are treated as pair-wise neighbors.

```python
libpysal.weights.block_weights?
```

Given this, we can use the `CNTY` attribute as our membership variable:

```python
wb = libpysal.weights.block_weights(shp["CNTY"])
```

Notice the warning about 6 disconected components. This is definitely a feature here, as the model precludes TAZs from different counties forming a neighbor pair.

Examining the block weight, we learn that it is much more dense than
 than the simple rook contiguity graph:

```python
print(wb.pct_nonzero, wrook.pct_nonzero)
```


## Intersection weights

We now have two weights objects that we can use to arrive at the desired neighbor graph. The rook weights object defines all TAZs that share an edge, including those pairs belonging to different counties. We want all of these pairs with the exception of the latter. The block weights define as neighbors all pairs of TAZs belonging to the same county. The intersection of these two weights objects will give us what we need:

```python
wint = libpysal.weights.w_intersection(wb, wrook)
```

```python
segs = w2line_graph(wint, shp)
fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal')
shp.plot(ax=ax, color='white', edgecolor='grey')
segs_plot = LineCollection(np.array(segs),colors="red")
segs_plot.set_linewidth(0.20)
ax.add_collection(segs_plot)
ax.set_axis_off()
```

```python
fig, ax = plt.subplots(figsize=(15,15))
ax.set_aspect('equal')
shp.plot(ax=ax,color='white', edgecolor='black')
shp.plot(column="CNTY", ax=ax, categorical=True,cmap="Pastel1",alpha=0.6)
segs_plot = LineCollection(np.array(segs),colors="red")
segs_plot.set_linewidth(0.20)
ax.add_collection(segs_plot)
ax.set_axis_off()
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Spatial Weights: Case Study</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
