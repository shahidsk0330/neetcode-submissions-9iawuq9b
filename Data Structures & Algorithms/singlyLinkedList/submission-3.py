from typing import List

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1  # Return -1 if index is out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head  # Insert at the head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node  # Append at the tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False  # List is empty

        if index == 0:
            self.head = self.head.next  # Remove the head
            return True

        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index - 1:
                curr.next = curr.next.next  # Skip over the node to be removed
                return True
            curr = curr.next
            i += 1  # Fix: increment index

        return False  # Index out of bounds

    def getValues(self) -> List[int]:
        curr = self.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
