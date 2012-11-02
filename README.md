# pygridgen

A Python interface to Pavel Sakov's C-based Gridgen Orthogonal Grid Generation Package

Pyechonest is an open source Python library for the Echo Nest API.  With Pyechonest you have Python access to the entire set of API methods including:

  * **simple GUI interface** - The GUI interface uses native matplotlib widgets for even more portability.
  * **arbitrary number of corners** - More corners means more complicated domains.  Great for domains with bays, estuaries, and other complicated features.
  * **a single orthogonal grid as a result** - Whites whiter!  Brights brighter!

## Install
We are working on packaging using Bento, but for now, you need to:

* cd external/nn; ./configure ; make install
* cd external/csa; ./configure ; make install
* cd external/gridutils; ./configure ; make install
* cd external/gridgen; ./configure ; make shlib
* cd pygridgen; python setup.py install

## Getting Started
 * Install pygridgen
 * **start in upper left hand corner** - to use the Echo Nest API you need an Echo Nest API key.  You can get one for free at [developer.echonest.com](http://developer.echonest.com).
 * **define points as 1 or 0** - you can do this one of two ways:
  * more information needs to be put in here....

## Examples
* Rob's sweet example number one
