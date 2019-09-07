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

# Visualisation

```python
%matplotlib inline

import geopandas
import seaborn
import contextily
import matplotlib.pyplot as plt
import pandas

db = geopandas.read_file('data/texas.shp')
```

## Non-spatial visualisation


### Univariate continuous


* Histograms

```python
db['HR90'].plot.hist()
```

* KDEs

```python
db['HR90'].plot.kde()
```

### Bivariate continuous


* Scatter plots

```python
db[['GI89', 'HR90']]\
  .plot.scatter('GI89', 
                'HR90')
```

* Hexbin plots

```python
seaborn.jointplot('GI89', 
                  'HR90', 
                  db, 
                  kind='hex')
```

* 2D KDEs

```python
seaborn.jointplot('GI89', 
                  'HR90', 
                  db, 
                  kind='kde')
```

### Categorical plots


* Categorical scatter plots

```python
db.PO90
```

```python
p90max = db.PO90.max()
```

```python
width = int(p90max/3)+2
db['pop_cats'] = pandas.cut(db.PO90, [0, 5000, 100000, p90max])
```

```python
seaborn.catplot(x="pop_cats",
                y="HR90",
                data=db)
```

* Box plots

```python
seaborn.catplot(x="pop_cats",
                y="HR90",
                data=db,
                kind='box')
```

* Violin plots

```python
seaborn.catplot(x="pop_cats",
                y="HR90",
                data=db,
                kind='violin')
```

## Anatomy of a graphic


### Figures

```python
f = plt.figure()
```

* Change size

```python
# Size
f = plt.figure(figsize=(12, 12))
```

### Axes


* One axis (`ax`) inside a figure (`f`)

```python
f, ax = plt.subplots(1)
```

* Two rows, one column of axes (`axs`) inside a figure (`f`)

```python
f, axs = plt.subplots(2)
```

* One row, two columns of axes (`axs`) inside a figure (`f`)

```python
f, axs = plt.subplots(1, 2)
```

* Embed data on an axis

```python
f, ax = plt.subplots(1)
db['HR90'].plot.hist()
#db.plot(ax=ax)
```

* Embed data on two axes

```python
f, axs = plt.subplots(1, 2, figsize=(12, 6))
# First axis

db['HR90'].plot.hist(ax=axs[0])
# Second axis
db['HR90'].plot.kde(ax=axs[1])
# Title
f.suptitle("HR90")
# Display
plt.show()
```

### Layers


* Tweak a layer

```python
# Transparency
db.HR90.plot.hist(alpha=0.5)
```

```python
# color and transparency
db.HR90.plot.hist(alpha=0.5, color='green')
```

## Exercises


* Create a scatter plot using `seaborn`'s `jointplot` (hint: have a look at the `seaborn`'s tutorial for [plotting bivariate distributions](http://seaborn.pydata.org/tutorial/distributions.html#plotting-bivariate-distributions)) 
* Replicate the Boxplot using the `boxen` option for a cooler alternative
* Create a figure with three subplots displaying the following:
    - Histogram of the `HR90`
    - Scatter plot of `HR90` against `GI89`
    - KDE of the `GI89`
