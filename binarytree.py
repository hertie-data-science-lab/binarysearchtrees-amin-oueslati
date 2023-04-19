# -*- coding: utf-8 -*-
"""
Submitted on 2nd April 2023

Re-using binary tree from assignment 6

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

from treetemplate import Tree
from abc import ABC, abstractmethod

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    
    @abstractmethod
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        pass
    
    @abstractmethod
    def right(self, p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child.
        """
        pass
    
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)