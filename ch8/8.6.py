import doctest
from collections import deque

class Tower():

  def __init__(self, n):
    self.disks = deque()
    for i in range(n):
      self.disks.appendleft(i)

  def add(self, disk: int):
    if self.disks and self.disks[-1] <= disk:
      print('Error adding disk ', disk)
    else:
      self.disks.append(disk)

  def move_top_to(self, tower):
    if self.disks:
      tower.add(self.disks.pop())

  def move_disks(self, n, dest, buff):
    if n > 0:
      self.move_disks(n-1, buff, dest)
      self.move_top_to(dest)
      buff.move_disks(n-1, dest, self)

def towers_of_hanoi(n):
  towers = [Tower(n), Tower(0), Tower(0)]
  for t in towers:
    print(t.disks)
  towers[0].move_disks(n, towers[2], towers[1])
  for t in towers:
    print(t.disks)

doctest.testmod()
