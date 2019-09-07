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

# Objects and Strings

Everthing in Python is an object.

All objects have three things:
- type
- value
- id

```python
s = 'a string'
```

```python
type(s)
```

```python
s # s is the objects name and if we execute this cell we gets its value
```

```python
id(s)
```

```python
print('hi world!')
```

```python
print('hi world')
```

```python
2+3
```

```python
x = 2 + 3
```

```python
x
```

```python
type(x)
```

```python
s = 'serge'
```

```python
type(s)
```

```python
id(s)
```

```python
import keyword
print(keyword.kwlist)
```

```python
7.4 == 7.4
```

```python
7.4 == 7.40001
```

```python
(7.4 == 7.4) * 10
```

```python
(7.4 == 7.41) * 10
```

```python
4**2
```

```python
7/4
```

```python
7/4.
```

```python
int(7/4.)
```

```python
round(7/4.)
```

```python
s = "A string of words"
```

```python
type(s)
```

```python
s
```

```python
print(s)
```

```python
str(10**2)
```

```python
int(str(10**2))
```

```python
s
```

```python
s[0]
```

```python
s[1]
```

```python
len(s)
```

```python
s[17]
```

```python
s[16]
```

```python
s[-1]
```

```python
s[-2]
```

```python
s[0:7]
```

```python
range(5)
```

```python
s
```

```python
s[1:5]
```

```python
s[:6]
```

```python
s[6:]
```

```python
s[-5:]
```

```python
dir(s)
```

```python
s
```

```python
s.center(40)
```

```python
s.count('s')
```

```python
s.find('s')
```

```python
s.find?
```

```python
s.title()
```

```python
s.upper()
```

```python
s.zfill(50)
```

```python
s
```

```python
s[2]
```

```python
s[2] = "S"
```

```python
first = "Bilbo"
last = "Baggins"
line = "The protoagonist is named %s %s." % (first, last)
print(line)
```

```python
R2 = 0.943
summary = "The model had and R2 value of %1.2f." % R2
```

```python
print(summary)
```

```python
# This is a comment. Let's assign 5 to x
x = 5
```

```python
x
```

```python
x = 5 # this is a comment
x
```

```python
x = 5
print(x)
y = 2
y = y * 5
print(y)
print(y+2)
```

```python
x = 5
print(x)
y = 2
"""
y = y * 5
print(y)
"""
print(y+2)
```
