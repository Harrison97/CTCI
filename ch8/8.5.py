import doctest

def multiply(low ,high):
  """
  Time: O(min(x, y))
  CAN BE FASTER
  >>> multiply(3, 4)
  12
  >>> multiply(4, 3)
  12
  >>> multiply(10, 4)
  40
  >>> multiply(0, 4)
  0
  >>> multiply(1, 4)
  4
  """
  if low <= 0 or high <= 0:
    return 0
  if low > high:
    temp = low
    low = high
    high = temp
  return __multiply(high, low, 1)

def __multiply(x, y, c):
  if c == y:
    return x
  return x + __multiply(x, y, c+1)

doctest.testmod()
