# -*- coding: utf-8 -*-
"""
Submitted on 19th April 2023

SUBMISSION ASSIGNMENT 8 

@authors: Fabian Metz | Amin Oueslati | Oskar Krafft | Paul Sharratt
"""

from linkedbinarytree import LinkedBinaryTree
from conversion import binary_tree_to_bst

# populate the tree

lbt = LinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt._add_root(2)
lbt._add_left(lbt.root(), 19)
lbt._add_right(lbt.root(), 8)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt._add_left(l, 10)
lbt._add_right(l, 12)

lbt._add_left(r, 16)
lbt._add_right(r, 20)

# perform inorder traversal before converting the tree
lbt.print_inorder()  # Output: [10, 19, 12, 2, 16, 8, 20]

# convert the binary tree to a binary search tree
binary_tree_to_bst(lbt, lbt.root())

# perform inorder traversal after converting the tree
lbt.print_inorder()  # Output: [2, 8, 10, 12, 16, 19, 20]