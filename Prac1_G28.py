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


bfs_dfs = 1 # Variable to change between Depth First Search and 
            # Breath First Seach tree traveral algorithms. bfs_dfs = 0 (BFS) bfs_dfs = 1 (DFS)

# Node class for the search tree
class Node:
    def __init__(self, rpsobject):
        self.rpsobject = rpsobject #The Rock, Paper or Scissor represented by the Node
        self.children = [None, None, None]  # Each node has 3 children as there could be 3 different Objects that could be played after 
                                            # the Object stored in the node
        self.visited = 0

# Recursive Tree constructor, with 3 children for each node (R, P and S).
# The depth of the tree is input depth-1
def construct_search_tree(depth,rpsobject = ""):
    if depth == 0:
        return None
    root = Node(rpsobject) #Root Node has no Object
    if depth > 1:
        root.children[0] = construct_search_tree(depth - 1,root.rpsobject +"R") # Child 1
        root.children[0].rpsobject = root.rpsobject + "R"                    # Rock
        
        root.children[1] = construct_search_tree(depth - 1,root.rpsobject +"P") # Child 2
        root.children[1].rpsobject = root.rpsobject+ "P"                    # Paper
            
        root.children[2] = construct_search_tree(depth - 1,root.rpsobject +"S") # Child 3
        root.children[2].rpsobject = root.rpsobject + "S"                    # Scissor
    return root

def print_tree(root, depth=0):
    if root is not None:
        print("  " * depth + str(root.rpsobject))
        for child in root.children:
            print_tree(child, depth + 1)
            
            
def DFS(root):
    if root is None:
        return []
    
    stack = [root]  # Stack to keep track of nodes to visit
    visited = []    # List to store visited node values
    while stack:
        current_node = stack.pop()  # Pop the top node from the stack
        current_node.visited = 1
        if not current_node == root:
            # Store the value of the current node
            visited.append(current_node.rpsobject)
        
        # Push the children of the current node onto the stack in reverse order
        # This ensures that the leftmost child is visited first
        for child in reversed(current_node.children):
            if child is not None:
                stack.append(child)            
    
    return visited

def test_for_break(prev_input):
    if (input == prev_input):
        return True
    else:
        return False
    
def win_move(input):
    if input == "R":
        return "P"
    
    if input == "P":
        return "S"
    
    if input == "S":
        return "R"


if  input == "":
    
    Tree_Depth = 2
    root = construct_search_tree(Tree_Depth)
    i = 0
    dfs_list = DFS(root)
    seq = dfs_list[i]
    i = i + 1
    output = seq[0]
    seq = seq[1:]
    last_input = input
    break_sequence = ""
    false_break = 0
    # print(output)
    
        
else:
    if (len(seq) == 0):
        # All of the Objects for the node have been played, a new node is needed.
        # Test if a break sequence occured
        if test_for_break(last_input):
            # The previous sequence was a break sequence !
            false_break = 0
            break_sequence = dfs_list[i-1]
            
            output = win_move(input)
        else:
            # no break sequence
            if (len(break_sequence) > 0 ):
                seq = break_sequence
                output = seq[0]
                seq = seq[1:]
                false_break = false_break + 1
                if (false_break > 3):
                    # We found a false break sequence
                    break_sequence = ""
            else:  
                # First test if there are still nodes to be tested
                if (i < len(dfs_list)):
                    # Move to the next node
                    seq = dfs_list[i]
                    i = i + 1
                    output = seq[0]
                    seq = seq[1:]
                else:
                    # All of the nodes have been tested, create a larger search tree
                    Tree_Depth = Tree_Depth +1
                    root = construct_search_tree(Tree_Depth)
                    i = 0
                    dfs_list = DFS(root)
                    seq = dfs_list[i]
                    i = i + 1
                    output = seq[0]
                    seq = seq[1:]
            
    else:
        # There are still objects in the node to be played
        output = seq[0]
        seq = seq[1:]        
    last_input = input
    
    # print(output)
    
    
    
   
            

    
    


            


