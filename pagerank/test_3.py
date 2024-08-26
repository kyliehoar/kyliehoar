from problem3 import *
import sys
import math
import pandas as pd
'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (15 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_count_in_links():
    ''' (5 points) count_in_links'''
    A = np.array([[0, 1, 1],
                  [1, 1, 1],
                  [1, 0, 0]]) # adjacency matrix of shape (3 by 3)
    c= count_in_links(A)
    assert c[0] == 2
    assert c[1] == 3
    assert c[2] == 1
    A = np.array([[0,1,1,1],
                  [1,0,0,0],
                  [1,1,1,1],
                  [1,0,0,1]]) # adjacency matrix of shape (4 by 4)
    c= count_in_links(A)
    assert c[0] == 3
    assert c[1] == 1
    assert c[2] == 4
    assert c[3] == 2
    A = np.loadtxt("data_A.csv",delimiter=",")
    c= count_in_links(A)
    assert c[0] == 1
    assert c[1] == 1
    assert c[2] == 1
    assert c[3] == 4
    assert c[4] == 1
    assert c[5] == 2
    assert c[6] == 1
    assert c[7] == 1
#---------------------------------------------------
def test_add_column_inlinks():
    ''' (5 points) add_column_inlinks'''
    X1 = pd.read_csv("data_X1.csv")
    A = np.loadtxt("data_A.csv", delimiter=",")
    c = count_in_links(A)
    X2 = add_column_inlinks(X1,c)
    assert type(X2) == pd.DataFrame
    assert X2.shape == (8, 6)
    assert X2.iloc[0].Inlinks== 1 
    assert X2.iloc[1].Inlinks== 1 
    assert X2.iloc[2].Inlinks== 1 
    assert X2.iloc[3].Inlinks== 4 
    assert X2.iloc[4].Inlinks== 1 
    assert X2.iloc[5].Inlinks== 2 
    assert X2.iloc[6].Inlinks== 1 
    assert X2.iloc[7].Inlinks== 1 
    # Now lets save the result into a CSV file, for further analysis
    X2.to_csv("data_X2.csv", index=False)
#---------------------------------------------------
def test_rank_inlinks():
    ''' (5 points) rank_inlinks'''
    X2 = pd.read_csv('data_X2.csv')
    R = rank_inlinks(X2)
    assert R.iloc[0].ID == 3
    assert R.iloc[0].Inlinks == 4
    assert R.iloc[1].ID == 5
    assert R.iloc[1].Inlinks == 2
    # Now lets save the result into a CSV file, for your review
    R.to_csv("data_R2.csv", index=False)

