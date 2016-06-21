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

def netflix_read(s):
	""" #pragma: no cover
	s is a string representing a line
	if it's a movie id, returns true and the id
	if it's a customer id, returns false and the id
	"""
	if ":" in s:
		return True, s.split(":")[0]
	else:
		return False, s.rstrip()
	netflix_set_cache (s)

# -------------
# netflix_print
# -------------

def netflix_print(w, n, flag):
	""" #pragma: no cover
	w a writer
	s is a string
	flag is a boolean, true if movie id, false if customer id
	"""
	if(flag):
		w.write( str(n) + ":\n" )
	else:
		w.write( str(round(float(n),1)) + "\n")

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

def netflix_rmse(sum, num):
	""" #pragma: no cover
	sum is a square root sum
	num is the number of elements
	"""
	return sqrt(mean(square(subtract(sum, num))))


