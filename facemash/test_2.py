from problem2 import *
import sys
import math
import re
'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (20 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

#---------------------------------------------------
def test_sample_pair():
    ''' (5 points) sample_pair'''
    count= [0]*7 # count how many times each image has been sampled
    for _ in range(200): # sample 200 times
        A, B = sample_pair(7)
        assert A < 7 and A>=0 # the sampled ID should be valid
        assert B < 7 and B>=0
        assert A != B # the two IDs should not be the same
        count[A]+=1
        count[B]+=1
    for c in count:
        c > 20
#---------------------------------------------------
def test_facemash():
    ''' (10 points) facemash'''
    c = app.test_client()
    response = c.get("/")
    assert response.status_code == 200
    r =response.data.decode("ASCII")
    assert len(r) ==1298
    assert r[:6] == "<html>"
    count= [0]*9 # count how many times each image has been sampled
    for _ in range(200): # sample 200 times
        response = c.get("/")
        assert response.status_code == 200
        r =response.data.decode("ASCII")
        m = re.findall("[0-8].jpg",r)
        A=int(m[0][0])
        B=int(m[1][0])
        assert A <=8 and A>=0 # the sampled ID should be valid
        assert B <=8 and B>=0
        assert A != B # the two IDs should not be the same
        count[A]+=1
        count[B]+=1
    for c in count:
        c > 20
#---------------------------------------------------
def test_vote():
    ''' (5 points) vote'''
    assert len(data) == 0
    c = app.test_client()
    response = c.get("/vote/2/0") # user votes 2.jpg wins, 0.jpg loses
    assert len(data) == 1
    assert data[0] == (2,0)
    assert response.status_code == 302 # should be redirected to homepage (facemash)
    response = c.get("/vote/1/5") # user votes 1.jpg wins, 5.jpg loses
    assert len(data) == 2
    assert data[0] == (2,0)
    assert data[1] == (1,5)

