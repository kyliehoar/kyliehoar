from problem3 import *
import sys
import math

'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (24 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_load_batting():
    ''' (3 points) load_batting'''
    x=load_batting()
    assert type(x) == pd.DataFrame
    assert x.shape == (105861, 22) 
    assert x.iloc[0,6] == 4
    assert x.iloc[330,6] == 136
#---------------------------------------------------
def test_filter_batting():
    ''' (3 points) filter_batting'''
    x=load_batting()
    y=filter_batting(x, year=1999) # filter with year 1999
    assert y.shape == (1299, 22) 
    assert y.iloc[0,1] == 1999
    assert y.iloc[1200,1] == 1999
    assert y.iloc[0,6] == 57 
    assert y.iloc[1,6] == 21 
    y=filter_batting(x,2001)  # filter with year 2001
    assert type(y) == pd.DataFrame
    assert y.shape == (1339, 22) 
    assert y.iloc[0,1] == 2001
    assert y.iloc[1338,1] == 2001
    assert y.iloc[0,6] == 1
    assert y.iloc[1,6] == 42 
    # Now lets save the dataset of year 2001 into a CSV file, for further analysis
    save_csv(y,"moneyball_X1.csv")
    # load from the saved file and check the correctness of the saved data 
    z= load_csv("moneyball_X1.csv")
    assert type(z) == pd.DataFrame
    assert z.shape == (1339, 22) 
    assert z.iloc[0,1] == 2001
    assert z.iloc[1338,1] == 2001
    assert z.iloc[0,6] == 1
    assert z.iloc[1,6] == 42
#---------------------------------------------------
def test_group_batting():
    ''' (3 points) group_batting'''
    x= load_csv("moneyball_X1.csv")
    y=group_batting(x)
    assert y.shape == (1220, 22)
    assert y.iloc[1,5] == 28  # the "G" column for player "abbotje01"
    assert y.iloc[1,6] == 42  # the "AB" column for player "abbotje01"
    assert y.iloc[7,5] == 59  # the "G" column for player "aceveju01"
    assert y.iloc[7,6] == 3  # the "AB" column for player "aceveju01"
    assert y.iloc[84,5] == 46 # the "G" column for player "bennega01"
    assert y.iloc[84,6] == 131  # the "AB" column for player "bennega01"
    assert y.iloc[84,-1] == 1  # the "GIDP" column for player "bennega01"
    # Now lets save the result into a CSV file, for further analysis
    save_csv(y,"moneyball_X2.csv")
#---------------------------------------------------
def test_merge_player():
    ''' (3 points) merge_player'''
    x= load_csv("moneyball_X2.csv")
    y= load_csv("moneyball_player.csv")
    z=merge_player(x,y)
    assert z.shape == (1220, 45)  
    assert z[z.playerID=="abreubo01"].iloc[0].G ==162
    assert z[z.playerID=="abreubo01"].iloc[0].birthYear ==1974
    assert z[z.playerID=="bradlmi01"].iloc[0].G == 77
    assert z[z.playerID=="bradlmi01"].iloc[0].birthYear == 1978
    assert z[z.playerID=="bradlmi01"].iloc[0].nameLast =="Bradley" 
    assert z[z.playerID=="bradlmi01"].iloc[0].nameFirst =="Milton" 
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X3.csv") 
#---------------------------------------------------
def test_filter_salary():
    ''' (3 points) filter_salary'''
    x= load_csv("moneyball_salary.csv")
    y=filter_salary(x,2002)
    # Now lets save the result into a CSV file, for further analysis
    save_csv(y,"moneyball_Z1.csv") 
    assert y.shape == (846, 5)  
    assert y[y.playerID=="anderga01"].iloc[0].yearID == 2002
    assert y[y.playerID=="anderga01"].iloc[0].salary == 5000000
    assert y[y.playerID=="miltoer01"].iloc[0].yearID == 2002
    assert y[y.playerID=="miltoer01"].iloc[0].salary == 4000000
    assert y[y.playerID=="woodwch01"].iloc[0].yearID == 2002
    assert y[y.playerID=="woodwch01"].iloc[0].salary == 235000
#---------------------------------------------------
def test_merge_salary():
    ''' (3 points) merge_salary'''
    x= load_csv("moneyball_X3.csv")
    y= load_csv("moneyball_Z1.csv")
    z= merge_salary(x,y)
    assert z.shape == (786, 49)
    assert z[z.playerID=="anderga01"].iloc[0].G== 161
    assert z[z.playerID=="anderga01"].iloc[0].nameLast== "Anderson"
    assert z[z.playerID=="anderga01"].iloc[0].salary == 5000000
    assert z[z.playerID=="miltoer01"].iloc[0].G == 35 
    assert z[z.playerID=="miltoer01"].iloc[0].nameLast=="Milton" 
    assert z[z.playerID=="miltoer01"].iloc[0].salary == 4000000
    assert z[z.playerID=="woodwch01"].iloc[0].G== 37
    assert z[z.playerID=="woodwch01"].iloc[0].nameLast == "Woodward"
    assert z[z.playerID=="woodwch01"].iloc[0].salary == 235000
    # Now lets save the result into a CSV file, for further analysis
    save_csv(z,"moneyball_X4.csv") 
#---------------------------------------------------
def test_filter_min_AB():
    ''' (3 points) filter_min_AB'''
    X4= load_csv('moneyball_X4.csv')
    X5 = filter_min_AB(X4, 300)
    assert X5.shape == (237,49)
    assert X5[X5.AB<300].shape == (0,49) # there should be no player in the list who has a smaller AB (at-bat)
    # Now lets save the result into a CSV file, for further analysis
    save_csv(X5,"moneyball_X5.csv")
#---------------------------------------------------
def test_filter_max_salary():
    ''' (3 points) filter_max_salary'''
    X5= load_csv('moneyball_X5.csv')
    X6 = filter_max_salary(X5, 1200000)
    assert X6.shape == (65,49)
    assert X6[X6.salary>1200000].shape == (0,49) # there should be no player in the list who has a higher salary
    # Now lets save the result into a CSV file, for further analysis
    save_csv(X6,"moneyball_X6.csv")

