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

# Directional Analysis of Dynamic LISAs

This notebook demonstrates how to use Rose Diagrams to visualize and carry out inference on directional LISAs.

```python
%matplotlib inline
from pysal.lib import examples
from pysal.lib import io
from pysal.explore.giddy.directional import Rose
import numpy as np
```

```python
f = open(examples.get_path('spi_download.csv'), 'r')
lines = f.readlines()
f.close()

```

```python
lines = [line.strip().split(",") for line in lines]
names = [line[2] for line in lines[1:-5]]
data = np.array([list(map(int, line[3:])) for line in lines[1:-5]])
```

```python
sids  = list(range(60))
out = ['"United States 3/"',
      '"Alaska 3/"',
      '"District of Columbia"',
      '"Hawaii 3/"',
      '"New England"','"Mideast"',
       '"Great Lakes"',
       '"Plains"',
       '"Southeast"',
       '"Southwest"',
       '"Rocky Mountain"',
       '"Far West 3/"']
```

```python
snames = [name for name in names if name not in out]
sids = [names.index(name) for name in snames]
states = data[sids,:]
us = data[0]
years = np.arange(1969, 2009)

```

```python
rel = states/(us*1.)
```

```python
gal = io.open(examples.get_path('states48.gal'))
w = gal.read()
w.transform = 'r'
```

```python
Y = rel[:, [0, -1]] # first and last year
```

```python
Y
```

```python
np.random.seed(100)
r4 = Rose(Y, w, k=4)
```

## Visualization

```python
r4.plot()
```

```python
r4.plot(Y[:,0]) # condition on starting relative income
```

```python
r4.plot(attribute=r4.lag[:,0]) # condition on the spatial lag of starting relative income
```

```python
r4.plot_vectors() # lisa vectors
```

```python
r4.plot_vectors(arrows=False)
```

```python
r4.plot_origin() # origin standardized


```

## Inference


The Rose class contains methods to carry out inference on the circular distribution of the LISA vectors. The  approach is based on a two-sided alternative where the null is that the distribution of the vectors across the segments reflects independence in the movements of the focal unit and its spatial lag. Inference is based on random spatial permutations under the null.

```python
r4.cuts
```

```python
r4.counts
```

```python
np.random.seed(1234)
r4.permute(permutations=999)
```

```python
r4.p
```

<div class="alert alert-success" style="font-size:120%">
<b>Exercise</b>: <br>
Carry out a directional analysis of the LISA vectors using $k=8$
    What additional insights over the $k=4$ case do you find?
</div>

```python
# %load solutions/410_1.py
```

## Readings
- [Rey, Anselin, Murray (2011) Visualizing regional income distribution dynamics. Letters in Spatial and Resource Sciences, 4: 81-90](https://link.springer.com/article/10.1007/s12076-010-0048-2)
- [Breau, Shin, Burkhart (2018) Pulling apart: new perspectives on the spatial dimensions of neighborhood income disparities in Canadian Cities. Journal of Geographical Systems, 20: 1-25.](https://link.springer.com/article/10.1007%2Fs10109-017-0255-0)



---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Directional Analysis of Dynamic LISAs</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

[Wei Kang](https://spatial.ucr.edu/peopleKang.html) contributed to this notebook.
