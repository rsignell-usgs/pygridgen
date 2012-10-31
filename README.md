# pygridgen

A Python interface to Pavel Sakov's C-based Gridgen Orthogonal Grid Generation Package

Pyechonest is an open source Python library for the Echo Nest API.  With Pyechonest you have Python access to the entire set of API methods including:

  * **simple GUI interface** - search for artists by name, description, or attribute, and get back detailed information about any artist including audio, similar artists, blogs, familiarity, hotttnesss, news, reviews, urls and video.
  * **arbitrary number of corners** - search songs by artist, title, description, or attribute (tempo, duration, etc) and get detailed information back about each song, such as hotttnesss, audio_summary, or tracks.
  * **a single orthogonal grid as a result** - upload a track to the Echo Nest and receive summary information about the track including key, duration, mode, tempo, time signature along with detailed track info including timbre, pitch, rhythm and loudness information.

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
  * click on 
  * or do this

## Examples
* Rob's sweet example number one

![alt text](http://i.imgur.com/WWLYo.gif "Frustrated cat can't believe this is the 12th time he's clicked on an auto-linked README.md URL")