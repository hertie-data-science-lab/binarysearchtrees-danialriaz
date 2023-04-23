# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Augusto Fonseca, Danial Riaz, Fernando Corral, Rodrigo Dornelles
"""

from mlbt import MutableLinkedBinaryTree
from BST import in_order_traversal, converter_bst

lbt = MutableLinkedBinaryTree()



lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)



print()

print()


print("In-order traversal of the Binary Tree:")
in_order_traversal(lbt, lbt.root())
print()

converter_bst(lbt)

print("Transformation to BST:")
in_order_traversal(lbt, lbt.root())