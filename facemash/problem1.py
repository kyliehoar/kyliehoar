
'''------------Turn on Word Wrap Setting in Your Editor--------------
    NOTE: For better readability of the instructions, 
          please turn on the 'Word Wrap' setting in your editor. 
    HOW: For example, in the VS Code editor, click "Settings" in the menu, 
         then type "word wrap" in the search box of the settings, 
    choose "on" in the drop-down menu.
    TEST: If you can read this long sentence without scrolling your screen from left to right, it means that your editor's word wrap setting is on and you are good to go. 
------------------------------------------------------------------'''

''' ------------Install *flask* package--------------
    *flask* is a python package for for creating web pages/applications.
    Please type the following command in your terminal to install the flask package.
      (Windows OS): python -m pip install flask
      (Mac /Linux): python3 -m pip install flask
     ------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import random
from flask import Flask
from jinja2 import Template,Environment,FileSystemLoader
app= Flask(__name__) # create an app for the website
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
    Goal of Problem 1: Getting familiar with flask package (25 points)
     In this problem, we will get familiar with the flask python package.  Flask is a library for website development in Python.  It provides fast, flexible, and easy website design framework.  We will use flask to build a simple website. You could read the tutorials for Flask: 
	 https://flask.palletsprojects.com/en/1.1.x/quickstart/.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: hello_page (5 points)--------------------
    Goal: (Hello World Page) In the first URL ('/'), let's create a simple page: when a user visited the homepage of our website, we just return a string 'Hello World!'. This is a static homepage, where the content of the webpage is always the same. 
    ---- Outputs: --------
    * webpage: a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/")
def hello_page():
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = "Hello World!"
    #########################################
    return webpage

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_hello_page
    (Mac &Linux): python3 -m pytest -v test_1.py::test_hello_page
---------------------------------------------------------------'''


''' 
    # -------------------------------------------------------
    # (Demo) Now you can test the website that you have built by typing the following in the terminal: 
    # (Windows OS): python demo1.py
    # (Linux/Mac ): python3 demo1.py
    # -------------------------------------------------------
    
'''


''' ---------Function: rand_page (5 points)--------------------
    Goal: (Random Number Page) In the second URL ('/rand'), let's create a simple dynamic page and send each user some different data in the webpage: Each time when a user visits this page, randomly generate a number (between 0 and 1) and return the string of the number back to the user. So when users visit this page multiple times, the user will see a different random number each time. 
    ---- Outputs: --------
    * webpage: a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/rand")
def rand_page():
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = str(random.randint(0,1))
    #########################################
    return webpage

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_rand_page
    (Mac &Linux): python3 -m pytest -v test_1.py::test_rand_page
---------------------------------------------------------------'''


''' 
    # -------------------------------------------------------
    # (Demo) Now you can test the website that you have built by typing the following in the terminal:
    # (Windows OS): python demo1.py
    # (Linux/Mac ): python3 demo1.py
    # Open the browser to visit the website with relative path "/rand"
    # -------------------------------------------------------
    
'''


''' ---------Function: vote (5 points)--------------------
    Goal: (Vote Page) In the third URL ('/vote/<ID>'), let's create a simple webpage for users to send data to the website host: Each time when a user visits this page with a number (ID) in the URL (for example, /vote/10), return a webpage with 'Thank you for voting <ID>' (for example, 'Thank you for voting 10'). 
    ---- Inputs: --------
    * ID: the ID of a user votes for, an integer scalar.
    ---- Outputs: --------
    * webpage: a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/vote/<int:ID>")
def vote(ID):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = 'Thank you for voting ' + str(ID)
    #########################################
    return webpage

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_vote
    (Mac &Linux): python3 -m pytest -v test_1.py::test_vote
---------------------------------------------------------------'''


''' 
    # -------------------------------------------------------
    # (Demo) Now you can test the website that you have built by typing the following in the terminal:
    # (Windows OS): python demo1.py
    # (Linux/Mac ): python3 demo1.py
    # Open the browser to visit the website with relative path "/vote/2"
    # -------------------------------------------------------
    
'''


''' ---------Function: create_template (5 points)--------------------
    Goal: (Template) create a jinja2 template that can be used to render 'Hello, <username>!' In this template, we need to have a variable named 'username'. For example, if the username ='Alex', when rendering this template, the returned string will be 'Hello, Alex!'; If the username = 'Bob', when rendering this template, the returned string will be 'Hello, Bob!'. 
    ---- Outputs: --------
    * t: a jinja2 template, which can be used to render a dynamic webpage.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def create_template():
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    t = Template('Hello, {{ username }}!')
    #########################################
    return t

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_create_template
    (Mac &Linux): python3 -m pytest -v test_1.py::test_create_template
---------------------------------------------------------------'''




''' ---------Function: load_template (5 points)--------------------
    Goal: load a jinja2 template from a file. 
    ---- Inputs: --------
    * filename: the filename of the template to be used for rendering webpage response, a string.
    ---- Outputs: --------
    * t: a jinja2 template, which can be used to render a dynamic webpage.
    ---- Hints: --------
    * You could user FileSystemLoader in jinja2 to create an Environment in the current folder (".") and use the created environment to load the template from the file. 
    * This problem can be solved using 3 line(s) of code. More lines are okay. ''' 

def load_template(filename):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    with open(filename) as file:
        t = Template(file.read())
    #########################################
    return t

'''---------- Test This Function -----------------
    Now you can test the correctness of your code above by typing the following in the terminal:
    (Windows OS): python -m pytest -v test_1.py::test_load_template
    (Mac &Linux): python3 -m pytest -v test_1.py::test_load_template
---------------------------------------------------------------'''





'''-------- TEST problem1.py file: (25 points) ----------
Now you can test the correctness of all the above functions in this file by typing the following in the terminal:
(Windows OS): python -m pytest -v test_1.py
(Mac &Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* webpage:  a webpage returned to the user's browser when a user visits the URL, a string of plain text or html. 
* ID:  the ID of a user votes for, an integer scalar. 
* filename:  the filename of the template to be used for rendering webpage response, a string. 
* t:  a jinja2 template, which can be used to render a dynamic webpage. 
--------------------------------------------'''



