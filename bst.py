#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            _insert(self.head, data)

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


def _preorder_traverse(node, acc):
    if node is not None:
        acc.append(node.data)
        _preorder_traverse(node.left, acc)
        _preorder_traverse(node.right, acc)


def _inorder_traverse(node, acc):
    if node is not None:
        _inorder_traverse(node.left, acc)
        acc.append(node.data)
        _inorder_traverse(node.right, acc)


def _postorder_traverse(node, acc):
    if node is not None:
        _postorder_traverse(node.left, acc)
        _postorder_traverse(node.right, acc)
        acc.append(node.data)


def _insert(node, data):
    if data < node.data:  # go left
        if node.left is None:  # do insert
            node.left = Node(data)
        else:
            _insert(node.left, data)
    elif data > node.data:  # go right
        if node.right is None:  # do insert
            node.right = Node(data)
        else:
            _insert(node.right, data)


if __name__ == "__main__":
    bst = BST()
    bst.insert(4)
    bst.insert(3)
    bst.insert(8)
    bst.insert(1)
    bst.insert(2)
    bst.insert(9)
    print(bst.preorder_traverse())
    print(bst.inorder_traverse())
    print(bst.postorder_traverse())
