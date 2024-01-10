from math_package.series import fibonacci
# from math_package.series import lucas
# from math_package.series import sum_series



def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = '0'
  assert actual == expected 

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = '1'
  assert actual == expected 

def test_fibonacci_two():
  actual = fibonacci(2)
  expected = '1'
  assert actual == expected 

def test_fibonacci_three():
  actual = fibonacci(3)
  expected = '2'
  assert actual == expected 

def test_fibonacci_nine():
  actual = fibonacci(9)
  expected = '21'
  assert actual == expected 