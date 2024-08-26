from problem4 import *
import sys
import math
import pandas as pd
'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 4 (48 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11

#---------------------------------------------------
def test_count_out_links():
    ''' (5 points) count_out_links'''
    A = np.array([[0, 1, 1],
                  [1, 0, 1],
                  [1, 0, 0]]) # adjacency matrix of shape (3 by 3)
    d= count_out_links(A)
    assert d[0] == 2
    assert d[1] == 1
    assert d[2] == 2
    A = np.array([[0,1,1,1],
                  [1,0,0,0],
                  [1,1,1,1],
                  [1,0,0,1]]) # adjacency matrix of shape (4 by 4)
    d= count_out_links(A)
    assert d[0] == 3
    assert d[1] == 2
    assert d[2] == 2
    assert d[3] == 3
    # test with a random matrix
    for _ in range(20):
        n = np.random.randint(2,20)
        A = np.random.random((n,n))
        A[A>0]=1.
        A[A<0]=0.
        d = count_out_links(A)
        i = np.random.randint(n)
        assert np.allclose(np.sum(A[:,i]),d[i], atol=0.5)
#---------------------------------------------------
def test_remove_sink_nodes():
    ''' (5 points) remove_sink_nodes'''
    A = np.array( [ [0, 1, 0],
                    [1, 0, 0],
                    [0, 1, 0]]) # adjacency matrix of shape (3 by 3)
    A = remove_sink_nodes(A)
    A_true = [[0, 1, 1],
              [1, 0, 1],
              [0, 1, 1]]
    assert np.allclose(A,A_true)
    A = np.array([[0,0,1,1],
                  [0,0,0,0],
                  [0,0,1,1],
                  [0,0,0,1]]) # adjacency matrix of shape (4 by 4)
    A = remove_sink_nodes(A)
    A_true = [[1,1,1,1],
              [1,1,0,0],
              [1,1,1,1],
              [1,1,0,1]]
    assert np.allclose(A,A_true)
    A = np.array([[0,0,0,0,0],
                  [1,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,1],
                  [0,0,0,0,0]])
    A = remove_sink_nodes(A)
    A_true = [[0,1,1,1,0],
              [1,1,1,1,0],
              [0,1,1,1,0],
              [0,1,1,1,1],
              [0,1,1,1,0]]
    assert np.allclose(A,A_true)
    A = np.loadtxt("data_A.csv",delimiter=",")
    A_ = remove_sink_nodes(A) 
    assert A_.shape == (8,8)
    assert np.allclose(A_[:,4],np.ones(8))
    assert A_[0,1]==1
    assert A_[0,2]==0
    assert A_[5,0]==1
    np.savetxt("data_A_.csv",A_,delimiter=",", fmt="%d")
#---------------------------------------------------
def test_compute_S():
    ''' (5 points) compute_S'''
    A = np.array( [ [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]]) # adjacency matrix of shape (3 by 3)
    S = compute_S(A)
    assert type(S) == np.ndarray
    assert S.shape == (3,3)
    S_real=np.array([[ 0. ,  0.5,  0.333333 ],
                     [ 0.5,  0. ,  0.333333 ],
                     [ 0.5,  0.5,  0.333333 ]] )
    assert np.allclose(S, S_real,atol=1e-3)
    A = np.array( [ [0, 1],
                    [1, 0]])
    S = compute_S(A) 
    assert S.shape == (2,2)
    assert np.allclose(S, A)
    A = np.array([[0, 1],
                  [1, 1]])
    S = compute_S(A) 
    assert S.shape == (2,2)
    S_real = np.array([[0., 0.5],
                       [1., 0.5]])
    assert np.allclose(S, S_real)
    A = np.array( [ [0, 1, 1, 1],
                    [1, 1, 0, 1],
                    [0, 1, 0, 1],
                    [1, 1, 1, 1]])
    S = compute_S(A) 
    assert type(S) == np.ndarray
    assert S.shape == (4,4)
    S_real=np.array([[ 0. ,  0.25,  0.5,  0.25 ],
                     [ 0.5,  0.25,  0. ,  0.25 ],
                     [ 0  ,  0.25,  0. ,  0.25 ],
                     [ 0.5,  0.25,  0.5,  0.25 ]] )
    assert np.allclose(S, S_real)
    A_ = np.loadtxt("data_A_.csv",delimiter=",")
    S = compute_S(A_) 
    assert S.shape == (8,8)
    assert np.allclose(S[:,4],np.ones(8)/8)
    assert S[0,1]==0.5
    assert S[0,2]==0
    assert S[5,0]==0.2
    np.savetxt("data_S.csv",S,delimiter=",", fmt="%.3f")
#---------------------------------------------------
def test_compute_G():
    ''' (6 points) compute_G'''
    S = np.array([[0., .5, 1.],
                  [.5, 0., 0.],
                  [.5, .5, 0.]]) # probability transition matrix of shape (3 by 3) after fixing the sink node problem
    G = compute_G(S, 1.0) 
    assert type(G) == np.ndarray
    assert G.shape == (3,3)
    S_=    np.array([[ 0. ,  0.5,  1. ],
                     [ 0.5,  0. ,  0. ],
                     [ 0.5,  0.5,  0. ]] )
    assert np.allclose(S,S_) # the matrix S should not be changed
    assert np.allclose(G, S) # when a = 1, matrix G is the same as matrix S
    G = compute_G(S, 0.0) 
    G_true=[[.33,.33,.33],
            [.33,.33,.33],
            [.33,.33,.33]]
    assert np.allclose(G, G_true,atol=0.01) # when a = 0, matrix G is a matrix with equal probabilities
    G = compute_G(S, 0.5) 
    G_true=[[0.167,0.417,0.667],
            [0.417,0.167,0.167],
            [0.417,0.417,0.167]]
    assert np.allclose(G, G_true,atol=0.01)
    S = np.array([[0., 1.], # test on another matrix of shape (2 by 2)
                  [1., 0.]])
    G = compute_G(S, 0.5) 
    assert G.shape == (2,2)
    G_true = [[ 0.25, 0.75],
              [ 0.75, 0.25]]
    assert np.allclose(G, G_true)
    S = np.array([[0., .5],
                  [1., .5]])
    G = compute_G(S,0.5) 
    assert G.shape == (2,2)
    G_true= np.array([[0.25, 0.5],
                       [0.75, 0.5]])
    assert np.allclose(G, G_true)
    G = compute_G(S,0.) 
    G_true = np.array([[0.5, 0.5],
                       [0.5, 0.5]])
    assert np.allclose(G, G_true)
    S = np.loadtxt("data_S.csv",delimiter=",")
    G = compute_G(S,0.8) 
    assert G.shape == (8,8)
    assert np.allclose(G[:,4],np.ones(8)/8)
    assert math.isclose(G[0,1],0.425)
    assert math.isclose(G[0,2],0.025)
    assert math.isclose(G[4,0],0.185)
    np.savetxt("data_G.csv",G,delimiter=",", fmt="%.3f")
#---------------------------------------------------
def test_random_walk_one_step():
    ''' (6 points) random_walk_one_step'''
    G = np.array([[ 0. ,  0.5,  1. ],
                  [ 0.5,  0. ,  0. ],
                  [ 0.5,  0.5,  0. ]]) # transition matrix of shape (3 by 3)
    x =  np.ones(3)/3
    x = random_walk_one_step(G, x)
    assert type(x) == np.ndarray
    assert len(x)== 3
    x_real=np.array([1.5, 0.5, 1.0])/3
    assert np.allclose(x_real, x)
    x = np.array([0,1,0]) # another initial score
    x= random_walk_one_step(G, x)
    x_real=np.array([0.5, 0.,0.5])
    assert np.allclose(x_real, x)
    x = np.array([1,0,0]) # another initial score
    x= random_walk_one_step(G, x)
    x_real=np.array([0., 0.5,0.5])
    assert np.allclose(x_real, x)
    G = np.array([[ 0.1,  0.4], # test with another matrix
                  [ 0.9,  0.6]]) # probability transition matrix of shape (2 by 2)
    x = np.array([0.5,0.5])
    x= random_walk_one_step(G, x)
    assert len(x)== 2
    x_real=np.array([0.25, 0.75])
    assert np.allclose(x_real, x)
    x = np.array([1,0]) # another initial score
    x= random_walk_one_step(G, x)
    x_real=np.array([0.1, 0.9])
    assert np.allclose(x_real, x)
#---------------------------------------------------
def test_all_close():
    ''' (5 points) all_close'''
    x = np.array([0.1,0.5,1.8,100.9])
    y = np.array([0.2,0.4,1.85,100.94])
    assert all_close(x,y,tol=0.1)
    y = np.array([0.2,0.4,1.85,100.7])
    assert not all_close(x,y,tol=0.1)
#---------------------------------------------------
def test_random_walk():
    ''' (6 points) random_walk'''
    G = np.array([[ 0. ,  0.5,  1. ],
                  [ 0.5,  0. ,  0. ],
                  [ 0.5,  0.5,  0. ]] ) # a transition matrix of shape (3 by 3)
    x_0 =  np.ones(3)/3
    x = random_walk(G, x_0)
    x_real = np.array([1.33333333, 0.66666667, 1.])/3
    assert np.allclose(x_real, x,atol=1e-2)
    x = random_walk(G, x_0,max_steps=2) # test max_steps
    x_real = np.array([1.25, 0.75, 1.])/3
    assert np.allclose(x_real, x)
    G = np.array([[ 0.5,  0.5],
                  [ 0.5,  0.5]]) # another transition matrix of shape (2 by 2)
    x_0 =  np.array([1,0])
    x = random_walk(G, x_0)
    assert type(x) == np.ndarray
    assert len(x)== 2
    x_real=np.array([.5, .5] )
    assert np.allclose(x_real, x,atol=1e-2)
    G = np.loadtxt("data_G.csv",delimiter=",")
    x = random_walk(G,np.ones(8)/8) 
    assert len(x) == 8
    assert np.allclose(x,[0.04268,0.03536,0.0353,0.2745,0.0353,0.1612,0.15824,0.2571],atol=0.02)
    np.savetxt("data_x.csv",x, delimiter=",", fmt="%.3f")
#---------------------------------------------------
def test_add_column_pagerank():
    ''' (5 points) add_column_pagerank'''
    X2 = pd.read_csv("data_X2.csv")
    x = np.loadtxt("data_x.csv", delimiter=",")
    X3 = add_column_pagerank(X2,x)
    assert type(X3) == pd.DataFrame
    assert X3.shape == (8, 7)
    assert X3.iloc[3].PageRank>0.25 
    assert X3.iloc[-1].PageRank>0.23 
    assert X3.iloc[-2].PageRank< 0.2 
    assert X3.iloc[-3].PageRank< 0.2 
    # Now lets save the result into a CSV file, for further analysis
    X3.to_csv("data_X3.csv", index=False)
#---------------------------------------------------
def test_rank_pages():
    ''' (5 points) rank_pages'''
    X3 = pd.read_csv('data_X3.csv')
    R = rank_pages(X3)
    assert R.iloc[0].ID == 3
    assert R.iloc[1].ID == 7
    # Now lets save the result into a CSV file, for your review
    R.to_csv("data_R3.csv", index=False)

