import doctest

def magic_index(l: [int]) -> int:
  """
  >>> magic_index([-1, 1, 3, 6, 8])
  1
  >>> magic_index([-10, -7, -4, 3, 10])
  3
  >>> magic_index([-10, -7, -4, 2, 10])
  -1
  >>> magic_index([-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13])
  2
  >>> magic_index([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])
  2
  """
  return __magic_index(l, 0, len(l) - 1)

def __magic_index(l: [int], start: int, end: int) -> int:
  if end < start:
    return -1
  mid = int((end+start)/2)
  if mid == l[mid]:
    return mid
  left = __magic_index(l, start, min(mid - 1, l[mid]))
  if left >= 0:
    return left

  return __magic_index(l, max(mid + 1, l[mid]), end)

doctest.testmod()

