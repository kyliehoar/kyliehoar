from problem4 import *
import sys
import math

'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 4 (30 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_load_G():
    ''' (5 points) load_G'''
    G = load_G() 
    assert type(G) == pd.DataFrame
    assert G.shape == (11621, 2)
    assert G.iloc[0,0] == 0 
    assert G.iloc[0,1] == 1 
    assert G.iloc[-1,0] == 667
    assert G.iloc[-1,1] == 286
#---------------------------------------------------
def test_load_teams():
    ''' (5 points) load_teams'''
    team_names = load_teams() 
    assert type(team_names) == pd.DataFrame
    assert team_names.shape == (1031, 2)
    assert team_names.iloc[0,1] == "Liberty"
    assert team_names.iloc[1,1] == "Randolph Col"
    assert team_names.iloc[-1,1] == "York (NE)"
#---------------------------------------------------
def test_compute_elo():
    ''' (10 points) compute_elo'''
    G = pd.DataFrame({"win_ID":[0],"lose_ID":[1]}) # only 1 Game: player 0 wins, player 1 loses
    R = compute_elo(G, 2,16)
    assert len(R) == 2
    assert R.iloc[0].ID == 0 # the ID column should be integers instead of floats
    assert R.iloc[0].Elo == 408
    assert R.iloc[1].ID == 1
    assert R.iloc[1].Elo == 392
    G = load_G()
    R = compute_elo(G, 1031,16)
    assert len(R) == 1031
    assert math.isclose(R.iloc[0].Elo,326,abs_tol=0.1)
    assert math.isclose(R.iloc[1].Elo,392,abs_tol=0.1)
    assert math.isclose(R.iloc[2].Elo,592.875,abs_tol=0.1)
    assert math.isclose(R.iloc[-1].Elo,392,abs_tol=0.1)
    # Now lets save the result into a CSV file, for further analysis
    R.to_csv("ncaa_R.csv", index=False)
#---------------------------------------------------
def test_merge_team():
    ''' (5 points) merge_team'''
    T= load_teams("ncaa_teams.csv")
    R= pd.read_csv("ncaa_R.csv")
    X=merge_team(T,R)
    assert X.shape == (1031, 3)  
    assert math.isclose(X[X.Name=="Liberty"].iloc[0].Elo, 326, abs_tol=0.1)
    assert math.isclose(X[X.Name=="Arizona"].iloc[0].Elo, 608.9, abs_tol=0.1)
    assert math.isclose(X[X.Name=="Worcester State"].iloc[0].Elo, 393, abs_tol=0.1)
    # Now lets save the result into a CSV file, for further analysis
    X.to_csv("ncaa_X.csv", index=False)
#---------------------------------------------------
def test_rank_teams_Elo():
    ''' (5 points) rank_teams_Elo'''
    X = pd.read_csv('ncaa_X.csv')
    R = rank_teams_Elo(X)
    assert R.iloc[0].ID == 102
    assert R.iloc[0].Name == "Villanova"
    assert R.iloc[1].ID == 242
    assert R.iloc[1].Name == "Kansas"
    # Now lets save the result into a CSV file, for your review
    R.to_csv("ncaa_R.csv", index=False)

