from problem2 import *
import sys
import math

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (22 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_ndarray():
    ''' (2 points) ndarray'''
    x=ndarray()
    assert type(x) == np.ndarray # check data type
    assert x.ndim == 2 # should be a matrix (2 dimensional array)
    assert x.shape == (2,3) # check shape of the matrix
    assert x[0,0] ==1
    assert x[1,1] ==5
    assert x[0,-1] ==3
    assert x[1,-1] ==6
#---------------------------------------------------
def test_float_array():
    ''' (2 points) float_array'''
    x=float_array()
    assert type(x) == np.ndarray # check data type
    assert x.ndim == 2 # should be a matrix (2 dimensional array)
    assert x.shape == (2,3) # check shape of the matrix
    assert x.dtype == float # check type of the data entry
    assert x[0,0] ==0.1
    assert x[1,1] ==0.5
    assert x[0,-1] ==0.3
    assert x[1,-1] ==0.6
#---------------------------------------------------
def test_get_shape():
    ''' (2 points) get_shape'''
    h,w=get_shape(np.zeros((4,5)))
    assert h == 4
    assert w == 5
#---------------------------------------------------
def test_all_one_matrix():
    ''' (2 points) all_one_matrix'''
    X=all_one_matrix(3,2)
    assert type(X) == np.ndarray # check data type
    assert X.shape == (3,2)
    for i in range(3):
        for j in range(2):
            assert X[i,j]==1.
#---------------------------------------------------
def test_mat_sum():
    ''' (3 points) mat_sum'''
    X= all_one_matrix(3,2)
    s = mat_sum(X)
    assert type(s) == np.ndarray
    assert s.shape == (2,)
    assert s[0]==3.
    assert s[1]==3.
#---------------------------------------------------
def test_mat_scalar_multiplication():
    ''' (3 points) mat_scalar_multiplication'''
    X= ndarray()
    Y =  mat_scalar_multiplication(X, 2.)
    assert type(Y) == np.ndarray
    assert Y.shape == (2,3)
    assert Y[0,0]==2.
    assert Y[0,1]==4.
    assert Y[0,-1]==6.
    assert Y[1,0]==8.
#---------------------------------------------------
def test_matrix_vector_multiplication():
    ''' (3 points) matrix_vector_multiplication'''
    X = np.array([[1.,2.],
                  [3.,4.]]) # matrix of shape (2 by 2)
    y = np.array([5., 10.]) # a vector of length 2
    z= matrix_vector_multiplication(X,y) 
    assert type(z) == np.ndarray
    assert z.shape == (2,) # test the shape of the vector 
    z_real = np.array([25., 55.])
    assert np.allclose(z, z_real)
    # test on random matrix
    for _ in range(20):
        m,n = np.random.randint(2,20,size= 2) 
        X = np.random.random((m,n))
        y = np.random.random(n)
        z = matrix_vector_multiplication(X,y)
        i = np.random.randint(m)
        assert np.allclose(z[i],  np.dot(X[i],y))
#---------------------------------------------------
def test_find_zeros():
    ''' (3 points) find_zeros'''
    x= np.array([1,0,4,0])
    d =  find_zeros(x)
    assert type(d) == np.ndarray
    assert d.shape == (2,)
    assert d[0]==1
    assert d[1]==3
#---------------------------------------------------
def test_diag_mat():
    ''' (2 points) diag_mat'''
    x= np.array([1,2,3])
    D =  diag_mat(x)
    assert type(D) == np.ndarray
    assert D.shape == (3,3)
    assert D[0,0]==1
    assert D[1,1]==2
    assert D[2,2]==3
    assert D[0,2]==0
    assert D[2,0]==0
    assert D[1,0]==0
    assert D[0,1]==0

