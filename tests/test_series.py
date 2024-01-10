from math_package.series import fibonacci
# from math_package.series import lucas
# from math_package.series import sum_series



def test_fibonacci_one():
  actual = fibonacci(1)
  expected = '1'
  assert actual == expected 

def test_fibonacci_two():
  actual = fibonacci(2)
  expected = '2'
  assert actual == expected 

def test_fibonacci_three():
  actual = fibonacci(3)
  expected = '3'
  assert actual == expected 

def test_fibonacci_four():
  actual = fibonacci(4)
  expected = '4'
  assert actual == expected 

def test_fibonacci_five():
  actual = fibonacci(5)
  expected = '5'
  assert actual == expected 