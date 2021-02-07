import doctest
from collections import deque

def find_path(grid: [[int]]) -> []:
  """
  Best Solution, uses 'memoization' kinda but only because it checks for
  most recent item so it doesn't create duplicates - dosen't keep a standard cache but tracks paths.
  Time
  >>> find_path([[0, 0, 0, 0, 0],
  ...            [0, 0, 0, 0, 0],
  ...            [0, 0, 0, 0, 0],
  ...            [0, 0, 0, 0, 0],
  ...            [0, 0, 0, 0, 0]])
  [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
  >>> find_path([[0, 0, 0, 0, 0],
  ...            [1, 0, 0, 0, 0],
  ...            [0, 1, 0, 1, 0],
  ...            [0, 0, 0, 0, 0],
  ...            [0, 0, 0, 0, 0]])
  [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
  >>> find_path([[0, 1],
  ...            [0, 0],
  ...            [1, 0]])
  [(0, 0), (1, 0), (1, 1), (2, 1)]
  >>> find_path([[0, 1],
  ...            [0, 1],
  ...            [1, 0]])
  >>> find_path([[]])
  """


  end = (len(grid) - 1, len(grid[0]) - 1)
  q = deque()
  q.append(((0, 0), [(0, 0)]))

  while q:
    curr = q.popleft()
    r = curr[0][0]
    c = curr[0][1]
    path = curr[1]
    if (r, c) == end:
      return path
    if r < end[0] and  grid[r + 1][c] == 0:
      q.append(((r + 1, c), path + [(r + 1, c)]))
    if c < end[1] and grid[r][c + 1] == 0:
      q.append(((r, c + 1), path + [(r, c + 1)]))

  return None

doctest.testmod()
