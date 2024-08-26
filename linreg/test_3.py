from problem3 import *
import sys
import math
import numpy as np
'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (50 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_extract_user_j():
    ''' (7 points) extract_user_j'''
    R_j= np.array([ 1, np.nan, 2, np.nan])
    I = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6],
                  [0.7, 0.8]])
    X,y = extract_user_j(R_j,I)
    X_true= np.array([[0.1,0.2],
                      [0.5,0.6]])
    assert np.allclose(X,X_true)
    y_true= np.array([1,2])
    assert np.allclose(y,y_true)
    R_j= np.array([ np.nan, 2, 1, np.nan, 3, np.nan, 5])
    I = np.array([[0.1, 0.2],
                  [0.2, 0.3],
                  [0.3, 0.4],
                  [0.4, 0.5],
                  [0.5, 0.6],
                  [0.6, 0.7],
                  [0.7, 0.8]])
    X,y = extract_user_j(R_j,I)
    X_true= np.array([[0.2, 0.3],
                      [0.3, 0.4],
                      [0.5, 0.6],
                      [0.7, 0.8]])
    assert np.allclose(X,X_true)
    y_true= np.array([2,1,3,5])
    assert np.allclose(y,y_true)
#---------------------------------------------------
def test_train_user_j():
    ''' (7 points) train_user_j'''
    X = np.array([[ 1.,-1.],  # the first rated item,
                  [ 1., 0.],  # the second rated item
                  [ 1., 1.]])
    y = np.array([1.5,2.5,3.5]) # ratings of these items
    Uj = train_user_j(X,y,a=0)
    assert type(Uj) == np.ndarray
    assert Uj.shape == (2,) 
    assert np.allclose(Uj, [2.5,1.], atol = 1e-2) 
    Uj = train_user_j(X,y,a = 1000)
    assert np.allclose(Uj, [0.,0.], atol = 1e-2) 
    for _ in range(20):
        p = np.random.randint(2,8)
        n = np.random.randint(200,400)
        Uj_true = np.random.random(p)
        X = np.random.random((n,p))*10
        e = np.random.randn(n)*0.01
        y = np.dot(X,Uj_true) + e
        Uj = train_user_j(X,y,a=0.001)
        assert np.allclose(Uj,Uj_true, atol = 0.1)
#---------------------------------------------------
def test_update_U():
    ''' (7 points) update_U'''
    R = np.array([[      1,  np.nan ],
                  [ np.nan,       4 ],
                  [      5,  np.nan ],
                  [ np.nan,       2 ]])
    I = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6],
                  [0.7, 0.8]])
    U = update_U(R,I,a=0)
    assert type(U) == np.ndarray
    U_true = np.array([[ 10, 0],
                       [-60, 55]])
    assert np.allclose(U,U_true,atol=0.1)
    U = update_U(R,I,a=1000)
    U_true = np.array([[0, 0],
                       [0, 0]])
    assert np.allclose(U,U_true,atol=0.1)
#---------------------------------------------------
def test_extract_item_i():
    ''' (7 points) extract_item_i'''
    Ri_= np.array([ 1, np.nan, 2, np.nan])
    U = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6],
                  [0.7, 0.8]])
    X,y = extract_item_i(Ri_,U)
    X_true= np.array([[0.1,0.2],
                      [0.5,0.6]])
    assert np.allclose(X,X_true)
    y_true= np.array([1,2])
    assert np.allclose(y,y_true)
    Ri_= np.array([ np.nan, 2, 1, np.nan, 3, np.nan, 5])
    U = np.array([[0.1, 0.2],
                  [0.2, 0.3],
                  [0.3, 0.4],
                  [0.4, 0.5],
                  [0.5, 0.6],
                  [0.6, 0.7],
                  [0.7, 0.8]])
    X,y = extract_item_i(Ri_,U)
    X_true= np.array([[0.2, 0.3],
                      [0.3, 0.4],
                      [0.5, 0.6],
                      [0.7, 0.8]])
    assert np.allclose(X,X_true)
    y_true= np.array([2,1,3,5])
    assert np.allclose(y,y_true)
#---------------------------------------------------
def test_train_item_i():
    ''' (7 points) train_item_i'''
    X = np.array([[ 1.,-1.],  # the first rated item,
                  [ 1., 0.],  # the second rated item
                  [ 1., 1.]])
    y = np.array([1.5,2.5,3.5]) # ratings of these items
    Ii = train_item_i(X,y,a=0)
    assert type(Ii) == np.ndarray
    assert Ii.shape == (2,) 
    assert np.allclose(Ii, [2.5,1.], atol = 1e-2) 
    Ii = train_item_i(X,y,a = 1000)
    assert np.allclose(Ii, [0.,0.], atol = 1e-2) 
    for _ in range(20):
        p = np.random.randint(2,8)
        m = np.random.randint(200,400)
        Ii_true = np.random.random(p)
        X = np.random.random((m,p))*10
        e = np.random.randn(m)*0.01
        y = np.dot(X,Ii_true) + e
        Ii = train_item_i(X,y,a=0.001)
        assert np.allclose(Ii,Ii_true, atol = 0.1)
#---------------------------------------------------
def test_update_I():
    ''' (7 points) update_I'''
    R = np.array([[      1,  np.nan ,      5, np.nan],
                  [ np.nan,       4 , np.nan,    2  ]])
    U = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6],
                  [0.7, 0.8]])
    I = update_I(R,U,a=0)
    I_true = np.array([[ 10, 0],
                       [-60, 55]])
    assert np.allclose(I,I_true,atol=0.1)
    I = update_I(R,U,a=1000)
    I_true = np.array([[0, 0],
                       [0, 0]])
    assert np.allclose(I,I_true,atol=0.1)
#---------------------------------------------------
def test_collaborative_filtering():
    ''' (8 points) collaborative_filtering'''
    # test with dense rating matrix (without missing values)
    R = np.ones((4,5))
    I,U = collaborative_filtering(R,k=1)
    assert np.allclose(R,I@(U.T),atol=0.1)
    R = np.zeros((5,6))
    I,U = collaborative_filtering(R,k=1)
    assert np.allclose(R,I@(U.T),atol=0.1)
    # test with a rating matrix with missing values
    R = np.ones((4,5))
    R[1,2] = np.nan
    I,U = collaborative_filtering(R,k=1)
    R[1,2] = 1
    assert np.allclose(R,I@(U.T),atol=0.1)
    # test with random rating matrix
    n = 0
    for _ in range(5):
        R = np.ones((4,5))
        I = np.random.rand(4,2)/1.5
        U = np.random.rand(5,2)/1.5
        R =  I@(U.T)
        I1,U1 = collaborative_filtering(R,k=2)
        if np.allclose(R,I1@(U1.T),atol=0.1):
            n+=1
    assert n>0