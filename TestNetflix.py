#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_print, collatz_eval, collatz_solve, collatz_cycle, collatz_recursion, collatz_eager, __cache__


# -----------
# TestCollatz
# -----------
class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "1 11\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 11)

    def test_read_3(self):
        s = "1 43\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 43)

    def test_read_4(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_5(self):
        s = "157 23\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 157)
        self.assertEqual(j, 23)

    # -----
    # print
    # -----
    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 725526, 639609, 504)
        self.assertEqual(w.getvalue(), "725526 639609 504\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 59571, 785044, 509)
        self.assertEqual(w.getvalue(), "59571 785044 509\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 11684, 171423, 383)
        self.assertEqual(w.getvalue(), "11684 171423 383\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 88997, 723963, 509)
        self.assertEqual(w.getvalue(), "88997 723963 509\n")

    # -----
    # solve
    # -----
    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 11\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 11 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000000 525\n")

    def test_solve_4(self):
        r = StringIO("200 100\n1 10\n201 210\n1000000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "200 100 125\n1 10 20\n201 210 89\n1000000 900 525\n")

    # ----
    # eval
    # ----
    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_4(self):
        v = collatz_eval(725526, 639609)
        self.assertEqual(v, 504)

    def test_eval_6(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    def test_eval_7(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_8(self):
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_9(self):
        v = collatz_eval(210, 201)
        self.assertEqual(v, 89)

    def test_eval_10(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_11(self):
        v = collatz_eval(639609, 725526)
        self.assertEqual(v, 504)

    def test_eval_12(self):
        v = collatz_eval(1000000, 1)
        self.assertEqual(v, 525)

    # -----
    # cycle
    # -----
    def test_cycle_1(self):
        v = collatz_cycle(1)
        self.assertEqual(v, 1)

    def test_cycle_2(self):
        v = collatz_cycle(2)
        self.assertEqual(v, 2)

    def test_cycle_3(self):
        v = collatz_cycle(3)
        self.assertEqual(v, 8)

    def test_cycle_4(self):
        v = collatz_cycle(5)
        self.assertEqual(v, 6)

    def test_cycle_5(self):
        v = collatz_cycle(9)
        self.assertEqual(v, 20)

    def test_cycle_6(self):
        v = collatz_cycle(15)
        self.assertEqual(v, 18)

    def test_cycle_7(self):
        v = collatz_cycle(16)
        self.assertEqual(v, 5)

    # ---------
    # recursion
    # ---------
    def test_recursion_1(self):
        v = collatz_recursion(1)
        self.assertEqual(v, 1)

    def test_recursion_2(self):
        v = collatz_recursion(2)
        self.assertEqual(v, 2)

    def test_recursion_3(self):
        v = collatz_recursion(3)
        self.assertEqual(v, 8)

    def test_recursion_4(self):
        v = collatz_recursion(5)
        self.assertEqual(v, 6)

    def test_recursion_5(self):
        v = collatz_recursion(9)
        self.assertEqual(v, 20)

    def test_recursion_6(self):
        v = collatz_recursion(15)
        self.assertEqual(v, 18)

    def test_recursion_7(self):
        v = collatz_recursion(16)
        self.assertEqual(v, 5)

    # -----
    # eager
    # -----
    def test_eager(self):
        collatz_eager()
        self.assertEqual(__cache__[16], 5)
        self.assertEqual(__cache__[32], 6)
        self.assertEqual(__cache__[64], 7)
        self.assertEqual(__cache__[128], 8)
        self.assertEqual(__cache__[256], 9)
        self.assertEqual(__cache__[512], 10)
        self.assertEqual(__cache__[837799], 525)

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
