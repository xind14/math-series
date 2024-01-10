def fibonacci(n):
  """
  Parameters:
  - n : the index of fibonacci to return
  Returns: nth element in the fibonacci series.

  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci (n-2)

def lucas(n):
  """
  Parameters:
  - n : the index of lucas to return
  Returns: nth element in the lucas series.

  """
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas (n-1) + lucas (n-2)
  

def sum_series (n, parameter1, parameter2):
     
  """
  Parameters:
  - n : determine which element in the series to print.
  - parameter1: optional first value of the series (default is 0 for Fibonacci, 2 for lucas).
  - parameter2 : optional second value of the series (default is 1 for Fibonacci, 1 for lucas)
  Returns: nth element in the generated series.

  """
    
  if parameter1==0 and parameter2==1:
    return fibonacci(n)
  elif parameter1==2 and parameter2==1:
    return lucas(n)
  else:
    return sum_series(n-1) + sum_series(n-2)

