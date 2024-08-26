from problem4 import *
import sys
import math
from problem2 import load_csv, save_csv
'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 4 (27 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_compute_players_BA():
    ''' (4 points) compute_players_BA'''
    z = load_csv('moneyball_X6.csv')
    compute_players_BA(z)
    assert z.shape == (65,50)
    assert math.isclose(z[z.playerID=="abernbr01"].iloc[0].BA, 0.2697,abs_tol=0.001)
    assert math.isclose(z[z.playerID=="youngmi02"].iloc[0].BA, 0.2487,abs_tol=0.001)
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X7.csv")
#---------------------------------------------------
def test_rank_players_BA():
    ''' (3 points) rank_players_BA'''
    X = load_csv('moneyball_X7.csv')
    R = rank_players_BA(X)
    assert R.iloc[0].playerID == "berkmla01"
    assert R.iloc[1].playerID == "pujolal01"
    assert R.iloc[2].playerID == "pierrju01"
    save_csv(R,"moneyball_R1.csv")
#---------------------------------------------------
def test_compute_players_OBP():
    ''' (4 points) compute_players_OBP'''
    z = load_csv('moneyball_X7.csv')
    compute_players_OBP(z)
    assert z.shape == (65,51)
    assert math.isclose(z[z.playerID=="abernbr01"].iloc[0].OBP, 0.3283,abs_tol=0.001)
    assert math.isclose(z[z.playerID=="youngmi02"].iloc[0].OBP, 0.2976,abs_tol=0.001)
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X8.csv")
#---------------------------------------------------
def test_rank_players_OBP():
    ''' (3 points) rank_players_OBP'''
    X = load_csv('moneyball_X8.csv')
    R = rank_players_OBP(X)
    save_csv(R,"moneyball_R2.csv")
    assert R.iloc[0].playerID == "berkmla01"
    assert R.iloc[1].playerID == "pujolal01"
    assert R.iloc[2].playerID == "giambje01"
    assert R.iloc[3].playerID == "mientdo01"
#---------------------------------------------------
def test_compute_players_1B():
    ''' (3 points) compute_players_1B'''
    z = load_csv('moneyball_X8.csv')
    compute_players_1B(z)
    assert z.shape == (65,52)
    assert z[z.playerID=="abernbr01"].iloc[0]["1B"]== 59
    assert z[z.playerID=="youngmi02"].iloc[0]["1B"]== 63
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X9.csv")
#---------------------------------------------------
def test_compute_players_TB():
    ''' (3 points) compute_players_TB'''
    z = load_csv('moneyball_X9.csv')
    compute_players_TB(z)
    assert z.shape == (65,53)
    assert z[z.playerID=="abernbr01"].iloc[0]["TB"]== 116
    assert z[z.playerID=="youngmi02"].iloc[0]["TB"]== 155
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X10.csv")
#---------------------------------------------------
def test_compute_players_SLG():
    ''' (4 points) compute_players_SLG'''
    z = load_csv('moneyball_X10.csv')
    compute_players_SLG(z)
    assert z.shape == (65,54)
    assert math.isclose(z[z.playerID=="abernbr01"].iloc[0].SLG, 0.38158,abs_tol=0.001)
    assert math.isclose(z[z.playerID=="youngmi02"].iloc[0].SLG, 0.40155,abs_tol=0.001)
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X11.csv")
#---------------------------------------------------
def test_rank_players_SLG():
    ''' (3 points) rank_players_SLG'''
    X = load_csv('moneyball_X11.csv')
    R = rank_players_SLG(X)
    save_csv(R,"moneyball_R3.csv")
    assert R.iloc[0].playerID == "berkmla01"
    assert R.iloc[1].playerID == "pujolal01"
    assert R.iloc[2].playerID == "millake01"
    assert R.iloc[3].playerID == "loducpa01"

