#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, __cache__


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

# ----
# main
# ----

if __name__ == "__main__":
    main()

