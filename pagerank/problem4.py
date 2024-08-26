

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import numpy as np
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 4: Ranking webpages using PageRank (AKA random walk with restart using matrix G) (48 points)
    In this problem, you will implement the ranking algorithm for webpages using PageRank (random walk with restart on the revised hyperlink graph to solve both sink node and sink region problems). 
 ------------------------------------ 
      Search Engine (Version 3) 
 ------------------------------------ 
 In this version of the search engine, we implement use random walk method on a revised hyperlink graph to address both sink node and sink region problem. (1) If a webpage has no hyperlink (which is a sink node), add a hyperlink from this webpage to all the webpages in the network (including itself); (2) for every step of the random walk, the user will have a small probability to jump to a random webpage ignoring the hyperlinks and a large probability to follow the hyperlink.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: count_out_links (5 points)--------------------
    Goal: Given an adjacency matrix A of a webpage hyperlink network, compute the count of out-links (also called 'degree') for each webpage in the network. 
    ---- Inputs: --------
    * A: the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i,j] =1, if there is a hyperlink from webpage j to webpage i; A[i][j]=0, if there is no hyperlink from webpage j to webpage i.
    ---- Outputs: --------
    * d: the vector storing the out-link degrees of all webpages, a numpy vector of length n. d[i] represents the out-link degree of webpage i, which is the number of hyperlinks on webpage i.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def count_out_links(A):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    d = np.sum(A, axis=0)
    #########################################
    return d

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_count_out_links
    (Mac /Linux): python3 -m pytest -v test_4.py::test_count_out_links
---------------------------------------------------------------'''



''' ---------Function: remove_sink_nodes (5 points)--------------------
    Goal: Given an adjacency matrix A (containing sink nodes), find all sink nodes in the network, then revise the adjacency matrix A by adding a hyperlink from each sink node to all the webpages (including itself) 
	 For example, if the adjacency matrix of 5 webpages are as follows: 
	   0,0,0,1,0 
	   1,0,0,0,0 
	   0,1,0,1,0 
	   0,1,0,0,0 
	   0,0,0,1,0 
	 In this adjacency matrix, the 3rd and 5th columns are both all-zero columns, which means that the 3rd and 5th webpages are sink nodes in the graph. 
	 In order to remove sink nodes, we want to add all-ones to these columns, so that the new adjacency matrix will be: 
	   0,0,1,1,1 
	   1,0,1,0,1 
	   0,1,1,1,1 
	   0,1,1,0,1 
	   0,0,1,1,1 
	 So this should be the output adjacency matrix A of this function . 
    ---- Inputs: --------
    * A: the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i,j] =1, if there is a hyperlink from webpage j to webpage i; A[i][j]=0, if there is no hyperlink from webpage j to webpage i.
    ---- Outputs: --------
    * A: the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i,j] =1, if there is a hyperlink from webpage j to webpage i; A[i][j]=0, if there is no hyperlink from webpage j to webpage i.
    ---- Hints: --------
    * You may reuse the previous function above to help solving this question. 
    * This problem can be solved using 3 line(s) of code. More lines are okay. ''' 

def remove_sink_nodes(A):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    d = np.all(A == 0, axis = 0)
    A = A.copy()
    A[:,d] = 1
    #########################################
    return A

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_remove_sink_nodes
    (Mac /Linux): python3 -m pytest -v test_4.py::test_remove_sink_nodes
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_A_.csv". You could take a look at this file for the result.
    
'''


''' ---------Function: compute_S (5 points)--------------------
    Goal: Given an adjacency matrix A_ of a webpage hyperlink network (after fixing all sink nodes), compute the probability transition matrix S. 
    ---- Inputs: --------
    * A_: the adjacency matrix indicating the hyperlinks between webpages (where all the sink nodes are fixed), a numpy matrix of shape (n X n). A_[i,j] =1, if there is a hyperlink from webpage j to webpage i; A_[i][j]=0, if there is no hyperlink from webpage j to webpage i.
    ---- Outputs: --------
    * S: the probability transition matrix among webpages (after solving the sink node problem), a (n by n) numpy matrix.  S[i,j] represents the probability of a random-walk user moving from webpage j to webpage i by clicking a hyperlink on webpage j. The values in each column of matrix S should sum to 1.
    ---- Hints: --------
    * You could use the functions you have implemented in the previous problems. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

def compute_S(A_):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    d = np.sum(A_, axis = 0)
    S = np.divide(A_, d)
    #########################################
    return S

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_compute_S
    (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_S
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_S.csv". You could take a look at this file for the result.
    
'''


''' ---------Function: compute_G (6 points)--------------------
    Goal: Given the probability transition matrix S of a webpage hyperlink network, fix the sink region problem in the probability transition matrix by allowing the random walk to have a large probability (alpha) to follow the hyperlinks and a small probability (1-alpha) to restart (jump to a random webpage, including itself, ignoring hyperlinks). 
    ---- Inputs: --------
    * S: the probability transition matrix among webpages (after solving the sink node problem), a (n by n) numpy matrix.  S[i,j] represents the probability of a random-walk user moving from webpage j to webpage i by clicking a hyperlink on webpage j. The values in each column of matrix S should sum to 1.
    * a: a float scalar value between 0 and 1, which is the probability of following the hyperlinks in the random walk.
    ---- Outputs: --------
    * G: the probability transition matrix of the hyperlink network (after fixing sink nodes and sink regions), a (n by n) numpy matrix of float values.  G[i,j] represents the probability of a user moving from webpage j to webpage i either by clicking a hyperlink or randomly jumping to webpage j. The values in each column of matrix G should sum to 1.
    ---- Hints: --------
    * You could use the ones_like(X) function in numpy to create an all-one matrix of the same shape as matrix X. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_G(S, a):
    #########################################
    ## INSERT YOUR CODE HERE (6 points)
    G = np.multiply(S, a) + np.multiply(np.ones_like(S), ((1-a)*(1/len(S))))
    #########################################
    return G

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_compute_G
    (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_G
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_G.csv". You could take a look at this file for the result.
    
'''


''' ---------Function: random_walk_one_step (6 points)--------------------
    Goal: (One-step Random Walk) Given the probability transition matrix G of a webpage hyperlink network and the vector x of the current scores for all webpages, compute the new scores of all webpages after one step of random walk and return these scores as vector y. 
    ---- Inputs: --------
    * G: the probability transition matrix of the hyperlink network (after fixing sink nodes and sink regions), a (n by n) numpy matrix of float values.  G[i,j] represents the probability of a user moving from webpage j to webpage i either by clicking a hyperlink or randomly jumping to webpage j. The values in each column of matrix G should sum to 1.
    * x: the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i.
    ---- Outputs: --------
    * y: the vector of probability distribution of the random walker on all webpages in the network (AFTER one step of random walk), a numpy vector of length n. y[i] represents the probability of the random walker in Webpage i.
    ---- Hints: --------
    * You could use matrix-vector multiplication to compute the result of one-step random walk. 
    * To multiply a numpy matrix A with a numpy vector b, you can use A@b. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def random_walk_one_step(G, x):
    #########################################
    ## INSERT YOUR CODE HERE (6 points)
    y = G@x
    #########################################
    return y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_random_walk_one_step
    (Mac /Linux): python3 -m pytest -v test_4.py::test_random_walk_one_step
---------------------------------------------------------------'''



''' ---------Function: all_close (5 points)--------------------
    Goal: Given two vectors of the webpage scores, check whether or not all the values in the two vectors are close enough. For example, if the tolerance (tol) is 0.1, the two values a and b are called 'close' if the absolute difference between the two values |a-b|<=0.1. Now when we have two vectors of values x, y, the two vectors are 'close' if all values of the two vectors are 'close'. 
    ---- Inputs: --------
    * x: the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i.
    * y: the vector of probability distribution of the random walker on all webpages in the network (AFTER one step of random walk), a numpy vector of length n. y[i] represents the probability of the random walker in Webpage i.
    * tol: the tolerance level, a float scalar, if all elements in two vectors x and y are close (|x[i]-y[i]|<= tol), then the x and y are close to each other.
    ---- Outputs: --------
    * c: a boolean scalar value of either True or False, if the two vectors x and y are close enough in all elements, c = True; if at least one of the elements of x and y has/have a bigger difference than tol (tolerance level) c= False.
    ---- Example: --------
    For example, suppose we have two vectors x=[1.05, 4.03], y=[1.02, 4.05], if the tolerance is 0.1, then x and y are 'close'. In this case, the returned result (c) should be True 
    For example, suppose we have two vectors m=[1.05, 4.03, 0.16], n=[1.02, 4.05, 0.35], if the tolerance is 0.1, then m and n are NOT 'close', because the last element is not close to each other within the tolerance. In this case, the returned result (c) should be False 
    ---- Hints: --------
    * numpy has a function 'allclose()' to test whether two vectors are close enough, by setting the absolute tolerance parameter (atol). 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def all_close(x, y, tol=0.01):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    c = np.allclose(x, y, atol=tol)
    #########################################
    return c

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_all_close
    (Mac /Linux): python3 -m pytest -v test_4.py::test_all_close
---------------------------------------------------------------'''



''' ---------Function: random_walk (6 points)--------------------
    Goal: Given the probability transition matrix G of a webpage network and a vector of the initial probability distribution (x) on all the webpages, compute the stationary probability distribution on the webpages (also called 'pagerank scores') and return them as vector x. 
	 (1) use a for-loop to repeat the random walk for max_steps times. 
	 (2) for each step inside the for-loop, 
		  (2.1) update the webpage scores using one-step random walk 
		  (2.2) check whether the scores before the random walk (x) and the scores after the random walk (y) are close enough within the tolerance (tol) 
		  (2.3) if the two score vectors are close, break the for-loop, otherwise update the score vector x with the new vector y. 
    ---- Inputs: --------
    * G: the probability transition matrix of the hyperlink network (after fixing sink nodes and sink regions), a (n by n) numpy matrix of float values.  G[i,j] represents the probability of a user moving from webpage j to webpage i either by clicking a hyperlink or randomly jumping to webpage j. The values in each column of matrix G should sum to 1.
    * x: the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i.
    * tol: the tolerance level, a float scalar, if all elements in two vectors x and y are close (|x[i]-y[i]|<= tol), then the x and y are close to each other.
    * max_steps: the maximum number of random walk steps, an integer scalar.
    ---- Outputs: --------
    * x: the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i.
    ---- Hints: --------
    * You could use the 'break' statement in python to break a for-loop. 
    * This function will take less than 1 second to run, if this function runs for a very long time without stopping, it means that the program never encountered the 'break' statement inside the for-loop. 
    * This problem can be solved using 5 line(s) of code. More lines are okay. ''' 

def random_walk(G, x, tol=0.01, max_steps=100):
    #########################################
    ## INSERT YOUR CODE HERE (6 points)
    for i in range(max_steps):
        y = random_walk_one_step(G, x)
        z = all_close(x, y, tol)
        if z == True:
            break
        else:
            i+=1
            x = y
    #########################################
    return x

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_random_walk
    (Mac /Linux): python3 -m pytest -v test_4.py::test_random_walk
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_x.csv". You could take a look at this file for the result.
    
'''


''' ---------Function: add_column_pagerank (5 points)--------------------
    Goal: Given the pagerank scores of each webpage in (x) and the dataframe storing all the webpage data (X2), add a new column called 'PageRank' to dataframe (X2) to store the PageRank scores for all webpages. 
    ---- Inputs: --------
    * X2: a dataframe of all the webpages containing the columns of word frequency and number of inlinks, where each row represents a webpage.
    * x: the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i.
    ---- Outputs: --------
    * X2: a dataframe of all the webpages containing the columns of word frequency and number of inlinks, where each row represents a webpage.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def add_column_pagerank(X2, x):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    X2['PageRank'] = x
    #########################################
    return X2

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_add_column_pagerank
    (Mac /Linux): python3 -m pytest -v test_4.py::test_add_column_pagerank
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_X3.csv", you could take a look at this file for the result.
    
'''


''' ---------Function: rank_pages (5 points)--------------------
    Goal: (Rank Webpages by PageRank Score) Given a dataframe (X3) of all the webpages, rank all the pages based upon descending order of pagerank scores (PageRank). 
    ---- Inputs: --------
    * X3: a dataframe of all the webpages containing the columns of pagerank socres, word frequency and number of inlinks, where each row represents a webpage.
    ---- Outputs: --------
    * R3: a dataframe of all the webpages, where the webpages are sorted according to descending order of the pagerank scores.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_pages(X3):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    R3 = X3.sort_values(by='PageRank', ascending=False)
    #########################################
    return R3

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_4.py::test_rank_pages
    (Mac /Linux): python3 -m pytest -v test_4.py::test_rank_pages
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_R3.csv". You could take a look at this file for the ranking result.
    
'''

'''---------- Demo -----------------
Please type the following command in your terminal to test the search engine that you have built:
    (Windows OS): python demo3.py
    (Mac /Linux): python3 demo3.py
The website will be hosted in your computer and you could copy the testing URL shown in the terminal to a web browser to use the website. Once it is done, you could terminate the web server by pressing Ctrl+C in the terminal.
-------------------------------------'''



'''-------- TEST problem4.py file: (48 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
    (Windows OS): python -m pytest -v test_4.py
    (Mac /Linux): python3 -m pytest -v test_4.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
    (Windows OS): python -m pytest -v
    (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
    (Windows OS): python grading.py
    (Mac /Linux): python3 grading.py
The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

 That's all! Great job! You did it!
-------------------------------------------------------------------------'''



'''---------List of All Variables ---------------
* A:  the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i,j] =1, if there is a hyperlink from webpage j to webpage i; A[i][j]=0, if there is no hyperlink from webpage j to webpage i. 
* d:  the vector storing the out-link degrees of all webpages, a numpy vector of length n. d[i] represents the out-link degree of webpage i, which is the number of hyperlinks on webpage i. 
* A_:  the adjacency matrix indicating the hyperlinks between webpages (where all the sink nodes are fixed), a numpy matrix of shape (n X n). A_[i,j] =1, if there is a hyperlink from webpage j to webpage i; A_[i][j]=0, if there is no hyperlink from webpage j to webpage i. 
* S:  the probability transition matrix among webpages (after solving the sink node problem), a (n by n) numpy matrix.  S[i,j] represents the probability of a random-walk user moving from webpage j to webpage i by clicking a hyperlink on webpage j. The values in each column of matrix S should sum to 1. 
* G:  the probability transition matrix of the hyperlink network (after fixing sink nodes and sink regions), a (n by n) numpy matrix of float values.  G[i,j] represents the probability of a user moving from webpage j to webpage i either by clicking a hyperlink or randomly jumping to webpage j. The values in each column of matrix G should sum to 1. 
* a:  a float scalar value between 0 and 1, which is the probability of following the hyperlinks in the random walk. 
* c:  a boolean scalar value of either True or False, if the two vectors x and y are close enough in all elements, c = True; if at least one of the elements of x and y has/have a bigger difference than tol (tolerance level) c= False. 
* n:  the number of all webpages in the network, an integer scalar. 
* x:  the vector of probability distribution of the random walker on all webpages in the network, a numpy vector of length n. x[i] represents the probability of the random walker in Webpage i. 
* y:  the vector of probability distribution of the random walker on all webpages in the network (AFTER one step of random walk), a numpy vector of length n. y[i] represents the probability of the random walker in Webpage i. 
* tol:  the tolerance level, a float scalar, if all elements in two vectors x and y are close (|x[i]-y[i]|<= tol), then the x and y are close to each other. 
* max_steps:  the maximum number of random walk steps, an integer scalar. 
* X2:  a dataframe of all the webpages containing the columns of word frequency and number of inlinks, where each row represents a webpage. 
* X3:  a dataframe of all the webpages containing the columns of pagerank socres, word frequency and number of inlinks, where each row represents a webpage. 
* R3:  a dataframe of all the webpages, where the webpages are sorted according to descending order of the pagerank scores. 
--------------------------------------------'''



