# -*- coding: utf-8 -*-
"""
Submitted on 19th April 2023

SUBMISSION ASSIGNMENT 8 

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

from linkedbinarytree import LinkedBinaryTree

lbt = LinkedBinaryTree()

# run inorder traversal and store the values as list
def store_inorder_values(tree, p, values):
    if p is None:
        return

    store_inorder_values(tree, tree.left(p), values)
    values.append(p.element())
    store_inorder_values(tree, tree.right(p), values)

# create binary search tree from sorted array
def sorted_array_to_bst(tree, p, values):
    if p is None or not values:
        return

    mid = len(values) // 2
    tree._replace(p, values[mid])

    sorted_array_to_bst(tree, tree.left(p), values[:mid])
    sorted_array_to_bst(tree, tree.right(p), values[mid + 1:])

# sort values in array and convert to binary search tree
def binary_tree_to_bst(lbt, position):
    if position is None:
        return None

    values = []
    store_inorder_values(lbt, position, values)
    values.sort()

    sorted_array_to_bst(lbt, position, values)