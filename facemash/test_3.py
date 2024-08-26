from problem3 import *
import sys
import math

'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (25 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_compute_EA():
    ''' (5 points) compute_EA'''
    EA = compute_EA(RA=100., RB=100.)
    assert math.isclose(EA,0.5,abs_tol=0.01) 
    EA = compute_EA(RA=100., RB=500.) 
    assert math.isclose(EA, 1/11,abs_tol=0.01)
    EA = compute_EA(RA=500., RB=100.)
    assert math.isclose(EA, 1/1.1,abs_tol=0.01)
#---------------------------------------------------
def test_compute_EB():
    ''' (5 points) compute_EB'''
    EB = compute_EB(0.1)
    assert math.isclose(EB,0.9,abs_tol=0.01) 
    EB = compute_EB(0.8)
    assert math.isclose(EB,0.2,abs_tol=0.01)
    EB = compute_EB(0.5)
    assert math.isclose(EB,0.5,abs_tol=0.01)
#---------------------------------------------------
def test_update_RA():
    ''' (5 points) update_RA'''
    RA_new = update_RA(RA=100., SA=1., EA=1.)
    assert RA_new == 100 
    RA_new = update_RA(RA=100., SA=0., EA=0.)
    assert RA_new == 100 
    RA_new = update_RA(RA=100., SA=1., EA=0.)
    assert RA_new == 116 
    RA_new = update_RA(RA=100., SA=0., EA=1.)
    assert RA_new == 84
    RA_new = update_RA(RA=100., SA=0., EA=1., K = 32)
    assert RA_new == 68
    RA_new = update_RA(RA=100., SA=1., EA=.5, K = 200)
    assert RA_new == 200 
#---------------------------------------------------
def test_update_RB():
    ''' (5 points) update_RB'''
    RB_new = update_RB(RB=100., SB=1., EB=1.)
    assert RB_new == 100 
    RB_new = update_RB(RB=100., SB=0., EB=0.)
    assert RB_new == 100 
    RB_new = update_RB(RB=100., SB=1., EB=0.)
    assert RB_new == 116 
    RB_new = update_RB(RB=100., SB=0., EB=1.)
    assert RB_new == 84
    RB_new = update_RB(RB=100., SB=0., EB=1., K = 32)
    assert RB_new == 68
    RB_new = update_RB(RB=100., SB=1., EB=.5, K = 200)
    assert RB_new == 200 
#---------------------------------------------------
def test_compute_ratings():
    ''' (5 points) compute_ratings'''
    G = pd.DataFrame({"win_ID":[0],"lose_ID":[1]}) # only 1 Game: player 0 wins, player 1 loses
    R = compute_ratings(G, n=2)
    assert len(R) == 2
    assert math.isclose(sum(R), 400*2, abs_tol =1e-2) # the sum of all players rating should stay the same after a game
    assert R[0]== 408
    assert R[1]== 392
    R = compute_ratings(G, n= 2, K=32.) # test k-factor
    assert math.isclose(sum(R), 400*2, abs_tol =1e-2) # the sum of all players rating should stay the same after a game
    assert R[0]== 416
    assert R[1]== 384
    G = pd.DataFrame({"win_ID":[1,2,3],"lose_ID":[0,1,0]})
    # Game 1: player 1 wins against player 0
    # Game 2: player 2 wins against player 1
    # Game 3: player 3 wins against player 0
    R = compute_ratings(G, n = 4)
    assert R[1]>R[0] # because of game 1
    assert R[2]>R[1] # because of game 2
    assert R[3]>R[0] # because of game 3
    assert R[2]>R[0] # because of game 1 & 2
    assert R[2]>R[3] # because player 2 beats player 1 (higher rating)
    assert math.isclose(sum(R), 400*4, abs_tol = 1e-1)

