from problem1 import *
import sys
import math

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (25 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_hello_page():
    ''' (5 points) hello_page'''
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
#---------------------------------------------------
def test_rand_page():
    ''' (5 points) rand_page'''
    c = app.test_client()
    response = c.get("/rand")
    assert response.status_code == 200
    a =float(response.data)
    assert a<=1 and a>=0 # the number should be between 0 and 1
    response = c.get("/rand")
    assert response.status_code == 200
    b =float(response.data)
    assert b<=1 and b>=0
    assert a != b # the two visits/users should see different random numbers
#---------------------------------------------------
def test_vote():
    ''' (5 points) vote'''
    c = app.test_client()
    response = c.get("/vote/2")
    assert response.status_code == 200
    assert response.data==b"Thank you for voting 2"
    response = c.get("/vote/1")
    assert response.status_code == 200
    assert response.data==b"Thank you for voting 1"
#---------------------------------------------------
def test_create_template():
    ''' (5 points) create_template'''
    t=create_template()
    assert type(t)== Template
    assert t.render(username="Alex")== "Hello, Alex!"
    assert t.render(username="Bob")== "Hello, Bob!"
#---------------------------------------------------
def test_load_template():
    ''' (5 points) load_template'''
    t=load_template("A.html")
    assert type(t)== Template
    assert t.render(name="Alex")== "Good morning, Alex!"
    assert t.render(name="Bob")== "Good morning, Bob!"
    t=load_template("B.html")
    assert type(t)== Template
    assert t.render(name="Alex")== "Good afternoon, Alex!"
    assert t.render(name="Bob")== "Good afternoon, Bob!"

