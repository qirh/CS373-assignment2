#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase


from Netflix import netflix_read, netflix_print, netflix_load_cache, netflix_rmse
from Netflix import cache_answers_location, cache_customer_avg_rating_location, cache_movie_avg_rating_location

# -----------
# TestNetflix
# -----------
class TestNetflix (TestCase):

	# ----
	# read
	# ----

	def test_read_1(self):
		s = "467:\n"
		b, i = netflix_read(s)
		self.assertEqual(i, "467")

	def test_read_2(self):
		s = "1109700,3,2001-07-12\n"
		b, i = netflix_read(s)
		self.assertEqual(i, "1109700")


"""
	def test_load_cache_1(self):
		cache = netflix_load_cache(cache_answers_location)
		self.assertEqual( cache[2043], {716091, 2})
		self.assertEqual( cache[2043], {1990901, 5})
		self.assertEqual( cache[2046], {1294425, 3})
		self.assertEqual( cache[2046], {2403193, 3})
		self.assertEqual( cache[2049], {2048459, 3})
		self.assertEqual( cache[2049], {2220019, 3})
	def test_load_cache_2(self):
		cache = netflix_load_cache(cache_customer_avg_rating_location)
		self.assertEqual( cache[2043], {716091, 2})
		self.assertEqual( cache[2043], {1990901, 5})
		self.assertEqual( cache[2046], {1294425, 3})
		self.assertEqual( cache[2046], {2403193, 3})
		self.assertEqual( cache[2049], {2048459, 3})
		self.assertEqual( cache[2049], {2220019, 3})
	def test_load_cache_3(self):
		cache = netflix_load_cache(cache_answers_location)
		self.assertEqual( cache[2043], {716091, 2})
		self.assertEqual( cache[2043], {1990901, 5})
		self.assertEqual( cache[2046], {1294425, 3})
		self.assertEqual( cache[2046], {2403193, 3})
		self.assertEqual( cache[2049], {2048459, 3})
		self.assertEqual( cache[2049], {2220019, 3})
"""		


# ----
# main
# ----

if __name__ == "__main__":
	main()

