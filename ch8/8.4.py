import doctest

def power_set(s: []) -> set(set()):
  """
  Best Solution.
  Time: O(n*2^n)
  Space: O(2^n)
  >>> power_set({1, 2, 3})
  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
  >>> power_set({1, 2})
  [[], [1], [2], [1, 2]]
  >>> power_set({1})
  [[], [1]]
  >>> power_set([])
  [[]]
  """
  if not s:
    return [[]]
  s_copy = s.copy()
  ps = [[]]
  while s_copy:
    elem = s_copy.pop()
    temp = []
    for e in ps:
      temp.append(e + [elem])
    ps += temp
  return ps

doctest.testmod()
