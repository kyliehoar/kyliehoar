

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import random
from problem1 import load_template
from flask import Flask,redirect,url_for
app= Flask(__name__) # create an app for the website
template = load_template("index.html") # load the template for the homepage, using the function you implemented in problem 1
data = [] # create an empty list, we will use this list to store all the user votes
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Build FaceMash (20 points)
     In this problem, we will build a webpage similar to FaceMash using Flask. We use 8 photos in the static folder as an example dataset. Each time when a user visit the website, we will randomly sample two images to show, and users can click to vote on the photo.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: sample_pair (5 points)--------------------
    Goal: (Random Sample) Given the total number of photos (n), randomly choose a pair of the photo IDs (A and B) to return. Here we assume the IDs of all the photos are: 0,1,2,..., n-1. For example, if we have 5 photos (n=5), the IDs of the photos will be: 0,1,2,3,4. We then randomly sample two IDs (such as A=2, B=0), where the two IDs should be different from each other. 
    ---- Inputs: --------
    * n: the number of all photos in the website, an integer scalar.
    ---- Outputs: --------
    * A: the ID of the photo A (displayed on the left of the webpage), an integer scalar.
    * B: the ID of the photo B (displayed on the right of the webpage), an integer scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def sample_pair(n):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    A, B = random.sample(range(0, n-1), 2)
    #########################################
    return A, B

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_2.py::test_sample_pair
    (Mac &Linux): python3 -m pytest -v test_2.py::test_sample_pair
---------------------------------------------------------------'''




''' ---------Function: facemash (10 points)--------------------
    Goal: (Homepage) Create the homepage of facemash. Each time when a user visit the URL '/', randomly sample two photo IDs (A and B), and use these IDs and the template to render the webpage. Here the 'template' variable (a global variable) was already created in line #5 of this file. You could use this template to render the webpage using the IDs (A and B). 
    ---- Outputs: --------
    * webpage: a webpage returned to the user's browser to render, a string of plain text or html code.
    ---- Hints: --------
    * We assume we only have 9 photos in the database. The IDs of these photos are 0,1,2,...,8. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

@app.route("/")
def facemash():
    #########################################
    ## INSERT YOUR CODE HERE (10 points)
    A, B = sample_pair(9)
    data = {'A': A, 'B': B}
    webpage = template.render(data)
    #########################################
    return webpage

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_2.py::test_facemash
    (Mac &Linux): python3 -m pytest -v test_2.py::test_facemash
---------------------------------------------------------------'''




''' ---------Function: vote (5 points)--------------------
    Goal: (Vote Page) Create a page for user to vote. For example, if a user visits (/vote/4/3), it means that the user was given two photos with ID 3 and 4. This user voted Photo 4 wins, Photo 3 loses. In this function, please (1) update the game result into the list (data), then (2) redirect the page to the homepage of facemash. 
	 (1) In line #6 of this file, we have created an empty list (called 'data') to store all the vote data. Please store the game result by add a tuple of (3,4) into the list (data). 
	 For example, at the beginning, the list is data = [], 
	 Suppose a user voted Photo 5 wins, Photo 3 loses, we need to add a tuple (5,3) to the data list, so now data = [(5,3)] 
	 Suppose another user voted Photo 0 wins and Photo 2 loses, we need to add a tuple (0,2) to the data list, so now data = [(5,3),(0,2)] 
	 (2) In the returned webpage, please redirect the user to the homepage of facemash . 
    ---- Inputs: --------
    * win_id: .
    * lose_id: .
    ---- Outputs: --------
    * webpage: a webpage returned to the user's browser to render, a string of plain text or html code.
    ---- Hints: --------
    * (1) append the vote data to the "data" list. 
    * (2) redirect to the homepage of facemash. 
    * You could use redirect() function in Flask to redirect to an URL. 
    * You could use url_for() function in Flask to find the URL for a page. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

@app.route("/vote/<int:win_id>/<int:lose_id>")
def vote(win_id, lose_id):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    data.append((win_id, lose_id))
    webpage = redirect("/vote/")
    #########################################
    return webpage

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_2.py::test_vote
    (Mac &Linux): python3 -m pytest -v test_2.py::test_vote
---------------------------------------------------------------'''


''' 
    # -------------------------------------------------------
    # (Demo) Now you can test the website that you have built by typing the following in the terminal:
    # (Windows OS): python demo2.py
    # (Linux/Mac ): python3 demo2.py
    # -------------------------------------------------------
    
'''



'''-------- TEST problem2.py file: (20 points) ----------
Now you can test the correctness of all the above functions in this file by typing the following in the terminal:
(Windows OS): python -m pytest -v test_2.py
(Mac &Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* A:  the ID of the photo A (displayed on the left of the webpage), an integer scalar. 
* B:  the ID of the photo B (displayed on the right of the webpage), an integer scalar. 
* n:  the number of all photos in the website, an integer scalar. 
* webpage:  a webpage returned to the user's browser to render, a string of plain text or html code. 
--------------------------------------------'''



