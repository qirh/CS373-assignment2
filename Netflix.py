#!/usr/bin/env python3


import sys
import os
import pickle
import datetime
from math import sqrt
from urllib.request import urlopen

#caches

#{int:dict{int:int} }: a dictionary cache, where the movie id was the key, and a dictionary was the value (that dictionary has customer_id's as keys, and the rating they gave as values
cache_answers = {}
cache_answers_location = "amm6364-answer.p"

#{int:float}: a dictionary cache, where customer_id was the key, and the average rating of all movies they watched as the value
cache_customer_avg_rating = {}
cache_customer_avg_rating_location = "amm6364-averageCustomerRating.p"

# {int:float}: a dictionary cache, where the movie_id was the key, and the average rating customers gave that movie as the value
cache_movie_avg_rating = {}
cache_movie_avg_rating_location = "amm6364-averageMovieRating.p"

#constants defined by specs
NUM_CUSTOMERS = 480189

MIN_CUSTOMER_ID = 1
MAX_CUSTOMER_ID = 2649429
MIN_RATING_DATE = datetime.date(1998,10,1)
MAX_RATING_DATE = datetime.date(2005,12,31)

MIN_MOVIE_ID = 1
MAX_MOVIE_ID = 17770
MIN_MOVIE_DATE = datetime.date(1890,1,1)
MAX_MOVIE_DATE = datetime.date(2005,12,31)


# ------------
# netflix_read
# ------------

def netflix_read(reader):
	""" #pragma: no cover
	s is a string representing a line
	if it's a movie id, returns true and the id
	if it's a customer id, returns false and the id
	"""
	return reader.readline().strip()


# -------------
# netflix_print
# -------------

def netflix_print(w, n):
	""" #pragma: no cover
	w a writer
	n is a number which is either the movie or customer id
	"""
	w.write(str(n) + "\n")


# --------------
# netflix_actual
# --------------

def netflix_actual(movie_avg, customer_avg, customer_rmse):
	""" #pragma: no cover
	"""
	return 0


# ---------------
# netflix_predict
# ---------------

def netflix_predict(movie_id, customer_id):
	""" #pragma: no cover
	"""
	return 0

# ------------------
# netflix_load_cache
# ------------------
def netflix_load_cache(cache_name):
	""" #pragma: no cover
	return a dict that represents the cache
	"""
	filepath = "/u/downing/public_html/netflix-caches/" + cache_name

	if os.path.isfile(filepath):
		print("in system")
		f = open(filepath, 'rb')
		cache = pickle.load(f)
		f.close() #always remember to close the file

	else:
		print("outside")
		cache_url = "http://www.cs.utexas.edu/users/downing/netflix-caches/" + cache_name
		cache_read_from_url = urlopen(cache_url).read()
		cache = pickle.loads(cache_read_from_url)
	
	print (cache)
	return cache

# ------------
# netflix_rmse
# ------------
def netflix_rmse(sum, num):
	""" #pragma: no cover
	sum is a square root sum
	num is the number of elements
	calculates the root mean square error
	"""
	return sqrt(mean(square(subtract(sum, num))))


# -------------
# netflix_solve
# -------------
def netflix_solve(reader, writer):
	"""
	r a reader
	w a writer
	"""



