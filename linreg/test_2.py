from problem2 import *
import sys
import math

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (20 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_least_square():
    ''' (10 points) least_square'''
    X = np.array([[ 1.,-1.],  # the first instance,
                  [ 1., 0.],  # the second instance
                  [ 1., 1.]])
    y = np.array([1.5,2.5,3.5])
    w = least_square(X,y)
    assert type(w) == np.ndarray
    assert w.shape == (2,) 
    assert np.allclose(w, [2.5,1.], atol = 1e-2) 
    count=0
    for _ in range(20):
        p = np.random.randint(2,8)
        n = np.random.randint(200,400)
        w_true = np.random.random(p)
        X = np.random.random((n,p))*10
        e = np.random.randn(n)*0.01
        y = np.dot(X,w_true) + e
        w = least_square(X,y)
        if np.allclose(w,w_true, atol = 0.1):
            count+=1
    assert count>18
#---------------------------------------------------
def test_ridge_regression():
    ''' (10 points) ridge_regression'''
    X = np.array([[ 1.,-1.],  # the first instance,
                  [ 1., 0.],  # the second instance
                  [ 1., 1.]])
    y = np.array([1.5,2.5,3.5])
    w = ridge_regression(X,y)
    assert type(w) == np.ndarray
    assert w.shape == (2,) 
    assert np.allclose(w, [2.5,1.], atol = 1e-2) 
    w = ridge_regression(X,y,a= 1000)
    assert np.allclose(w, [0.,0.], atol = 1e-2) 
    count=0
    for _ in range(20):
        p = np.random.randint(2,8)
        n = np.random.randint(200,400)
        w_true = np.random.random(p)
        X = np.random.random((n,p))*10
        e = np.random.randn(n)*0.01
        y = np.dot(X,w_true) + e
        w = ridge_regression(X,y)
        if np.allclose(w,w_true, atol = 0.1):
            count+=1
    assert count>18

