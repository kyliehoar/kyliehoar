

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import numpy as np
from problem1 import RandomPlayer,Node
from game import BoardGame,Player
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Monte Carlo Tree Search (MCTS) (50 points)
    In this problem, you will implement the AI player based upon Monte-Carlo Tree Search.
    
'''
# ---------------------------------------------------------

'''------------- Class: MCNode (40.0 points) -------
    Now let's implement tree nodes first. Then we can connect the nodes into a search tree.
    This is the class for a Node of a Monte Carlo Search Tree
 
'''
''' ---- Class Properties ----
    * s: the current state of the game, s.b is an integer matrix  (shape: 3 by 3 in TictacToe, 8 by 8 in Othello). 
        s.b[i,j] = 0 denotes that the i-th row and j-th column is empty
        s.b[i,j] = 1 denotes that the i-th row and j-th column is taken by "X". 
        s.b[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
        s.x: who's turn in this step of the game (if X player: x=1, or if O player: x=-1)
.
    * p: the parent node of this node.
    * m: the move that it takes from the parent node to reach this node.  m is a tuple (row,column), row:row of move, column:column of the move 
.
    * c: a python list of all the children nodes of this node.
    * v: a float scalar, the sum of game results for all games that used this node during simulation.
    For example, if we have 5 game simulations used this node, and the results of the games are (1,-1,0,1,1),
    the sum of the game results will be 2 = (1 + (-1) + 0 + 1 + 1)
.
    * N: an integer scalar, the number games that used this node for simulation. We can use the these two statistics (v and N) to compute the average pay-offs of each node.
    '''
class MCNode(Node):
    #------------- Method: __init__  ------
    ''' Goal: Create a new node for a Monte Carlo Search Tree    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * s: the current state of the game
    * p: the parent node of this node
    * m: the move that it takes from the parent node to reach this node
    '''
    def __init__(self, s, p=None, m=None):
        super(MCNode, self).__init__(s,p=p,m=m,v=0) # initialize v as 0
        self.N=0 # initialize the number of times the node is selected in the simulation as 0
        
        
    #----------------------------------------------------------
    
    #------------- Method: sample  ------
    ''' Goal: Simulation: Use a Monte-Carlo simulation to sample a game result from the current node (self) of the tree. Simulate a game starting from this selected node (self) until the game reaches an end. In the simulation, both players are random players. 
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello
    ---- Outputs: --------
    * e: the result of the game of simulation (X player won:1, tie:0, lose: -1), an integer scalar.
    ---- Example: --------
    In TicTacToe, if the game state in the selected node (n) is:
|-------------------
| Selected Node n
|
|  s.b=[[ 0, 1, 1],
|       [ 0,-1, 1],
|       [-1, 1,-1]]     -- the game state in the node
|  s.x= -1              -- it's "O" player's turn in this step of the game
|    ...
|-------------------
Let's run one random game (where both players are random players, who choose random moves in the game).
# Game Result 1: Suppose in the simulation, the "O" player chooses the move (r=1,c=0), 
then "X" player chooses the move (r=0,c=0), so "X" player wins (e=1). 
# Game Result 2: If the "O" player chooses the move (0,0), then the game ends, "O" player wins (e=-1)
If we run this sample() function multiple times, the function should have equal chance to 
return Result 1 and Result 2. 
 
    ---- Hints: --------
    * You could use RandomPlayer in problem 1 and run_a_game() function in a BoardGame class in game.py to simulate a game starting from the current game state in the node (self). 
    * You could start a game simulation starting with any game state (s) using run_a_game(s=s), by specifying the initial state of the game. 
    * This problem can be solved using only 2 line(s) of code. More lines are okay.'''
    def sample(self, g):
        ##############################
        ## INSERT YOUR CODE HERE (4.0 points)
        e = BoardGame.run_a_game(g, RandomPlayer(), RandomPlayer(), s=self.s)
        ##############################
        return e
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_sample
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_sample
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: expand  ------
    ''' Goal: Expand the current tree node by adding one layer of children nodes by adding one child node for each valid next move. Then select one of the children nodes to return.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello
    ---- Outputs: --------
    * c: one of the children nodes of the current node (self). After calling expand(), all the children nodes are equally new, so we could just select any child node for the next step (to run the simulation).
    ---- Example: --------
    In TicTac, if the current node (BEFORE expanding) is like:
|-------------------
|Current Node:   
|  s.b=[[ 0, 1,-1],
|       [ 0,-1, 1],
|       [ 0, 1,-1]]     -- the game state in the node
|  s.x= 1               -- it's "X" player's turn in this step of the game
|    p= None           
|    m= None            
|    c=[] -- no children node
|    v= 0 
|    N= 0 
|-------------------
  There are 3 valid next moves from the current game state.
  AFTER expanding this node, we add three children nodes to the current node.
  The tree looks like this after being expanded:
                      |--> Child Node A
     Current Node --> |--> Child Node B 
                      |--> Child Node C 
  Here are the details of the tree (attributes of each tree node):
 |-------------------
 |Current Node:   
 |  s.b=[[ 0, 1,-1],
 |       [ 0,-1, 1],
 |       [ 0, 1,-1]]     
 |  s.x= 1        -- it's "X" player's turn in this step of the game  
 |    p= None           
 |    m= None            
 |    c=[Child_A, Child_B, Child_C] -- Three children nodes are created and added here
 |    v= 0 
 |    N= 0 
 |-------------------------------
         |Child Node A:   
         |  s.b=[[ 1, 1,-1],
         |       [ 0,-1, 1],
         |       [ 0, 1,-1]]     
         |  s.x=-1            -- it's "O" player's turn in this step of the game 
         |    p= Current_Node -- The parent node of this node is "Current_Node" 
         |    m= (0,0)        -- The move it takes from parent node 
         |                         to this node: first row (0), first column (0) 
         |    c=[] -- this node has not been expanded yet 
         |    v= 0 
         |    N= 0 
         |-----------------------
         |Child Node B:   
         |  s.b=[[ 0, 1,-1],
         |       [ 1,-1, 1],
         |       [ 0, 1,-1]]     
         |  s.x=-1            -- it's "O" player's turn in this step of the game 
         |    p= Current_Node -- The parent node of this node is "Current_Node" 
         |    m= (1,0)        -- The move it takes from parent node 
         |                        to this node: second row (1), first column (0) 
         |    c=[] -- this node has not been expanded yet 
         |    v= 0 
         |    N= 0 
         |-----------------------
         |Child Node C:   
         |  s.b=[[ 0, 1,-1],
         |       [ 0,-1, 1],
         |       [ 1, 1,-1]]     
         |  s.x=-1            -- it's "O" player's turn in this step of the game 
         |    p= Current_Node -- The parent node of this node is "Current_Node" 
         |    m= (2,0)        -- The move it takes from parent node 
         |                        to this node: third row (2), first column (0) 
         |    c=[] -- this node has not been expanded yet 
         |    v= 0 
         |    N= 0 
         |-----------------------
  After the expansion, you need to return one of the children nodes as the output.
  For example, you could return Child Node A, or Child Node B, or Child Node C.
 
    ---- Hints: --------
    * This function is very similar to the expand() in problem 1. 
    * Step 1: get the list of valid next move-state pairs from the current game state.. 
    * You could use g.get_move_state_pairs() function to get all the next moves and next game states from the current game state.. 
    * Step 2: expand the node with one level of children nodes.. 
    *   Step 2.1: for each next move m and game state s, create a new child node.. 
    *   Step 2.2: append the new child node to the child list of the current node.. 
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def expand(self, g):
        ##############################
        ## INSERT YOUR CODE HERE (8.0 points)
        node = g.get_move_state_pairs(self.s)
        for move, next in node:
            child = MCNode(next, self, move)
            self.c.append(child)
            c = child
        ##############################
        return c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_expand
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_expand
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: backprop  ------
    ''' Goal: Back propagation: after one simulation in node (S), use the game result to update the statistics in the nodes on the path from node S to the root node. 
    Along the way, update v (sum of simulation results) and N (count of simulations). 
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * e: the result of the game of simulation (X player won:1, tie:0, lose: -1), an integer scalar.
    ---- Example: --------
    In TicTacToe, the current game state is
|-------------------
| Root Node:   
|  s.b=[[ 1,-1, 1],
|       [ 0, 0, 0],
|       [ 0, 0,-1]]     -- the game state in the node
|  s.x= 1               -- it's "X" player's turn in this step of the game
|    p= None           
|    m= None            
|    c=[] -- list of children nodes
|    v= None               
|    N= None               
|-------------------

Suppose the tree looks like this:

               |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
               |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
               |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
               |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
               |
               |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
               |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
               |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
               |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
               |
Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
 1,-1, 1 (v=19)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
 0, 0, 0 (N=54)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
 0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
               |
               |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
               |     1,-1, 1 (v=13) |--> Grand Child D2 (v=3,N=5)
               |     0, 0, 0 (N=21) |--> Grand Child D3 (v=4,N=5)(S: selected node)  
               |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
               |
               |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                     1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                     0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1) 
                     0, 1,-1        |--> Grand Child E4 (v=0,N=1)

Here v is the sum of simulation results, N is the count of game simulations. 
Suppose the selected node for running simulation is "Grand Child D3".
Now we run a simulation starting from D3 node, and get one sample result: X player win (e=1).
The back-propagation is to update the nodes on the path from D3 to Root node.
In each node on the path, the statistics are updated with the game result (e=1)
After back-propagation, the tree looks like this:

               |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
               |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
               |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
               |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
               |
               |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
               |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
               |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
               |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
               |
Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
 1,-1, 1 (v=20)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
 0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
 0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
               |
               |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
               |     1,-1, 1 (v=14) |--> Grand Child D2 (v=3,N=5)
               |     0, 0, 0 (N=22) |--> Grand Child D3 (v=5,N=6)(S: selected node)  
               |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
               |
               |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                     1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                     0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1) 
                     0, 1,-1        |--> Grand Child E4 (v=0,N=1)
 There are three nodes on the path and their statistics are updated as:
 (1) Grand Child D3: v =(4 -> 5),    N =(5 -> 6)
 (2) Child Node D:   v =(13 -> 14),  N =(21 -> 22)
 (3) Root Node:      v =(19 -> 20),  N =(54 -> 55)
 
    ---- Hints: --------
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def backprop(self, e):
        ##############################
        ## INSERT YOUR CODE HERE (8.0 points)
        # Here v is the sum of simulation results, N is the count of game simulations.
        self.v += e
        self.N += 1
        if self.p != None:
             MCNode.backprop(self.p, e)
        pass 
        ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_backprop
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_backprop
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: compute_UCB  ------
    ''' Goal: Suppose the current node (self) is the i-th child node of a parent node. Given the role and counts in the parent node, compute UCB (Upper Confidence Bound) of this child node (self, or the i-th child node of its parent node).
The UCB score is the sum of two terms:
(1) Exploitation: the average payoffs of the child node = x*vi/ni
(2) Exploration: the need for exploring the child node = sqrt( log(N) / ni ). 
                  Note: when ni=0, this term should equals to positive infinity (instead of a divide-by-zero error).
The final score is computed as  (1)+ c* (2). 
A larger UCB score means that the child node leads to a better average pay-offs for the player, or the child node needs exploring.
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * N: total number of simulations on the parent node, an integer scalar
    * x: the role of the parent node ('X' player:1 or 'O' player:-1)
    * c: the parameter to trade-off between exploration and exploitation, a float scalar
    ---- Outputs: --------
    * b: the UCB score of the child node, a float scalar.
    ---- Hints: --------
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def compute_UCB(self, N, x, c=1.142):
        ni= self.N # the number of simulations choosing the i-th child node (self)
        vi= self.v # the sum of game results after choosing the i-th child node (self)
        ##############################
        ## INSERT YOUR CODE HERE (4.0 points)
        if ni == 0:
            b = (x*vi) + c*(np.inf)
        else:
            b = (x*vi/ni) + c*(np.sqrt(np.log(N)/ni))
        ##############################
        return b
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_compute_UCB
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_compute_UCB
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: select_a_child  ------
    ''' Goal: Select a child node of the current node which has the highest UCB score, return the child node as the result.
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    ---- Outputs: --------
    * c: the child node of the current node (self) with the highest UCB score
    ---- Example: --------
    suppose we have a parent node with two children nodes:
---------------------
Parent Node:  N = 12, x= -1 ('O' player)
    |Child Node A: v =-1, N = 2 
    |Child Node B: v =-5, N = 10
---------------------
The UCB bound of Child Node A: vi=-1, ni=2, N= 12, x=-1 
The UCB bound of Child Node B: vi=-5, ni=10, N= 12, x=-1 
In this example, the average payoffs (x*vi/ni) for the two nodes are the same.
The second term (exploration) determines which nodes get higher score: Child Node A is under-explored.
So the Child Node A will have a higher UCB score, and this function will select Child Node A to return.

When there is a tie in the UCB score, use the index of the child node as the tie-breaker.
 
    ---- Hints: --------
    * Step 1: get a list of UCB scores for all children nodes. 
    * Step 2: return the child node with the largest score. 
    * This problem can be solved using only 2 line(s) of code. More lines are okay.'''
    def select_a_child(self):
        ##############################
        ## INSERT YOUR CODE HERE (4.0 points)

        child_scores = [(MCNode.compute_UCB(child, self.N, self.s.x, 1.142), i) for i, child in enumerate(self.c)]
        c = self.c[max(child_scores)]


        nodes = []
        score = []
        max = -100
        for child in self.c:
            score.append(MCNode.compute_UCB(child, self.N, self.s.x, 1.142))
            nodes.append(child)
        ##############################
        return c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_select_a_child
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_select_a_child
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: selection  ------
    ''' Goal: Select a leaf node by traveling down the tree from the root to a leaf node. Here a leaf node is a node with no child node. In each step, choose the child node with the highest UCB score, until reaching a leaf node.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    ---- Outputs: --------
    * l: the leaf node selected
    ---- Example: --------
    In TicTac, suppose we have a search tree:
                        (O's turn)
                |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
                |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
                |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
                |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
                |
                |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
                |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
                |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
                |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
  (X's turn)    |
 Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
  1,-1, 1 (v=20)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
  0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
  0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
                |
                |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
                |     1,-1, 1 (v=14) |--> Grand Child D2 (v=3,N=5)
                |     0, 0, 0 (N=22) |--> Grand Child D3 (v=5,N=6)
                |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
                |
                |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                      1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                      0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1) 
                      0, 1,-1        |--> Grand Child E4 (v=0,N=1)

    We will call the function l = selection(Root_Node)
    Among the first level of children nodes,  the "Child Node D" has the highest UCB score.
    Then in the second level, we travel down to the "Child Node D" and find that "Grand Child D3" has the highest score
    among all the children nodes of "Child Node D".
    Then we travel down to the "Grand Child D3" and find that this node is a leaf node (no child).
    So we return "Grand Child D3" as the selected node to return.
 
    ---- Hints: --------
    * You could use recursion to solve this problem recursively.. 
    * Step 1: if the root node is a leaf node (no child), return root node. 
    * Step 2: otherwise: select a child node (c) of the root node. 
    * Step 3: recursively select the children nodes of node (c). 
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def selection(self):
        ##############################
        ## INSERT YOUR CODE HERE (8.0 points)
        
        ##############################
        return l
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_selection
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_selection
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: build_tree  ------
    ''' Goal: Given a node of the current game state, build a Monte-Carlo Search Tree by n iteration of (selection->expand->sample->backprop).    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello
    * n_iter: number of iterations/samples in the Monte Carlo Tree Search, an integer scalar
    ---- Example: --------
    In TicTacToe, suppose the current game state:

          Root Node 
           1,-1, 1 (v=0)
           0, 0, 0 (N=0)
           0, 0,-1 (X player's turn)  

      Now let's run one iteration of Monte-Carlo Tree Search (selection->expand->sample->backprop):
      ---------------------------------
      Iteration 1:  
      ---------------------------------
      (1) selection:  starting from root node, select one leaf node (L)
          In this case, the root node is a leaf node (no child node yet)
      (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node. 
          Then one of the children nodes will be selected, the tree becomes:
                          (O's turn)
                  |--> Child Node A 
                  |     1,-1, 1 (v=0) (S: Selected Node) 
                  |     1, 0, 0 (N=0)  
                  |     0, 0,-1        
                  |
                  |--> Child Node B
                  |     1,-1, 1 (v=0)  
                  |     0, 1, 0 (N=0)  
                  |     0, 0,-1        
    (X's turn)    |
   Root Node ---> |--> Child Node C 
    1,-1, 1 (v= 0)|     1,-1, 1 (v= 0) 
    0, 0, 0 (N= 0)|     0, 0, 1 (N=0)  
    0, 0,-1       |     0, 0,-1        
                  |
                  |--> Child Node D 
                  |     1,-1, 1 (v= 0) 
                  |     0, 0, 0 (N= 0) 
                  |     1, 0,-1        
                  |
                  |--> Child Node E 
                        1,-1, 1 (v=0)  
                        0, 0, 0 (N=0)  
                        0, 1,-1        

      (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is a draw (e=0)
      (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
          The statistics of the tree look like this:
                       |--> Child Node A (v=0,N=1) (S: Selected Node) 
                       |--> Child Node B (v=0,N=0)
   Root (v=0,N=1) ---> |--> Child Node C (v=0,N=0) 
                       |--> Child Node D (v=0,N=0) 
                       |--> Child Node E (v=0,N=0) 

      ---------------------------------
      Iteration 2:  
      ---------------------------------
      (1) selection:  starting from root node, select one leaf node (L)
          In the first level of children nodes, "Child Node B" has the largest UCB score (with index as tie-breaker).
          It is also a leaf node (no child node yet), so this node will be selected as the leaf node. 
      (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node. 
          Then one of the children nodes will be selected, the tree becomes:

                          (O's turn)                       (X's turn)
                       |--> Child Node A (v=0,N=1) 
                       |--> Child Node B (v=0,N=0)--> |--> Grand Child B1 (v=0,N=0) (S: Selected Node)
                       |                              |--> Grand Child B2 (v=0,N=0)
                       |                              |--> Grand Child B3 (v=0,N=0)
     (X's turn)        |                              |--> Grand Child B4 (v=0,N=0)
   Root (v=0,N=1) ---> |--> Child Node C (v=0,N=0) 
                       |--> Child Node D (v=0,N=0) 
                       |--> Child Node E (v=0,N=0) 
      (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is X win (e=1)
      (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
          The statistics of the tree look like this:

                          (O's turn)                       (X's turn)
                       |--> Child Node A (v=0,N=1) 
                       |--> Child Node B (v=1,N=1)--> |--> Grand Child B1 (v=1,N=1) (S: Selected Node)
                       |                              |--> Grand Child B2 (v=0,N=0)
                       |                              |--> Grand Child B3 (v=0,N=0)
     (X's turn)        |                              |--> Grand Child B4 (v=0,N=0)
   Root (v=1,N=2) ---> |--> Child Node C (v=0,N=0) 
                       |--> Child Node D (v=0,N=0) 
                       |--> Child Node E (v=0,N=0) 

      ---------------------------------
      Iteration 3:  
      ---------------------------------
      (1) selection:  starting from root node, select one leaf node (L)
          In the first level of children nodes, "Child Node C" has the largest UCB score (with index as tie-breaker).
          It is also a leaf node (no child node yet), so this node will be selected as the leaf node. 
      (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node. 
          Then one of the children nodes will be selected, the tree becomes:

                          (O's turn)                       (X's turn)
                       |--> Child Node A (v=0,N=1) 
                       |--> Child Node B (v=1,N=1)--> |--> Grand Child B1 (v=1,N=1) 
                       |                              |--> Grand Child B2 (v=0,N=0)
                       |                              |--> Grand Child B3 (v=0,N=0)
                       |                              |--> Grand Child B4 (v=0,N=0)
     (X's turn)        | 
   Root (v=1,N=2) ---> |--> Child Node C (v=0,N=0)--> |--> Grand Child c1 (v=0,N=0) (S: Selected Node)
                       |                              |--> Grand Child c2 (v=0,N=0)
                       |                              |--> Grand Child c3 (v=0,N=0)
     (X's turn)        |                              |--> Grand Child c4 (v=0,N=0) 
                       |--> Child Node D (v=0,N=0) 
                       |--> Child Node E (v=0,N=0) 

      (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is (e=-1)
      (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
          The statistics of the tree look like this:

                          (O's turn)                       (X's turn)
                       |--> Child Node A (v= 0,N=1) 
                       |--> Child Node B (v= 1,N=1)--> |--> Grand Child B1 (v=1,N=1) 
                       |                               |--> Grand Child B2 (v=0,N=0)
                       |                               |--> Grand Child B3 (v=0,N=0)
                       |                               |--> Grand Child B4 (v=0,N=0)
     (X's turn)        | 
   Root (v=1,N=2) ---> |--> Child Node C (v=-1,N=1)--> |--> Grand Child C1 (v=-1,N=1) (S: Selected Node)
                       |                               |--> Grand Child C2 (v=0,N=0)
                       |                               |--> Grand Child C3 (v=0,N=0)
     (X's turn)        |                               |--> Grand Child C4 (v=0,N=0) 
                       |--> Child Node D (v= 0,N=0) 
                       |--> Child Node E (v= 0,N=0) 

      ...


      ---------------------------------
      Suppose that, after 55 iterations, the tree looks like this: 
                          (O's turn)             (X's turn)
                  |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                  |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                  |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                  |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                  |
                  |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                  |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                  |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                  |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
    (X's turn)    |
   Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
    1,-1, 1 (v=25)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
    0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
    0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                  |
                  |--> Child Node D -->|--> Child D1 (v= 5,N=6) -->| Child D11 (v= 5,N=5) (game ends)
                  |     1,-1, 1 (v=20) |--> Child D2 (v= 5,N=5) -->| ...
                  |     0, 0, 0 (N=22) |--> Child D3 (v= 5,N=5) -->| ... 
                  |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                  |
                  |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                        1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                        0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ... 
                        0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...

      ---------------------------------
      Iteration 56:  
      ---------------------------------
      (1) selection:  starting from root node, select one leaf node (L)
          In the first level of children nodes, "Child Node D" has the largest UCB score for X player.
          In the second level of children nodes, "Child D1" has the largest UCB score for O player.
          In the third level of children nodes, "Child D11" has the largest UCB score for X player.
          It is also a leaf node (no child node), so this node will be selected as the leaf node. 
      (2) expand: Since the game in the D11 node has ended, we DON'T expand the node. 
          So Node D11 will be selected.
      (3) Sample: run a Monte-Carlo simulation on the selected Node (D11), suppose the result of the game is X win (e=1)
      (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
          The statistics of the tree look like this:

                          (O's turn)             (X's turn)
                  |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                  |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                  |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                  |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                  |
                  |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                  |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                  |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                  |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
    (X's turn)    |
   Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
    1,-1, 1 (v=26)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
    0, 0, 0 (N=56)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
    0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                  |
                  |--> Child Node D -->|--> Child D1 (v= 6,N=7) -->| Child D11 (v=6,N=6) (selected)
                  |     1,-1, 1 (v=21) |--> Child D2 (v= 5,N=5) -->| ...
                  |     0, 0, 0 (N=23) |--> Child D3 (v= 5,N=5) -->| ... 
                  |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                  |
                  |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                        1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                        0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ... 
                        0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...
 
    ---- Hints: --------
    * You could use the functions you implemented above, such as selection(), expand(), sample(),backprop(), to solve this problem.. 
    * Step 1: selection: starting from root node, select one leaf node (L). 
    * Step 2: check if the game in node L has ended, if not ended:. 
    *   Step 2.1: expansion: expand node (L) with one level of children nodes and select one of L's children nodes (C) as the leaf node. 
    *   Step 2.2: simulation: sample a game result from the selected leaf node (C). 
    * Step 3: back propagation: backpropagate the result of the simulation. If the game in node L has already ended, use the game result in L to back propagate. 
    * This problem can be solved using only 6 line(s) of code. More lines are okay.'''
    def build_tree(self, g, n_iter=100):
        for _ in range(n_iter):
            ##############################
            ## INSERT YOUR CODE HERE (4.0 points)
            pass 
            ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCNode_build_tree
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCNode_build_tree
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: MCTSPlayer (10.0 points) -------
    AI Player 3 (MCTS Player): Now let's implement the Monte-Carlo Tree Search agent for the game.
The goal of this agent is to find the approximately optimal move for the current game state.
(1) Build Tree: we will first build a Monte-Carlo Search Tree, where the root of the tree is the current game state.
(2) Choose Optimal Next Move: the agent will choose the child node with the largest number (N) as the next move.
 
'''
''' ---- Class Properties ----
    * n_iter: the number of simulations/iterations in the Monte Carlo sampling.
    '''
class MCTSPlayer(Player):
    #------------- Method: __init__  ------
    ''' Goal: Create a new AI player of Monte Carlo tree search    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * n_iter: the number of simulations/iterations in the Monte Carlo sampling
    '''
    def __init__(self, n_iter=100):
        self.n_iter = n_iter
        
        
    #----------------------------------------------------------
    
    #------------- Method: choose_optimal_move  ------
    ''' Goal: (Choose Optimal Next Move) Assume we have a Monte-Carlo search tree, and the statistics of all nodes are already computed.
Choose Next Move: the agent will choose the child node with the largest N value as the next move.
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * n: the root node of the search tree, assuming the statistics in all nodes are already computed.
    ---- Outputs: --------
    * r: the row number of the optimal next move, an integer scalar with value 0, 1, or 2.
    * c: the column number of the optimal next move, an integer scalar with value 0, 1, or 2.
    ---- Example: --------
    In TicTacToe, suppose we have the following search tree (X player's turn):
                        (O's turn)             (X's turn)
                |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                |
                |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
  (X's turn)    |
 Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
  1,-1, 1 (v=26)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
  0, 0, 0 (N=56)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
  0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                |
                |--> Child Node D -->|--> Child D1 (v= 6,N=7) -->| ... 
                |     1,-1, 1 (v=21) |--> Child D2 (v= 5,N=5) -->| ...
                |     0, 0, 0 (N=23) |--> Child D3 (v= 5,N=5) -->| ... 
                |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                |
                |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                      1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                      0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ... 
                      0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...     
    The optimal next move will be child node with the largest N (Child Node D) in the first level of the tree. 
    So in this example, the next move should be (r=2, c=0)
 
    ---- Hints: --------
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def choose_optimal_move(self, n):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        
        ##############################
        return r, c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCTSPlayer_choose_optimal_move
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCTSPlayer_choose_optimal_move
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: choose_a_move  ------
    ''' Goal: The action function of the MCTS player, which chooses next move in the game.  
Build a search tree with the current state as the root. Then find the most visited child node as the next move.
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello.
    * s: the current state of the game, 
s.b is an integer matrix:
s.b[i,j] = 0 denotes that the i-th row and j-th column is empty
s.b[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O") 
s.b[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
s.x: the role of the player, 1 if you are the "X" player in the game
    -1 if you are the "O" player in the game. 

    ---- Outputs: --------
    * r: the row number of the optimal next move, an integer scalar with value 0, 1, or 2.
    * c: the column number of the optimal next move, an integer scalar with value 0, 1, or 2.
    ---- Hints: --------
    * Step 1: create a tree node (n) with the current game state. 
    * Step 2: build a search tree with the tree node (n) as the root and n_iter as the number of simulations. 
    * Step 3: choose the best next move: the children node of the root node (n) with the largest number of samples (N). 
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def choose_a_move(self, g, s):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        
        ##############################
        return r, c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m MCTSPlayer_choose_a_move
        (Mac /Linux): python3 -m pytest -v test_2.py -m MCTSPlayer_choose_a_move
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (MCTS player) on TicTacToe game:
        (Windows OS): python demo1.py mcts
        (Mac /Linux): python3 demo1.py mcts
    You could play with the AI player in TicTacToe game by clicking a block on the board. It should be very hard to win a game with the AI player
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (MCTS player) on Othello game:
        (Windows OS): python demo2.py mcts
        (Mac /Linux): python3 demo2.py mcts
    You could play with the AI player in Othello game by clicking a highlighted block on the board (a valid move). It should be very hard to win a game with the AI player. The AI may be very slow in the first few steps.
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (MCTS player) on GO game (with a small board size):
        (Windows OS): python demo3.py mcts
        (Mac /Linux): python3 demo3.py mcts
    You could play with the AI player in GO game by clicking an intersection on the board. It should be easy to win a game with AI player. Bonus: If you want to improve the AI's performance a little bit, you could change the parameter of the demo3.py file. Change the number of iterations in 'MCTSPlayer(n_iter = 300)' to 1000. But the AI will be very slow.
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    

'''-------- TEST problem2.py file: (50 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_2.py
        (Mac /Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
        (Windows OS): python -m pytest -v
        (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
        (Windows OS): python grading.py
        (Mac /Linux): python3 grading.py
 The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

 That's all! Great job! You did it!
-------------------------------------------------------------------------'''




