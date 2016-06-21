#!/usr/bin/env python3


# -------
# imports
# -------

import sys

from Netflix import netflix_read, netflix_print

# ----
# main
# ----

if __name__ == "__main__":
    netflix_read("bis266-probeAns.p")
    netflix_print(sys.stdout, 4.1, False)
