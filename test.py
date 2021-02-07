
class Node():
  val = None
  nxt = None

  def print(self):
    print(self.val)
    curr = self.nxt
    while curr:
      print(curr.val)
      curr = curr.nxt

def sum_lists(l1, l2):
  s = Node()
  Sum = s

  carry = 0

  while l1 != None:
    Sum.val = (l1.val + l2.val) % 10 + carry

    carry = int((l1.val + l2.val) / 10)

    l1 = l1.nxt
    l2 = l2.nxt

    Sum.nxt = Node()

    Sum = Sum.nxt

  return s

ll1 = Node()
ll1.val = 7
ll1.nxt = Node()
ll1.nxt.val = 1
ll1.nxt.nxt = Node()
ll1.nxt.nxt.val = 6

ll2 = Node()
ll2.val = 5
ll2.nxt = Node()
ll2.nxt.val = 9
ll2.nxt.nxt = Node()
ll2.nxt.nxt.val = 2
