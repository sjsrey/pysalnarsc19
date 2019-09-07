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

Geoprocessing with GeoPandas
============================

[Serge Rey](http://sergerey.org)

We continue exploring geopandas and more of its geoprocessing
capabilities. In this notebook we assume the role of a social scientist
who is interested in the topic of environmental equity. They are broadly
concerned with the question of whether different racial groups are
exposed to different levels of environmental hazards in urban settings.

Their empirical analysis will focus on the case of Riverside County, CA,
where the spatial unit of analysis is the Census tract which we
encountered and processed in the previous notebook. The researcher will
examine the spatial relationships between the highway network and the
census tracts to develop operational measures that feed into their
environmental equity analysis.

In this notebook we focus on generating new features that will be used
in subsequent econometric modeling to test various hypothesis about
environmental justice. We want to create new variables that express the
exposure to the highway network for census tracts in Riverside, CA.

Objectives
----------

-   Processing polyline shapefiles to represent road networks
-   Learn about geographical clipping
-   Integrate spatial data sources with different coordinate reference
    systems
-   Apply buffering to derive new features for subsequent analysis

Setup and Imports
-----------------

Again we begin with our usual imports:

```python
%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
```

```python
import geopandas as gpd
```

Read a LineString Shapefile
===========================

Thus far we have encountered two different types of geometries in our
shapefiles, namely point and polygons. For our current research, are
going to examine the data set [\"Sanctioned routes for commercial truck
traffic located on the state highway
system](http://www.dot.ca.gov/hq/tsip/gis/datalibrary/Metadata/Trknet.html)\"
from the California Department of Transportation. That has been
downloaded and stored in the `data` directory.

We begin by reading this into a geopandas DataFrame:

```python
routes_df = gpd.read_file('data/Truck_Route_Network.shp')
```

and taking a view of the features

```python
routes_df.plot()
```

Futhter exploration reveals the geometries are LineStrings

```python
routes_df.head()
```

```python
routes_df['geometry'].head()
```

Since we will be using this layer with other spatial datasets, it is
good practice to familiarlize ourselves with the Coordinate Reference
System:

```python
routes_df.crs
```

```python
routes_df.shape
```

So the coordinates in our LineStrings are in longitude and latitude.

Route Clipping
==============

The researcher has the truck route network for the entire state of
California. However, her interest is on the specific case of Riverside
County so she needs a way to extract the portions of the network that
are within the county. This can be done using the geoprocessing
operation *clipping*.

To do this we need to create a layer that will serve to \"clip\" the
road network layer to remove everything outside of Riverside County. We
can use the polygon shapefile we created from the previous notebook:

Read a Polygon Shapefile
------------------------

```python
tracts_df = gpd.read_file('data/clinics.shp')
```

```python
tracts_df.head()
```

```python
tracts_df.plot()
```

Get routes intersecting Riverside County
----------------------------------------

To select only the routes within Riverside County we could take several
approaches. We have the tract layer for the county that has 453 tracts,
as well as the road network layer for the state. That has 966 segments.
We could then use the intersects method for each tract to test if it
intersects with a particular segment of the road network, and then keep
all the segments where we find an intersection with the tract.

While this would work, it turns out to be very inefficient as a brute
force approach would require we compare each of 453 tracts against each
of 966 segments and test for an intersection.

We can do better.

If we think about our problem from a slightly different perspective, we
know that if we find a segment that intersects with a tract within
Riverside county, it must, by definition, intersect with the County
polygon, if we had such a thing.

This would substantially reduce the number of intersection tests (or
more broadly, \"hit tests\") we need to conduct. Rather than having to
compare 453 tract polygons with 966 road segments, we now only need
compare 1 polygon against each of the road segments. That is a 453X
reduction in computation. Nice.

### Dissolve

Ok, but we do not yet have the magical county polygon. It seems worth it
to get one, and using another method of the geopandas DataFrame for the
tracts, we can. First, we can re-examine our DataFrame:

```python
tracts_df.plot(edgecolor='k')
```

What we are going to do is dissolve all the tract boundaries that do not
coincide with the boundary of the DataFrame\'s geometry collection.

This is done by creating a new attribute that takes on the same values
for each feature, and calling the `dissovle` method with that attribute
as the argument to the `by` option:

```python
tracts_df['dummy'] = 1.0
county = tracts_df.dissolve(by='dummy')
```

```python
county.plot()
```

```python
county.shape
```

Note that we could have also obtained this polygon by using the
`unary_union` method of the GeoSeries:

```python
county_uu = tracts_df['geometry'].unary_union
county_uu
```

This gives us a Shapely Polygon. We would then have toconstruct a new
GeoDataFrame with this as the Geometry column. Instead, we will continue
with the `county` DataFrame obtained from the dissolve operation since
this saves us one step. (We simply note the unary~union~ as you never
know when you may need it.)

We now have our single polygon for the county.

In our earlier notebook we saw that care needs to be taken when testing
for intersections between features from two different DataFrames, as
this is done on an element-wise basis.

There are a couple of ways to handle this. First, using what are known
as **lambdas**:

```python
r = routes_df['geometry']
```

```python
type(r)
```

```python
r.apply(lambda x: x.intersects(county.iloc[0]['geometry']))
```

```python
rc_routes = r[r.apply(lambda x: x.intersects(county.iloc[0]['geometry']))]
```

```python
rc_routes.shape
```

```python
rc_routes.plot()
```

Plotting the two layers to see what we are now working with gives us:

```python
ax = plt.gca()
rc_routes.plot(ax=ax, edgecolor='k')
county.plot(ax=ax)
plt.show()
```

Lambdas are handy, but tend to make code a little more difficult to
read. Technically they are known as \"anonymous functions\". A more
transparent approach is to use a simple loop and test each route segment
for intersection with the county, and append the segment to a list to
store all the segments that intersect with the county:

```python
geoms = []
for idx, route in enumerate(rc_routes):
    print(idx)
    geoms.append(route.intersection(county.iloc[0]['geometry']))
```

Now we use this Python list of intersection objects (which are segments)
into a GeoSeries:

```python
rc_hw = gpd.GeoSeries(geoms)
rc_hw.plot()
```

and, plot the new series with our county polygon:

```python

ax = plt.gca()
county.plot(ax=ax)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-118.0, -114.0); ax.set_ylim(33.25, 34.25)
ax.set_aspect('equal')
plt.show()
```

we set the limits for the horizontal and vertical axes to zoom in. We
can also change the plot size:

```python
plt.rcParams['figure.figsize'] = (10, 8)
ax = plt.gca()
county.plot(ax=ax)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-118.0, -114.0); ax.set_ylim(33.25, 34.25)
ax.set_aspect('equal')
plt.show()
```

```python
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
tracts_df.plot(ax=ax, edgecolor='grey', alpha=0.2)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-118.0, -114.0); ax.set_ylim(33.25, 34.25)
ax.set_aspect('equal')
plt.show()
```

And finally, let us create a DataFrame from the GeoSeries:

```python
type(rc_hw)
```

```python
rc_hw = gpd.GeoDataFrame({'geometry': rc_hw})
```

```python
rc_hw.shape
```

```python
tracts_df.shape
```

Spatial Joins: Which Tracts Intersect the Truck Network?
========================================================

We now have the truck route network clipped to the extent of Riverside
County. Using this layer, we can determine which census tracts intersect
the network within the county. For this, we revisit the concept of a
spatial join. There are different flavors of spatial joins that can be
used in practice. Here we explore the options before deciding which one
serves our particular need best.

We begin with a so called \"inner\" join:

```python
# spatial join, tracts with roads
tracts_with_roads = gpd.sjoin(tracts_df, rc_hw, how='inner', op='intersects')
```

We see the warning about the CRS mismatch. Let us see what is going on:

```python
tracts_df.crs
```

and

```python
rc_hw.crs
```

So the route DataFrame does not have a CRS. We can correct this by
setting it to that of the tracts data frame:

```python
rc_hw.crs = tracts_df.crs # create a crs for the rc_hw
rc_hw = rc_hw.to_crs(tracts_df.crs) # update the coordinates accordingly
```

and when we repeat the join:

```python
# spatial join, tracts with roads
tracts_with_roads = gpd.sjoin(tracts_df, rc_hw, how='inner', op='intersects')
```

Silence is golden.

Now we can see what our join operation has returned. We stored the
results in a new object:

```python
tracts_with_roads.head()
```

If we scroll to the right of the DataFrame output, we see a column
labeled **index~right~**. The values in this column indicate the index
of the features in the right DataFrame (in our case the road network)
that intersect with the feature in the current row of the left DataFrame
(the tracts).

Plotting the resulting DataFrame we see:

```python
tracts_with_roads.plot(edgecolor='grey', alpha=0.2)
```

Close inspection reveals some missing tracts. What is going on here?

```python
tracts_with_roads.shape
```

We see there are 256 features in our new DataFrame resulting from the
join. But this is less than the number of tracts in the county:

```python
tracts_df.shape
```

So our plot is not incorrect. It is giving us what we asked for - a plot
of the DataFrame for the tracts that intersect the truck network.

A second type of join can be obtained by setting the `how` option to
`'left'`:

```python
# spatial join, tracts with roads
tracts_with_roads = gpd.sjoin(tracts_df, rc_hw, how='left', op='intersects')
```

This overwrites the resulting DataFrame, so the number of features
changes:

```python
tracts_with_roads.shape
```

This is a larger number than the number of tracts. What is going on?

```python
## 'how=left' uses keys from left_df and retains left_df geometry
# shows all tracts with or withing intersection with network
tracts_with_roads.plot(edgecolor='grey', alpha=0.2)
```

The plot doesn\'t suggest anything fishy. More introspection:

```python
tracts_with_roads.head()
```

Again, scrolling to the right we see the **index~right~** column, but
now we see a mixture of `NaN` and numerical values. The `NaN` values
appear in rows for tracts that do not intersect the road network. Hence
there is no feature in the right DataFrame that intersects with that
feature in the left DataFrame.

But, this doesn\'t explain why we have more features in the resulting
DataFrame than in the left data frame. Something else must be happening.
And it is:

```python
len(tracts_with_roads['GEOID10'].unique())
```

We have the correct number of unique geographic identifiers. Using these
we can determine how many records we have for each unique identifier
(tract):

```python
tracts_with_roads.groupby(['GEOID10']).size()
```

Ah, there are some tracts that appear multiple times in the resulting
DataFrame. We can examine one of these using

```python
tracts_with_roads[tracts_with_roads['GEOID10']=='06065030502']
```

and scrolling over to the right of the output cell reveals that the
tract with the GEOID10 of 06065030502 intersects with three different
segments of the road network: 29.0, 39.0, and 3.

What has happen is the \'left\' join keeps all of the features from the
left database and reports either an `NaN` value, or each unique
intersection between the tract and a particular segment of the road
network. In other words, there will be at least as many features in the
resulting DataFrame as in the left DataFrame. There will be more when
one or more features from the left data frame intersects with more than
a single feature from the right DataFrame.

Thus far we have examined a \"inner\" join and a \"left\" join. The
final option is a \"right\" join:

```python
# spatial join, tracts with roads
tracts_with_roads = gpd.sjoin(tracts_df, rc_hw, how='right', op='intersects')
```

```python
tracts_with_roads.shape
```

There is that number again: 256. What is happening here?

```python
## 'how=right' uses keys from right DataFrame and retains right df geometry
tracts_with_roads.plot(edgecolor='grey', alpha=0.2)
```

These are not tracts but rather the LineStirngs. What is happening is
that a `right` join keeps each of the features from the right DataFrame
and lists each unique intersection with a feature from the left
DataFrame:

So, if we are interested in the question of whether tracts intersecting
the highway network are different from those not interseting the
highways, which one do we want?

There are several ways we could do this, but the approach we take here
is to use the inner join:

```python
tracts_with_roads = gpd.sjoin(tracts_df, rc_hw, how='inner', op='intersects')
```

```python
tracts_with_roads.shape
```

With this in hand, we can create an indicator variable for use in
subsequent analysis. Here the indicator will be 1 if the tract
intersects one or more route segments, and zero other wise:

```python
# Let's create an indicator (dummy) variable for use later
import numpy as np
geoids = tracts_df['GEOID10'].values
tract_hw = np.array([geoid in tracts_with_roads['GEOID10'].values for geoid in geoids])

tract_hw
```

We convert the Boolean valued array into a numerical type and store it
in our indicator variable `intersectshw` in our tract DataFrame:

```python
tracts_df['intersectshw'] = tract_hw*1.
```

We can now visualize our work:

```python
tracts_df.plot()
```

That plots the entire DataFrame. We would like to distinguish tracts
that intersect the network from those that do not:

```python
tracts_df.plot(column='intersectshw')
```

Great, but which color represents the tract intersecting the network? We
can tighten up this visualization:

```python
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
tracts_df.plot(ax=ax, column='intersectshw',edgecolor='grey', alpha=0.2)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-118.0, -114.0); ax.set_ylim(33.25, 34.25)
ax.set_aspect('equal')
plt.show()
```

And we see the results of our geoprocessing.

We can save our DataFrame by writing it out to a shapefile for future
analysis.

```python
# save our work to an augmented shapefile
tracts_df.to_file('data/tracts_routes.shp')
```

Spatial Joins: Take Two
=======================

Our social scientist is pretty happy with what she has been able to
accomplish with Geopandas and its geoprocessing.

Taking advantage of these new skills, she wants to further refine the
scope of her analysis as she realizes much of the eastern part of the
county consists of very large census tracts with low population. So she
decides to focus only on the case of the City of Riverside.

She has obtained a shapefile for the official city boundaries from the
[California Department of
Transportation](http://www.dot.ca.gov/hq/tsip/gis/datalibrary/zip/Boundaries/Cities2015.zip):

```python
city = gpd.read_file('data/riverside_city.shp')

city.plot()
```

And she uses this to do a spatial join to determine which tracts in
Riverside County are within Riverside City:

```python
city_tracts = gpd.sjoin(tracts_df, city, how='inner', op='intersects')

city_tracts.head()
```

```python
city_tracts.shape
```

```python
city_tracts.plot(edgecolor='grey',facecolor='white')
```

Recall that previously we created the indicator variable `intersectshw`
for all the tracts in Riverside County that intersected with the road
network. One of the nice features of GeoPandas is that for many of the
geoprocessing operations, the attributes are passed along to the derived
GeoDataFrames. In our case, `city_tracts` is really just a subset of
`tracts_df` so since the latter was the DataFrame that we originally
defined the `intersectshw` variable, that attribute gets propagated
along to the derived `city_tract` GeoDataFrame.

```python
city_tracts.plot(column='intersectshw', edgecolor='grey')
```

```python
city_tracts.head()
```

```python
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
city_tracts.plot(ax=ax, column='intersectshw',edgecolor='grey', alpha=0.2)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-118.0, -114.0); ax.set_ylim(33.25, 34.25)
ax.set_aspect('equal')
plt.show()
```

Using the `total_bounds` of the new DataFrame we can zoom in to the
western part of Riverside County that is centered on the City of
Riverside:

```python
w, s, e, n = city_tracts.total_bounds
w, s, e, n
```

```python
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
city_tracts.plot(ax=ax, column='intersectshw',edgecolor='grey', alpha=0.2)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(w, e); ax.set_ylim(s, n)
#ax.set_aspect('equal')
plt.show()
```

Buffering
=========

Our researcher has identified the tracts that intersect the truck route
network and has sharpened the lens to the City of Riverside. However,
zooming in further she sees a geographical relationship that gives her
pause:

```python
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
city_tracts.plot(ax=ax, column='intersectshw',edgecolor='grey', alpha=0.2)
rc_hw.plot(ax=ax, edgecolor='k')
ax.set_xlim(-117.53, -117.37); ax.set_ylim(33.875, 33.975)
#ax.set_aspect('equal')
plt.show()
```

It seems to her that there are cases where a segment of the road network
separates two tracts, yet only one of those tracts is identified as
intersecting the network. While tracts are typically defined using
blocks and street center lines she would expect the tracts that share a
road segment as a common part of their respective borders should both be
considered intersecting the network. For her environmental equity
analysis she thinks that individuals that are equidistant from the
network, but on opposite sides of the highway, should face the same
level of exposure. Yet, the variable she has painstakingly constructed
thus far would give an asymmetric exposure measure to these individuals.

There are several reasons these apparent inconsistencies can arise.
First, the origin of the tract boundaries is different from that of the
route network so there is no guarantee that the same digitization
process was used. Second, even if the same agency/researcher did the
digitization of the two layers, if they do not follow good practice, the
topological relationships may be in error. In either case, the two
layers may be yield these kinds of inconsistencies when considered
together.

Fortunately, our researcher knows about the concept of **buffering** and
can call on this to develop a more robust representation of proximity to
the highway. The idea is to define a critical distance, say 500 feet,
and then define a new polygon that contains all of the points that are
within 500 feed of the route network. The resulting polygon is called a
**buffer**.

Once we have the 500-ft buffer, we can then repeat our intersection test
for the tracts to see which tracts are within 500 feet of the route
network. This would address the asymmetry problem our researcher has
identified.

One issue we face, however, is that the tract CRS is unprojected:

```python
tracts_df.crs
```

In other words, if we ignore the CRS, our distances are going to be in
decimal degrees and not feet. So we need to put the tracts on a CRS with
more appropriate units. Fortunately, our behavioral clinics data set has
just such a CRS:

```python
clinics = gpd.read_file('data/behavioralHealth.shp')
```

```python
clinics.crs
```

And, we can change the CRS of the city~tracts~ to that of the clinics:

```python
city_tracts = city_tracts.to_crs(clinics.crs)
```

```python
city_tracts.plot()
```

Notice that the units on the axes have changed from what we had above.

Since we will be doing a buffer around the segments of the highway in
the county as well

```python
rc_hw.plot()
```

```python
type(rc_hw)
```

```python
rc_hw = rc_hw.to_crs(city_tracts.crs)
```

```python
rc_hw.plot()
```

Now we can define the buffer. If we

```python
buf = rc_hw.buffer(500)
```

```python
buf.plot()
```

```python
rc_hw.columns
```

Cool. That gives us a buffer but for the network in the entire county.
What about just in the city?

```python
city_tracts.columns
```

Now if we just want the segments in the city boundaries, we know a
spatial join can get us these:

```python
city_hw = gpd.sjoin(routes_df, city, how='inner', op ='intersects')
```

```python
city_hw.plot()
```

and, we take care to set its CRS accordingly:

```python
city_hw = city_hw.to_crs(city_tracts.crs)
```

```python
city_hw.plot()
```

And, we can buffer these segments:

```python
b500 = city_hw.buffer(500)
```

```python
b500.plot()
```

```python
ct = city_tracts[['GEOID10', 'geometry']]
b500 = gpd.GeoDataFrame({'geometry': b500})
b500.crs = ct.crs
```

Now we can ask to find the tracts in Riverside City that intersect with
the 500-ft buffer around the highways:

```python
tracts_intersecting_hw = gpd.sjoin(ct, b500, how='inner', op='intersects')
```

```python
tracts_intersecting_hw.plot()
```

This creates a new DataFrame with only those tracts for which the hit
test (buffer intersection) is True:

```python
tracts_intersecting_hw.shape
```

Now can create a dummy variable for these tracts to place back in the
DataFrame that contains all the city tracts:

```python
geoids = city_tracts['GEOID10'].values
tract_hw = np.array([geoid in tracts_intersecting_hw['GEOID10'].values for geoid in geoids])
tract_hw
```

```python
city_tracts['b500'] = tract_hw * 1
```

```python
city_tracts.plot()
```

Comparing our two different operational constructs for environmental
equity we have:

```python
city_tracts.plot(column='b500',edgecolor='grey')
```

```python
w, s, e, n = city_tracts.total_bounds
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
city_tracts.plot(ax=ax, column='intersectshw',edgecolor='grey', alpha=0.2)
b500.plot(ax=ax, edgecolor='k')
ax.set_xlim(w, e); ax.set_ylim(s, n)
#ax.set_aspect('equal')
plt.show()
```

```python
w, s, e, n = city_tracts.total_bounds
plt.rcParams['figure.figsize'] = (12, 10)
ax = plt.gca()
city_tracts.plot(ax=ax, column='b500',edgecolor='grey', alpha=0.2)
b500.plot(ax=ax, edgecolor='k')
ax.set_xlim(w, e); ax.set_ylim(s, n)
#ax.set_aspect('equal')
plt.show()
```

And we save our tracts and buffer to their own shapefiles for the next
phase of our analysis.

```python
city_tracts.to_file('data/city_tracts.shp')
b500.to_file('data/b500.shp')
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Geoprocessing with GeoPandas</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

```python

```
