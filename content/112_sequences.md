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

# Sequences

## Standard Types (Primatives)

- numbers
- strings
- **lists**
- **tuples**
- sets 
- dictionaries


## Lists

### Characteristics

- flexibile containers (strings only contain alphanumeric characters)
- heterogeneous elements
- nestable
- mutable

### Creation

```python
x = ['a', 1, 'b', -8, 7.2]
x
```

```python
z = [x, 'a string of words']
z
```

```python
y = []
y
```

### Slicing

```python
x
```

```python
x[2]
```

```python
x[1:-1]
```

```python
x[0]
```

```python
x[-3:]
```

### Nestable

```python
a = ['lat', 'lon']
b = ['every', 'other', 'word']
c = [a, b]
c
```

```python
len(a)
```

```python
len(b)
```

```python
len(c)
```

```python
len(c[0])
```

```python
len(c[1])
```

### Mutable


```python
c
```

```python
c[0] = 'this is a string'
c
```

```python
c[0][0]
```

```python
c[0][0] = 'T'
```

List Operations

```python
a = ['1', 'serge', 1000]
```

```python
b = a + a
b
```

```python
c = a * 4
c
```

List functions

```python
x = [1, 2, 3, 90]
len(x)
```

```python
max(x)
```

```python
min(x)
```

List methods

```python
y = []
y
```

```python
y.append(10)
y
```

```python
x = [1, 2, 3]
x
```

```python
x.append(y)
x
```

```python
x.extend(y)
x
```

Note the subtle difference between the two methods. Sometimes you will want to use append, and other times extend is what you need.

Other list methods, sort and reverse:



```python
x = [7, 1, 3, 12]
x
```

```python
x.sort()
x
```

```python
x.reverse()
x
```

Keep in mind that they are in-place methods meaning they modify the object. In other words they don’t return anything, but rather work on the object’s data:



```python
z = x.sort()
```

```python
z
```

```python
type(z)
```

If you want to keep the original list as is but get a new list with elements equal to the sorted elements from the first list:

```python
x = [2, 3, 1, 7, 4]
z = sorted(x)
```

```python
z
```

```python
x
```

Other useful list methods

```python
x = [1, 2, 3, 3, 3, 4, 5, 6, 7]
x.count(3)
```

```python
x.count(-8)
```

```python
3 in x
```

```python
-8 in x
```

```python
x.remove(3)
```

```python
x
```

```python
x.pop()
```

Lists as Stacks (LIFO)


```python
l = list(range(5))
l
```

```python
l.pop()
```

```python
l.pop()

```

```python
l.pop()

```

```python
l.pop()

```

```python
l.pop()
```

```python
l.pop()
```

Lists as Ques (FIFO)

```python
l = list(range(5))
```

```python
l.pop(0)
```

```python
l.pop(0)
```

```python
l.pop(0)
```

```python
l.pop(0)
```

```python
l.pop(0)
```

## Tuples

### Characteristics

- similar to lists
- exception: immutable

### Creating Tuples

```python
t = (1, 2, 3, 'a', 'b', 'stella')
t
```

```python
t = 1, 2, 3, 'a', 'b', 'stella'
t
```

```python
x = 1,
```

```python
x
```

```python
y = 1
```

```python
y
```

```python
x == y
```

Tuple Methods

```python
t = 'a', 'b', 'c'
t
```

```python
t.count('b')
```

```python
t.index('b')
```

```python
t.index('s')
```

### Immutability

```python
t
```

```python
t[0] = 'A'
```

### Nestable

```python
t
```

```python
s = 1, 2, t
s
```

Note that while the tuple is immutable, if it contains any elements that are mutable we can change the elements of the mutable elements of the tuple.



```python
s = [1,2,3]
t = 'a', s
```

```python
t
```

```python
t[1][1] = 7
```

```python
t
```

```python
t[0][0]
```

```python
t[0][0] = 'A'
```

### Converting between lists and tuples

```python
t = 'a', 'b', 'c'
t
```

```python
l = list(t)
l
```

```python
tl = tuple(l)
tl
```
