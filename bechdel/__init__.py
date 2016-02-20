import requests

_base_url = 'http://bechdeltest.com/api/v1/'

def parseResponse(response):
    content = response.json()
    if 'status' in content.keys():
        raise requests.exceptions.HTTPError(
        'Request returned: {} - {}.'.format(content['status'],
            content['description']))
    return content

def getMovieByImdbId(imdbid):
    """
    Takes a string with an IMDB ID as input.

    Returns a dictionary with the following items:
        visible:      Has this movie been approved (currently always returns 1).
        date:         The date this movie was added to the list
        submitterid:  The ID of the submitter. Currently of no use.
        rating:       The actual score. 0 = no two women, 1 = no talking,
                      2 = talking about a man, 3 = passes test).
        dubious:      Whether the submitter considered the rating dubious.
        imdbid:       The IMDb id.
        id:           The bechdeltest.com unique id.
        title:        The title of the movie. Any non-ascii characters are HTML encoded
        year:         The year this movie was released (according to IMDb).
    """
    url = _base_url + 'getMovieByImdbId'
    response = requests.get(url, params={'imdbid':imdbid})
    return parseResponse(response)

def getMoviesByTitle(title):
    """
    Returns list of dictionaries with movie information. See documentation for
    getMovieByImdbId for info on returned items.
    """
    url = _base_url + 'getMoviesByTitle'
    response = requests.get(url, params={'title':title})
    return parseResponse(response)


def getAllMovieIds():
    """
    Returns a list of dictionaries containing bechdeltest.com and ImDb IDs.
    """
    url = _base_url + 'getAllMovieIds'
    response = requests.get(url)
    return parseResponse(response)


def goToMoviePage(imdbid):
    """
    Takes a string with an IMDB ID as input.

    Opens the default webbrowser and navigates to the bechdeltest.com page
    for the requested movie.
    """
    url = 'http://bechdeltest.com/view/' + imdbid
    webbrowser.open(url)
