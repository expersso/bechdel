Bechdel
=======
[![PyPI](https://img.shields.io/pypi/v/bechdel.svg)]()
[![PyPI](https://img.shields.io/pypi/dm/bechdel.svg)]()
[![Travis-CI Build Status](https://travis-ci.org/expersso/bechdel.svg?branch=master)](https://travis-ci.org/expersso/bechdel)
[![codecov.io](https://codecov.io/github/expersso/bechdel/coverage.svg?branch=master)](https://codecov.io/github/expersso/bechdel?branch=master)

### Introduction

The `Bechdel` package wraps the [bechdeltest.com](http://bechdeltest.com) API and allows users to programmatically retrieve the [Bechdel score](https://enwikipedia.org/wiki/Bechdel_test) for movies.

You can search for movies either by title...

``` python

import bechdel
movies = bechdel.getMoviesByTitle('terminator')
len(movies) # 5
print movies[0]

{u'date': u'2015-07-02 06:24:18',
 u'dubious': u'0',
 u'id': u'6340',
 u'imdbid': u'1340138',
 u'rating': u'0',
 u'submitterid': u'12302',
 u'title': u'Terminator Genisys',
 u'visible': u'1',
 u'year': u'2015'}

```

...or by IMDb id:

``` python

terminator_genisys = bechdel.getMovieByImdbId('1340138')

```

### Disclaimer

This package and its author are unaffiliated with
[bechdeltest.com](http://bechdeltest.com).  Please don't abuse the API with
unnecessary requests.
