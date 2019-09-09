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

# Functions

```python
name = 'serge rey'
```

```python
name.upper()
```

```python
type(name)
```

```python
numbers = range(10)
```

```python
numbers

```

```python
max(numbers)
```

```python
max?
```

```python
max(name)
```

```python
# write a function to square an integer

def square(x):
    x2 = x * x
    x2 = x**2
```

```python
square(5)
```

```python
def square(x):
    x2 = x**2
    return x2
```

```python
square(5)
```

```python
def square(x):
    return x*x
```

```python
square(3)
```

```python
def power(base, exponent):
    return base**exponent
```

```python
power(3, 2)
```

```python
power(2, 3)
```

```python
def power(base, exponent=2):
    return base**exponent
```

```python
power(2, 3)
```

```python
power(2)
```

```python
power(2, 5)
```

```python
def power(base=4, exponent=2):
    return base**exponent
```

```python
power()
```

```python
power(exponent=3, base=10)
```

```python
power()
```

```python
import csv
newlines = []
with open('data/airports.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        newlines.append(line)
        
```

```python
def read_csv(file_name):
    newlines = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            newlines.append(line)
    return newlines
    
```

```python
data = read_csv('data/airports.csv')
```

```python
def get_attribute(data, attribute_name):
    header = data[0]
    idx = header.index(attribute_name)
    return [record[idx] for record in data[1:]]
```

```python
get_attribute(data, 'latitude')
```

```python
def to_float(attribute_list):
    return list(map(float, attribute_list))
```

```python
flat = to_float(get_attribute(data, 'latitude'))
```

```python
flat[:3]
```

```python
lat = to_float(get_attribute(data, 'latitude'))
lon = to_float(get_attribute(data, 'longitude'))
points = list(zip(lat, lon))
points[:3]
```

```python
from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

      R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c

# Usage
lon1 = -103.548851
lat1 = 32.0004311
lon2 = -103.6041946
lat2 = 33.374939

print(haversine(lat1, lon1, lat2, lon2))
```

```python
haversine(0, 0, 0, 1)
```

```python
haversine(45,0, 45, 1)
```

```python
from math import inf
# find the nearest neighbor for an origin airport 
def nearest_airport(origin_airport, points):
    nnd = inf
    closest_j = inf
    i = origin_airport
    o_lat, o_lon = points[i]
    for j, point in enumerate(points):
        if i != j:
            d_lat, d_lon = point
            d = haversine(o_lat, o_lon, d_lat, d_lon)
            if d < nnd:
                nnd = d
                closest_j = j
    return closest_j, nnd
    
```

```python
nearest_airport(0, points)
```

```python
names = get_attribute(data, 'name')
```

```python
names[4901]
```

```python
names[0]
```

```python
nearest_airport(4901, points)
```

# Functions as first class objects

```python
def spam():
    print('Hi world')
```

```python
spam()
```

```python
def do_twice(f):
    f()
    f()
```

```python
do_twice(spam)
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
 Find the most isolated airport in our dataset (Hint: think nearest neighbor distance).
</div>

```python
# %load solutions/115_1.py
```

```python
# %load solutions/115_2.py
```

```python
# %load solutions/115_3.py
```

---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Functions</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
