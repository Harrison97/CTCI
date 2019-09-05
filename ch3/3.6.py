import LinkedList

LinkedList = LinkedList.SinglyLinkedList

# Could be implemented w 2 Queues to
# reduce specific dequeing time to O(1)
class AnimalShelter(LinkedList):
    DOG = 'DOG'
    CAT = 'CAT'

    def __init__(self):
        super().__init__()
    def enqueue(self, name, animal_type):
        # Time: O(1)
        super().append_to_tail((name, animal_type))
    def dequeue(self):
        # Time: O(1)
        animal = self.head.val
        self.head = self.head.next
        return animal
    def dequeue_dog(self):
        # Time: O(n)
        if self.head.val[1] == self.DOG:
            dog = self.head.val
            self.head = self.head.next
            return dog
        curr = self.head
        while curr.next and curr.next.next and curr.next.val[1] != self.DOG:
            curr = curr.next
        if curr.next.val[1] == self.DOG:
            dog = curr.next.val
            curr.next = curr.next.next
            return dog
        return None
    def dequeue_cat(self):
        # Time: O(n)
        if self.head.val[1] == self.CAT:
            cat = self.head.val
            self.head = self.head.next
            return cat
        curr = self.head
        while curr.next and curr.next.next and curr.next.val[1] != self.CAT:
            curr = curr.next
        if curr.next.val[1] == self.CAT:
            cat = curr.next.val
            curr.next = curr.next.next
            return cat
        return None

a = AnimalShelter()
a.enqueue('Bob', 'CAT')
a.enqueue('Bobby', 'CAT')
a.enqueue('Bill', 'DOG')
a.enqueue('Sam', 'DOG')
a.enqueue('Sammy', 'CAT')
a.enqueue('Bob', 'DOG')
a.enqueue('Mike', 'CAT')
