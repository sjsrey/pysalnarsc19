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

# Spatial Weights



Spatial weights are mathematical structures used to represent spatial relationships. Many spatial analytics, such as spatial autocorrelation statistics and regionalization algorithms rely on spatial weights. Generally speaking, a spatial weight $w_{i,j}$ expresses the notion of a geographical relationship between locations $i$ and $j$. These relationships can be based on a number of criteria including contiguity, geospatial distance and general distances.

libpysal offers functionality for the construction, manipulation, analysis, and conversion of a wide array of spatial weights.

We begin with construction of weights from common spatial data formats.


```python
import libpysal 
from libpysal.weights import Queen, Rook, KNN, Kernel
import numpy as np
import geopandas
import pandas
%matplotlib inline
import matplotlib.pyplot as plt
```

There are functions to construct weights directly from a file path. 


## Weight Types


### Contiguity

#### Queen Weights


A commonly-used type of weight is a queen contigutiy weight, which reflects adjacency relationships as a binary indicator variable denoting whether or not a polygon shares an edge or a vertex with another polygon. These weights are symmetric, in that when polygon $A$ neighbors polygon $B$, both $w_{AB} = 1$ and $w_{BA} = 1$.

To construct queen weights from a shapefile, we will use geopandas to read the file into a GeoDataFrame, and then use   libpysal to construct the weights:

```python
shp_path = "data/texas.shp"
df = geopandas.read_file(shp_path)
df.head()
```

```python
qW = Queen.from_dataframe(df)
```

```python
qW
```

All weights objects have a few traits that you can use to work with the weights object, as well as to get information about the weights object. 

To get the neighbors & weights around an observation, use the observation's index on the weights object, like a dictionary:

```python
qW[155] #neighbors & weights of the 156th observation (0-index remember)
```

By default, the weights and the pandas dataframe will use the same index. So, we can view the observation and its neighbors in the dataframe by putting the observation's index and its neighbors' indexes together in one list:

```python
self_and_neighbors = [155]
self_and_neighbors.extend(qW.neighbors[155])
print(self_and_neighbors)
```

and grabbing those elements from the dataframe:

```python
df.loc[self_and_neighbors]
```

A full, dense matrix describing all of the pairwise relationships is constructed using the `.full` method, or when `libpysal.weights.full` is called on a weights object:

```python
Wmatrix, ids = qW.full()
#Wmatrix, ids = libpysal.weights.full(qW)
```

```python
Wmatrix
```

```python
n_neighbors = Wmatrix.sum(axis=1) # how many neighbors each region has
```

```python
n_neighbors[155]
```

```python
qW.cardinalities[155]
```

Note that this matrix is binary, in that its elements are either zero or one, since an observation is either a neighbor or it is not a neighbor. 

However, many common use cases of spatial weights require that the matrix is row-standardized. This is done simply in PySAL using the `.transform` attribute

```python
qW.transform = 'r'
```

Now, if we build a new full matrix, its rows should sum to one:

```python
Wmatrix, ids = qW.full()
```

```python
Wmatrix.sum(axis=1) #numpy axes are 0:column, 1:row, 2:facet, into higher dimensions
```

Since weight matrices are typically very sparse, there is also a sparse weights matrix constructor:

```python
qW.sparse
```

```python
qW.pct_nonzero #Percentage of nonzero neighbor counts
```

Let's look at the neighborhoods of the 101th observation - Howard County, Texas

```python
df.iloc[100]
```

```python
qW.neighbors[100]
```

```python
len(qW.neighbors[100])
```

```python
df.iloc[qW.neighbors[100]]
```

```python
df.assign(weights = qW.sparse[100,:].toarray().flatten()).plot('weights', cmap='plasma')           
```

By default, PySAL assigns each observation an index according to the order in which the observation was read in. This means that, by default, all of the observations in the weights object are indexed by table order.

```python
pandas.Series(qW.cardinalities).plot.hist(bins=9)
```

```python
qW.cardinalities.values()
```

#### Rook Weights


Rook weights are another type of contiguity weight, but consider observations as neighboring only when they share an edge. The rook neighbors of an observation may be different than its queen neighbors, depending on how the observation and its nearby polygons are configured. 

We can construct this in the same way as the queen weights:

```python
rW = Rook.from_dataframe(df)
```

```python
rW.neighbors[100]
```

```python
len(rW.neighbors[100])
```

```python
df.iloc[rW.neighbors[100]]
```

```python
df.assign(weights = rW.sparse[100,:].toarray().flatten()).plot('weights', cmap='plasma')
```

```python
pandas.Series(rW.cardinalities).plot.hist(bins=9)
```

#### Bishop Weights


In theory, a "Bishop" weighting scheme is one that arises when only polygons that share vertexes are considered to be neighboring. But, since Queen contiguigy requires either an edge or a vertex and Rook contiguity requires only shared edges, the following relationship is true:

$$ \mathcal{Q} = \mathcal{R} \cup \mathcal{B} $$

where $\mathcal{Q}$ is the set of neighbor pairs *via* queen contiguity, $\mathcal{R}$ is the set of neighbor pairs *via* Rook contiguity, and $\mathcal{B}$ *via* Bishop contiguity. Thus:

$$ \mathcal{Q} \setminus \mathcal{R} = \mathcal{B}$$

Bishop weights entail all Queen neighbor pairs that are not also Rook neighbors.

PySAL does not have a dedicated bishop weights constructor, but you can construct very easily using the `w_difference` function. This function is one of a family of tools to work with weights, all defined in `libpysal.weights`, that conduct these types of set operations between weight objects.

```python
bW = libpysal.weights.w_difference(qW, rW, constrained=False)
```

```python
bW = libpysal.weights.w_difference(qW, rW, constrained=False)
```

```python
df.assign(weights = bW.sparse[100,:].toarray().flatten()).plot('weights', cmap='plasma')
```

```python
bW.histogram
```

Thus, the vast majority of counties have no bishop neighbors. But, a few do. A simple way to see these observations in the dataframe is to find all elements of the dataframe that are not "islands," the term for an observation with no neighbors:

```python
islands = bW.islands
```

```python
bW
```

```python
# Using `.head()` to limit the number of rows printed
df.query('FIPS not in @islands').head()
```

## Distance


There are many other kinds of weighting functions in PySAL. Another separate type use a continuous measure of distance to define neighborhoods. 

```python
radius_mile = libpysal.cg.sphere.RADIUS_EARTH_MILES
radius_mile
```

great circle (arc) distance -  maximum nearest neighbor distance in miles between the $n$ observations

```python
threshold = libpysal.weights.min_threshold_dist_from_shapefile('data/texas.shp',
                                                               radius=radius_mile) 
```

```python
threshold
```

```python
radius_km = libpysal.cg.sphere.RADIUS_EARTH_KM
radius_km
```

```python
libpysal.weights.min_threshold_dist_from_shapefile('data/texas.shp',
                                                               radius=radius_km) 
```

```python
libpysal.weights.min_threshold_dist_from_shapefile('data/texas.shp')
```

### knn defined weights

```python
knn4_bad = KNN.from_dataframe(df, k=4) # ignore curvature of the earth
```

```python
knn4_bad.histogram
```

```python
knn4 = KNN.from_dataframe(df, k=4, radius=radius_mile)
```

```python
knn4.histogram
```

```python
knn4[0]
```

```python
knn4_bad[0]
```

```python
knn4_bad.neighbors == knn4.neighbors
```

```python

df.assign(weights = 
          knn4_bad.sparse[0,:].toarray().flatten()).plot('weights', 
                                                           cmap='plasma')
```

```python

df.assign(weights = 
          knn4.sparse[0,:].toarray().flatten()).plot('weights', 
                                                           cmap='plasma')
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Enumerate the counties for which ignoring curvature results in an incorrect neighbor set for knn.
</div>

```python
# %load solutions/300_1.py
```

### Kernel W


Kernel Weights are continuous distance-based weights that use kernel densities to define the neighbor relationship.
Typically, they estimate a `bandwidth`, which is a parameter governing how far out observations should be considered neighboring. Then, using this bandwidth, they evaluate a continuous kernel function to provide a weight between 0 and 1.

Many different choices of kernel functions are supported, and bandwidths can either be fixed (constant over all units) or adaptive in function of unit density.

For example, if we want to use **adaptive bandwidths for the map and weight according to a gaussian kernel**:


#### Adaptive gaussian kernel weights

bandwidth = the distance to the kth nearest neighbor for each
                  observation
   
bandwith is changing across observations

```python
kernelWa = Kernel.from_dataframe(df, k=10, fixed=False, function='gaussian')
df.assign(weights = 
          kernelWa.sparse[100,:].toarray().flatten()).plot('weights', 
                                                           cmap='plasma')
```

```python
kernelWa.bandwidth
```

```python
df.assign(bw=kernelWa.bandwidth.flatten()).plot('bw', cmap='Reds')
```

**fixed bandwidths for the map and weight according to a gaussian kernel**

bandwidth = maximum of (the distances to the kth nearest neighbor for all observations)

```python
kernelWa = Kernel.from_dataframe(df, k=2, fixed=True, function='gaussian')

df.assign(weights=kernelWa.sparse[100,:].toarray().flatten()).plot('weights', cmap='plasma')

```

```python
kernelWa = Kernel.from_dataframe(df, k=2, fixed=True, function='gaussian')

df.assign(weights=kernelWa.sparse[1,:].toarray().flatten()).plot('weights', cmap='plasma')
```

```python
kernelWa.bandwidth
```

```python
df.assign(bw=kernelWa.bandwidth.flatten()).plot('bw', cmap='Reds')
```

## Block Weights

```python
w,s,e,n = df.total_bounds
```

```python
mx = (w+e)/2
my = (n+s)/2
```

```python
import shapely
```

```python
centroids = df.geometry.centroid
```

```python
lon = centroids.apply(lambda p: p.x).values
lat = centroids.apply(lambda p: p.y).values
```

```python
north = lat > my
south = lat <= my
east = lon > mx
west = lon <= mx
```

```python
nw = west * north * 2
ne = east * north * 1
sw = west * south * 3
se = east * south *4
quad = nw + ne + sw + se
```

```python
quad
```

```python
df['quad'] = quad
df.plot(column="quad", categorical=True)
```

```python
blockW = libpysal.weights.block_weights(df["quad"])
```

```python
blockW.n
```

```python
blockW.pct_nonzero
```

```python
pandas.Series(blockW.cardinalities).plot.hist()
```

```python
df.groupby(by='quad').count()
```

```python
rW.plot(df)
```

```python
qW.plot(df)
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
    Which spatial weights structure would be more dense, Texas counties based on rook contiguity or Texas counties based on knn with k=4?
</div>

```python
# %load solutions/300_2.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
    Which counties have fewer neighbors under rook contiguity relative to knn4?
</div>

```python
# %load solutions/300_3.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
    Which counties have identicical neighbors under queen contiguity and queen rook contiguity?
</div>

```python
# %load solutions/300_4.py
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Spatial Weights</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
