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

Introduction to GeoPandas
=========================

[Serge Rey](http://sergerey.org)

The second library in the Python geospatial stack that we examine is
[GeoPandas](http://geopandas.org/). GeoPandas builds on the capabilities
of Shapely and combines these with the popular
[pandas](http://pandas.pydata.org) library that provides
high-performance and easy-to-use data structures for data analysis in
Python.

Objectives
----------

-   Understand GeoDataSeries and GeoDatatFrames
-   Learn reading and writing common vector spatial data formats
-   Carry out geoprocessing with GeoPandas

Setup and Imports
-----------------

We utilize our common imports

```python
%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
```

and import geopandas as an alias `gpd`

```python
import geopandas as gpd
```

GeoPandas Structure
===================

As mentioned above, geopandas builds on-top of shapely which means we
have access to all the functionality we saw in the previous notebook. To
get a better sense of this connection, let\'s create a few shapely
Polygons and then see how they are used in geopandas:

```python
from shapely.geometry import Polygon
poly_1 = Polygon([ (0,0), (0,10), (10, 10), (10, 0) ] )
poly_2 = Polygon([ (10,0), (10,10), (20, 10), (20, 0) ] )
poly_3 = Polygon([ (20,0), (20,10), (30, 10), (30, 0) ] )
```

GeoSeries: Putting the Geo in GeoPandas
---------------------------------------

We are going to combine these three polygons in a geopandas `GeoSeries`:

```python
polys = gpd.GeoSeries([poly_1, poly_2, poly_3])
polys.plot(edgecolor='k')
```

The `GeoSeries` can be thought of as a vector, with each element of the
vector corresponding to one or more Shapely geometry objects:

```python
polys
```

so here we see three elements, each of type `POLYGON` along with their
coordinates.

```python attributes={"classes": ["py"], "id": ""}
type(polys)
```

Depending on what we need, we can either work on an *element-wise* basis
or with the geoseries as a unified object. For example, an example of
the former is:

```python
polys.bounds
```

which returns the bounds of each of the polygons. Alternatively, if we
want the bounds for the collection:

```python
polys.total_bounds
```

Binary operations between two geoseries will be carried out element
wise, and this can lead to some counter intuitive results. For example,
a second `GeoSeries` created as:

```python
from shapely.geometry import Point
p_1 = Point(15, 5)
p_2 = Point(25, 9)
points = gpd.GeoSeries([p_1, p_2])
points.plot()
```

consists of two points. Each of the points is contained by the `polys`
`GeoSeries`:

```python
polys.contains(p_1)
```

and

```python
polys.contains(p_2)
```

Plotting the two `GeoSeries` confirms this:

```python
ax = plt.gca()
polys.plot(ax=ax, edgecolor='k')
points.plot(ax=ax, edgecolor='r', facecolor='r')
plt.show()
```

Yet, when we check if the points as a `GeoSeries` are contained by the
`polys` `GeoSeries` we get:

```python
polys.contains(points)
```

This is because the first point is not contained in the first polygon,
and the second point is not contained in the second polygon, while there
is no third point.

A second point geoseries can clarify this:

```python
points = gpd.GeoSeries([Point(5,5), Point(15, 6), Point([25,9])])
polys.contains(points)
```

whereas if we change the ordering of the second and third points we get:

```python
points = gpd.GeoSeries([Point(5,5), Point(25, 9), Point([15,6])])
polys.contains(points)
```

GeoDataFrame: Putting the Panda in GeoPandas
--------------------------------------------

-   geometry column is populated with a geoseries
-

```python
polys_df = gpd.GeoDataFrame({'names': ['west', 'central', 'east'], 'geometry': polys})
polys_df
```

The dataframe provides the ability to add add additional columns:

```python
polys_df['Unemployment'] = [ 7.8, 5.3, 8.2]
polys_df
```

and it supports different types of subsetting and traditional (i.e.,
nonspatial) queries. For example, find the regions with unemployment
rates above 6 percent:

```python
polys_df[polys_df['Unemployment']>6.0]
```

There is nothing sacred about the column labeled \'geometry\' in the
GeoDataFrame. Moreover, we can add additional GeoSeries to the same
dataframe, as they will be treated as regular columns. However, only one
GeoSeries can serve as the column against which any spatial methods are
applied when called upon. This column can be accessed through the
`geometry` attribute of the `GeoDataFrame`:

```python
polys_df.geometry
```

Let\'s create a new Points GeoSeries and add it to this GeoDataFrame as
a regular column:

```python
points = gpd.GeoSeries([Point(5,5), Point(15, 6), Point([25,9])])
polys_df['points'] = points
polys_df.geometry
```

So the `polys` column is currently serving as the `geometry` property
for the `GeoDataFrame` and `points` is just another column:

```python
polys_df
```

so when we call the `plot` method we get the polygon representation:

```python
polys_df.plot(edgecolor='k')
```

However, if we explicity set the geometry property (and assign this to a
new object with the same name), and plot, things change:

```python
polys_df = polys_df.set_geometry('points')
polys_df.plot()
```

and this is because

```python
polys_df.geometry
```

Read a Polygon Shapefile
========================

```python
tracts_df = gpd.read_file('data/california_tracts.shp')
```

```python
tracts_df.head()
```

```python
tracts_df.shape
```

```python
tracts_df.plot()
```

```python
tracts_df.crs
```

```python
tracts_df.columns
```

Read a Point Shapefile
======================

```python
clinics_df = gpd.read_file('data/behavioralHealth.shp')
```

```python
clinics_df.plot()
```

```python
clinics_df.columns
```

```python
clinics_df.shape
```

```python
clinics_df['geometry'].head()
```

What we want to do now is focus on the relationships between the
locations of these clinics in Riverside county and the census tracts in
that county. We have two issues to deal with in order to do so.

First, our dataframe for the tracts includes all 58 counties, whereas we
only need Riverside county. Second, if you look closely at the plot of
the clinics you will see that the units on the axes are different from
those in the plot of the census tracts. This is because the two
dataframes have different coordinate reference systems (CRS).

Extracting Riverside County Tracts {#riverside-county}
==================================

```python
riverside_tracts = tracts_df[tracts_df['GEOID10'].str.match("^06065")]
```

```python
riverside_tracts.plot()
```

Coordinate Reference Systems
============================

Spatial Joins
=============

Let\'s find out which tracts have clinics.

```python
clinics_df.plot()
```

```python
clinics_df.to_crs(riverside_tracts.crs).plot()
```

```python
# convert crs of clinics to match that of tracts
clinics_df = clinics_df.to_crs(riverside_tracts.crs)
```

```python
clinics_df.plot()
```

```python
clinics_tracts = gpd.sjoin(clinics_df, riverside_tracts, op='within')
```

```python
clinics_tracts.head()
```

```python
clinics_tracts.shape
```

```python
clinics_df.columns
```

```python
clinics_tracts.columns
```

```python
# GEOID10 is now attached to each clinic (i.e., tract identifier)
```

```python
clinics_tracts[['GEOID10', 'index_right']].groupby('GEOID10').agg('count')
```

```python
clinics_tracts.groupby(['GEOID10']).size()
```

```python
clinics_tracts.groupby(['GEOID10']).size().reset_index(name='clinics')
```

```python
twc = clinics_tracts.groupby(['GEOID10']).size().reset_index(name='clinics')
```

```python
twc.plot()
```

```python
riverside_tracts_clinics = riverside_tracts.merge(twc, how='left', on='GEOID10')
```

```python
riverside_tracts_clinics.head()
```

```python
riverside_tracts_clinics.fillna(value=0, inplace=True)
```

```python
riverside_tracts_clinics.head()
```

```python
riverside_tracts_clinics['clinics'].sum()
```

Writing Shapefiles
==================

```python
# save to a new shapefile
riverside_tracts_clinics.to_file('data/clinics.shp')
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Introduction to GeoPandas</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

```python

```

```python

```

```python

```
