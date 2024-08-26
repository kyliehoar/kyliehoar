#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
from problem2 import *
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 3: (Moneyball) Data Preprocessing in Baseball Dataset (24 points)
    In this problem, you will practise data preprocessing with baseball dataset.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: load_batting (3 points)--------------------
    Goal: (Loading Data) Let's start with the raw data, 'moneyball_batting.csv'. Let's load this CSV file into a pandas dataframe (X).. 
    ---- Inputs: --------
    * filename: the file name of a CSV file, a string.
    ---- Outputs: --------
    * X: a dataframe containing the batting data of all players in all years, loaded from moneyball_batting.csv.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def load_batting(filename='moneyball_batting.csv'):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X = load_csv(filename)
    #########################################
    return X

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_load_batting
    (Mac &Linux): python3 -m pytest -v test_3.py::test_load_batting
---------------------------------------------------------------'''

    
    

''' ---------Function: filter_batting (3 points)--------------------
    Goal: (Filtering by Year) The dataset contains records of all years. In this study, suppose we just want to choose players for the year 2002, based upon data of year 2001.  We need to filter the data and only keep the data records of year 2001. 
    ---- Inputs: --------
    * X: a dataframe containing the batting data of all players in all years, loaded from moneyball_batting.csv.
    * year: an integer scalar, the year of the data to be used.
    ---- Outputs: --------
    * X1: a dataframe containing the batting data only in the searched year (2001).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def filter_batting(X, year):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X1 = X[X['yearID'] == year]
    #########################################
    return X1

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_filter_batting
    (Mac &Linux): python3 -m pytest -v test_3.py::test_filter_batting
---------------------------------------------------------------'''

    
    

''' ---------Function: group_batting (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X1.csv'. This 2001 dataset contains multiple records for each player: a same player may have two/three records, because the player has changed team in year 2001. For example, playerID='guilljo01' (or 'houstty01') has two rows.  We need to sum the game statistics of the same player together, so that each player only contains one row in the data frame. For example if the same player with ID 'player1' has three rows of records, 'player2' has two rows of records: 
	player ID  | H  | AB 
	--------------------- 
	  player 1 | 5  | 10 
	  player 1 | 3  | 20 
	  player 1 | 1  | 30 
	  player 2 | 1  | 40 
	  player 2 | 2  | 50 
	  player 3 | 1  | 60 
	--------------------- 
 we should sum the data for each player into one row: 
	player ID  | H          | AB 
	----------------------------------------- 
	  player 1 | 9=(5+3+1)  | 60 = (10+20+30) 
	  player 2 | 3=(1+2)    | 90 = (40+50) 
	  player 3 | 1          | 60 
	----------------------------------------- 
 (Group by playerID) Given a data frame of batting statistics (X1), group the data records with respect to playerID, so that the game statistics are added together for each player. For example, player 'houstty01' has two rows, where the number of hits (column H) has values: 58, 4 We want to combine these two rows into one row, such that all the game statistics are the sum of the raw values (for example, number hits now should be 58+4 = 62) . 
    ---- Inputs: --------
    * X1: a dataframe containing the batting data only in the searched year (2001).
    ---- Outputs: --------
    * X2: a dataframe containing the batting data in the year (2001) after grouping the statistics for players.
    ---- Hints: --------
    * You could use some function implemented in problem2.py to solve this problem. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

# !!!!!!!!!!!!!!!FIX THIS!!!!!!!!!!!!!!!!!!!!!!!

def group_batting(X1):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    # X2 = group_sum(X1,'playerID')
    A=X1.groupby('playerID', as_index = False).sum().reset_index()
    X2=A.reset_index()
    #########################################
    return X2

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_group_batting
    (Mac &Linux): python3 -m pytest -v test_3.py::test_group_batting
---------------------------------------------------------------'''

    
    

''' ---------Function: merge_player (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X2.csv. Now the dataset only contains game statistics, but no information about the players is available, like first name, last name, weight, height, etc. We have another CSV file 'moneyball_player.csv', which contains the player information, such as first name, weight, height, etc. It would be better if we can combine these two datasets into one data frame, so the new data frame contains both game statistics and player information. 
 (Merge the two dataframes) Given a data frame (X2) of batting statistics , and a data frame (Y) of player information (loaded from 'moneyball_player.csv'), Combine the two data frames into one, according to the playerID column. . 
    ---- Inputs: --------
    * X2: a dataframe containing the batting data in the year (2001) after grouping the statistics for players.
    * Y: a dataframe containing the player information, such as first name, weight, height, which is loaded from moneyball_player.csv.
    ---- Outputs: --------
    * X3: a dataframe containing both batting data and player information in the year (2001).
    ---- Hints: --------
    * You could use some function implemented in problem2.py to solve this problem. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def merge_player(X2, Y):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X3 = merge(X2, Y, 'playerID')
    #########################################
    return X3

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_merge_player
    (Mac &Linux): python3 -m pytest -v test_3.py::test_merge_player
---------------------------------------------------------------'''

    
    

''' ---------Function: filter_salary (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X3.csv'. Now the dataset contains both game statistics and player information. However, we still need to know the salary of each player in year 2002, which represents the market price of each player in 2002, in order to hire the player into our team. We have another CSV file 'moneyball_salary.csv', which contains the player's salary information in all years. We first need to find the players' salaries only in year 2002, then we want to merge the salary information into the dataset. 
 (Filter salary for year 2002) Given the dataframe (Z) containing players' salary data of all years, filter the dataframe with year 2002, return the salary data only in year 2002. 
    ---- Inputs: --------
    * Z: a dataframe containing the salary data of all players in all years.
    * year: an integer scalar, the year of the data to be used.
    ---- Outputs: --------
    * Z1: a dataframe containing the salary data only in the searched year (2002).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def filter_salary(Z, year):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    Z1 = Z[Z['yearID'] == year]
    #########################################
    return Z1

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_filter_salary
    (Mac &Linux): python3 -m pytest -v test_3.py::test_filter_salary
---------------------------------------------------------------'''

    
    

''' ---------Function: merge_salary (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_Z1.csv'. Now let's merge the salary information into the dataset. 
 (Join the batting data with salary data) Given a data frame X3 (containing both batting statistics and player information, loaded from 'moneyball_X3.csv'), and a dataframe (Z1) of salary information (loaded from 'moneyball_Z1.csv'), combine the two data frames into one, according to the 'playerID' column. 
    ---- Inputs: --------
    * X3: a dataframe containing both batting data and player information in the year (2001).
    * Z1: a dataframe containing the salary data only in the searched year (2002).
    ---- Outputs: --------
    * X4: a dataframe containing all the required data (batting data, player information and salary data) for player evaluation in the year (2001).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def merge_salary(X3, Z1):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X4 = merge(X3, Z1, 'playerID')
    #########################################
    return X4

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_merge_salary
    (Mac &Linux): python3 -m pytest -v test_3.py::test_merge_salary
---------------------------------------------------------------'''

    
    

''' ---------Function: filter_min_AB (3 points)--------------------
    Goal:  If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X4.csv'. This file contains all the information we need for player evaluation. 
 (Filter At-Bats) Given a dataframe (X4) of all the players on the market in year 2002, find the candidate players who have sufficient experience: the players with minimum number of At-Bats(AB). Any player who has smaller number of AB than min_AB in X4 should be excluded. The remaining players are candidate players (in the dataframe X5), who have sufficient previous experience (AB >= min_AB) . 
    ---- Inputs: --------
    * X4: a dataframe containing all the required data (batting data, player information and salary data) for player evaluation in the year (2001).
    * min_AB: an integer scalar, the threshold on AB (at-Bat). To find good players, we should exclude those without sufficient experience. The players with AB less than the min_AB should be excluded from the ranked list..
    ---- Outputs: --------
    * X5: a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def filter_min_AB(X4, min_AB):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X5 = X4[X4['AB'] >= min_AB]
    #########################################
    return X5

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_filter_min_AB
    (Mac &Linux): python3 -m pytest -v test_3.py::test_filter_min_AB
---------------------------------------------------------------'''

    
    

''' ---------Function: filter_max_salary (3 points)--------------------
    Goal:  If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X5.csv'.  Now let's remove the players who are too expensive. 
(Find Affordable Players) Given a dataframe (X5) of all the players with sufficient experience, find the candidate players who are affordable: the players with salary no higher than max_salary. Any player who has higher salary than max_salary in X5 should be excluded. The remaining players are candidate players (in the dataframe X6), who have both sufficient experience (AB >= min_AB) and are affordable (salary < max_salary). 
    ---- Inputs: --------
    * X5: a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB).
    * max_salary: an integer scalar, the maximum salary that we can afford for a player. To find affordable players, we should exclude those too expensive player. The players with higher salaries than max_salary should be excluded from the ranked list..
    ---- Outputs: --------
    * X6: a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def filter_max_salary(X5, max_salary):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X6 = X5[X5['salary'] <= max_salary]
    #########################################
    return X6

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_3.py::test_filter_max_salary
    (Mac &Linux): python3 -m pytest -v test_3.py::test_filter_max_salary
---------------------------------------------------------------'''

    
    


'''-------- TEST problem3.py file: (24 points) ----------
Now you can test the correctness of all the above functions in this file by typing the following in the terminal:
(Windows OS): python -m pytest -v test_3.py
(Mac &Linux): python3 -m pytest -v test_3.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* filename:  the file name of a CSV file, a string. 
* year:  an integer scalar, the year of the data to be used. 
* X:  a dataframe containing the batting data of all players in all years, loaded from moneyball_batting.csv. 
* X1:  a dataframe containing the batting data only in the searched year (2001). 
* X2:  a dataframe containing the batting data in the year (2001) after grouping the statistics for players. 
* X3:  a dataframe containing both batting data and player information in the year (2001). 
* X4:  a dataframe containing all the required data (batting data, player information and salary data) for player evaluation in the year (2001). 
* X5:  a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB). 
* X6:  a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary). 
* Y:  a dataframe containing the player information, such as first name, weight, height, which is loaded from moneyball_player.csv. 
* Z:  a dataframe containing the salary data of all players in all years. 
* Z1:  a dataframe containing the salary data only in the searched year (2002). 
* min_AB:  an integer scalar, the threshold on AB (at-Bat). To find good players, we should exclude those without sufficient experience. The players with AB less than the min_AB should be excluded from the ranked list.. 
* max_salary:  an integer scalar, the maximum salary that we can afford for a player. To find affordable players, we should exclude those too expensive player. The players with higher salaries than max_salary should be excluded from the ranked list.. 
--------------------------------------------'''



