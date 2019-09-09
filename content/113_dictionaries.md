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

# Dictionaries and Sets


## Dictionaries

* key : value 
* unordered

```python
d = {}
```

```python
type(d)
```

```python
d['first'] = 1
```

```python
d
```

```python
len(d)
```

```python
d['second'] = 2
```

```python
d
```

```python
len(d)
```

```python
d['third'] = 'wolf'
```

```python
d
```

```python
d.keys()
```

```python
d.values()
```

```python
d.items()
```

```python
data = d.items()
```

```python
data
```

```python
d = dict(data) #list to dict
```

```python
d
```

```python
dow = "mon", "tue", "wed", "thu", "fri", "sat", "sun"
```

```python
dow
```

```python
ids = range(len(dow))
```

```python
ids
```

```python
dow
```

```python
zip(dow, ids)
```

```python
dow_id = dict(zip(dow, ids))
```

```python
dow_id
```

```python
dow_di = dict(zip(ids, dow))
dow_di
```

### Dictionary Methods

```python
dow_id.keys()
```

```python
dow_id.values()
```

```python
dow_id.items()
```

```python
dow_id['sun'] = -4
```

```python
dow_id
```

```python
e = {'bono': 'humble singer', 'edge': 'the sound'}
```

```python
e
```

```python
dow_id
```

```python
dow_id.update?
```

```python
dow_id.update(e)
```

```python
dow_id
```

```python
dir(dow_id)
```

## Sets

* a collection of unordered, unique objects
* supports operations and concepts from set theory
* mutable

```python
l = range(5)
```

```python
l
```

```python
s = set(l)
```

```python
s
```

```python
type(s)
```

```python
b = [0, 1, 0, 2, 2, 3 , 6]
```

```python
b
```

```python
sb = set(b)
sb
```

```python
c = [ 6, 2, 2, -6, 4]
set(c)
```

```python
s = 'My name is joe the plumber'
ss = set(s)
ss
```

```python
s = set(s.split())
```

```python
s
```

```python
s = set([1,2,3,4])
s
```

```python
s.add(5)
```

```python
s
```

```python
s.add(1)
```

```python
s
```

```python
b = [4,5,6,7]
```

```python
b
```

```python
sb = set(b)
```

```python
sb
```

```python
s.update(sb)
```

```python
s
```

```python
group1 = set(range(1,6))
group2 = set(range(2,7))
```

```python
group1
```

```python
group2
```

```python
group1.intersection(group2)
```

```python
group1.union(group2)
```

```python
s1 = set(range(3))
s2 = set(range(10))
```

```python
s1
```

```python
s2
```

```python
s1.issubset(s2)
```

```python
s2.issuperset(s1)
```

```python
s1.issuperset(s2)
```

```python
s2.symmetric_difference(s1)
```

```python
s1.symmetric_difference(s2)
```

```python
s2.difference(s1)
```

```python
s1.difference(s2)
```

```python
s1
```

```python
s1.remove(1)
```

```python
s1
```

```python
s1.remove(10)
```

```python
s1.discard(10)
```

```python
s1
```

```python
s1.discard(2)
```

```python
s1
```

```python
s4 = s1.discard(2)
s4
```
