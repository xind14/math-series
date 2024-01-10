from math_package.series import fibonacci
from math_package.series import lucas
from math_package.series import sum_series



def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected 

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected 

def test_fibonacci_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected 

def test_fibonacci_three():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected 

def test_fibonacci_nine():
  actual = fibonacci(9)
  expected = 34
  assert actual == expected 



def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected 

def test_lucas_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected 

def test_lucas_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected 

def test_lucas_three():
  actual = lucas(3)
  expected = 4
  assert actual == expected 

def test_lucas_nine():
  actual = lucas(9)
  expected = 76
  assert actual == expected 


def test_sum_series_fibonacci():
  actual = sum_series(9,0,1)
  expected = 34
  assert actual == expected 

def test_sum_series_lucas():
  actual = sum_series(9,2,1)
  expected = 76
  assert actual == expected 