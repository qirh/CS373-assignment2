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

		s = StringIO("467:\n")
		i = netflix_read(s)
		self.assertEqual(i, "467:")

	def test_read_2(self):
		s = StringIO("1109700,3,2001-07-12\n")
		i = netflix_read(s)
		self.assertEqual(i, "1109700,3,2001-07-12")
	
	def test_read_3(self):
		s = StringIO("4320:\n")
		i = netflix_read(s)
		self.assertEqual(i, "4320:")

	def test_read_4(self):
		s = StringIO("1687310,2005-09-30\n")
		i = netflix_read(s)
		self.assertEqual(i, "1687310,2005-09-30")

	def test_read_5(self):
		s = StringIO("5867:\n")
		i = netflix_read(s)
		self.assertEqual(i, "5867:")

	def test_read_6(self):
		s = StringIO("1286101,2005-03-11\n")
		i = netflix_read(s)
		self.assertEqual(i, "1286101,2005-03-11")

	# -----
	# print
	# -----
	def test_print_1(self):
		w = StringIO()
		netflix_print(w, 2)
		self.assertEqual(w.getvalue(), "2\n")
	def test_print_2(self):
		w = StringIO()
		netflix_print(w, 4525)
		self.assertEqual(w.getvalue(), "4525\n")
	def test_print_3(self):
		w = StringIO()
		netflix_print(w, 3)
		self.assertEqual(w.getvalue(), "3\n")
	def test_print_4(self):
		w = StringIO()
		netflix_print(w, 2)
		self.assertEqual(w.getvalue(), "2\n")
	def test_print_5(self):
		w = StringIO()
		netflix_print(w, 235325523)
		self.assertEqual(w.getvalue(), "235325523\n")
	def test_print_6(self):
		w = StringIO()
		netflix_print(w, 124214)
		self.assertEqual(w.getvalue(), "124214\n")
	def test_print_7(self):
		w = StringIO()
		netflix_print(w, 276578)
		self.assertEqual(w.getvalue(), "276578\n")

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

