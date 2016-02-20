from unittest import TestCase
import bechdel


class TestBechdel(TestCase):
    def test_imdbid(self):
        movie = bechdel.getMovieByImdbId('0367631')
        self.assertTrue(isinstance(movie, dict))
        self.assertTrue('title' in movie.keys())

    def test_imdb_title(self):
        movies = bechdel.getMoviesByTitle('terminator')
        self.assertTrue(isinstance(movies, list))
        self.assertTrue('title' in movies[0].keys())

    def test_get_all_ids(self):
        movie_ids = bechdel.getAllMovieIds()
        self.assertTrue(isinstance(movie_ids, list))
        self.assertTrue('imdbid' in movie_ids[0].keys())
