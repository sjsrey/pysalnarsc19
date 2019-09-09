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

# Pandas

This notebook presents an introduction to the `pandas` package.
We focus on only the most commonly used features of `pandas` as they pertain to geospatial data analysis. More extensive references are given at the end of the notebook.

```python
import pandas
import numpy as np
```

```python
ward = np.tile([1,2,3,4,5], 5)
population = np.random.randint(5000, size=(25,))
poverty = np.random.random(size=(25,)) * .4
```

```python
poverty
```

```python
population
```

```python
ward
```

```python
df = pandas.DataFrame({'population': population,
                      'ward': ward,
                      'poverty': poverty})
```

```python
df.head()
```

```python
df.shape
```

```python
type(df)
```

```python
type(df.population)
```

## indexing

```python
df['population']
```

```python
df.population
```

```python
df[0:4]
```

```python
df[-4:]
```

```python
df[df.ward==2]
```

```python
df[(df.ward==2) & (df.population < 1000)]
```

```python
df[~(df.ward==2) & (df.population < 1000)] # not in ward 2 and less than 1000 population
```

```python
df[~((df.ward==2) & (df.population < 1000))] # not (in ward 2 and less than 1000 population)
```

```python
df[(df.ward==2) | (df.population < 1000)] #in ward 2 or less than 1000 population)
```

## New Columns

```python
df.head()
```

```python
pop_pov = df.population * df.poverty
pop_pov
```

```python
df['pop_pov'] = pop_pov.astype('int')
```

```python
df.head()
```

```python

```

## Aggregation/Groupby

```python
df.groupby(by='ward').sum()
```

```python
df.groupby(by='ward').sum()[['population', 'pop_pov']]
```

```python
ward_df = df.groupby(by='ward').sum()[['population', 'pop_pov']]
```

```python
ward_df['poverty'] = ward_df.pop_pov / ward_df.population
```

```python
ward_df.head()
```

## Joins

```python
ward_df.index
```

```python
df.merge(ward_df, how='left', on='ward')
```

```python
df = df.merge(ward_df, how='left', on='ward')
```

```python
names = df.columns
```

```python
new_names = [name.replace("_y", "_ward") for name in names]
df.columns = new_names
df.head()
```

```python
df[df.poverty_x > df.poverty_ward]
```


<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Which ward has the highest poverty rate?
</div>

```python
# %load solutions/120_1.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Which tract the highest poverty rate as a percentage of its ward's poverty rate?
</div>

```python
# %load solutions/120_2.py
```

## Dealing with *real data*

```python
data = pandas.read_csv('data/CAINC1__ALL_STATES_1969_2017.csv', encoding='latin-1', 
                      skipfooter=3, engine='python')
```

```python
data.shape
```

```python
data.head()
```

```python
pandas.set_option('display.max_columns', 500)
```

```python
data.head()
```

```python
data.tail(10)
```

```python
data.columns
```

```python
data['1969']
```

```python
data['1969'].sort_values()
```

so there are undisclosed values in the cases of `(NA)`

```python
data.isna().sum() # so no na values in the numpy / pandas sense
```

```python
data1 = data.replace("(NA)", 0)
data1['1969'] = data1['1969'].astype(int)
```

```python
data1['1969'].sort_values()
```

```python
for year in range(1969, 2018):
    print(year, data[data[str(year)]=='(NA)'].shape)
```

## subsetting

```python
small = data[data.LineCode.isin( [2, 3] )]
```

```python
small.shape
```

```python
data.shape
```

```python
small.head()
```

```python
for year in range(1969, 2018):
    small = small[small[str(year)] != "(NA)"] #drop all records with NA
```

```python
small.shape
```

```python
small.head(20)
```

```python
small['1969']
```

```python
convert_dict = dict([(str(year), int) for year in range (1969, 2018)])
```

```python
small = small.astype(convert_dict)
```

```python
small['1969']
```

```python
small['2017']
```

```python
geofips = pandas.unique(small.GeoFIPS)
```

```python
geofips
```

```python
geofips.shape
```

```python
small['GeoFIPS'] = [fips.replace("\"", "").strip() for fips in small.GeoFIPS]
```

```python
geofips = pandas.unique(small.GeoFIPS)
```

```python
geofips
```

```python
pc_inc = small[small.LineCode==3]
```

```python
pc_inc.shape
```

```python
pc_inc.head()
```

```python
pc_inc.max()
```

```python
cid_1969 = pc_inc.columns.get_loc('1969')
cid_1969
```

```python
pc_inc.iloc[:,8]
```

```python
pc_inc.iloc[:, 8:20]
```

```python
pc_inc.iloc[:, 8:].idxmax(axis=0) 
```

```python
max_ids = pc_inc.iloc[:, 8:].idxmax() 
pc_inc.loc[max_ids]
```

```python
for y, max_id in enumerate(max_ids):
    year = y + 1969
    name = pc_inc.loc[max_id].GeoName
    pci = pc_inc.loc[max_id, str(year)]
    print(year, pci, name)
    
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Identify the area with the lowest per-capita income each year.
</div>

```python
min_ids = pc_inc.iloc[:, 8:].idxmin() 
for y, min_id in enumerate(min_ids):
    year = y + 1969
    name = pc_inc.loc[min_id].GeoName
    pci = pc_inc.loc[min_id, str(year)]
    print(year, pci, name)
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
    As a percentage of the minimum per-captia income, calculate the relative income gap between the extremes of the income distribution each year.
    
   Identify the year with the maximum relative income gap.
   
</div>

```python
# %load solutions/120_3.py
```

<div class="alert alert-info" style="font-size:120%">
<b>Further Readings</b>: <br>
    <a rel='further' href="https://pandas.pydata.org/pandas-docs/stable/index.html">Pandas Documentation</a>
</div>


---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Pandas</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
