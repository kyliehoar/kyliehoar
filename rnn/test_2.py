from problem2 import *
import sys
import pytest 

import torch as th
from torch import nn
'''
    Unit test 2  (Total Points: 50)
    This file includes unit tests for problem2.py.
'''

def test_python_version():
    assert sys.version_info[0]==3 # require python 3.6 or above 
    assert sys.version_info[1]>=6

# ============= Class: ScaleDotProductScore ===========================
# Total Points: 20.0
# ***********  Method: forward  (Class: ScaleDotProductScore) **************** 
# Total Points: 20.0

# ---- Test Case: shape (Method: forward, Class: ScaleDotProductScore) 
# Goal: Test if shape of the output tensor is correct
# Points: 6.0
@pytest.mark.ScaleDotProductScore_forward
def test_ScaleDotProductScore_forward_shape():
    f = ScaleDotProductScore()
    q = th.randn((2,2,4),requires_grad=True)
    k = th.randn( 2,2,4)
    y = f(q, k)
    assert y.size() == th.Size([2,2,2])
    y.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: forward, Class: ScaleDotProductScore) 
# Goal: Test if values of the output tensor are correct
# Points: 14.0
@pytest.mark.ScaleDotProductScore_forward
def test_ScaleDotProductScore_forward_value():
    f = ScaleDotProductScore()
    # Define query, key, and value tensors (batch_size=2, sequence_length=3, d_model=4)
    query = th.tensor([[[1.0, 2.0, 3.0, 4.0],
                        [2.0, 3.0, 4.0, 5.0],
                        [3.0, 4.0, 5.0, 6.0]],
                       [[-1.0, -2.0, -3.0, -4.0],
                        [-2.0, -3.0, -4.0, -5.0],
                        [-3.0, -4.0, -5.0, -6.0]]])
    key = th.tensor([[[0.1, 0.2, 0.3, 0.4],
                      [0.2, 0.3, 0.4, 0.5],
                      [0.3, 0.4, 0.5, 0.6]],
                     [[-0.1, -0.2, -0.3, -0.4],
                      [-0.2, -0.3, -0.4, -0.5],
                      [-0.3, -0.4, -0.5, -0.6]]])
    y = f(query, key)
    y_true = th.tensor([[[1.5, 2.0, 2.5],
                      [2.0, 2.7, 3.4],
                      [2.5, 3.4, 4.3]],
                     [[1.5, 2.0, 2.5],
                      [2.0, 2.7, 3.4],
                      [2.5, 3.4, 4.3]]])
    assert th.allclose(y,y_true)
    # In this example, we mask out the last position in each sequence.
    mask = th.tensor([[[1, 1, 0], 
                       [1, 1, 0], 
                       [1, 1, 0]],
                      [[1, 1, 0], 
                       [1, 1, 0], 
                       [1, 1, 0]]], dtype=th.bool)
    y = f(query, key,mask=mask)
    assert th.allclose(y[mask],y_true[mask])
    assert th.all(th.isinf(y[~mask]))
# --------------------------------

# ============= Class: SoftMax ===========================
# Total Points: 5.0

# ***********  Method: forward  (Class: SoftMax) **************** 
# Total Points: 5.0

# ---- Test Case: value (Method: forward, Class: SoftMax) 
# Goal: Test if values of the output tensor are correct
# Points: 5.0
@pytest.mark.SoftMax_forward
def test_SoftMax_forward_value():
    f = SoftMax()
    x = th.tensor([ [1.,1.], # batch_size = 3
                    [1.,3.], # feature_dim = 2
                    [-1.,-2.]],requires_grad=True)
    y = f(x)
    assert y.size() == th.Size([3,2])
    print(y)
    assert th.allclose(y,th.tensor([[0.5000, 0.5000],
                                    [0.1192, 0.8808],
                                    [0.7311, 0.2689]]),atol= 0.01)
    y.sum().backward()
    g = SoftMax(dim=-1)
    y = g(x)
    print(y)
    assert th.allclose(y,th.tensor([[0.5000, 0.5000],
                                    [0.1192, 0.8808],
                                    [0.7311, 0.2689]]),atol= 0.01)
    y.sum().backward()
# --------------------------------

# ============= Class: ScaleDotProductAttention ===========================
# Total Points: 10.0

# ***********  Method: forward  (Class: ScaleDotProductAttention) **************** 
# Total Points: 10.0

# ---- Test Case: shape (Method: forward, Class: ScaleDotProductAttention) 
# Goal: Test if shape of the output tensor is correct
# Points: 10.0
@pytest.mark.ScaleDotProductAttention_forward
def test_ScaleDotProductAttention_forward_shape():
    f = ScaleDotProductAttention()
    v = th.randn((3,2,4),requires_grad=True)
    s = th.randn( 3,2,2)
    y = f(s, v)
    assert y.size() == th.Size([3,2,4])
    y.sum().backward()
    fs = ScaleDotProductScore()
    query = th.tensor([[[ 1.0,  2.0,  3.0], 
                        [ 4.0,  5.0,  6.0], 
                        [ 7.0,  8.0,  9.0]],
                       [[-1.0, -2.0, -3.0], 
                        [-4.0, -5.0, -6.0], 
                        [-7.0, -8.0, -9.0]]])
    key = th.tensor([[[ 0.1,  0.2,  0.3], 
                      [ 0.4,  0.5,  0.6], 
                      [ 0.7,  0.8,  0.9]],
                     [[-0.1, -0.2, -0.3], 
                      [-0.4, -0.5, -0.6], 
                      [-0.7, -0.8, -0.9]]])
    value = th.tensor([[[10.0, 20.0, 30.0], 
                        [40.0, 50.0, 60.0], 
                        [70.0, 80.0, 90.0]],
                       [[-10.0, -20.0, -30.0], 
                        [-40.0, -50.0, -60.0], 
                        [-70.0, -80.0, -90.0]]])
    score = fs(query, key)
    print(score)
    fz = ScaleDotProductAttention()
    z = fz(score,value) 
    print(z)
    z_true = th.tensor([[[ 57.7478,  67.7478,  77.7478],
                         [ 67.6251,  77.6251,  87.6251],
                         [ 69.5232,  79.5232,  89.5232]],
                        [[-57.7478, -67.7478, -77.7478],
                         [-67.6251, -77.6251, -87.6251],
                         [-69.5232, -79.5232, -89.5232]]])
    assert th.allclose(z,z_true,atol=0.1)
# --------------------------------

# ============= Class: AttentionHead ===========================
# Total Points: 10.0

# ***********  Method: compute_qkv  (Class: AttentionHead) **************** 
# Total Points: 5.0

# ---- Test Case: shape (Method: compute_qkv, Class: AttentionHead) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.AttentionHead_compute_qkv
def test_AttentionHead_compute_qkv_shape():
    f = AttentionHead(4,2)
    x = th.randn((3,5,4),requires_grad=True)
    q,k,v = f.compute_qkv(x)
    assert q.size() == th.Size([3,5,2])
    assert k.size() == th.Size([3,5,2])
    assert v.size() == th.Size([3,5,2])
    q.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: compute_qkv, Class: AttentionHead) 
# Goal: Test if the values of the output tensor are correct
# Points: 4.0
@pytest.mark.AttentionHead_compute_qkv
def test_AttentionHead_compute_qkv_value():
    f = AttentionHead(4,2)
    # batch_size = 2, sequence_len=3, d_model = 4
    f = AttentionHead(3,2)
    x = th.tensor(
        [
            [
                [1,0,1,0],
                [0,1,0,1],
                [1,1,0,0]
            ],
            [
                [2,0,2,0],
                [0,2,0,2],
                [0,2,2,0]
            ]
        ]
    ).float()
    # d_model = 4, d_head = 2
    f.Wq=th.tensor(
        [
            [1,-1],
            [1,-1],
            [0, 0],
            [0, 0]
        ]
    ).float()
    f.Wk=th.tensor(
        [
            [0, 0],
            [0, 0],
            [1,-1],
            [1,-1]
        ]
    ).float()
    f.Wv=th.tensor(
        [
            [3,-2],
            [0, 0],
            [0, 0],
            [4,-1]
        ]
    ).float()
    q,k,v = f.compute_qkv(x)
    q_true = th.tensor([[[ 1., -1.],
                         [ 1., -1.],
                         [ 2., -2.]],
                        [[ 2., -2.],
                         [ 2., -2.],
                         [ 2., -2.]]])
    assert th.allclose(q,q_true)
    k_true = th.tensor([[[ 1., -1.],
                         [ 1., -1.],
                         [ 0.,  0.]],
                        [[ 2., -2.],
                         [ 2., -2.],
                         [ 2., -2.]]])
    assert th.allclose(k,k_true)
    v_true= th.tensor([[[ 3., -2.],
                        [ 4., -1.],
                        [ 3., -2.]],
                       [[ 6., -4.],
                        [ 8., -2.],
                        [ 0.,  0.]]])
    assert th.allclose(v,v_true)
# --------------------------------


# ***********  Method: forward  (Class: AttentionHead) **************** 
# Total Points: 5.0

# ---- Test Case: shape (Method: forward, Class: AttentionHead) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.AttentionHead_forward
def test_AttentionHead_forward_shape():
    f = AttentionHead(4,2)
    x = th.randn((3,5,4),requires_grad=True)
    z = f(x)
    assert z.size() == th.Size([3,5,2])
    z.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: forward, Class: AttentionHead) 
# Goal: Test if the values of the output tensor are correct
# Points: 4.0
@pytest.mark.AttentionHead_forward
def test_AttentionHead_forward_value():
    # batch_size = 2, sequence_len=3, d_model = 4
    f = AttentionHead(4,2)
    x = th.tensor(
        [
            [
                [1,0,1,0],
                [0,1,0,1],
                [1,1,0,0]
            ],
            [
                [2,0,2,0],
                [0,2,0,2],
                [0,2,2,0]
            ]
        ]
    ).float()
    mask = th.tensor(
        [
            [
                [1,0,0],
                [1,1,0],
                [1,1,1]
            ],
            [
                [1,0,0],
                [1,1,0],
                [1,1,1]
            ]
        ]
    ).bool()
    # d_model = 4, d_head = 2
    f.Wq=th.tensor(
        [
            [1,-1],
            [1,-1],
            [0, 0],
            [0, 0]
        ]
    ).float()
    f.Wk=th.tensor(
        [
            [0, 0],
            [0, 0],
            [1,-1],
            [1,-1]
        ]
    ).float()
    f.Wv=th.tensor(
        [
            [3,-2],
            [0, 0],
            [0, 0],
            [4,-1]
        ]
    ).float()
    z = f(x,mask=mask)
    print(z)
    z_true= th.tensor([[[ 3.0000, -2.0000],
                        [ 3.5000, -1.5000],
                        [ 3.4856, -1.5144]],
                       [[ 6.0000, -4.0000],
                        [ 7.0000, -3.0000],
                        [ 4.6667, -2.0000]]])
    assert th.allclose(z,z_true,atol=0.01)
# --------------------------------

# ============= Class: ResidualLayer ===========================
# Total Points: 5.0

# ***********  Method: forward  (Class: ResidualLayer) **************** 
# Total Points: 5.0

# ---- Test Case: shape (Method: forward, Class: ResidualLayer) 
# Goal: Test if shape of the output tensor is correct
# Points: 5.0
@pytest.mark.ResidualLayer_forward
def test_ResidualLayer_forward_shape():
    f =  nn.Linear(2,2)
    r = ResidualLayer(f)
    x = th.tensor([ [1.,3.], # batch_size = 3
                    [3.,5.], # feature_dim = 2
                    [5.,7.]],requires_grad=True)
    y = r(x)
    fx= f(x)
    assert y.size() == th.Size([3,2])
    assert th.allclose(y, x+fx)
    y.sum().backward()
# --------------------------------


