#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        s = ["["]
        while node is not None:
            if node.next is None:
                s.append(str(node))
            else:
                s.append(str(f"{node}, "))
            node = node.next
        s.append("]")
        return "".join(s)

    def insert_after(self, curr, data):
        if self.head is None:
            self.head = Node(data)
        else:
            old_next = curr.next
            new_next = Node(data)
            new_next.next = old_next
            curr.next = new_next

    def insert_end(self, data):
        curr = self.head
        prev = None
        while curr is not None:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = Node(data)
        else:
            prev.next = Node(data)

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_after(ll.head, 1)
    ll.insert_after(ll.head, 2)
    ll.insert_after(ll.head, 3)
    ll.insert_after(ll.head, 4)
    ll.insert_after(ll.head, 5)
    ll.insert_after(ll.head, 6)
    print(ll)
    ll.insert_end(7)
    print(ll)
    ll.reverse()
    print(ll)
