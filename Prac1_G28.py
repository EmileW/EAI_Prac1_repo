"""
EAI 320 Practical 1 : DFS and BFS Tree Traversal to find an opponents break sequence

Group Members: Emile Wepener u21494780
               Muller Pretorius u21444553
               
Date : 26/02/2024

Notes for Self: Object - Rock, Paper or Scissor 
                Move - A round where each opponent shows an Object
                Match - A series of Moves (rounds) where at the end a winner is allocated
                Sequence - Series of played Objects by an Opponent

""" 

import numpy as np


bfs_dfs = 0 # Variable to change between Depth First Search and 
            # Breath First Seach tree traveral algorithms. bfs_dfs = 0 (BFS) bfs_dfs = 1 (DFS)

# Node class for the search tree
class Node:
    def __init__(self, rpsobject):
        self.rpsobject = rpsobject #The Rock, Paper or Scissor represented by the Node
        self.children = [None, None, None]  # Each node has 3 children as there could be 3 different Objects that could be played after 
                                            # the Object stored in the node

# Recursive Tree constructor, with 3 children for each node (R, P and S).
# The depth of the tree is input depth-1
def construct_search_tree(depth):
    if depth == 0:
        return None
    root = Node("") #Root Node has no Object
    if depth > 1:
        root.children[0] = construct_search_tree(depth - 1) # Child 1
        root.children[0].rpsobject = "R"                    # Rock
        
        root.children[1] = construct_search_tree(depth - 1) # Child 2
        root.children[1].rpsobject = "P"                    # Paper
            
        root.children[2] = construct_search_tree(depth - 1) # Child 3
        root.children[2].rpsobject = "S"                    # Scissor
    return root

def print_tree(root, depth=0):
    if root is not None:
        print("  " * depth + str(root.rpsobject))
        for child in root.children:
            print_tree(child, depth + 1)


# root = construct_search_tree(10)
# print_tree(root)

if not input:
    # This is the first Move
    Tree_Size = 2
    
    
else:
    # This is the 2nd+ Move
    print("AWE")
    
    


            


