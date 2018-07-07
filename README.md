# DistroWatch API

**What is DistroWatch?** [DistroWatch](https://www.distrowatch.com) is a website dedicated to talking about, reviewing and keeping up to date with open source operating systems. This site particularly focuses on Linux distributions and flavours of BSD, though other open source operating systems are sometimes discussed. There is a lot of information out there on Linux distributions and this site tries to collect and present that information in a consistent manner to make it easier to locate.

## The Project

The project conciste of creating a tool that realizes the collection of the distributions that exist in the site and also the ranking of distributions that are more accessed in a time of 12, 6, 3 and 1 month.

After this collection will be performed a data analysis to collect possible results of the ranking of distributions, and also in the future the creation of a mobile application that presents this data.

## Tools Used

- [Python 3](https://www.python.org/download/releases/3.0/?)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](http://docs.python-requests.org/en/master/)
- [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html)
- [CSV](https://docs.python.org/2/library/csv.html)
- [Flask](http://flask.pocoo.org/)

## Installation

**BeautifulSoup**
```
$ pip install beautifulsoup4
```

**Requests**
Making a request with Requests is very simple.

Begin by importing the Requests module:
```
>>> import requests
```

**MySQLdb**
```
pip install mysqlclient
```
In python version 3:
```
$ sudo apt-get install python-mysqldb andpython3-mysqldb
```
**CSV**
csv is part of python's standard library so you don't need to install it with pip. Just use it with:
```
import csv
```
**Flask**
```
$ pip install -U Flask
```

## Directories

The ***crawler_db*** directory contains the codes related to the collection of data from the DistroWatch site and also the insertion into the database for the mobile application to use later. Also in this folder contains .csv files for data analysis.

The ***api*** directory contains the code related to creating a webservices to feed the mobile application.

## To Contribute

To contribute with some project just take the Fork and perform a PR with the modifications made.

For more information, access the [![Gitter](https://img.shields.io/gitter/room/DAVFoundation/DAV-Contributors.svg?style=flat-square)](https://gitter.im/curiosity_data_analysis/random).
