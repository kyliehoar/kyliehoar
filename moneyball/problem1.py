''' ------------Install *pytest* package--------------
    *pytest* is a python package for for unit testing your code and automatic grading.
    Please type the following command in your terminal to install the pytest package.
      (Windows OS): python -m pip install pytest
      (Mac /Linux): python3 -m pip install pytest
     ------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.

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
    Goal of Problem 1: (Moneyball) Player Statistics (Sabermetrics) (22 points)
    In this problem, you will implement different evaluation metrics for baseball players..
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_BA (3 points)--------------------
    Goal: (Batting Average) Given the number of hits and number of at-bats for a player in the games, compute the batting average of the player. The batting average (BA) is defined by the number of hits divided by at-bats. 
    ---- Inputs: --------
    * H: (hits) the number of hits in games by a player, an integer scalar. A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice. There are four types of hits in baseball: singles, doubles, triples and home runs. All four are counted equally when deciphering batting average. If a player is thrown out attempting to take an extra base (e.g., turning a single into a double), that still counts as a hit.
    * AB: (at-bats) the number of at-bats in games by a player,  an integer scalar. An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error or when a batter is put out on a non-sacrifice. At-bats are used as the denominator when determining batting average and slugging percentage. Players who bat higher in the order will typically finish the season with more at-bats than players who hit toward the bottom. Similarly, players who walk infrequently also typically record a higher-than-usual number of at-bats in a season, because walks do not count as at-bats.
    ---- Outputs: --------
    * BA: (batting average) the batting average of a player, a float scalar. One of the oldest and most universal tools to measure a hitter's success at the plate, batting average is determined by dividing a player's hits by the total at-bats for a number between zero (shown as .000) and one (1.000). In recent years, the league-wide batting average has typically hovered around .250.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_BA(H, AB):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    BA = H/AB
    #########################################
    return BA

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_BA
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_BA
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_OBP (3 points)--------------------
    Goal: (On Base Percentage) Given the in-game statistics of a player, compute the on-base-percentage of the player. 
    ---- Inputs: --------
    * H: (hits) the number of hits in games by a player, an integer scalar. A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice. There are four types of hits in baseball: singles, doubles, triples and home runs. All four are counted equally when deciphering batting average. If a player is thrown out attempting to take an extra base (e.g., turning a single into a double), that still counts as a hit.
    * AB: (at-bats) the number of at-bats in games by a player,  an integer scalar. An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error or when a batter is put out on a non-sacrifice. At-bats are used as the denominator when determining batting average and slugging percentage. Players who bat higher in the order will typically finish the season with more at-bats than players who hit toward the bottom. Similarly, players who walk infrequently also typically record a higher-than-usual number of at-bats in a season, because walks do not count as at-bats.
    * BB: (walks) the number of walks achieved by a player,  an integer scalar. A 'walk' (or base on balls) occurs when a pitcher throws four pitches out of the strike zone, none of which are swung at by the hitter. After refraining from swinging at four pitches out of the zone, the batter is awarded first base. As a stat, walks can be used to measure an important skill: a hitter's eye (meaning his ability to tell whether a pitch is a strike or a ball and swing -- or not swing -- accordingly). Because this factor is extremely important in the process, walks are looked at as a stat for hitters.
    * HBP: (hit-by-pitch) the number of times that the player is hit by pitch in games,  an integer scalar. A hit-by-pitch occurs when a batter is struck by a pitched ball without swinging at it. He is awarded first base as a result. Strikes supersede hit-by-pitches, meaning if the umpire rules that the pitch was in the strike zone or that the batter swung, the HBP is nullified.  A batter is awarded a hit-by-pitch, even if the ball only touches a portion of his uniform or protection (helmet, shin guard, etc.).
    * SF: (sacrifice-fly) the number of sacrifice fly in games by a player,  an integer scalar. A sacrifice fly occurs when a batter hits a fly-ball out to the outfield or foul territory that allows a runner to score. A sacrifice fly does not count as an at-bat and therefore does not count against a player's batting average. The thinking behind the rule is that with a man on third base and fewer than two outs, a batter will often intentionally try to hit a fly ball, sacrificing his time at bat to help score a run. However, sacrifice flies count against a player's on-base percentage.
    ---- Outputs: --------
    * OBP: (on-base-percentage) the on-base-percentage of a player, a float scalar. OBP refers to how frequently a batter reaches base per plate appearance. Times on base include hits, walks and hit-by-pitches, but do not include errors, times reached on a fielder's choice or a dropped third strike. (Separately, sacrifice bunts are removed from the equation entirely, because it is rarely a hitter's decision to sacrifice himself, but rather a manager's choice as part of an in-game strategy.) A hitter's goal is to avoid making an out, and on-base percentage shows which hitters have accomplished that task the best.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_OBP(H, AB, BB, HBP, SF):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    OBP = (H + BB + HBP)/(AB + BB + SF + HBP)
    #########################################
    return OBP

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_OBP
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_OBP
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_B1 (3 points)--------------------
    Goal: (Singles) Now we want to compute more statistics like 'Slugging Percentage' and 'runs created'. However, they both require the number of 'singles'(B1), which is not directly available in the data, but this number (B1) can be computed indirectly using the number of hits, doubles, triples and home_runs. Given the in-game statistics of a player, compute the 'singles' (B1) of the player.. 
    ---- Inputs: --------
    * H: (hits) the number of hits in games by a player, an integer scalar. A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice. There are four types of hits in baseball: singles, doubles, triples and home runs. All four are counted equally when deciphering batting average. If a player is thrown out attempting to take an extra base (e.g., turning a single into a double), that still counts as a hit.
    * B2: (doubles) the number of 'doubles' a player has been credited,  an integer scalar. A batter is credited with a 'double' when he hits the ball into play and reaches second base without the help of an intervening error or attempt to put out another baserunner. Doubles are typically hit either into a gap, down the lines or off the outfield wall. They often score speedier runners from first base -- except for in the instance of a ground-rule double, where the ball bounces into the stands and all baserunners, including the batter, are awarded two bases.
    * B3: (triples) the number of triples a player is credited,  an integer scalar. A 'triple' occurs when a batter hits the ball into play and reaches third base without the help of an intervening error or attempt to put out another baserunner.
    * HR: (home runs) the number of home runs a player has achieved,  an integer scalar. A home run occurs when a batter hits a fair ball and scores on the play without being put out or without the benefit of an error.
    ---- Outputs: --------
    * B1: (singles) the number of 'singles' a player has been credited,  an integer scalar. A 'single' occurs when a batter hits the ball and reaches first base without the help of an intervening error or attempt to put out another baserunner. Singles are the most common type of hit in baseball, and they occur in many varieties. If a batter beats out a bunt or an infield dribbler -- it's a single. And if a batter hits a rocket to the outfield wall but is held at first base -- it's also a single. (A batter is still credited with a single if he reaches first safely but is thrown out while trying to advance to second.).
    ---- Hints: --------
    * The total number of hits (H) is the sum of singles, doubles, triples and home_runs: H = B1 + B2 + B3 + HR. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_B1(H, B2, B3, HR):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    B1 = H-B2-B3-HR
    #########################################
    return B1

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_B1
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_B1
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_TB (3 points)--------------------
    Goal: (Total Bases) Given the in-game statistics of a player, compute the 'total number of bases' (TB) of the player. TB is the number of bases a player has gained with hits. It is a weighted sum for which the weight value is 1 for a single, 2 for a double, 3 for a triple and 4 for a home run. 
    ---- Inputs: --------
    * B1: (singles) the number of 'singles' a player has been credited,  an integer scalar. A 'single' occurs when a batter hits the ball and reaches first base without the help of an intervening error or attempt to put out another baserunner. Singles are the most common type of hit in baseball, and they occur in many varieties. If a batter beats out a bunt or an infield dribbler -- it's a single. And if a batter hits a rocket to the outfield wall but is held at first base -- it's also a single. (A batter is still credited with a single if he reaches first safely but is thrown out while trying to advance to second.).
    * B2: (doubles) the number of 'doubles' a player has been credited,  an integer scalar. A batter is credited with a 'double' when he hits the ball into play and reaches second base without the help of an intervening error or attempt to put out another baserunner. Doubles are typically hit either into a gap, down the lines or off the outfield wall. They often score speedier runners from first base -- except for in the instance of a ground-rule double, where the ball bounces into the stands and all baserunners, including the batter, are awarded two bases.
    * B3: (triples) the number of triples a player is credited,  an integer scalar. A 'triple' occurs when a batter hits the ball into play and reaches third base without the help of an intervening error or attempt to put out another baserunner.
    * HR: (home runs) the number of home runs a player has achieved,  an integer scalar. A home run occurs when a batter hits a fair ball and scores on the play without being put out or without the benefit of an error.
    ---- Outputs: --------
    * TB: (total bases) the total number of bases a player has gained with hits,  an integer scalar. Total bases refer to the number of bases gained by a batter through hits. A batter records one total base for a single, two total bases for a double, three total bases for a triple and four total bases for a home run.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_TB(B1, B2, B3, HR):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    TB = B1 + 2*B2 + 3*B3 + 4*HR
    #########################################
    return TB

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_TB
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_TB
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_SLG (3 points)--------------------
    Goal: (Slugging Percentage) Given the in-game statistics of a player, compute the slugging percentage of the player.  Slugging percentage (SLG) is a measure of the batting productivity of a hitter. It is calculated as total bases divided by at bats. 
    ---- Inputs: --------
    * TB: (total bases) the total number of bases a player has gained with hits,  an integer scalar. Total bases refer to the number of bases gained by a batter through hits. A batter records one total base for a single, two total bases for a double, three total bases for a triple and four total bases for a home run.
    * AB: (at-bats) the number of at-bats in games by a player,  an integer scalar. An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error or when a batter is put out on a non-sacrifice. At-bats are used as the denominator when determining batting average and slugging percentage. Players who bat higher in the order will typically finish the season with more at-bats than players who hit toward the bottom. Similarly, players who walk infrequently also typically record a higher-than-usual number of at-bats in a season, because walks do not count as at-bats.
    ---- Outputs: --------
    * SLG: (slugging percentage) the slugging percentage of a player, a float scalar. Slugging percentage represents the total number of bases a player records per at-bat. Unlike on-base percentage, slugging percentage deals only with hits and does not include walks and hit-by-pitches in its equation. Slugging percentage differs from batting average in that all hits are not valued equally. While batting average is calculated by dividing the total number of hits by the total number of at-bats, the formula for slugging percentage is: (B1 + B2 x 2 + B3 x 3 + HRx4)/AB.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_SLG(TB, AB):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    SLG = TB / AB
    #########################################
    return SLG

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_SLG
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_SLG
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_runs (3 points)--------------------
    Goal: (Runs Created Formula) Given the in-game statistics of a team in a year, compute the expected runs created by the team using Bill James' runs created formula. 
    ---- Inputs: --------
    * H: (hits) the number of hits in games by a player, an integer scalar. A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice. There are four types of hits in baseball: singles, doubles, triples and home runs. All four are counted equally when deciphering batting average. If a player is thrown out attempting to take an extra base (e.g., turning a single into a double), that still counts as a hit.
    * BB: (walks) the number of walks achieved by a player,  an integer scalar. A 'walk' (or base on balls) occurs when a pitcher throws four pitches out of the strike zone, none of which are swung at by the hitter. After refraining from swinging at four pitches out of the zone, the batter is awarded first base. As a stat, walks can be used to measure an important skill: a hitter's eye (meaning his ability to tell whether a pitch is a strike or a ball and swing -- or not swing -- accordingly). Because this factor is extremely important in the process, walks are looked at as a stat for hitters.
    * TB: (total bases) the total number of bases a player has gained with hits,  an integer scalar. Total bases refer to the number of bases gained by a batter through hits. A batter records one total base for a single, two total bases for a double, three total bases for a triple and four total bases for a home run.
    * AB: (at-bats) the number of at-bats in games by a player,  an integer scalar. An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error or when a batter is put out on a non-sacrifice. At-bats are used as the denominator when determining batting average and slugging percentage. Players who bat higher in the order will typically finish the season with more at-bats than players who hit toward the bottom. Similarly, players who walk infrequently also typically record a higher-than-usual number of at-bats in a season, because walks do not count as at-bats.
    ---- Outputs: --------
    * RC: the expected number of runs created by a team, a float scalar.
    ---- Hints: --------
    * There are multiple versions of the 'runs created' formula, here we are using the basic version: ((Hits + Walks) x Total Bases) / (At Bats + Walks). 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_runs(H, BB, TB, AB):
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    RC = ((H + BB) * TB) / (AB + BB)
    #########################################
    return RC

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_runs
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_runs
---------------------------------------------------------------'''

    
    

''' ---------Function: compute_wins (4 points)--------------------
    Goal: (Winning Probability) Given the in-game statistics of a team, compute the expected wining probability of a team in a game using Bill James' Pythagorean expectation. 
    ---- Inputs: --------
    * RC: the expected number of runs created by a team, a float scalar.
    * RA: the number of runs allowed by a team,  an integer scalar.
    ---- Outputs: --------
    * W: the expected winning probability of a team in a game, a float scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_wins(RC, RA):
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    W = 1/(1+(RA/RC)**2)
    #########################################
    return W

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_compute_wins
    (Mac &Linux): python3 -m pytest -v test_1.py::test_compute_wins
---------------------------------------------------------------'''

    
    


'''-------- TEST problem1.py file: (22 points) ----------
Now you can test the correctness of all the above functions in this file by typing the following in the terminal:
(Windows OS): python -m pytest -v test_1.py
(Mac &Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* H:  (hits) the number of hits in games by a player, an integer scalar. A hit occurs when a batter strikes the baseball into fair territory and reaches base without doing so via an error or a fielder's choice. There are four types of hits in baseball: singles, doubles, triples and home runs. All four are counted equally when deciphering batting average. If a player is thrown out attempting to take an extra base (e.g., turning a single into a double), that still counts as a hit. 
* AB:  (at-bats) the number of at-bats in games by a player,  an integer scalar. An official at-bat comes when a batter reaches base via a fielder's choice, hit or an error or when a batter is put out on a non-sacrifice. At-bats are used as the denominator when determining batting average and slugging percentage. Players who bat higher in the order will typically finish the season with more at-bats than players who hit toward the bottom. Similarly, players who walk infrequently also typically record a higher-than-usual number of at-bats in a season, because walks do not count as at-bats. 
* BB:  (walks) the number of walks achieved by a player,  an integer scalar. A 'walk' (or base on balls) occurs when a pitcher throws four pitches out of the strike zone, none of which are swung at by the hitter. After refraining from swinging at four pitches out of the zone, the batter is awarded first base. As a stat, walks can be used to measure an important skill: a hitter's eye (meaning his ability to tell whether a pitch is a strike or a ball and swing -- or not swing -- accordingly). Because this factor is extremely important in the process, walks are looked at as a stat for hitters. 
* HBP:  (hit-by-pitch) the number of times that the player is hit by pitch in games,  an integer scalar. A hit-by-pitch occurs when a batter is struck by a pitched ball without swinging at it. He is awarded first base as a result. Strikes supersede hit-by-pitches, meaning if the umpire rules that the pitch was in the strike zone or that the batter swung, the HBP is nullified.  A batter is awarded a hit-by-pitch, even if the ball only touches a portion of his uniform or protection (helmet, shin guard, etc.). 
* SF:  (sacrifice-fly) the number of sacrifice fly in games by a player,  an integer scalar. A sacrifice fly occurs when a batter hits a fly-ball out to the outfield or foul territory that allows a runner to score. A sacrifice fly does not count as an at-bat and therefore does not count against a player's batting average. The thinking behind the rule is that with a man on third base and fewer than two outs, a batter will often intentionally try to hit a fly ball, sacrificing his time at bat to help score a run. However, sacrifice flies count against a player's on-base percentage. 
* B1:  (singles) the number of 'singles' a player has been credited,  an integer scalar. A 'single' occurs when a batter hits the ball and reaches first base without the help of an intervening error or attempt to put out another baserunner. Singles are the most common type of hit in baseball, and they occur in many varieties. If a batter beats out a bunt or an infield dribbler -- it's a single. And if a batter hits a rocket to the outfield wall but is held at first base -- it's also a single. (A batter is still credited with a single if he reaches first safely but is thrown out while trying to advance to second.). 
* B2:  (doubles) the number of 'doubles' a player has been credited,  an integer scalar. A batter is credited with a 'double' when he hits the ball into play and reaches second base without the help of an intervening error or attempt to put out another baserunner. Doubles are typically hit either into a gap, down the lines or off the outfield wall. They often score speedier runners from first base -- except for in the instance of a ground-rule double, where the ball bounces into the stands and all baserunners, including the batter, are awarded two bases. 
* B3:  (triples) the number of triples a player is credited,  an integer scalar. A 'triple' occurs when a batter hits the ball into play and reaches third base without the help of an intervening error or attempt to put out another baserunner. 
* HR:  (home runs) the number of home runs a player has achieved,  an integer scalar. A home run occurs when a batter hits a fair ball and scores on the play without being put out or without the benefit of an error. 
* TB:  (total bases) the total number of bases a player has gained with hits,  an integer scalar. Total bases refer to the number of bases gained by a batter through hits. A batter records one total base for a single, two total bases for a double, three total bases for a triple and four total bases for a home run. 
* BA:  (batting average) the batting average of a player, a float scalar. One of the oldest and most universal tools to measure a hitter's success at the plate, batting average is determined by dividing a player's hits by the total at-bats for a number between zero (shown as .000) and one (1.000). In recent years, the league-wide batting average has typically hovered around .250. 
* OBP:  (on-base-percentage) the on-base-percentage of a player, a float scalar. OBP refers to how frequently a batter reaches base per plate appearance. Times on base include hits, walks and hit-by-pitches, but do not include errors, times reached on a fielder's choice or a dropped third strike. (Separately, sacrifice bunts are removed from the equation entirely, because it is rarely a hitter's decision to sacrifice himself, but rather a manager's choice as part of an in-game strategy.) A hitter's goal is to avoid making an out, and on-base percentage shows which hitters have accomplished that task the best. 
* SLG:  (slugging percentage) the slugging percentage of a player, a float scalar. Slugging percentage represents the total number of bases a player records per at-bat. Unlike on-base percentage, slugging percentage deals only with hits and does not include walks and hit-by-pitches in its equation. Slugging percentage differs from batting average in that all hits are not valued equally. While batting average is calculated by dividing the total number of hits by the total number of at-bats, the formula for slugging percentage is: (B1 + B2 x 2 + B3 x 3 + HRx4)/AB. 
* RC:  the expected number of runs created by a team, a float scalar. 
* RA:  the number of runs allowed by a team,  an integer scalar. 
* W:  the expected winning probability of a team in a game, a float scalar. 
--------------------------------------------'''



