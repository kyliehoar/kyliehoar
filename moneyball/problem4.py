#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 4: (Moneyball) Player Ranking for Oakland A's Baseball Team (OAK) in year 2002 (27 points)
    In this problem, you will rank baseball players for Oakland A's using different methods.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_players_BA (4 points)--------------------
    Goal: (Compute Players' Batting Average) Given a dataframe (X6) of all the candidate players, compute the Batting Average (BA) of each player and insert a new column named 'BA' to store the data. 
    ---- Inputs: --------
    * X6: a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_BA(X6):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X6['BA'] = X6['H'] / X6['AB']
    pass 
    #########################################
'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_compute_players_BA
    (Mac &Linux): python3 -m pytest -v test_4.py::test_compute_players_BA
---------------------------------------------------------------'''

    
    

''' ---------Function: rank_players_BA (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X7.csv'.  Now let's rank all of these players using the traditional metric: Batting Average. 
(Rank Players by BA) Given a dataframe (X7) of all the candidate players, rank all the players based upon descending order of Batting Average (BA). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R1.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X7: a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Outputs: --------
    * R1: a dataframe containing candidate players ranked by descending order of Batting Average (BA).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_BA(X7):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R1 = X7.sort_values(by='BA', ascending=False)
    #########################################
    return R1

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_rank_players_BA
    (Mac &Linux): python3 -m pytest -v test_4.py::test_rank_players_BA
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_players_OBP (4 points)--------------------
    Goal: (Compute Players' On-Base Percentage) Given a dataframe (X7) of all the candidate players, compute the (OBP) of each player and insert a new column named 'OBP' to store the data. 
    ---- Inputs: --------
    * X7: a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_OBP(X7):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X7['OBP'] = (X7['H'] + X7['BB'] + X7['HBP'])/(X7['AB'] + X7['BB'] + X7['SF'] + X7['HBP'])
    pass 
    #########################################
'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_compute_players_OBP
    (Mac &Linux): python3 -m pytest -v test_4.py::test_compute_players_OBP
---------------------------------------------------------------'''

    
    

''' ---------Function: rank_players_OBP (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X8.csv'.  Now let's rank all of these players using the new metric: On-Base Percentage. 
(Rank Players by OBP) Given a dataframe (X8) of all the candidate players, rank all the players based upon descending order of On-Base Percentage (OBP). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R2.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X8: a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Outputs: --------
    * R2: a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_OBP(X8):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R2 = X8.sort_values(by='OBP', ascending=False)
    #########################################
    return R2

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_rank_players_OBP
    (Mac &Linux): python3 -m pytest -v test_4.py::test_rank_players_OBP
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_players_1B (3 points)--------------------
    Goal: (Compute Players' 1B) Given a dataframe (X8) of all the candidate players, compute the number of singles (1B) of each player and insert a new column named '1B' to store the data. 
    ---- Inputs: --------
    * X8: a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_1B(X8):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X8['1B'] = X8['H'] - X8['2B'] - X8['3B'] - X8['HR']
    pass 
    #########################################
'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_compute_players_1B
    (Mac &Linux): python3 -m pytest -v test_4.py::test_compute_players_1B
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_players_TB (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X9.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' TB) Given a dataframe (X9) of all the candidate players, compute the total number of bases (TB) of each player and insert a new column named 'TB' to store the data. 
    ---- Inputs: --------
    * X9: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_TB(X9):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X9['TB'] = X9['1B'] + 2 * X9['2B'] + 3 * X9['3B'] + 4 * X9['HR']
    pass 
    #########################################
'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_compute_players_TB
    (Mac &Linux): python3 -m pytest -v test_4.py::test_compute_players_TB
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_players_SLG (4 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X10.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' SLG) Given a dataframe (X10) of all the candidate players, compute the slugging percentage (SLG) of each player and insert a new column named 'SLG' to store the data. 
    ---- Inputs: --------
    * X10: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_SLG(X10):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X10['SLG'] = X10['TB']/X10['AB']
    pass 
    #########################################
'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_compute_players_SLG
    (Mac &Linux): python3 -m pytest -v test_4.py::test_compute_players_SLG
---------------------------------------------------------------'''

    
    

''' ---------Function: rank_players_SLG (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X11.csv'.  Now let's rank all of these players using the new metric: Slugging Percentage. 
(Rank Players by SLG) Given a dataframe (X11) of all the candidate players, rank all the players based upon descending order of Slugging Percentage (SLG). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R3.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X11: a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG).
    ---- Outputs: --------
    * R3: a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_SLG(X11):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R3 = X11.sort_values(by='SLG', ascending=False)
    #########################################
    return R3

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_4.py::test_rank_players_SLG
    (Mac &Linux): python3 -m pytest -v test_4.py::test_rank_players_SLG
---------------------------------------------------------------'''

    
    


'''-------- TEST problem4.py file: (27 points) ----------
Now you can test the correctness of all the above functions in this file by typing the following in the terminal:
(Windows OS): python -m pytest -v test_4.py
(Mac &Linux): python3 -m pytest -v test_4.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. Now you can test the correctness of all the problem files by typing the following:
 (Windows OS): python -m pytest -v 
 (Mac &Linux): python3 -m pytest -v 
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
 If you have finished all the problems in this HW assignment, you could run the following command in the terminal to compute your score of this HW assignment:
     ---------------------------------------------------
     (Windows OS): python grading.py
     (Mac &Linux): python3 grading.py
     ---------------------------------------------------
 The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

 That's all! Great job! You did it!
-------------------------------------------------------------------------'''



'''---------List of All Variables ---------------
* X6:  a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary). 
* X7:  a dataframe containing all the candidate players info, including Batting Average (BA). 
* X8:  a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP). 
* X9:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B). 
* X10:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB). 
* X11:  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG). 
* R1:  a dataframe containing candidate players ranked by descending order of Batting Average (BA). 
* R2:  a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP). 
* R3:  a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG). 
--------------------------------------------'''



