from problem1 import *
import sys
import pytest 

import torch as th
from torch.utils.data import Dataset, DataLoader
'''
    Unit test 1  (Total Points: 50)
    This file includes unit tests for problem1.py.
'''

def test_python_version():
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

# ============= Class: RNN ===========================
# Total Points: 50.0

# ***********  Method: compute_zt  (Class: RNN) **************** 
# Total Points: 7.5

# ---- Test Case: value (Method: compute_zt, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 6.0
@pytest.mark.RNN_compute_zt
def test_RNN_compute_zt_value():
    # 2 time sequences of 3 input features at the current time step t 
    # n = 2, p = 3 
    xt = th.tensor([
                   #---------- the first time sequence in the mini-batch at time step t ------
                   [0.2,0.4,0.6],
                   #---------- the second time sequence in the mini-batch at time step t ------
                   [0.3,0.6,0.9],
                    ])
    # hidden states of 2 neurons after the previous step t-1
    # h = 2
    ht_1 = th.tensor([[ 0.5,-0.4],  # the hidden states for the first time sequence in the mini-batch
                      [-0.3, 0.6]], # the hidden states for the second time sequence in the mini-batch
                     requires_grad=True) 
    m = RNN(3,2)
    m.U = th.tensor([[1.,2.],
                     [3.,4.],
                     [5.,6.]],
                     requires_grad=True) 
    m.V = th.tensor([[1.,-2.],
                     [3.,-4.]],
                     requires_grad=True) 
    m.b_h = th.tensor([1.,  # bias for the first hidden state
                      -1.], # bias for the second hidden state
                      requires_grad=True)
    zt = m.compute_zt(xt,ht_1)
    # check if the values are correct
    assert type(zt) == th.Tensor 
    assert zt.size() == th.Size([2,2])
    zt_true= th.tensor([[4.7, 5.2],
                        [9.1, 5.6]])
    assert th.allclose(zt,zt_true, atol = 0.1)
    # check if the gradients are connected correctly
    # create a simple loss function (sum of all elements in z)
    L = zt.sum()
    # back propagation
    L.backward()
    # the gradient for ht_1
    dL_dh_t_1 = th.tensor([[-1., -1.],
                           [-1., -1.]])
    dL_dU = th.tensor([[0.5, 0.5],
                       [1.0, 1.0],
                       [1.5, 1.5]])
    dL_dV = th.tensor([[0.2, 0.2],
                       [0.2, 0.2]])
    assert th.allclose(ht_1.grad, dL_dh_t_1, atol= 0.1)
    assert th.allclose(m.U.grad, dL_dU, atol= 0.1)
    assert th.allclose(m.V.grad, dL_dV, atol= 0.1)
    assert th.allclose(m.b_h.grad, th.tensor([2.,2.]), atol= 0.1)
# --------------------------------

# ---- Test Case: shape (Method: compute_zt, Class: RNN) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.5
@pytest.mark.RNN_compute_zt
def test_RNN_compute_zt_shape():
    # test the function with random input sizes
    h = th.randint(2,10,()) # number of hidden states 
    p = th.randint(2,10,()) # number of input features at each time step 
    n = th.randint(2,10,()) # number of sequences in a mini-batch
    m = RNN(p,h)
    xt  = th.randn(n,p)
    m.U  = th.randn(p,h)
    m.V  = th.randn(h,h)
    m.b_h  = th.randn(h)
    ht_1 = th.randn(n,h)
    zt = m.compute_zt(xt,ht_1)
    assert zt.size(),th.Size([n,h])
# --------------------------------


# ***********  Method: compute_ht  (Class: RNN) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: compute_ht, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 4.0
@pytest.mark.RNN_compute_ht
def test_RNN_compute_ht_value():
    # 2 time sequences in a mini-batch at the current time step t, with 3 hidden states (neurons)
    # n = 2, h = 3 
    m = RNN(4,3)
    zt = th.tensor([
                   #---------- the hidden states for the first time sequence in the mini-batch at time step t ------
                   [0.0, 0.2, 1000.],
                   #---------- the hidden states for the second time sequence in the mini-batch at time step t ------
                   [0.5,-0.2,-1000.],
                    ], requires_grad=True)
    ht = m.compute_ht(zt)
    assert type(ht) == th.Tensor 
    ht_true = th.tensor([[ 0.0000,  0.1974,  1.],
                         [ 0.4621, -0.1974, -1.]])
    assert th.allclose(ht,ht_true,atol=1e-2)
    # check if the gradients are connected correctly
    # create a simple loss function (sum of all elements in h)
    L = ht.sum()
    # back propagation
    L.backward()
    # the gradient for zt
    dL_dz_t = th.tensor([[1.0000, 0.961, 0.],
                         [0.7864, 0.961, 0.]])
    assert th.allclose(zt.grad, dL_dz_t, atol= 0.01)
# --------------------------------

# ---- Test Case: shape (Method: compute_ht, Class: RNN) 
# Goal: Test if the shape of the output tensor is correct
# Points: 1.0
@pytest.mark.RNN_compute_ht
def test_RNN_compute_ht_shape():
    # test the function with random input sizes
    h = th.randint(2,10,()) # number of hidden states 
    n = th.randint(2,10,()) # number of sequences in a mini-batch
    m = RNN(4,h)
    zt = th.randn(n,h)
    ht = m.compute_ht(zt)
    assert ht.size()== th.Size([n,h])
# --------------------------------


# ***********  Method: step  (Class: RNN) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: step, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 4.0
@pytest.mark.RNN_step
def test_RNN_step_value():
    # 2 time sequences of 3 input features at the current time step t 
    # n = 2, p = 3 
    m = RNN(4,3)
    xt = th.tensor([
                   #---------- the first time sequence in the mini-batch at time step t ------
                   [0.2,0.4,0.6],
                   #---------- the second time sequence in the mini-batch at time step t ------
                   [0.3,0.6,0.9],
                    ])
    m.U = th.tensor([[ 0.1,-0.2],
                     [-0.3, 0.4],
                     [ 0.5,-0.6]],
                     requires_grad=True) 
    m.V = th.tensor([[0.1,-0.2],
                     [0.3,-0.4]],
                     requires_grad=True) 
    m.b_h = th.tensor([0.2,-0.2], requires_grad=True)
    # hidden states of 2 neurons after the previous step t-1
    # h = 2
    ht_1 = th.tensor([[ 0.5,-0.4],  # the hidden states for the first time sequence in the mini-batch
                      [-0.3, 0.6]], # the hidden states for the second time sequence in the mini-batch
                     requires_grad=True) 
    ht = m.step(xt,ht_1) 
    # check if the values are correct
    assert type(ht) == th.Tensor 
    assert ht.size() == th.Size([2,2])
    ht_true= th.tensor([[ 0.3185, -0.3627],
                        [ 0.5717, -0.6291]])
    assert th.allclose(ht,ht_true, atol = 0.1)
    # check if the gradients are connected correctly
    # create a simple loss function (sum of all elements in ht)
    L = ht.sum()
    # back propagation
    L.backward()
    # the gradient for ht_1
    dL_dh_t_1 = th.tensor([[-0.0838, -0.0778],
                           [-0.0535, -0.0397]])
    dL_dU = th.tensor([[0.3817, 0.3549],
                       [0.7633, 0.7099],
                       [1.1450, 1.0648]])
    dL_dV = th.tensor([[0.2473, 0.2530],
                       [0.0445, 0.0151]])
    dL_db_h = th.tensor([1.5717, 1.4726])
    assert th.allclose(ht_1.grad, dL_dh_t_1, atol= 0.01)
    assert th.allclose(m.U.grad, dL_dU, atol= 0.01)
    assert th.allclose(m.V.grad, dL_dV, atol= 0.01)
    assert th.allclose(m.b_h.grad, dL_db_h, atol= 0.01)
# --------------------------------

# ---- Test Case: shape (Method: step, Class: RNN) 
# Goal: Test if the shape of the output tensor is correct
# Points: 1.0
@pytest.mark.RNN_step
def test_RNN_step_shape():
    # test the function with random input sizes
    h = th.randint(2,10,()) # number of hidden states 
    p = th.randint(2,10,()) # number of input features at each time step 
    n = th.randint(2,10,()) # number of sequences in a mini-batch
    m = RNN(p,h)
    xt  = th.randn(n,p)
    ht_1 = th.randn(n,h)
    zt = m.compute_zt(xt,ht_1)
    assert zt.size()== th.Size([n,h]) 
# --------------------------------


# ***********  Method: compute_z  (Class: RNN) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: compute_z, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 5.0
@pytest.mark.RNN_compute_z
def test_RNN_compute_z_value():
    # 2 time sequences in a mini-batch at the current time step t, with 3 hidden states (neurons)
    # n = 2, h = 3 
    m = RNN(4,3)
    ht = th.tensor([
                   #---------- the hidden states for the first time sequence in the mini-batch at the last time step t ------
                   [0.0, 0.2, 1.],
                   #---------- the hidden states for the second time sequence in the mini-batch at the last time step t ------
                   [0.5,-0.2,-1.],
                    ], requires_grad=True)
    m.W = th.tensor([1., 2., -3.], requires_grad=True)
    m.b = th.tensor(1., requires_grad=True)
    z = m.compute_z(ht)
    assert type(z) == th.Tensor 
    assert z.size()==th.Size([2])
    assert th.allclose(z,th.tensor([-1.6,  4.1]),atol=1e-2)
    # check if the gradients are connected correctly
    # create a simple loss function (sum of all elements in h)
    L = z.sum()
    # back propagation
    L.backward()
    # the gradient for zt
    dL_dh_t = th.tensor([[ 1.,  2., -3.],
                         [ 1.,  2., -3.]])
    assert th.allclose(ht.grad, dL_dh_t, atol= 0.01)
    # test the function with random input sizes
    h = th.randint(2,10,()) # number of hidden states 
    n = th.randint(2,10,()) # number of sequences in a mini-batch
    m= RNN(4,h)
    ht = th.randn(n,h)
    z = m.compute_z(ht)
    assert z.size()==th.Size((n,))
# --------------------------------


# ***********  Method: forward  (Class: RNN) **************** 
# Total Points: 7.5

# ---- Test Case: value (Method: forward, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 6.0
@pytest.mark.RNN_forward
def test_RNN_forward_value():
    # 2 time sequences of 3 time steps with 2 input features at each time step 
    # n = 2, l=3 p = 2
    x = th.tensor([
                     #---------- the first time sequence in the mini-batch ------
                     [
                       [1.,0.], # the first time step of the time sequence
                       [0.,1.], # the second time step of the time sequence
                       [1.,0.]  # the third time step of the time sequence
                     ],
                     #---------- the second time sequence in the mini-batch ------
                     [
                       [1.,0.], # the first time step of the time sequence
                       [1.,0.], # the second time step of the time sequence
                       [0.,1.]  # the third time step of the time sequence
                     ]
                     #------------------------------------------------------------
                   ])
    m = RNN(4,2)
    #---------------------------
    # Layer 1: Recurrent layer
    #---------------------------
    # 4 hidden states 
    # h = 4 (p=2)
    m.U = th.tensor([[ 2.1, 2.2, 2.3, 2.4],
                     [-1.1,-1.2,-2.3,-2.4]],
                     requires_grad=True) 
    m.V = th.tensor([[0.0,-1.0, 0.0,  0.0],
                     [0.0, 0.0,-1.0,  0.0],
                     [0.0, 0.0, 0.0,  1.0],
                     [0.0, 0.0, 0.0,  0.0]],
                     requires_grad=True) 
    m.b_h = th.tensor([-0.1,0.1,-0.1,0.1], requires_grad=True)
    #---------------------------
    # Layer 2: Fully-connected layer
    #---------------------------
    m.W = th.tensor([-1., 1., -1., 1.], requires_grad=True)
    m.b = th.tensor(0., requires_grad=True)
    z = m.forward(x)
    assert type(z) == th.Tensor 
    assert z.size()==th.Size((2,))
    assert th.allclose(z.data,th.tensor([-0.0587, -0.0352]), atol=1e-2)
    # check if the gradients are connected correctly
    # create a simple loss function (sum of all elements in h)
    L = z.sum()
    # back propagation
    L.backward()
    # the gradient for the parameters
    dL_dW = th.tensor([ 0.1304,  0.0279, -0.0007,  0.0078])
    dL_db = th.tensor(2.)
    dL_dU = th.tensor([[-0.0752,  0.0067,  0.0502,  0.1800],
                       [-0.3073,  0.0629, -0.0049,  0.1941]])
    dL_dV = th.tensor([[-0.2416,  0.0556,  0.0563,  0.0371],
                       [-0.2038,  0.0488,  0.0588, -0.0052],
                       [-0.1922,  0.0467,  0.0589, -0.0166],
                       [-0.2497,  0.0576,  0.0577,  0.0375]])
    dL_dbh = th.tensor([-0.3825,  0.0695,  0.0453,  0.3740])
    assert th.allclose(m.W.grad, dL_dW, atol= 0.01)
    assert th.allclose(m.b.grad, dL_db, atol= 0.01)
    assert th.allclose(m.U.grad, dL_dU, atol= 0.01)
    assert th.allclose(m.V.grad, dL_dV, atol= 0.01)
    assert th.allclose(m.b_h.grad, dL_dbh, atol= 0.01)
# --------------------------------

# ---- Test Case: shape (Method: forward, Class: RNN) 
# Goal: Test if the shape of the output tensor is correct
# Points: 1.5
@pytest.mark.RNN_forward
def test_RNN_forward_shape():
    # test the function with random input sizes
    h = th.randint(2,10,()) # number of hidden states 
    l = th.randint(2,10,()) # number of time steps in a sequence 
    p = th.randint(2,10,()) # number of input features at each time step 
    n = th.randint(2,10,()) # number of sequences in a mini-batch
    x  = th.randn(n,l,p)
    m = RNN(p,h)
    z = m.forward(x)
    assert z.size()==th.Size((n,))
# --------------------------------


# ***********  Method: compute_L  (Class: RNN) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: compute_L, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 5.0
@pytest.mark.RNN_compute_L
def test_RNN_compute_L_value():
    # batch_size = 4
    # linear logits in a mini-batch
    m= RNN(2,2)
    z = th.tensor([1.,-1., -1000, 1000.], requires_grad=True) 
    # the labels of the mini-batch: vector of length 4 (batch_size)
    y = th.Tensor([0,1,0,1])
    L = m.compute_L(z,y)
    assert type(L) == th.Tensor 
    assert L.requires_grad
    assert th.isclose(L,th.tensor(0.6566),atol=1e-4) 
    # check if the gradients of z is connected to L correctly
    L.backward() # back propagate gradient to W and b
    dL_dz_true = th.tensor([ 0.1828, -0.1828,  0.,  0.])
    assert th.allclose(z.grad,dL_dz_true, atol=0.01)
    #-----------------------------------------    
    # batch_size = 2
    # linear logits in a mini-batch
    z = th.tensor([-1000., 1000.], requires_grad=True) 
    y = th.Tensor([1,0])
    L = m.compute_L(z,y)
    assert L.data >100
    assert L.data < float('inf')
    L.backward() # back propagate gradient to W and b
    assert z.grad[0]<0
    assert z.grad[1]>0
# --------------------------------



# ***********  Method: train  (Class: RNN) **************** 
# Total Points: 10.0

# ---- Test Case: value (Method: train, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 10.0
@pytest.mark.RNN_train
def test_RNN_train_value():
    # n = 4, l=3, p = 2 
    X  = [
          [ # instance 0
            [0.,0.], # time step 0 
            [0.,0.], # time step 1
            [0.,0.]  # time step 2
          ], 
          [ # instance 1
            [0.,0.], 
            [0.,0.], 
            [0.,1.]
          ],
          [ # instance 2
            [0.,0.], 
            [1.,0.], 
            [0.,0.]
          ],
          [ # instance 3
            [0.,1.], 
            [0.,0.], 
            [0.,0.]
          ] 
         ]
    Y = [0,0,1,1]
    class toy(Dataset):
        def __init__(self):
            self.X  = th.Tensor(X)            
            self.Y = th.Tensor(Y)
        def __len__(self):
            return 4 
        def __getitem__(self, idx):
            return self.X[idx], self.Y[idx]
    d = toy()
    h=32
    n=2
    loader = th.utils.data.DataLoader(d, batch_size = n,shuffle=True)
    m = RNN(2,h)
    m.train(loader,n_epoch=100)
    z = m.forward(th.Tensor(X))
    assert z[0] < z[2]
    assert z[1] < z[2]
    assert z[0] < z[3]
    assert z[1] < z[3]
# --------------------------------


# ***********  Method: predict  (Class: RNN) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: predict, Class: RNN) 
# Goal: Test if values of the output tensor are correct
# Points: 5.0
@pytest.mark.RNN_predict
def test_RNN_predict_value():
    # n = 4, l=3, p = 2 
    X  = [
          [ # instance 0
            [0.,0.], # time step 0 
            [0.,0.], # time step 1
            [0.,0.]  # time step 2
          ], 
          [ # instance 1
            [0.,0.], 
            [0.,0.], 
            [0.,1.]
          ],
          [ # instance 2
            [0.,0.], 
            [1.,0.], 
            [0.,0.]
          ],
          [ # instance 3
            [0.,1.], 
            [0.,0.], 
            [0.,0.]
          ] 
         ]
    Y = [0,0,1,1]
    class toy(Dataset):
        def __init__(self):
            self.X  = th.Tensor(X)            
            self.Y = th.Tensor(Y)
        def __len__(self):
            return 4 
        def __getitem__(self, idx):
            return self.X[idx], self.Y[idx]
    d = toy()
    h=32
    n=2
    m= RNN(2,h)
    loader = th.utils.data.DataLoader(d, batch_size = n,shuffle=True)
    m.train(loader,n_epoch=300)
    y_predict = m.predict(th.Tensor(X))
    assert th.allclose(y_predict, th.tensor(Y).int(),atol=0.1)
# --------------------------------


