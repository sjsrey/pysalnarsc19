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

# PySAL


### Documentation

```python
from IPython.display import IFrame
IFrame(src="http://pysal.org/?useformat=mobile", width=800, height=550)
```

### Source Code


Source is at http://github.com/pysal


# Introduction to Jupyter Notebook

We will cover the basic operations/interface of the notebook which we will, in turn, use for the remainder of the workshop


## What is Jupyter Notebook?

- web-based interface for working with Python (and other languages)
- Similar in spirit to a scientific notebook
    - record experiments
    - document
    - share
- literate programming
- simple JSON format
    - web citizen
    - git friendly


## Starting the notebook

<!-- #region -->
From a shell or terminal we can start the notebook with:
```
jupyter notebook
```

This brings up the **dashboard** which will list any notebooks encountered in the current working directory.

You can either open an existing notebook or create a new one from the dashboard.
<!-- #endregion -->

## Notebook Inteface


### Menu


### Help System


### Keyboard Shortcuts

A list of keyboard shortcuts can be revealed by entering `h`.


Note there are two *modes* for the notebook, *Edit Mode* and *Command mode*. The latter is used to *manipulate* notebook cells, while the former is used to *edit* the content of a cell.

- To enter *Command Mode* press `ESC`.
- To enter *Edit Mode* press `Enter` on a cell.



### Navigation

When in command mode, you can use keyboard shortcuts to move from cell to cell

- `k` moves the cursor up one cell
- `j` moves the cursor down one cell




### Manipulating Cells

* merging
* splitting
* copy
* paste
* moving 
* inserting

```python

```

## [Cell Types](http://jupyter-notebook.readthedocs.io/en/stable/notebook.html#structure-of-a-notebook-document)


### Code Cells


In command mode, `y` will set the cell to code. After that, pressing `Enter` will let you edit the text.

```python
x = range(10) # Shift-Enter to execute and create a new cell
```

```python
x = range(10)
y = [ xi*3 for xi in x] # Ctrl-Return to execute but stay in the current cell
```

Comments



### Raw Cells


*Raw cells provide a place in which you can write output directly*. In command mode, `r` will set the cell to text. After that, pressing `Enter` will let you edit the text.


### Markdown Cells

<!-- #region -->
In command mode, ```m``` gives us a [Markdown] cell.


[Markdown]: http://daringfireball.net/projects/markdown/

We can then use Markdown syntax to do things like lists:

- first
- second
- third
  - nested one
  - nested two
- fourth


As well as **LaTeX**.

This is an in-line equation $\hat{\beta} = (X'X)^{-1}X'y$ for the ordinary least squares estimator.

A display equation is done with

$$ y = \rho W y + X\beta + \epsilon$$

**NOTE**: LaTeX will only render if [mathjax](https://www.mathjax.org/) is available via a network connection or if it has been installed locally.
<!-- #endregion -->

## Kernel


### Stoping and Restarting


`00` (enter the zero key twice)  will restart the kernel.


## Exporting and Saving


You can save in several formats via the **File** menu entry


### Saving

In command mode, `s` will save the notebook, and mark a checkpoint. You can use checkpoints to rollback to a previous version if needed.


## Examples

* [Book](https://geographicdata.science/)
* [Course](http://learnds.com)
* [Gallery](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
* [GDS Book](https://geographicdata.science/2019/08/29/project-launch.html)


---

<a rel="license" href="http://creativecommons.org/licenses/by-nc-
sa/4.0/"><img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span
xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Introduction Jupyter Notebooks</span> by <a xmlns:cc="http://creativecommons.org/ns#"
href="http://sergerey.org" property="cc:attributionName"
rel="cc:attributionURL">Serge Rey</a> is licensed under a <a
rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative
Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
