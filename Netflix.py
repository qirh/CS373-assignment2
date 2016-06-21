#!/usr/bin/env python3


import sys
import os
import pickle
import datetime
from urllib.request import urlopen

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
	print(MIN_MOVIE_DATE)
	netflix_set_cache (s)

# -----------------
# netflix_set_cache
# -----------------
def netflix_set_cache(name_of_cache):
	filepath = "/u/downing/public_html/netflix-caches/" + name_of_cache

	if os.path.isfile(filepath):
		print("in system")
		f = open(filepath, 'rb')
		cache = pickle.load(f)
		f.close() #always remember to close the file

	else:
		print("outside")
		base_url = "http://www.cs.utexas.edu/users/downing/netflix-caches/"
		cache_url = base_url + name_of_cache
		cache_read_from_url = urlopen(cache_url).read()
		cache = pickle.loads(cache_read_from_url)
	
	print (cache)


