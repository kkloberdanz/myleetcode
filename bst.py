#!/usr/bin/env python3


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{repr(self.key)}: {repr(self.value)}"


class BST:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            _insert(self.head, key, value)

    def inorder_traverse(self):
        acc = []
        _inorder_traverse(self.head, acc)
        return acc

    def preorder_traverse(self):
        acc = []
        _preorder_traverse(self.head, acc)
        return acc

    def postorder_traverse(self):
        acc = []
        _postorder_traverse(self.head, acc)
        return acc

    def get(self, key):
        return _search(self.head, key)

    def __contains__(self, key):
        return self.get(key) is not None


def _search(node, key):
    if node is None:
        return None

    if key == node.key:
        return node

    if key < node.key:  # go left
        return _search(node.left, key)

    if key > node.key:  # go right
        return _search(node.right, key)


def _preorder_traverse(node, acc):
    if node is not None:
        acc.append(node)
        _preorder_traverse(node.left, acc)
        _preorder_traverse(node.right, acc)


def _inorder_traverse(node, acc):
    if node is not None:
        _inorder_traverse(node.left, acc)
        acc.append(node)
        _inorder_traverse(node.right, acc)


def _postorder_traverse(node, acc):
    if node is not None:
        _postorder_traverse(node.left, acc)
        _postorder_traverse(node.right, acc)
        acc.append(node)


def _insert(node, key, value):
    if key < node.key:  # go left
        if node.left is None:  # do insert
            node.left = Node(key, value)
        else:
            _insert(node.left, key, value)
    elif key > node.key:  # go right
        if node.right is None:  # do insert
            node.right = Node(key, value)
        else:
            _insert(node.right, key, value)


if __name__ == "__main__":
    bst = BST()
    bst.insert("four", 4)
    bst.insert("three", 3)
    bst.insert("eight", 8)
    bst.insert("one", 1)
    bst.insert("two", 2)
    bst.insert("nine", 9)
    print(bst.preorder_traverse())
    print(bst.inorder_traverse())
    print(bst.postorder_traverse())
    print(bst.get("nine"))
    print(bst.get("zero"))
    print(bst.get("two"))
    print("four" in bst)
    print("zero" in bst)
