from problem1 import *
import sys
import math

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (30 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_transpose():
    ''' (3 points) transpose'''
    X=np.array([[1,2,3],[4,5,6]])
    Xt=transpose(X)
    assert type(Xt) == np.ndarray # check data type
    assert Xt.ndim == 2 # should be a matrix (2 dimensional array)
    assert Xt.shape == (3,2) # check shape of the matrix
    Xt_true=np.array([[1,4],[2,5],[3,6]])
#---------------------------------------------------
def test_identity_matrix():
    ''' (3 points) identity_matrix'''
    n= 10
    I=identity_matrix(n)
    assert type(I) == np.ndarray # check data type
    assert I.shape == (n,n)
    for i in range(n):
        for j in range(n):
            if i==j:
                assert I[i,j]==1
            else:
                assert I[i,j]==0
#---------------------------------------------------
def test_matrix_multiplication():
    ''' (6 points) matrix_multiplication'''
    X=np.array([[1,2,3],[4,5,6]])
    Y=np.array([[-1,-4],[-2,-5],[-3,-6]])
    Z =  matrix_multiplication(X, Y)
    assert type(Z) == np.ndarray
    assert Z.shape == (2,2)
    assert Z[0,0]==-14
    assert Z[0,1]==-32
    assert Z[1,0]==-32
    assert Z[1,1]==-77
    # test on random matrix
    for _ in range(20):
        r,c,k = np.random.randint(2,20,size= 3) 
        X = np.random.random((r,k))
        Y = np.random.random((k,c))
        Z = matrix_multiplication(X,Y)
        assert Z.shape == (r,c)
        i = np.random.randint(r)
        j = np.random.randint(c)
        assert np.allclose(Z[i,j], np.dot(X[i],Y[:,j]))
#---------------------------------------------------
def test_matrix_inverse():
    ''' (6 points) matrix_inverse'''
    X=np.array([[2,0],[0,4]])
    Xi =  matrix_inverse(X)
    assert type(Xi) == np.ndarray
    assert Xi.shape == (2,2)
    assert Xi[0,0]==0.5
    assert Xi[0,1]==0
    assert Xi[1,0]==0
    assert Xi[1,1]==0.25
    X=np.array([[1,2],[3,4]])
    Xi =  matrix_inverse(X)
    assert type(Xi) == np.ndarray
    assert Xi.shape == (2,2)
    assert np.allclose(Xi,[[-2,1],[1.5,-0.5]])
#---------------------------------------------------
def test_is_missing():
    ''' (3 points) is_missing'''
    x=np.array([1,2,np.nan,3,np.nan])
    m = is_missing(x)
    assert type(m) == np.ndarray # check data type
    assert np.allclose(m,[False,False,True,False,True])
    x=np.array([2,np.nan,3,np.nan,5])
    m = is_missing(x)
    assert np.allclose(m,[False,True,False,True,False])
#---------------------------------------------------
def test_inverse():
    ''' (3 points) inverse'''
    m=np.array([False,False,True,False,True])
    m_ = inverse(m)
    assert np.allclose(m_,[True,True,False,True,False])
    m=np.array([False,True,False,True,False])
    m_ = inverse(m)
    assert np.allclose(m_,[True,False,True,False,True])
#---------------------------------------------------
def test_subset_vector():
    ''' (3 points) subset_vector'''
    x=np.array([1,2,3,4,5])
    m=np.array([True,True,False,True,False])
    x_m = subset_vector(x,m)
    assert np.allclose(x_m,[1,2,4])
    m=np.array([True,False,False,False,True])
    x_m = subset_vector(x,m)
    assert np.allclose(x_m,[1,5])
#---------------------------------------------------
def test_subset_matrix():
    ''' (3 points) subset_matrix'''
    X=np.array([[1,2],[3,4],[5,6]])
    m=np.array([True,False,True])
    X_m = subset_matrix(X,m)
    assert np.allclose(X_m,[[1,2],[5,6]])
    m=np.array([False,True,True])
    X_m = subset_matrix(X,m)
    assert np.allclose(X_m,[[3,4],[5,6]])

