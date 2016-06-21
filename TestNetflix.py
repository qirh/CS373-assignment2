#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase


from Netflix import netflix_read, netflix_print, netflix_load_cache, netflix_rmse
from Netflix import cache_customer_avg_rating_location, cache_answers_location, cache_movie_avg_rating_location

# -----------
# TestNetflix
# -----------
class TestNetflix (TestCase):

	# ----
	# read
	# ----

	def test_read_1(self):
		s = "1 10\n"
		i = netflix_read(s)
		self.assertEqual(i, s)

	def test_load_cache(self):
		cache = netflix_load_cache(cache_answers_location)
		self.assertEqual( cache[2043], {716091, 2})
		self.assertEqual( cache[2043], {1990901, 5})
		self.assertEqual( cache[2046], {1294425, 3})
		self.assertEqual( cache[2046], {2403193, 3})
		self.assertEqual( cache[2049], {2048459, 3})
		self.assertEqual( cache[2049], {2220019, 3})
		


# ----
# main
# ----

if __name__ == "__main__":
	main()

