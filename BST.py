
from linkedbinarytree import LinkedBinaryTree

"""Firstly, perform an in-order traversal of a binary tree."""

def in_order_traversal(tree, position, depth=0):
    if tree.left(position) is not None:
        in_order_traversal(tree, tree.left(position), depth + 1)
    print(" " * depth + "|--", position.element())
    if tree.right(position) is not None:
        in_order_traversal(tree, tree.right(position), depth + 1)


""" Then construct a binary search tree (BST) from a sorted list of elements by 
recursively inserting the middle element of the list into the tree and constructing its left and right subtrees"""

def construct_bst(tree, position, elements):
    if not elements:
        return
    mid = len(elements) // 2
    tree.replace(position, elements[mid])
    if mid > 0 and tree.left(position) is None:
        tree.add_left(position, None)
    if mid < len(elements) - 1 and tree.right(position) is None:
        tree.add_right(position, None)
    if tree.left(position) is not None:
        construct_bst(tree, tree.left(position), elements[:mid])
    if tree.right(position) is not None:
        construct_bst(tree, tree.right(position), elements[mid+1:])


""" Finally, convert a binary tree to a BST using our inorder generator and BST constructor method """

def converter_bst(tree):
    if tree.is_empty():
        return
    in_order_elements = [p.element() for p in tree.inorder_gen()]
    in_order_elements.sort()
    construct_bst(tree, tree.root(), in_order_elements)