

from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.next = next
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val: int) -> None:
        node = Node(val)
        
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node
    
    def append(self, val: int) -> None:
        node = Node(val)
        
        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur:
            if not cur.next:
                cur.next = node
                break
            cur = cur.next

    def insert(self, val: int, index: int) -> None:
        if index == 0:
            return self.prepend(val)
        
        prev_node = self.search(index - 1)
        if not prev_node: 
            raise IndexError("The index is out of list's size")

        node = Node(val)
        node.next = prev_node.next
        prev_node.next = node

    def shift(self) -> Optional[Node]:
        if not self.head:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp

    def pop(self) -> Optional[Node]:
        if not self.head:
            return None

        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = cur.next
        
        if prev:
            prev.next = None
        else:
            self.head = None

        return cur
            

    def search(self, index: int) -> Node:
        cnt = 0
        cur = self.head

        while cur:
            if cnt == index:
                return cur
            cur = cur.next
            cnt += 1
        
        raise IndexError("The index is out of list's size")

    def display(self) -> str:
        res = ""
        
        cur = self.head
        while cur:
            res += str(cur.val)
            if cur.next:
                res += " -> "
            cur = cur.next
 
        return res
    
ll = LinkedList()
ll.append(2)
ll.append(4)
ll.prepend(1)
ll.insert(3,2)
# ll.pop()
# ll.pop()
# ll.pop()
# ll.shift()


print(ll.display())
