from problem1 import *
import sys
import pytest 

import numpy as np
from game import GameState, TicTacToe,Othello, GO_state, GO
import copy
'''
    Unit test 1  (Total Points: 50)
    This file includes unit tests for problem1.py.
'''

def test_python_version():
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

# ============= Class: RandomPlayer ===========================
# Total Points: 5.0
# ***********  Method: choose_a_move  (Class: RandomPlayer) **************** 
# Total Points: 5.0

# ---- Test Case: tictactoe (Method: choose_a_move, Class: RandomPlayer) 
# Goal: Test if the AI works with TicTacToe game class
# Points: 1.0
@pytest.mark.RandomPlayer_choose_a_move
def test_RandomPlayer_choose_a_move_tictactoe():
    g = TicTacToe()  # game 
    p = RandomPlayer()
    b=np.array([[ 0, 1, 1],
                [ 1, 0,-1],
                [ 1, 1, 0]])
    b_=np.array([[ 0, 1, 1],
                 [ 1, 0,-1],
                 [ 1, 1, 0]])
    s= GameState(b,x=1)
    count=np.zeros(3)
    for _ in range(100):
        r,c = p.choose_a_move(g,s)
        assert b_[r,c]==0 # player needs to choose a valid move 
        assert np.allclose(s.b,b_) # the player should never change the game state object
        assert r==c # in this example the valid moves are on the diagonal of the matrix
        assert r>-1 and r<3
        count[c]+=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    b=np.array([[ 1, 1, 0],
                [ 1, 0,-1],
                [ 0, 1, 1]])
    s= GameState(b,x=1)
    for _ in range(100):
        r,c = p.choose_a_move(g,s)
        assert b[r,c]==0 
        assert r==2-c 
        assert r>-1 and r<3
# --------------------------------

# ---- Test Case: othello (Method: choose_a_move, Class: RandomPlayer) 
# Goal: The AI agent should also be compatible with the game Othello
# Points: 1.5
@pytest.mark.RandomPlayer_choose_a_move
def test_RandomPlayer_choose_a_move_othello():
    g = Othello()  # game 
    b=np.array([[ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0,-1,-1,-1, 0, 0],
                [ 0, 0, 0, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_ = b.copy()
    p = RandomPlayer()
    s= GameState(b,x=1)
    count = np.zeros(5)
    for _ in range(200):
        r,c = p.choose_a_move(g,s)
        assert np.allclose(b,b_) # the player should never change the game state object
        assert b[r,c]==0 # player needs to choose a valid move 
        assert r==2 
        assert c>1 and c<7
        count[c-2]+=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    assert count[3]>20
    assert count[4]>20
# --------------------------------

# ---- Test Case: othello_run_game (Method: choose_a_move, Class: RandomPlayer) 
# Goal: test whether we can run a game using random player
# Points: 1.5
@pytest.mark.RandomPlayer_choose_a_move
def test_RandomPlayer_choose_a_move_othello_run_game():
    g = Othello()  # game 
    p = RandomPlayer()
    b=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s= GameState(b,x=1)
    for i in range(10):
        e = g.run_a_game(p,p,s=s)
        assert e==-1
    b=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s= GameState(b,x=1)
    w=0
    for i in range(10):
        e = g.run_a_game(p,p,s=s)
        w+=e
    assert np.abs(w)<9
    b=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s= GameState(b,x=1)
    for i in range(10):
        e = g.run_a_game(p,p,s=s)
        assert e==-1
    b=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    w=0
    s= GameState(b,x=1)
    for i in range(10):
        e = g.run_a_game(p,p,s=s)
        w+=e
    assert np.abs(w)<9
# --------------------------------

# ---- Test Case: GO (Method: choose_a_move, Class: RandomPlayer) 
# Goal: The AI agent should also be compatible with the game GO
# Points: 1.0
@pytest.mark.RandomPlayer_choose_a_move
def test_RandomPlayer_choose_a_move_GO():
    g = GO(board_size=2)  # game (2 x 2 board)
    s = g.initial_game_state()
    p = RandomPlayer()
    b_= s.b.copy()
    count = np.zeros(5)
    for _ in range(200):
        r,c = p.choose_a_move(g,s)
        assert np.allclose(s.b,b_) # the player should never change the game state object
        assert s.a==0 
        if r is None and c is None: # the player choose to pass without placing any stone in the step
            count[-1]+=1
        else:
            count[2*r+c] +=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    assert count[3]>20
    assert count[4]>20 
# --------------------------------

# ============= Class: Node ===========================
# Total Points: 0.0
# ============= Class: MMNode ===========================
# Total Points: 30.0
# ***********  Method: expand  (Class: MMNode) **************** 
# Total Points: 6.0

# ---- Test Case: tictactoe (Method: expand, Class: MMNode) 
# Goal: Test if the code works with TicTacToe game
# Points: 1.2
@pytest.mark.MMNode_expand
def test_MMNode_expand_tictactoe():
    g = TicTacToe()  # game 
    # Current Node (root)
    b=np.array([[0, 1,-1],
                [0,-1, 1],
                [0, 1,-1]])
    s = GameState(b,x=1) #it's X player's turn
    n = MMNode(s) 
    # expand
    n.expand(g)
    assert len(n.c) ==3 
    assert n.s.x==1
    b_=np.array([[0, 1,-1],
                 [0,-1, 1],
                 [0, 1,-1]])
    # the current game state should not change after expanding
    assert np.allclose(n.s.b,b_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.s.x==-1
        assert c.p==n
        assert c.c==[] #only add one level of children nodes, not two levels.
        assert c.v==None
    # child node A
    b=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
    assert c
    # child node B
    b=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(1,0)
    assert c
    # child node C
    b=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(2,0)
    assert c
# --------------------------------

# ---- Test Case: tictactoe2 (Method: expand, Class: MMNode) 
# Goal: Test the code when the current turn is O player in the game
# Points: 1.2
@pytest.mark.MMNode_expand
def test_MMNode_expand_tictactoe2():
    g = TicTacToe()  # game 
    # Current Node (root)
    b=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    s=GameState(b,x=-1) #it's O player's turn
    n = MMNode(s) 
    n.expand(g)
    assert n.s.x==-1
    assert len(n.c) ==2
    for c in n.c:
        assert c.s.x==1
        assert c.p==n
        assert c.c==[]
    # child node A
    b=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(1,0)
    assert c
    # child node B
    b=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(2,0)
    assert c
# --------------------------------

# ---- Test Case: tictactoe3 (Method: expand, Class: MMNode) 
# Goal: Test the code when the current turn is X player in the game
# Points: 1.2
@pytest.mark.MMNode_expand
def test_MMNode_expand_tictactoe3():
    g = TicTacToe()  # game 
    s=GameState(np.zeros((3,3)),x=1) #it's X player's turn
    n = MMNode(s)
    n.expand(g)
    assert n.s.x==1
    assert len(n.c) ==9
    for c in n.c:
        assert c.s.x==-1
        assert c.p==n
        assert c.c==[]
        assert np.sum(c.s.b)==1
        assert c.v==None
# --------------------------------

# ---- Test Case: othello (Method: expand, Class: MMNode) 
# Goal: The AI agent should also be compatible with Othello game
# Points: 1.2
@pytest.mark.MMNode_expand
def test_MMNode_expand_othello():
    g = Othello()  # game 
    b=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_=b.copy()
    s=GameState(b,x=1) #it's X player's turn
    n = MMNode(s) 
    # expand
    n.expand(g)
    assert len(n.c) ==2 
    assert n.s.x==1
    # the current game state should not change after expanding
    assert np.allclose(n.s.b,b_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.p==n
        assert c.c==[]
        assert c.v==None
    # child node A
    b=np.array([[ 1, 1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
            assert x.s.x==1 # it is still X player's turn because there is no valid move for O player
    assert c
    # child node B
    b=np.array([[ 0,-1, 1, 1, 1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,4)
            assert x.s.x==-1 
    assert c
# --------------------------------

# ---- Test Case: GO (Method: expand, Class: MMNode) 
# Goal: The AI agent should also be compatible with the GO game
# Points: 1.2
@pytest.mark.MMNode_expand
def test_MMNode_expand_GO():
    g = GO(board_size=2)  # game (2 x 2 board)
    b=np.array([[ 0, 1],
                [ 1, 0]])
    b_=b.copy()
    s=GO_state(b,x=-1) #it's O player's turn
    n = MMNode(s) 
    # expand
    n.expand(g)
    assert len(n.c) ==1 # only one valid move for O player: 'pass'
    assert n.s.x==-1
    # the current game state should not change after expanding
    assert np.allclose(n.s.b,b_) 
    c = n.c[0]
    assert type(c)==MMNode
    assert c.p==n
    assert c.c==[]
    assert c.v==None
    assert np.allclose(c.s.b,b_)
    assert c.m[0] is None
    assert c.m[1] is None
    s=GO_state(b,x=1) #it is X player's turn
    n = MMNode(s) 
    # expand
    n.expand(g)
    assert len(n.c) ==3  
# --------------------------------


# ***********  Method: build_tree  (Class: MMNode) **************** 
# Total Points: 9.0

# ---- Test Case: tictactoe (Method: build_tree, Class: MMNode) 
# Goal: Test if the code works on tictactoe
# Points: 1.8
@pytest.mark.MMNode_build_tree
def test_MMNode_build_tree_tictactoe():
    g = TicTacToe()  # game 
    # current node (root node)
    b=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    # the current game state should not change after building the tree 
    assert np.allclose(b,b_)
    assert len(n.c) ==3 
    assert n.s.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    assert np.allclose(n.s.b,b_) 
    for c in n.c:
        assert type(c)==MMNode
        assert c.s.x==-1
        assert c.p==n
        assert len(c.c)==2
        assert c.v==None
    #-----------------------
    # child node A
    b=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
            ca=x
    assert c
    # child node B
    b=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(1,0)
            cb=x
    assert c
    # child node C
    b=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(2,0)
            cc=x
    assert c
    #-----------------------
    # Child Node A's children
    for c in ca.c:
        assert c.s.x==1
        assert c.p==ca
        assert c.v==None
    # grand child node A1
    b=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            #-----------------------
            # Great Grand Child Node A11
            assert x.c[0].s.x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c
    # grand child node A2
    b=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(2,0)
            assert x.c== []
    assert c
    #-----------------------
    # Child Node B's children
    for c in cb.c:
        assert c.s.x==1
        assert c.p==cb
        assert c.c==[]
        assert c.v==None
    # grand child node B1
    b=np.array([[-1, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
    assert c
    # grand child node B2
    b=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(2,0)
    assert c
    #-----------------------
    # Child Node C's children
    for c in cc.c:
        assert c.s.x==1
        assert c.p==cc
        assert c.v==None
    # grand child node C1
    b=np.array([[-1, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
            assert x.c== []
    assert c
    # grand child node C2
    b=np.array([[ 0, 1,-1],
                [-1,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            # Great Grand Child Node C21
            assert x.c[0].s.x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c
# --------------------------------

# ---- Test Case: tictactoe2 (Method: build_tree, Class: MMNode) 
# Goal: Test if the code works on tictactoe when the current turn is for O player
# Points: 1.8
@pytest.mark.MMNode_build_tree
def test_MMNode_build_tree_tictactoe2():
    g = TicTacToe()  # game 
    b=np.array([[ 0, 0, 1],
                [ 0, 1, 1],
                [-1, 0,-1]])
    s = GameState(b,x=-1) #it's O player's turn
    n = MMNode(s) 
    n.build_tree(g)
    assert len(n.c) ==4 
    assert n.s.x==-1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    b1=np.array([[-1, 0, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    b2=np.array([[ 0,-1, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    b3=np.array([[ 0, 0, 1],
                 [-1, 1, 1],
                 [-1, 0,-1]])
    b4=np.array([[ 0, 0, 1],
                 [ 0, 1, 1],
                 [-1,-1,-1]])
    for c in n.c:
        assert c.s.x== 1
        assert c.v==None
        assert c.p==n
        if np.allclose(c.s.b,b1):
            assert c.m == (0,0)
            assert len(c.c) ==3
        if np.allclose(c.s.b,b2):
            assert c.m == (0,1)
            assert len(c.c) ==3
        if np.allclose(c.s.b,b3):
            assert c.m == (1,0)
            assert len(c.c) ==3
        if np.allclose(c.s.b,b4):
            assert c.m == (2,1)
            assert c.c == [] #terminal node, no child
# --------------------------------

# ---- Test Case: othello (Method: build_tree, Class: MMNode) 
# Goal: Test if the code works on Othello
# Points: 1.8
@pytest.mark.MMNode_build_tree
def test_MMNode_build_tree_othello():
    g = Othello()  # game 
    b=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    # the current game state should not change after building the tree 
    assert np.allclose(n.s.b,b_)
    assert len(n.c) ==2 
    assert n.s.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    for c in n.c:
        assert type(c)==MMNode
        assert c.s.x==-1
        assert c.p==n
        assert c.v==None
        assert len(c.c)==1
    #-----------------------
    # child node A
    b=np.array([[ 0, 0,-1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,5)
            ca=x
    assert c
    #-----------------------
    # child node B
    b=np.array([[ 0, 1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,1)
            cb=x
    assert c
    #-----------------------
    # Child Node A's children
    # grand child node A1
    assert ca.c[0].p==ca
    assert ca.c[0].v==None
    assert ca.c[0].m==(0,6)
    assert ca.c[0].c==[]
    b=np.array([[ 0, 0,-1,-1,-1,-1,-1, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(ca.c[0].s.b,b)
    #-----------------------
    # Child Node B's children
    # grand child node B1
    assert cb.c[0].p==cb
    assert cb.c[0].v==None
    assert cb.c[0].m==(0,0)
    assert cb.c[0].c==[]
    b=np.array([[-1,-1,-1,-1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(cb.c[0].s.b,b)
# --------------------------------

# ---- Test Case: othello2 (Method: build_tree, Class: MMNode) 
# Goal: Test if the code works on Othello
# Points: 1.8
@pytest.mark.MMNode_build_tree
def test_MMNode_build_tree_othello2():
    g = Othello()  # game 
    b=np.array([[ 0,-1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    # the current game state should not change after building the tree 
    assert np.allclose(n.s.b,b_)
    assert len(n.c) ==2 
    assert n.s.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    for c in n.c:
        assert type(c)==MMNode
        assert c.p==n
        assert c.v==None
        assert len(c.c)==1
    #-----------------------
    # child node A
    b=np.array([[ 1, 1, 1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,0)
            assert x.s.x==1 # there is no valid move for O player, so O player needs to give up the chance
            ca=x
    assert c
    #-----------------------
    # child node B
    b=np.array([[ 0,-1, 1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    c = False
    for x in n.c:
        if np.allclose(x.s.b,b):
            c=True
            assert x.m==(0,5)
            assert x.s.x==-1
            cb=x
    assert c
    #-----------------------
    # Child Node A's children
    # grand child node A1
    assert ca.c[0].p==ca
    assert ca.c[0].v==None
    assert ca.c[0].m==(0,5)
    assert ca.c[0].c==[]
    b=np.array([[ 1, 1, 1, 1, 1, 1, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(ca.c[0].s.b,b)
    #-----------------------
    # Child Node B's children
    # grand child node B1
    assert cb.c[0].p==cb
    assert cb.c[0].v==None
    assert cb.c[0].m==(0,6)
    assert cb.c[0].c==[]
    b=np.array([[ 0,-1,-1,-1,-1,-1,-1, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    assert np.allclose(cb.c[0].s.b,b)
# --------------------------------

# ---- Test Case: GO (Method: build_tree, Class: MMNode) 
# Goal: Test if the code works on GO game
# Points: 1.8
@pytest.mark.MMNode_build_tree
def test_MMNode_build_tree_GO():
    g = GO(board_size=2)  # game (2 x 2 board)
    b=np.array([[ 1, 1],
                [ 1, 0]])
    s=GO_state(b,x=1,a=1) #it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    assert len(n.c) ==1 
    assert n.c[0].s.x==-1
    assert n.c[0].s.a ==2 
    assert len(n.c[0].c)==0
    s=GO_state(b,x=-1,p=(1,1),a=1) #it's O player's turn
    n = MMNode(s) 
    n.build_tree(g)
    assert len(n.c) ==1 
    assert n.c[0].s.x==1
    assert n.c[0].s.a ==2 
    assert len(n.c[0].c)==0
    g = GO(board_size=2,max_game_length=1)  # game (2 x 2 board)
    b=np.array([[ 1, 1],
                [ 1, 0]])
    s=GO_state(b,x=-1) #it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    assert len(n.c) ==2 
    assert n.c[0].s.x==1
    assert len(n.c[0].c)==0
    g = GO(board_size=2,max_game_length=2)  # game (2 x 2 board)
    b=np.array([[ 1, 1],
                [ 1, 0]])
    s=GO_state(b,x=-1) #it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    assert len(n.c) ==2 
    for c in n.c:
        assert c.s.x==1
        if np.allclose(c.s.b, b):
            assert len(c.c) == 1 
        else:
            assert len(c.c) == 4 
# --------------------------------


# ***********  Method: compute_v  (Class: MMNode) **************** 
# Total Points: 15.0

# ---- Test Case: terminal (Method: compute_v, Class: MMNode) 
# Goal: Test when the current node is a terminal node, game ended
# Points: 3.75
@pytest.mark.MMNode_compute_v
def test_MMNode_compute_v_terminal():
    g = TicTacToe()  # game 
    # the value of a terminal node is its game result
    b=np.array([[ 1, 0, 0],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.compute_v(g) 
    assert  n.v== 1 # X player won the game
    # the value of a terminal node is its game result
    b=np.array([[ 1, 1,-1],
                [-1, 1, 1],
                [ 1,-1,-1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.compute_v(g) 
    assert  n.v== 0 # tie 
    # the value of a terminal node is its game result
    b=np.array([[ 1, 0, 1],
                [ 0, 0, 1],
                [-1,-1,-1]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.compute_v(g) 
    assert  n.v==-1 # O player won the game
# --------------------------------

# ---- Test Case: children (Method: compute_v, Class: MMNode) 
# Goal: Test when the current node has children nodes
# Points: 3.75
@pytest.mark.MMNode_compute_v
def test_MMNode_compute_v_children():
    g = TicTacToe()  # game 
    # if it is X player's turn, the value of the current node is the max value of all its children nodes.
    b=np.array([[ 0,-1, 1],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    # the current node has 3 children nodes, two of which are terminal nodes (X player wins)
    n.compute_v(g) 
    # so the max value among the three children nodes max(1,?,1) = 1 (here ? is either 1 or 0 or -1)
    assert  n.v== 1 # X player won the game
    #-------------------------
    # if it is O player's turn, the value of the current node is the min value of all its children nodes.
    b=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.build_tree(g)
    # the current node has 2 children nodes, one of them is a terminal node (O player wins)
    n.compute_v(g) 
    # so the min value among the two children nodes min(-1,0) =-1 
    assert  n.v==-1 # O player won the game
    #-------------------------
    # a tie after one move
    b=np.array([[-1, 1,-1],
                [-1, 1, 1],
                [ 0,-1, 1]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0  
# --------------------------------

# ---- Test Case: optimal (Method: compute_v, Class: MMNode) 
# Goal: Test if the value of the current node can be computed correctly with deeper trees
# Points: 3.75
@pytest.mark.MMNode_compute_v
def test_MMNode_compute_v_optimal():
    g = TicTacToe()  # game 
    #-------------------------
    # optimal moves lead to: O player wins
    b=np.array([[-1, 1,-1],
                [ 1, 0, 0],
                [ 1, 0, 0]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v==-1
    #-------------------------
    # optimal moves lead to a tie
    b=np.array([[ 0, 1, 0],
                [ 0, 1, 0],
                [ 0, 0,-1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0
    #-------------------------
    # optimal moves lead to: X player wins
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0,-1, 0]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 0, 0]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [-1, 0, 0],
                [ 0, 0, 0]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [-1, 0, 0]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 1],
                [ 0, 0,-1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v==-1
    b=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    s = GameState(b,x=1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 1
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 1,-1]])
    s = GameState(b,x=-1)
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    assert  n.v== 0
# --------------------------------

# ---- Test Case: othello (Method: compute_v, Class: MMNode) 
# Goal: Test if the method works on Othello game
# Points: 3.75
@pytest.mark.MMNode_compute_v
def test_MMNode_compute_v_othello():
    g = TicTacToe()  # game 
    # Game: Othello 
    g = Othello()  # game 
    b=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    n.compute_v(g)
    assert np.allclose(n.s.b,b_)
    assert  n.v== 1
    b=np.array([[ 0, 0,-1, 1,-1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==-1
    b=np.array([[ 0, 0,-1, 1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s = GameState(b,x=-1) # it's O player's turn
    n = MMNode(s) 
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==-1
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==1
    b=np.array([[ 0,-1, 1,-1, 1,-1, 0, 0],
                [ 1, 0, 0, 0, 0, 0, 0, 0],
                [ 1, 0, 0, 0, 0, 0, 0, 0],
                [-1, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s) 
    n.build_tree(g)
    n.compute_v(g)
    assert  n.v==1
# --------------------------------

# ============= Class: MiniMaxPlayer ===========================
# Total Points: 15.0
# ***********  Method: choose_optimal_move  (Class: MiniMaxPlayer) **************** 
# Total Points: 7.5

# ---- Test Case: tictactoe (Method: choose_optimal_move, Class: MiniMaxPlayer) 
# Goal: Test if the code works on TicTacToe
# Points: 3.75
@pytest.mark.MiniMaxPlayer_choose_optimal_move
def test_MiniMaxPlayer_choose_optimal_move_tictactoe():
    g = TicTacToe()  # game 
    p = MiniMaxPlayer()
    #-------------------------
    b=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 2
    assert c == 0
    #-------------------------
    b=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [ 0, 1,-1]])
    s = GameState(b,x=-1) # it's O player's turn
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 2
    assert c == 0
    #-------------------------
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    s = GameState(b,x=-1) # it's O player's turn
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 1
    assert c == 1
    #-------------------------
    b=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [-1, 1,-1]])
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g) 
    r,c=p.choose_optimal_move(n)
    assert r == 1
    assert c == 0
# --------------------------------

# ---- Test Case: othello (Method: choose_optimal_move, Class: MiniMaxPlayer) 
# Goal: Test if the function works on Othello
# Points: 3.75
@pytest.mark.MiniMaxPlayer_choose_optimal_move
def test_MiniMaxPlayer_choose_optimal_move_othello():
    g = Othello()  # game 
    p = MiniMaxPlayer()
    b=np.array([[ 0,-1, 1,-1, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    n = MMNode(s)
    n.build_tree(g)
    n.compute_v(g)
    assert np.allclose(n.s.b,b_)
    r,c=p.choose_optimal_move(n)
    assert r == 0
    assert c == 0
# --------------------------------


# ***********  Method: choose_a_move  (Class: MiniMaxPlayer) **************** 
# Total Points: 7.5

# ---- Test Case: tictactoe (Method: choose_a_move, Class: MiniMaxPlayer) 
# Goal: Test if the code works with TicTacToe
# Points: 3.75
@pytest.mark.MiniMaxPlayer_choose_a_move
def test_MiniMaxPlayer_choose_a_move_tictactoe():
    g = TicTacToe()  # game
    # two possible moves: one leads to win
    p = MiniMaxPlayer()
    b=np.array([[ 0,-1, 1],
                [-1, 1, 1],
                [ 0, 1,-1]])
    b_ = b.copy()
    s = GameState(b,x=1) # it's X player's turn
    r, c = p.choose_a_move(g,s)
    assert np.allclose(s.b,b_)
    assert r==2  
    assert c==0  
    # three possible moves, one leads to win
    p = MiniMaxPlayer()
    b=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    s = GameState(b,x=1) # it's X player's turn
    r, c = p.choose_a_move(g,s) 
    assert r==2  
    assert c==0  
    #-------------------------
    p = MiniMaxPlayer()
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    s = GameState(b,x=-1) # it's O player's turn
    r, c = p.choose_a_move(g,s) 
    assert r == 1
    assert c == 1
# --------------------------------

# ---- Test Case: game (Method: choose_a_move, Class: MiniMaxPlayer) 
# Goal: Test the AI against other AIs (random player and then itself)
# Points: 3.75
@pytest.mark.MiniMaxPlayer_choose_a_move
def test_MiniMaxPlayer_choose_a_move_game():
    g = TicTacToe()  # game
    # play against random player in the game
    p1 = MiniMaxPlayer()
    p2 = RandomPlayer()
    # X Player: MinMax
    # O Player: Random 
    b=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    for i in range(10):
        s = GameState(b,x=1) # it's X player's turn
        e = g.run_a_game(p1,p2,s=s)
        assert e==1
    #-------------------------
    # play against MinMax player in the game
    # X Player: MinMax 
    # O Player: MinMax  
    b=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    for i in range(10):
        s = GameState(b,x=1) # it's X player's turn
        e = g.run_a_game(p1,p1,s=s)
        assert e==1
    b=np.array([[ 0, 0, 1],
                [ 0,-1, 0],
                [ 1,-1, 0]])
    s = GameState(b,x=1) # it's X player's turn
    e = g.run_a_game(p1,p1,s=s)
    assert e==0
    b=np.array([[ 0, 0, 0],
                [ 0,-1, 0],
                [ 1, 0, 0]])
    s = GameState(b,x=1) # it's X player's turn
    e = g.run_a_game(p1,p1,s=s)
    assert e==0
    b=np.array([[ 0, 0, 0],
                [ 0, 0, 0],
                [ 1,-1, 0]])
    s = GameState(b,x=1) # it's X player's turn
    e = g.run_a_game(p1,p1,s=s)
    assert e==1
    b=np.array([[ 0, 0, 0],
                [ 0, 1, 0],
                [ 0,-1, 0]])
    s = GameState(b,x=1) # it's X player's turn
    e = g.run_a_game(p1,p1,s)
    assert e==1
    b=np.array([[ 0, 0, 0],
                [ 0, 1, 0],
                [-1, 0, 0]])
    s = GameState(b,x=1) # it's X player's turn
    e = g.run_a_game(p1,p1,s)
    assert e==0
# --------------------------------


