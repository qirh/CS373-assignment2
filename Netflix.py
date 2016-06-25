#!/usr/bin/env python3


import sys
import os
import pickle
import datetime
from statistics import mean
from numpy import mean, sqrt, square, subtract
from urllib.request import urlopen

#caches

#{int:dict{int:int} }: a dictionary cache, where the movie id was the key, and a dictionary was the value (that dictionary has customer_id's as keys, and the rating they gave as values
cache_answers = {}
cache_answers_location = "amm6364-answer.p"

#{int:float}: a dictionary cache, where customer_id was the key, and the average rating of all movies they watched as the value
cache_customer_avg = {}
cache_customer_avg_location = "amm6364-averageCustomerRating.p"

# {int:float}: a dictionary cache, where the movie_id was the key, and the average rating customers gave that movie as the value
cache_movie_avg = {}
cache_movie_avg_location = "amm6364-averageMovieRating.p"

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
	reads s
	"""
	return reader.readline().strip()


# -------------
# netflix_print
# -------------

def netflix_print(writer, n):
	""" #pragma: no cover
	w a writer
	n is a number which is either the movie or customer id
	prints n to w
	"""
	writer.write(str(n) + "\n")


# --------------
# netflix_actual
# --------------

def netflix_actual(movie_id, customer_id):
	""" #pragma: no cover
	"""

	return cache_answers[movie_id][customer_id]


# ---------------
# netflix_predict
# ---------------

def netflix_predict(movie_id, customer_id):
	""" #pragma: no cover
	"""
	customer_avg = cache_customer_avg[customer_id]
	customer_avg = cache_movie_avg[movie_id]
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
	return cache

# ------------
# netflix_rmse
# ------------
def netflix_rmse(squ_diff, num):
	""" #pragma: no cover
	sum is a square root sum
	num is the number of elements
	calculates the root mean square error
	"""
	return sqrt( mean( pow(subtract(squ_diff, num), 2)))

def rmse_numpy (a, p) :
    return sqrt(mean(square(subtract(a, p))))



# -------------
# netflix_solve
# -------------
def netflix_solve(reader, writer):
	"""
	r a reader
	w a writer
	"""
	#loading caches
	cache_answers = netflix_load_cache(cache_answers_location)
	cache_customer_avg = netflix_load_cache(cache_customer_avg_location)
	cache_movie_avg = netflix_load_cache(cache_movie_avg_location)

	count = 0
	squ_diff = 0
	flag = True

	while (flag) :

		line = netflix_read(reader)

		print("line -->" + line)

		if not line :
			netflix_print(writer, "RMSE: " + str(netflix_rmse(squ_diff,count)))
			flag = False

		elif line[-1] != ":" : #customer id

			prediction = netflix_predict(cache_customer_avg[line],cache_movie_avg[currentMovieID])
			actual = cache_answers[currentMovieID + "-" + line]
			squ_diff += ((actual - prediction) ** 2)
			count += 1

			netflix_print(writer, prediction)
	  
		else : #movie id
			currentMovieID=line[:-1]
			netflix_print(writer, line)

