

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import torch as th
from torch import nn
import torch.nn.functional as F
import math
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Transformer Model (50 points)
    In this problem, you will implement a few key components of the transformer model. Instead of using multi-head attention, in this problem, we focus on building single-head attention layer..
    
'''
# ---------------------------------------------------------

'''------------- Class: ScaleDotProductScore (20.0 points) -------
    Build a neural network layer that can compute scale dot product scores: Give the query vectors and key vectors of a set of words, compute the pairwise similarity scores between word pairs using scaled dot product. These scores can later on be converted into attention scores between word pairs 
'''

class ScaleDotProductScore(nn.Module):
    #------------- Method: forward  ------
    ''' Goal: Give the query vectors and key vectors of a set of words, compute the pairwise similarity scores between word pairs using scaled dot product.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * q: the query vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    * k: the key vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    * mask: the mask tensor for the words in the data, None (which means no mask) or a boolean tensor of shape (batch_size,num_words,num_words). mask[i,j,k] is False if the attention of the jth word in the ith sentence should not have access to the k-th word in the same sentence, so the score for that pair should be set to -inf
    ---- Outputs: --------
    * s: the score of the scale dot product between queries and keys, a tensor of shape (batch_size, num_words, num_words). s[i,j,k] is the score from the j-th word (query) to the k-th word (key) in the i-th sentence of the mini-batch.
    ---- Hints: --------
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def forward(self, q, k, mask=None):
        ##############################
        ## INSERT YOUR CODE HERE (20.0 points)
        d_k = q.size(-1)
        s = th.matmul(q, k.transpose(-2, -1)) / th.sqrt(th.tensor(d_k, dtype=q.dtype))
        if mask is not None:
            s = s.masked_fill(mask == False, float('-inf'))
        ##############################
        return s
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m ScaleDotProductScore_forward
        (Mac /Linux): python3 -m pytest -v test_2.py -m ScaleDotProductScore_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: SoftMax (5.0 points) -------
    Build a neural network layer that can compute along a certain dimension of the input tensor: Give the scale dot product scores, compute the pairwise attention scores between word pairs using softmax 
'''

class SoftMax(nn.Module):
    #------------- Method: __init__  ------
    ''' Goal: Create a softmax layer which will compute the softmax along a certain dimension (dim)    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * dim: the dim parameter specifies along which dimension the softmax operation is applied.
    '''
    def __init__(self, dim=-1):
        super(SoftMax, self).__init__()
        self.dim = dim
        
        
    #----------------------------------------------------------
    
    #------------- Method: forward  ------
    ''' Goal: Give the scale dot product scores, compute the pairwise attention scores between word pairs using softmax.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * s: the raw scores before softmax
    ---- Outputs: --------
    * a: the attention scores, a tensor of the same shape
    ---- Hints: --------
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def forward(self, s):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        a = th.nn.functional.softmax(s, self.dim)
        ##############################
        return a
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m SoftMax_forward
        (Mac /Linux): python3 -m pytest -v test_2.py -m SoftMax_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: ScaleDotProductAttention (10.0 points) -------
    Build a neural network layer that can compute scale dot product attention results: Give the value vectors and the scale dot product scores (before softmax), compute output features (z) for all the words. The output feature of a word is the weighted some of all other similar words in the same sentence. Here the weights are attention scores. 
'''

class ScaleDotProductAttention(nn.Module):
    #------------- Method: __init__  ------
    ''' Goal: Build a neural network layer that can compute scale dot product attention results    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    '''
    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax= SoftMax(dim=-1) # the softmax layer
        
        
    #----------------------------------------------------------
    
    #------------- Method: forward  ------
    ''' Goal: Give the value vectors and the scale dot product scores (before softmax), compute output features (z) for all the words. The output feature of a word is the weighted some of all other similar words in the same sentence. Here the weights are attention scores computed with softmax.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * s: the raw scores before softmax
    * v: the value vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    ---- Outputs: --------
    * z: the output features of the words, a tensor of shape (batch_size, num_words, d_k)
    ---- Hints: --------
    * This problem can be solved using only 2 line(s) of code. More lines are okay.'''
    def forward(self, s, v):
        ##############################
        ## INSERT YOUR CODE HERE (10.0 points)
        a = self.softmax(s)
        z = th.matmul(a, v)
        ##############################
        return z
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m ScaleDotProductAttention_forward
        (Mac /Linux): python3 -m pytest -v test_2.py -m ScaleDotProductAttention_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: AttentionHead (10.0 points) -------
    Build a neural network layer for one attention head: Give the word embeddings, first compute the q,k,v tensors, then use the neural network layers implemented above to compute the result featurs of the attention head 
'''

class AttentionHead(nn.Module):
    #------------- Method: __init__  ------
    ''' Goal: Build a neural network layer for one attention head    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * d_model: the number of dimensions in word embeddings
    * d_k: the number of dimensions of an attention head
    '''
    def __init__(self, d_model, d_k):
        super(AttentionHead,self).__init__()
        self.Wq = th.randn(d_model,d_k)
        self.Wk = th.randn(d_model,d_k)
        self.Wv = th.randn(d_model,d_k)
        self.step1 = ScaleDotProductScore()
        self.step2 = ScaleDotProductAttention()
        
        
    #----------------------------------------------------------
    
    #------------- Method: compute_qkv  ------
    ''' Goal: Give the word embeddings, first compute the q,k,v tensors using the weight matrices Wq, Wk, Wv    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * x: the word embeddings of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_model). Here d_model is the number of dimensions of the word embeddings.
    ---- Outputs: --------
    * q: the query vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    * k: the key vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    * v: the value vectors of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_k). Here d_k is the number of dimensions of an attention head.
    ---- Hints: --------
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def compute_qkv(self, x):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        q = th.matmul(x, self.Wq)
        k = th.matmul(x, self.Wk)
        v = th.matmul(x, self.Wv)
        ##############################
        return q, k, v
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m AttentionHead_compute_qkv
        (Mac /Linux): python3 -m pytest -v test_2.py -m AttentionHead_compute_qkv
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: forward  ------
    ''' Goal: Give the word embeddings, first compute the q,k,v tensors, then use the neural network layers implemented above to compute the result featurs of the attention head    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * x: the word embeddings of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_model). Here d_model is the number of dimensions of the word embeddings.
    * mask: the mask tensor for the words in the data, None (which means no mask) or a boolean tensor of shape (batch_size,num_words,num_words). mask[i,j,k] is False if the attention of the jth word in the ith sentence should not have access to the k-th word in the same sentence, so the score for that pair should be set to -inf
    ---- Outputs: --------
    * z: the output features of the words, a tensor of shape (batch_size, num_words, d_k)
    ---- Hints: --------
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def forward(self, x, mask=None):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        q, k, v = self.compute_qkv(x)
        s = self.step1(q, k, mask)
        z = self.step2(s, v)
        ##############################
        return z
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m AttentionHead_forward
        (Mac /Linux): python3 -m pytest -v test_2.py -m AttentionHead_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
'''------------- Class: ResidualLayer (5.0 points) -------
    Build a neural network layer for residual connection 
'''

class ResidualLayer(nn.Module):
    #------------- Method: __init__  ------
    ''' Goal: Build a neural network layer for residual connection    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * f: the neural network module for f(x) function
    '''
    def __init__(self, f):
        super(ResidualLayer, self).__init__()
        self.f = f # the f(x) function/nn.Module in the residual layer
        
        
    #----------------------------------------------------------
    
    #------------- Method: forward  ------
    ''' Goal: Give a input feature tensor, and the function f(x), compute the residual connection    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * x: the word embeddings of a mini-batch of sentences, a tensor of shape (batch_size, num_words, d_model). Here d_model is the number of dimensions of the word embeddings.
    ---- Outputs: --------
    * y: the new features of the words after residual connection, a tensor of shape (batch_size, num_words, d_model)
    ---- Hints: --------
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def forward(self, x):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        y = x + self.f(x)
        ##############################
        return y
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py -m ResidualLayer_forward
        (Mac /Linux): python3 -m pytest -v test_2.py -m ResidualLayer_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    

'''-------- TEST problem2.py file: (50 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_2.py
        (Mac /Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
        (Windows OS): python -m pytest -v
        (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
        (Windows OS): python grading.py
        (Mac /Linux): python3 grading.py
 The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

 That's all! Great job! You did it!
-------------------------------------------------------------------------'''




