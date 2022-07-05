from io import TextIOWrapper


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        

def is_palindrome(head):
    arr = []
    curr = head
    while curr is not None:
        arr.append(curr.val)
        curr = curr.next
    print(arr, list(reversed(arr)))
    if arr == list(reversed(arr)):
        return True
    else:
        return False 

# 1 - 2 - 3 - 3 - 2 - 1
head = Node(1)
one = Node(2)
three = Node(3)
four = Node(3)
five = Node(2)
six = Node(1)
head.next = one
one.next = three
three.next = four
four.next = five
five.next = six

print(is_palindrome(head))

