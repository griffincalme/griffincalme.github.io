---
layout: post
title: Immunohistochemistry and Computer Vision with Python
---

For my blog debut, we're going to learn how to implement the programs I
used in my paper for the [MicroDeconvolution](https://github.com/griffincalme/MicroDeconvolution)
project.

##Color Deconvolution
![Color deconvolution]({{ site.baseurl }}/images/IHC/CD.png)

##Startup

We'll be using Python 3 with scikit-image, matplotlib for visualizations,
and a bit of numpy for linear algebra operations.

If you can't figure out how to install these I highly recommend using
the [Anaconda](https://www.continuum.io/downloads) python distribution.
It comes with all of the most popular scientific packages already installed.
Additionally, the `conda install` command allows you to get access to an
even larger collection of pre-compiled python packages, so no
messing around with compiler errors!


##An Introduction

For part 1, we're going to learn color deconvolution, an algorithm for
unmixing stains that was developed by 
[A.C. Ruifrok and D.A. Johnston](http://s3.amazonaws.com/academia.edu.documents/39858226/AnalQuantCytHist-AR.pdf?AWSAccessKeyId=AKIAJ56TQJRTWSMTNPEA&Expires=1472431002&Signature=t3t33hDhza3AnbmBy59A2nVbrpI%3D&response-content-disposition=inline%3B%20filename%3DAnal_Quant_Cyt_Hist_AR.pdf).

Scikit-image offers very simple functions  for color deconvolution that
we can dig down into a bit, see how they work, and modify to our needs.


```python
import matplotlib.pyplot as plt
```
