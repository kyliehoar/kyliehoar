
'''------------Turn on Word Wrap Setting in Your Editor--------------
    NOTE: For better readability of the instructions, 
          please turn on the 'Word Wrap' setting in your editor. 
    HOW: For example, in the VS Code editor, click "Settings" in the menu, 
         then type "word wrap" in the search box of the settings, 
    choose "on" in the drop-down menu.
    TEST: If you can read this long sentence without scrolling your screen from left to right, it means that your editor's word wrap setting is on and you are good to go. 
------------------------------------------------------------------'''

''' ------------Install *pygame* package--------------
    *pygame* is a python package for running demos of different games.
    Please type the following command in your terminal to install the pygame package:
        (Windows OS): python -m pip install pygame
        (Mac /Linux): python3 -m pip install pygame
     ------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import numpy as np
from game import GameState,BoardGame,Player
#---------------------------------------------------------

#--------------------------
def Terms_and_Conditions():
    ''' 
      By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically copied your solution from your desktop computer to your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework and building your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other students about this homework, only discuss high-level ideas or use pseudo-code. Don't discuss about the solution at the code level. For example, two students discuss about the solution of a function (which needs 5 lines of code to solve) and they then work on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences (variable names are different). In this case, the two students violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Note: We may use the Stanford Moss system to check your code for code similarity. https://theory.stanford.edu/~aiken/moss/
      Historical Data: In one year, we ended up finding 25% of the students in that class violating one of the above terms and we handled ALL of these violations according to the WPI Academic Honesty Policy. 
    '''
    #*******************************************
    # CHANGE HERE: if you have read and agree with the term above, change "False" to "True".
    Read_and_Agree = True
    #*******************************************
    return Read_and_Agree
#--------------------------

# ---------------------------------------------------------
'''
    Goal of Problem 1: Random and MiniMax AI players (50 points)
    In this problem, you will implement two different AI players for board games (random player and MiniMax). .
    
'''
# ---------------------------------------------------------

'''------------- Class: RandomPlayer (5.0 points) -------
     AI Player 1 (Random Player): Let's first implement the simplest player AI to get familiar with TicTacToe AI.  The random player chooses a random valid move at each step of the game.  This player is the simplest AI agent for the tic-tac-toe game.  It is also the foundation of Monte-Carlo Sampling which we will need to use later. Note that the AI player needs to be general for different types of board games. In the game.py file, we have 3 board games (TicTacToe, Othello, GO). The AI player should work with any of these three games. 
'''

class RandomPlayer(Player):
    #------------- Method: choose_a_move  ------
    ''' Goal: The action function, which chooses one random valid move in each step of the game.  This function will be called by the game at each game step.  For example, suppose we have 2 random players (say A and B) in a game.  The game will call the choose_a_move() function of the two players in turns as follows:
    Repeat until game ends:
      (1) r,c = A.choose_a_move(game,game_state, x=1 ) --- "X" player (A) choose a move
      (2) the game updates its game state 
      (3) r,c = B.choose_a_move(game,game_state, x=-1 ) --- "O" player (B) choose a move
      (4) the game updates its game state 
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, an object of a child class of the BoardGame class in game.py, such as TicTacToe, Othello or GO
    * s: the current state of the game, which is an object of the GameState class in game.py.  Here s.b represents the current setting of the board, an integer matrix of shape 3 by 3 (TicTacToe) or 8 by 8 (Othello).
    s.b[i,j] = 0 denotes that the i-th row and j-th column is empty;
    s.b[i,j] = 1 denotes that the i-th row and j-th column is taken by "X" player;
    s.b[i,j] = -1 denotes that the i-th row and j-th column is taken by "O" player.
    For example, in TicTacToe, the following game state 
    | X |   | O |
    | O | X |   |
    | X |   | O |
    is represented as the following numpy matrix
    s.b= [[ 1 , 0 ,-1 ],
          [-1 , 1 , 0 ],
          [ 1 , 0 ,-1 ]]
    s.x: who's turn in this step of the game, x=1 if "X" player's turn; x=-1 if "O" player's turn.

    ---- Outputs: --------
    * r: the row number of the next move, an integer scalar
    * c: the column number of the next move, an integer scalar
    ---- Example: --------
    For example, in the above example, the valid moves are the empty grid cells: 
        (r=0,c=1) --- the first row, second column 
        (r=1,c=2) --- the second row, the third column 
        (r=2,c=1) --- the third row , the second column
        The random player should randomly choose one of the valid moves.
 
    ---- Hints: --------
    * For any board game class in the game.py (such as TicTacToe, Othello or GO), you can always use get_valid_moves() method to get the list of valid moves in the game. 
    * Step 1: find all valid moves in the current game state. 
    * Step 2: randomly choose one valid move. 
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def choose_a_move(self, g, s):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        m = g.get_valid_moves(s)
        randInt = np.random.randint(0,len(m))
        x = m[randInt]
        r = x[0]
        c = x[1]
        ##############################
        return r, c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RandomPlayer_choose_a_move
        (Mac /Linux): python3 -m pytest -v test_1.py -m RandomPlayer_choose_a_move
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (random player) on TicTacToe game:
        (Windows OS): python demo1.py
        (Mac /Linux): python3 demo1.py
    You could play with the random player in TicTacToe game by clicking a block on the board. It should be very easy to win a game with random player
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (random player) on Othello game:
        (Windows OS): python demo2.py
        (Mac /Linux): python3 demo2.py
    You could play with the random player in Othello game by clicking a highlighted block on the board (a valid move). It should be very easy to win a game with random player
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (random player) on GO game (with a small board size):
        (Windows OS): python demo3.py
        (Mac /Linux): python3 demo3.py
    You could play with the random player in GO game by clicking an intersection on the board. It should be very easy to win a game with random player. Bonus: If you want to play on the full size of the board, you could change the parameter of the demo3.py file. Change the line "Board_SIZE = 5" to 19 
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: Node (0.0 points) -------
    AI Player 2 (MiniMax Player): Now let's implement the MiniMax agent for the game.
The goal of this agent is to find the optimal (best) move for the current game state.
MiniMax player will build a fully expanded search tree, where each tree node corresponds to a game state.
The root of the tree is the current game state.
Then we compute the score (value) of each node recursively using minimax algorithm.
Finally, the MiniMax agent will choose the child node with the largest value as the next move. 
For example, suppose the current game state is:
      s.b=[[ -1, 1, 1],
           [ -1,-1,-1],
           [  0,-1, 1]]
and it's "O" player's turn (s.x=-2).
Then the search tree will be: 
|-------------------
|Root Node:   
|  s.b=[[ -1, 1, 1],
|       [ -1,-1,-1],
|       [  0,-1, 1]]     -- the game state in the node
|  s.x=-2               -- it's "O" player's turn at this step of the game
|    p= None            -- The root node has no parent node
|    m= None            -- the move it takes from parent node to this node (no parent node) 
|    c=[Child_Node_A, Child_Node_B] -- list of children nodes
|    v=-2               -- The value of the game state:  
|                            assuming both players follows their optimal moves,
|                            from this game state,  "O" player will win (-2).
|----------------------------
  |Child Node A:  ---- If O player chooses the move (r=-1,c=0)
  |  s.b=[[-2, 1, 1],
  |       [-1,-1,-1],
  |       [ 0,-1, 1]] -- the game state in the node
  |  s.x= 0           -- it's "X" player's turn 
  |    p= Root_Node   -- The parent node is the root node
  |    m= (-1,0)       -- from parent node, took the move (r=0, c=0) to reach this node
  |    c=[Grand Child Node C] -- list of children nodes
  |    v= 0           -- The value of the game state:  
  |                            assuming both players follows their optimal moves,
  |                            from this game state,  "X" player will win (0).
  |----------------------------
      |Grand Child Node A0: ---- If X player chooses the move (r=1, c=0)
      |  s.b=[[-2, 1, 1],
      |       [ 0,-1,-1],
      |       [ 0,-1, 1]]    -- the game state in the node
      |  s.x=-2              -- it's "O" player's turn 
      |    p= Child_Node_B   -- The parent node is the child node B
      |    m= (0,0)          -- from parent node, took the move (r=1,c=0) to reach this node
      |    c=[] -- list of children nodes, no child node because the game has ended
      |    v= -1               -- The score of the game state:  
      |                          Terminal node, the game ends with a Tie (-1).
  |------------------------------ 
  |Child Node B:  ---- If O player chooses the move (r=0,c=0)
  |  s.b=[[-1, 1, 1],
  |       [-2,-1,-1],
  |       [ 0,-1, 1]]     -- the game state in the node
  |  s.x= 0               -- it's "X" player's turn in this step of the game
  |    p= Root_Node       -- The parent node is the root node
  |    m= (0,0)           -- from parent node, took the move (r=1,c=0) to reach this node
  |    c=[] -- list of children nodes, no child node because the game has ended
  |    v=-2               -- The value of the game state:  
  |                           Terminal node, the game ends: O player won (-2) 
  |--------------------------
    The tree looks like this:
                      |--> Child Node A (v=-1) |--> Grand Child Node A1 (v=0)
    Root Node(v=-2)-->| 
                      |--> Child Node B (v=-2) 
    In this example, the two children nodes have values as v=-1 (child A) and v=-1 (child B). 
    The "O" player will choose the child node with the smallest value as the next move.
    In this example, the smallest value is Child Node B (v=-2), so the optimal next move is (r=1, c=0)
------------------------------------------------------------
MiniMax is a search-tree-based  methods. 
Now let's implement tree nodes first.  Then we can connect the nodes into a search tree.
------------------------------------------------------------
 
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
    * v: a float scalar, the value of the current node.
    '''
class Node:
    #------------- Method: __init__  ------
    ''' Goal: Search Tree Node. This is a base/general class of search tree node, which can be used later by all search tree based methods, such as MiniMax, Monte-Carlo Tree Search.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * s: the current state of the game
    * p: the parent node of this node
    * m: the move that it takes from the parent node to reach this node
    * v: a float scalar, the value of the current node.
    '''
    def __init__(self, s, p=None, m=None, v=None):
        self.s = s # the current state of the game
        self.p = p # the parent node of the current node
        self.m = m # the move that it takes from the parent node to reach this node
        self.c = [] # a list of children nodes
        self.v = v # the value of the node (X player will win:1, tie: 0, lose: -1)
        
        
    #----------------------------------------------------------
    
'''------------- Class: MMNode (30.0 points) -------
    A Node of a MiniMax Search Tree. It is a child class of the general search tree node class: Node. But this MiniMax Node class supports additional operations of MiniMax Search algorithm on the tree node, such as "expand", "build_tree" etc. 
'''

class MMNode(Node):
    #------------- Method: expand  ------
    ''' Goal: In order to build a search tree, we first need to implement an elementary operation:  
Expand the current tree node (self) by adding one layer of children nodes.
Add one child node for each of the valid next moves from the current game state.
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello
    ---- Example: --------
    In TicTacToe, if the current node (BEFORE expanding) is like:
|-------------------
|Current Node:   
|  s.b=[[ 0, 1,-1],
|       [ 0,-1, 1],
|       [ 0, 1,-1]]     -- the game state in the node
|  s.x= 1               -- it's "X" player's turn in this step of the game
|    p= None           
|    m= None            
|    c=[] -- no children node
|    v= None               
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
|    v= None               
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
        |    v= None               
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
        |    v= None               
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
        |    v= None               
 
    ---- Hints: --------
    * Step 1: get the list of valid next move-state pairs from the current game state. Here you could call a function "get_move_state_pairs()" in the BoardGame class (in game.py) to get a list of the move-state pairs for a game state. 
    * Step 2: expand the node with one level of children nodes. 
    *      2.1: for each next move m and game state s, create a new child node. 
    *      2.2: append the new child node into the list children nodes on the current node. 
    * In the Othello game, given a parent node p and its child node c,  p.x and c.x NOT necessarily have opposite sign.  When there is no valid move for one player, that player will give up the move, so in this case the p.x and c.x can be the same. 
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def expand(self, g):
        ##############################
        ## INSERT YOUR CODE HERE (6.0 points)
        node = g.get_move_state_pairs(self.s)
        for move, next in node:
            child = MMNode(next, self, move)
            self.c.append(child)
        pass 
        ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m MMNode_expand
        (Mac /Linux): python3 -m pytest -v test_1.py -m MMNode_expand
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: build_tree  ------
    ''' Goal: Given a tree node (the current state of the game), build a fully-grown search tree, which includes all the possible future game states in the tree.  
Note, in this function, we don't need to compute the values of the nodes, just leave them as None. 
We will compute them later in compute_v(). 
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, an object of a child class of the BoardGame class in game.py, such as TicTacToe, Othello or GO
    ---- Example: --------
    For example, in TicTacToe, the current node is (BEFORE building tree)
|-------------------
|Current Node:   
|  s.b=[[ 0, 1,-1],
|       [ 0,-1, 1],
|       [ 0, 1,-1]]     -- the game state in the node
|  s.x= 1               -- it's "X" player's turn in this step of the game
|    p= None           
|    m= None            
|    c=[] -- list of children nodes
|    v= None               
|-------------------
AFTER expanding this node, we have a tree as follows:
The tree looks like this after being expanded:
                                         |--> Grand Child Node A1 |--> Great Grand Child A11
                    |--> Child Node A -->| 
                    |                    |--> Grand Child Node A2
                    |
                    |                    |--> Grand Child Node B1 
   Current Node --> |--> Child Node B -->| 
                    |                    |--> Grand Child Node B2 
                    |
                    |                    |--> Grand Child Node C1 
                    |--> Child Node C -->| 
                                         |--> Grand Child Node C2 |--> Great Grand Child C21
Each node of the tree represents a possible future game state.
Here are the detailed attribute values of tree nodes
--------------------
|Current Node   
|  s.b=[[ 0, 1,-1],
|       [ 0,-1, 1],
|       [ 0, 1,-1]]     
|  s.x= 1        -- it's "X" player's turn in this step of the game  
|    p= None           
|    m= None            
|    c=[Child_A, Child_B, Child_C] -- Three children nodes are created and added here
|    v= None               
|-------------------------------
    |Child Node A:   
    |  s.b=[[ 1, 1,-1],
    |       [ 0,-1, 1],
    |       [ 0, 1,-1]]     
    |  s.x=-1               -- it's "O" player's turn in this step of the game 
    |    p= Current_Node    -- The parent node of this node is "Current_Node" 
    |    m= (0,0)           -- The move it takes to from parent node 
    |                           to this node is first row (0), first column (0) 
    |    c=[Grand_Child_A, Grand_Child_B] -- Two children nodes 
    |    v= None               
    |-------------------------------
            |Grand Child Node A1:   
            |  s.b=[[ 1, 1,-1],
            |       [-1,-1, 1],
            |       [ 0, 1,-1]]     
            |  s.x= 1            -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_A -- The parent node of this node is "Child Node A" 
            |    m= (1,0)        -- The move it takes from parent node 
            |                         to this node: second row (1),first column (0) 
            |    c=[Great_Grand_Child_A11] -- one child node
            |    v= None       
            |--------------------------------
                    |Great Grand Child Node A11:   
                    |  s.b=[[ 1, 1,-1],
                    |       [-1,-1, 1],
                    |       [ 1, 1,-1]]     
                    |  s.x=-1             -- it's "O" player's turn in this step of the game 
                    |    p= Grand_Child_Node_A1  -- The parent node of this node 
                    |    m= (2,0)         -- The move from parent node 
                    |                        to this node is third row (2),first column (0) 
                    |    c=[] -- Terminal node (no child) 
                    |    v= None       
            -------------------------
            |Grand Child Node A2:   
            |  s.b=[[ 1, 1,-1],
            |       [ 0,-1, 1],
            |       [-1, 1,-1]]     
            |  s.x= 1            -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_A -- The parent node of this node is "Child Node A" 
            |    m= (2,0)        -- The move it takes from parent node 
            |                        to this node: third row (2),first column (0) 
            |    c=[] -- terminal node (game ends), no child node 
            |    v= None    
    |-----------------------
    |Child Node B:   
    |  s.b=[[ 0, 1,-1],
    |       [ 1,-1, 1],
    |       [ 0, 1,-1]]     
    |  s.x=-1            -- it's "O" player's turn in this step of the game 
    |    p= Current_Node -- The parent node of this node is "Current_Node" 
    |    m= (1,0)        -- The move it takes from parent node to this node
    |    c=[] -- this node has not been expanded yet 
    |    v= None               
    |--------------------------------
            |Grand Child Node B1:   
            |  s.b=[[-1, 1,-1],
            |       [ 1,-1, 1],
            |       [ 0, 1,-1]]     
            |  s.x= 1             -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_B  -- The parent node of this node 
            |    m= (0,0)         -- The move it takes from parent node to this node
            |    c=[]             -- Terminal node (no child)
            |    v= None       
            -------------------------
            |Grand Child Node B2:   
            |  s.b=[[ 0, 1,-1],
            |       [ 1,-1, 1],
            |       [-1, 1,-1]]     
            |  s.x= 1             -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_B  -- The parent node of this node 
            |    m= (2,0)         -- The move it takes from parent node to this node
            |    c=[] -- Terminal node (no child) 
            |    v= None    
    |--------------------------------
    |Child Node C:   
    |  s.b=[[ 0, 1,-1],
    |       [ 0,-1, 1],
    |       [ 1, 1,-1]]     
    |  s.x=-1               -- it's "O" player's turn in this step of the game 
    |    p= Current_Node    -- The parent node of this node is "Current_Node" 
    |    m= (2,0)           -- The move it takes to from parent node to this node
    |    c=[] -- this node has not been expanded yet 
    |    v= None               
    |-------------------------------
            |Grand Child Node C1:   
            |  s.b=[[-1, 1,-1],
            |       [ 0,-1, 1],
            |       [ 1, 1,-1]]     
            |  s.x= 1               -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_A    -- The parent node of this node is "Child Node A" 
            |    m= (0,0)           -- The move it takes to from parent node to this node 
            |    c=[] -- game ends, no child 
            |    v= None       
            -------------------------
            |Grand Child Node C2:   
            |  s.b=[[ 0, 1,-1],
            |       [-1,-1, 1],
            |       [ 1, 1,-1]]     
            |  s.x= 1             -- it's "X" player's turn in this step of the game 
            |    p= Child_Node_A  -- The parent node of this node is "Child Node A" 
            |    m= (1,0)         -- The move it takes from parent node to this node
            |    c=[Great_Grand_Child_C21] -- one child node 
            |    v= None  
            |--------------------------------
                    |Great Grand Child Node C21:   
                    |  s.b=[[ 1, 1,-1],
                    |       [-1,-1, 1],
                    |       [ 1, 1,-1]]     
                    |  s.x=-1            -- it's "O" player's turn in this step of the game 
                    |    p= Grand_Child_Node_C2  -- The parent node of this node 
                    |    m= (0,0)        -- The move  from parent node to this node 
                    |    c=[] -- Terminal node (no child) 
                    |    v= None     
                    |------------------------ 
 
    ---- Hints: --------
    * You could use recursion to build the tree recursively. 
    * Step 1: if the game in the current state has already ended, exit the function. 
    * Step 2: expand the current node by one-level of children nodes. 
    * Step 3: recursion: for each child node, call build_tree() function to build a subtree rooted from each child node. 
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def build_tree(self, g):
        ##############################
        ## INSERT YOUR CODE HERE (9.0 points)
        if g.check_game(self.s) == None:
            MMNode.expand(self, g)
            for child in self.c:
                MMNode.build_tree(child, g)
        else:
            pass
        pass
        ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m MMNode_build_tree
        (Mac /Linux): python3 -m pytest -v test_1.py -m MMNode_build_tree
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: compute_v  ------
    ''' Goal: Given a fully-built tree, compute optimal values of the all the nodes in the tree using minimax algorithm. Here we assume that the whole search-tree is fully grown, but no value on any node has been computed yet before calling this function.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * g: the game environment being played, such as TicTacToe or Othello
    ---- Example: --------
    MinMax Algorithm: 
The optimal value of a tree node is defined as follows:
(1) if the node is a terminal node, the value of the node is the game result (1, -1 or 0)
(2) if the node has children nodes, which means that it is not a terminal node, and the game has not ended yet 
        (2.1) if it is X player's turn in the current node:
                the value of the node is maximum value of all the children nodes' values.
        (2.2) if it is O player's turn in the current node:
                the value of the node is minimum value of all the children nodes' values.
For example, the current game state is
|-------------------
|Current Node:   
|  s.b=[[ 1,-1, 1],
|       [ 0, 0, 0],
|       [ 0, 0,-1]]     -- the game state in the node
|  s.x= 1               -- it's "X" player's turn in this step of the game
|    p= None           
|    m= None            
|    c=[] -- list of children nodes
|    v= None               
|-------------------
The search tree will have 5 levels of children nodes.
The first two levels of the tree looks like this:
                    |--> Child Node A -->|--> Grand Child Node A1 
                    |     1,-1, 1        |--> Grand Child Node A2 
                    |     1, 0, 0        |--> Grand Child Node A3
                    |     0, 0,-1        |--> Grand Child Node A4 
                    |
                    |--> Child Node B -->|--> Grand Child Node B1 
                    |     1,-1, 1        |--> Grand Child Node B2 
                    |     0, 1, 0        |--> Grand Child Node B3 
                    |     0, 0,-1        |--> Grand Child Node B4 
                    |
  Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 
   1,-1, 1          |     1,-1, 1        |--> Grand Child Node C2 
   0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 
   0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 
                    |
                    |--> Child Node D -->|--> Grand Child Node D1 
                    |     1,-1, 1        |--> Grand Child Node D2 
                    |     0, 0, 0        |--> Grand Child Node D3  
                    |     1, 0,-1        |--> Grand Child Node D4 
                    |
                    |--> Child Node E -->|--> Grand Child Node E1 
                          1,-1, 1        |--> Grand Child Node E2 
                          0, 0, 0        |--> Grand Child Node E3  
                          0, 1,-1        |--> Grand Child Node E4 
If we finish computing the values of all the Grand Children nodes, we have: 
                         (O's turn)             
                    |--> Child Node A -->|--> Grand Child Node A1 (v=1) 
                    |     1,-1, 1        |--> Grand Child Node A2 (v=1) 
                    |     1, 0, 0        |--> Grand Child Node A3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node A4 (v=1) 
                    |
                    |--> Child Node B -->|--> Grand Child Node B1 (v=1) 
                    |     1,-1, 1        |--> Grand Child Node B2 (v=1) 
                    |     0, 1, 0        |--> Grand Child Node B3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node B4 (v=1) 
   (X's turn)       |
  Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0) 
   1,-1, 1          |     1,-1, 1        |--> Grand Child Node C2 (v=0) 
   0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0) 
   0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1) 
                    |
                    |--> Child Node D -->|--> Grand Child Node D1 (v=1) 
                    |     1,-1, 1        |--> Grand Child Node D2 (v=1) 
                    |     0, 0, 0        |--> Grand Child Node D3 (v=1)  
                    |     1, 0,-1        |--> Grand Child Node D4 (v=1) 
                    |
                    |--> Child Node E -->|--> Grand Child Node E1 (v=0) 
                          1,-1, 1        |--> Grand Child Node E2 (v=0) 
                          0, 0, 0        |--> Grand Child Node E3 (v=1)  
                          0, 1,-1        |--> Grand Child Node E4 (v=0) 
In Child Node A, it is "O" player's turn, so the value of Child Node A is the MINIMUM of all its children nodes' values: min(1,1,0,1) = 0
Similarly, we can compute all the children nodes' (A,B,C,D).
                         (O's turn)             
                    |--> Child Node A -->|--> Grand Child Node A1 (v=1) 
                    |     1,-1, 1 (v=0)  |--> Grand Child Node A2 (v=1) 
                    |     1, 0, 0        |--> Grand Child Node A3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node A4 (v=1) 
                    |
                    |--> Child Node B -->|--> Grand Child Node B1 (v=1) 
                    |     1,-1, 1 (v=0)  |--> Grand Child Node B2 (v=1) 
                    |     0, 1, 0        |--> Grand Child Node B3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node B4 (v=1) 
   (X's turn)       |
  Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0) 
   1,-1, 1          |     1,-1, 1 (v=-1) |--> Grand Child Node C2 (v=0) 
   0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0) 
   0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1) 
                    |
                    |--> Child Node D -->|--> Grand Child Node D1 (v=1) 
                    |     1,-1, 1 (v=1)  |--> Grand Child Node D2 (v=1) 
                    |     0, 0, 0        |--> Grand Child Node D3 (v=1)  
                    |     1, 0,-1        |--> Grand Child Node D4 (v=1) 
                    |
                    |--> Child Node E -->|--> Grand Child Node E1 (v=0) 
                          1,-1, 1 (v=1)  |--> Grand Child Node E2 (v=0) 
                          0, 0, 0        |--> Grand Child Node E3 (v=1)  
                          0, 1,-1        |--> Grand Child Node E4 (v=0) 
Now the values of all the children nodes of the current node are ready, we can compute the value of the current node.
In the current node, it is "X" player's turn, so the value of the current node is the MAXIMUM of all its children nodes' values: max(0,0,-1,1,0) = 1
                         (O's turn)             
                    |--> Child Node A -->|--> Grand Child Node A1 (v=1) 
                    |     1,-1, 1 (v=0)  |--> Grand Child Node A2 (v=1) 
                    |     1, 0, 0        |--> Grand Child Node A3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node A4 (v=1) 
                    |
                    |--> Child Node B -->|--> Grand Child Node B1 (v=1) 
                    |     1,-1, 1 (v=0)  |--> Grand Child Node B2 (v=1) 
                    |     0, 1, 0        |--> Grand Child Node B3 (v=0) 
                    |     0, 0,-1        |--> Grand Child Node B4 (v=1) 
   (X's turn)       |
  Current Node -->  |--> Child Node C -->|--> Grand Child Node C1 (v=0) 
   1,-1, 1 (v=1)    |     1,-1, 1 (v=-1) |--> Grand Child Node C2 (v=0) 
   0, 0, 0          |     0, 0, 1        |--> Grand Child Node C3 (v=0) 
   0, 0,-1          |     0, 0,-1        |--> Grand Child Node C4 (v=-1) 
                    |
                    |--> Child Node D -->|--> Grand Child Node D1 (v=1) 
                    |     1,-1, 1 (v=1)  |--> Grand Child Node D2 (v=1) 
                    |     0, 0, 0        |--> Grand Child Node D3 (v=1)  
                    |     1, 0,-1        |--> Grand Child Node D4 (v=1) 
                    |
                    |--> Child Node E -->|--> Grand Child Node E1 (v=0) 
                          1,-1, 1 (v=0)  |--> Grand Child Node E2 (v=0) 
                          0, 0, 0        |--> Grand Child Node E3 (v=1)  
                          0, 1,-1        |--> Grand Child Node E4 (v=0) 
 
    ---- Hints: --------
    * You could use recursion to compute the values of the current node recursively. 
    * Step 1: if the game has already ended, the value of the node is the game result. 
    * Step 2: if the game has not ended yet:. 
    *  Step (2.1) first compute values of all children nodes recursively by calling compute_v() in each child node. 
    *   Step (2.2) now the values of all the children nodes are computed, let's compute the value of the current node. 
    *     Step (2.2.1) if it is X player's turn, the value of the current node is the max of all children node's values. 
    *     Step (2.2.2) if it is O player's turn, the value of the current node is the min of all children node's values. 
    * This problem can be solved using only 9 line(s) of code. More lines are okay.'''
    def compute_v(self, g):
        ##############################
        ## INSERT YOUR CODE HERE (15.0 points)
        if g.check_game(self.s) == None:
            for child in self.c:
                MMNode.compute_v(child, g)
            if self.s.x == 1:
                self.v = max(child.v for child in self.c)
            if self.s.x == -1:
                self.v = min(child.v for child in self.c)
        else:
            self.v = g.check_game(self.s)
            pass
        pass 
        ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m MMNode_compute_v
        (Mac /Linux): python3 -m pytest -v test_1.py -m MMNode_compute_v
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: MiniMaxPlayer (15.0 points) -------
    AI Player 2 (MinMax Player): Now let's implement the MinMax agent for the game.
Minimax player is an AI player who chooses optimal moves by searching the tree with min-max.
The goal of this agent is to find the optimal (best) move for the current game state.
(1) Build Tree: we will first build a fully-grown search tree, where the root of the tree is the current game state.
(2) Compute Node Values: Then we compute the value of each node recursively using MinMax algorithm.
(3) Choose Optimal Next Move: the agent will choose the child node with the largest/smallest value as the next move.
        if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes. 
        if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes. 
 
'''

class MiniMaxPlayer(Player):
    #------------- Method: choose_optimal_move  ------
    ''' Goal: (Choose Optimal Next Move) Assume we have a fully-grown search tree, and the values of all nodes are already computed.
Step (3): Choose Next Move: the agent will choose the child node of current node with the largest/smallest value as the next move.
    if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes. 
    if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes. 
    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * n: the current node of the search tree, assuming the values in all nodes are already computed.
    ---- Outputs: --------
    * r: the row number of the optimal next move, an integer scalar with value 0, 1, or 2.
    * c: the column number of the optimal next move, an integer scalar with value 0, 1, or 2.
    ---- Example: --------
    Suppose we have the following search tree (X player's turn):
                        |--> Child Node A 
                        |    |1,-1, 1|(v=0)  
                        |    |1, 0, 0|(m=(1,0))       
                        |    |0, 0,-1|       
                        |
                        |--> Child Node B 
                        |    |1,-1, 1|(v=0)  
                        |    |0, 1, 0|(m=(1,1))       
                        |    |0, 0,-1|       
       (X's turn)       |
      Current Node -->  |--> Child Node C 
      |1,-1, 1|(v=1)    |    |1,-1, 1|(v=-1) 
      |0, 0, 0|         |    |0, 0, 1|(m=(1,2))       
      |0, 0,-1|         |    |0, 0,-1|        
                        |
                        |--> Child Node D 
                        |    |1,-1, 1|(v=1)  
                        |    |0, 0, 0|(m=(2,0))         
                        |    |1, 0,-1|       
                        |
                        |--> Child Node E 
                             |1,-1, 1|(v=0)  
                             |0, 0, 0|(m=(2,1))         
                             |0, 1,-1|       
The optimal next move will be child node with the largest value (Child Node D). 
So in this example, the next move should be (r=2, c=0)
 
    ---- Hints: --------
    * You could use the argmax() function in numpy package to find the index of the max value in a numpy array.. 
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def choose_optimal_move(self, n):
        ##############################
        ## INSERT YOUR CODE HERE (7.5 points)
        if n.s.x == 1:
            for child in n.c:
                if child.v == max(child.v for child in n.c):
                    r, c = child.m[0], child.m[1]
        else:
            for child in n.c:
                if child.v == min(child.v for child in n.c):
                    r, c = child.m[0], child.m[1]
        ##############################
        return r, c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m MiniMaxPlayer_choose_optimal_move
        (Mac /Linux): python3 -m pytest -v test_1.py -m MiniMaxPlayer_choose_optimal_move
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: choose_a_move  ------
    ''' Goal: The action function of the minimax player, which chooses next move in the game.  
The goal of this agent is to find the optimal (best) move for the current game state.
(1) Build Tree: we will first build a fully-grown search tree, where the root of the tree is the current game state.
(2) Compute Node Values: Then we compute the value of each node recursively using MinMax algorithm.
(3) Choose Next Move: the agent will choose the child node with the largest/smallest value as the next move.
        if the MinMax player is the "X" player in the game, it will choose the largest value among children nodes. 
        if the MinMax player is the "O" player in the game, it will choose the smallest value among children nodes. 
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
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def choose_a_move(self, g, s):
        ##############################
        ## INSERT YOUR CODE HERE (7.5 points)
        # MMNode.build_tree(s, g)
        # MMNode.compute_v(s, g)
        for move, node in g.get_move_state_pairs(s):
            r, c = self.choose_optimal_move(node)
        ##############################
        return r, c
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m MiniMaxPlayer_choose_a_move
        (Mac /Linux): python3 -m pytest -v test_1.py -m MiniMaxPlayer_choose_a_move
    ---------------------------------------------------------------'''

    ''' ---------- Demo -----------------
    Please type the following command in your terminal to play with the AI (MiniMax) on TicTacToe game:
        (Windows OS): python demo1.py minimax
        (Mac /Linux): python3 demo1.py minimax
    You could play with the MiniMax player in TicTacToe game by clicking a block on the board. It should be impossible to win a game with this AI player
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    

'''-------- TEST problem1.py file: (50 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_1.py
        (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''






