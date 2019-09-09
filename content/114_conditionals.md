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

# Iterables, Conditional execution, and Files

```python
x = list(range(10)) # python 2 safe
```

```python
print('My input values are: ', x)
```

```python
k = 10
summation = 0
for i in range(k):
    summation = summation + i
    print(i, summation)
    
print('we are done')
print('The sum of the first {} integers is {}'.format(k, summation))
    
```

```python
x
```

```python
sum(x)
```

```python
sum(x) / len(x)
```

```python
sum(x) * 1. / len(x)
```

## Nesting

```python
print('i j')
for i in range(4):
    for j in range(3):
        print(i, j)
```

```python
print('i j')
for i in range(4):
    for j in range(3):
        if i != j:
            print(i,j)
```

# if else

```python
x = range(10)
x
```

```python
for i in x:
    if i < 4:
        print(i)
```

```python
for i in x:
    if i < 4:
        print(i)
    else:
        print('{} is not less than 4'.format(i))
```

```python
for i in x:
    if i < 4:
        print('{} is less than 4'.format(i))
    elif i > 4:
        print('{} is greater than 4'.format(i))
```

```python
for i in x:
    if i < 4:
        print('{} is less than 4'.format(i))
    elif i > 4:
        print('{} is greater than 4'.format(i))
    else:
        print('{} is equal to 4'.format(i))
```

```python
x = range(1000)
```

```python
v = 6
if v%2:
    print(v)
else:
    print('here')
    print(v)
```

```python
v = 7
v % 2
```

```python
odds = []
for i in x:
    # check if i is odd, if so append to odds
    if i % 2:
        odds.append(i)
    
```

```python
odds[:10]
```

```python
len(odds)
```

```python
odds1 = [i for i in x if i%2]
```

```python
odds1[:10]
```

```python
odds1 = [i for i in x if i%2 and i>72]
len(odds1)
```

```python
odds1 = []
for i in x:
    if i%2 and i>72:
        odds1.append(i)
len(odds1)
```

## Files

```python
with open('data/airports.csv', 'r') as f:
    lines = f.readlines()
```

```python
type(lines)
```

```python
lines[:3]
```

```python
lines[-3:]
```

```python
len(lines)
```

```python
lines[1]
```

```python
rec1 = lines[1]
```

```python
rec1
```

```python
s = "my name is joe"
```

```python
s.split()
```

```python
s = "my,name,is,joe"
s.split(",")
```

```python
s.split()
```

```python
rec1
```

```python
rec1.split(',')
```

```python
rec1.strip().split()
```

```python
with open('data/airports.csv', 'r') as f:
    lines = f.readlines()
```

```python
data = []
for line in lines:
    data.append(line.strip().split(','))
```

```python
len(data)
```

```python
data[1]
```

```python
data[0]
```

```python
k = len(data[0])
```

```python
k
```

```python
latitude = data[0].index('latitude')
```

```python
latitude
```

```python
data[1][latitude]
```

```python
header = data[0]
```

```python
header
```

```python
len(header)
```

```python
k = len(header)
for record in data:
    rec_k = len(record)
    if rec_k != k:
        print(rec_k, record)
```

```python
k = len(header)
for i, record in enumerate(data):
    rec_k = len(record)
    if rec_k != k:
        print(i, rec_k, record)
```

```python
import csv
newlines = []
with open('data/airports.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        newlines.append(line)
print(newlines[4442])
```

```python
k = len(header)
for i, record in enumerate(newlines):
    rec_k = len(record)
    if rec_k != k:
        print(i, rec_k, record)
```

```python
header
```

```python
lat = header.index('latitude')
lon = header.index('longitude')
```

```python
lat,lon
```

```python
[header.index(name) for name in header]
```

```python
lookup = dict([(name, header.index(name)) for name in header])
```

```python
lookup['latitude']
```

```python
lat = lookup['latitude']
lon = lookup['longitude']
```

```python
lon
```

```python
newlines[:3]
```

```python
points = [(float(record[lon]),float(record[lat])) for record in newlines[1:]]
```

```python
points[:3]
```

```python
lats = [float(record[lat]) for record in newlines[1:]]
lons = [float(record[lon]) for record in newlines[1:]]
```

```python
points_zip = list(zip(lons, lats))
```

```python
points_zip[:3]
```

```python
min_lat = float('inf')
min_lat 
```

```python
10**2 < min_lat
```

```python
southmost = min_lat
for lat in lats:
    if lat < southmost:
        southmost = lat
```

```python
southmost
```

```python
southern = []
for i, lat in enumerate(lats):
    if lat < 0:
        southern.append(i)
```

```python
southern[:10]
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
 Find the western most airport in the northern hemisphere.
 
</div>

```python
# %load solutions/114_1.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
 Find the western most airport in the southern hemisphere.
 
</div>

```python
# %load solutions/114_2.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
 Find the southern most airport in the western hemisphere.
</div>

```python
# %load solutions/114_3.py
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
 Find the northern most airport in the eastern hemisphere.
</div>

```python
# %load solutions/114_4.py
```
