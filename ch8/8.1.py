import doctest

def triple_step_1(n: int) -> int:
  """
  Bottom-Up, Iterative, minimal cache solution
  Time: O(n)
  Space: O(1)
  >>> triple_step_1(0)
  0
  >>> triple_step_1(-1)
  0
  >>> triple_step_1(1)
  1
  >>> triple_step_1(2)
  2
  >>> triple_step_1(3)
  4
  >>> triple_step_1(6)
  24
  """
  if n <= 0:
    return 0
  if n <= 2:
    return n
  if n == 3:
    return 4

  min1 = 4
  min2 = 2
  min3 = 1

  for i in range(4, n+1):
    ans = min1 + min2 + min3
    min3 = min2
    min2 = min1
    min1 = ans

  return ans

def triple_step_2(n: int) -> int:
  """
  Top-Down, Recursive Solution w/ Memoization
  Time: O(n)
  Space: O(n)
  >>> triple_step_2(0)
  0
  >>> triple_step_2(-1)
  0
  >>> triple_step_2(1)
  1
  >>> triple_step_2(2)
  2
  >>> triple_step_2(3)
  4
  >>> triple_step_2(6)
  24
  """
  if n <= 0:
    return 0

  memo = {}
  memo[1] = 1
  memo[2] = 2
  memo[3] = 4

  return __triple_step_2(n, memo)

def __triple_step_2(n: int, m: {}) -> int:
  if n in m:
    return m[n]
  if n-1 in m and n-2 in m and n-3 in m:
    m[n] = m[n-1] + m[n-2] + m[n-3]
    return m[n]
  m[n] = __triple_step_2(n-1, m) + __triple_step_2(n-2, m) + __triple_step_2(n-3, m)
  return m[n]

def triple_step_3(n: int) -> int:
  """
  Top-Down, Recursive Solution w/o Memoization
  Time: O(3^n)
  Space: O(3^n)
  >>> triple_step_3(0)
  1
  >>> triple_step_3(-1)
  0
  >>> triple_step_3(1)
  1
  >>> triple_step_3(2)
  2
  >>> triple_step_3(3)
  4
  >>> triple_step_3(6)
  24
  """

  # Simplified base cases by returning 1 for n == 0
  if n < 0:
    return 0
  if n == 0:
    return 1

  return triple_step_3(n-1) + triple_step_3(n-2) + triple_step_3(n-3)

doctest.testmod()
