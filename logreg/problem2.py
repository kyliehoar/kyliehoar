

''' ------------Install *torch* package--------------
    *torch* is a python package for for building deep learning models.
    Please type the following command in your terminal to install the torch package:
    (Windows OS): python -m pip install torch
    (Mac /Linux): python3 -m pip install torch
------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import torch as th
from model import LogisticRegression
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Logistic Regression (with PyTorch) (20 points)
    In this problem, you will re-implement the logistic regression method using PyTorch. Implementing logistic regression in PyTorch is much easier than in NumPy, because we now have many high-level functions/tools to use in PyTorch, which are specially designed for neural networks. In the model.py file, we have already build the network structure of a logistic regression model in PyTorch, now we need to figure out how to train the model parameters using data. We will get familiar with how to compute the loss on a mini-batch of training samples, and use back-propagation to compute the gradients 
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_z (5 points)--------------------
    Goal: (Forward Function 1) Given a logistic regression model (m) defined as in 'model.py', please compute the linear logits z on a mini-batch of data samples x =[x1, x2, ... x_batch_size]. In the mean time, please also connect the global gradient of the linear logits z (dL_dz) with the global gradients of the weights dL_dw and the biases dL_db in the PyTorch tensors. 
    ---- Inputs: --------
    * x: the feature vectors of a mini-batch of data samples, a float torch tensor of shape (batch_size, p), each row x[i] is the feature vector of the i-th data sample in the mini-batch.
    * m: a logistic regression model (a PyTorch nn.Module), which is defined in "model.py" (LogisticRegression class), it includes the weights and bias in the linear layer.
    ---- Outputs: --------
    * z: the linear logits on a mini-batch of data samples, a float torch tensor of shape (batch_size, 1), each row z[i,0] is the linear logit of the i-th data sample in the mini-batch.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_z(x, m):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    z = m(x)
    #########################################
    return z

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_2.py::test_compute_z
    (Mac /Linux): python3 -m pytest -v test_2.py::test_compute_z
---------------------------------------------------------------'''



''' ---------Function: compute_L (5 points)--------------------
    Goal: (Forward Function 2) Suppose we are given a logistic regression model and we have already computed the linear logits z on a mini-batch of training samples. Suppose the labels of the training samples are in y. Please compute the average cross-entropy loss of the logistic regression model on the mini-batch of training samples. In the mean time, please also connect the global gradients of the linear logits z (dL_dz) with the loss L correctly. 
    ---- Inputs: --------
    * z: the linear logits on a mini-batch of data samples, a float torch tensor of shape (batch_size, 1), each row z[i,0] is the linear logit of the i-th data sample in the mini-batch.
    * y: the labels of a mini-batch of data samples, a torch integer vector of length batch_size. y[i,0] is the label of the i-th training sample, which can be 0 or 1.
    ---- Outputs: --------
    * L: the average binary cross entropy loss on a mini-batch of training samples, a torch float scalar.
    ---- Hints: --------
    * We need to use BINARY cross entropy loss instead of regular cross-entropy loss, because regular cross-entropy loss is designed for multi-class classification problem. But in our problem, we only have binary categories: owner vs non-owner. 
    * In order to avoid numerical issues, we need to find a function in PyTorch that combines the sigmoid function and negative log likelihood function together for binary classification. So the input is linear logit (z) instead of activation (a). 
    * The loss L is a scalar, computed from the average of the cross entropy losses on all samples in the mini-batch. For example, if the cross entropy losses on the 3 training samples are 0.1, 0.2, 0.3, then the average loss L is (0.1+0.2+0.3)/3 = 0.2. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_L(z, y):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    loss_fn = th.nn.BCEWithLogitsLoss()
    L = loss_fn(z, y.float())
    #########################################
    return L

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_2.py::test_compute_L
    (Mac /Linux): python3 -m pytest -v test_2.py::test_compute_L
---------------------------------------------------------------'''



''' ---------Function: update_parameters (5 points)--------------------
    Goal: (Gradient Descent) Suppose we are given a logistic regression model with parameters (w and b) and we have a mini-batch of training data samples (x,y).  Suppose we have already computed the global gradients of the average loss L w.r.t. the weights w on the mini-batch of data samples. Assume that we have already created an optimizer for the parameter w and b. Please update the weights w and bias b using gradient descent. After the update, the global gradients of w and b should be set to all zeros. 
    ---- Inputs: --------
    * optimizer: a PyTorch optimizer (such as SGD, ADAM, RMSProp) to handle the gradient descent for parameters in the model (weights and bias).
    ---- Hints: --------
    * Although the parameters w and b are NOT given explicitly in the input of this function, but we can assume the w and b are already properly configured in the optimizer. So the optimizer is configured to handle the parameters w and b. 
    * Although the gradients of the parameters dL_dw and dL_db are NOT given explicitly in the input of this function, but we can assume that in the PyTorch tensors w and b, the gradients are already properly computed and are stored in W.grad (for dL_dw) and b.grad (for dL_db). 
    * Although the learning rate is NOT given explicitly in the input of this function, but we can assume that the optimizer was already configured with the learning rate parameter. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

def update_parameters(optimizer):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    optimizer.step()
    optimizer.zero_grad()
    pass 
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_2.py::test_update_parameters
    (Mac /Linux): python3 -m pytest -v test_2.py::test_update_parameters
---------------------------------------------------------------'''



''' ---------Function: train (5 points)--------------------
    Goal: (Training Logistics Regression) Given a training dataset X (features), Y (labels) in a data loader, train the logistic regression model using mini-batch stochastic gradient descent: iteratively update the weights w and biases b using the gradients on each mini-batch of random data samples.  We repeat n_epoch passes over all the training samples. 
    ---- Inputs: --------
    * data_loader: a PyTorch loader of a dataset, which is use to load a mini-batch of training samples at a time from a large dataset.
    * p: the number of input features.
    * alpha: the step-size parameter of gradient descent, a float scalar.
    * n_epoch: the number of passes to go through the training dataset in the training process, an integer scalar.
    ---- Outputs: --------
    * m: a logistic regression model (a PyTorch nn.Module), which is defined in "model.py" (LogisticRegression class), it includes the weights and bias in the linear layer.
    ---- Hints: --------
    * Step 1 Forward pass: compute the linear logits z and loss L. 
    * Step 2 Back propagation: compute the gradients of w and b. 
    * Step 3 Gradient descent: update the parameters w and b using gradient descent. 
    * This problem can be solved using 3 line(s) of code. More lines are okay. ''' 

def train(data_loader, p, alpha=0.001, n_epoch=100):
    m = LogisticRegression(p) # initialize the model
    optimizer = th.optim.SGD(m.parameters(), lr=alpha) # create an SGD optimizer
    for _ in range(n_epoch): # iterate through the dataset n_epoch times
        for mini_batch in data_loader: # iterate through the dataset, with one mini-batch of random training samples (x,y) at a time
            x=mini_batch[0] # the feature vectors of the data samples in a mini-batch
            y=mini_batch[1] # the labels of the samples in a mini-batch
            #########################################
            ## INSERT YOUR CODE HERE (5 points)
            optimizer.zero_grad()
            z = compute_z(x, m)
            L = compute_L(z, y)
            L.backward()
            update_parameters(optimizer)
            #########################################
    return m

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_2.py::test_train
    (Mac /Linux): python3 -m pytest -v test_2.py::test_train
---------------------------------------------------------------'''




'''-------- TEST problem2.py file: (20 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
    (Windows OS): python -m pytest -v test_2.py
    (Mac /Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* p:  the number of input features. 
* batch_size:  the number of samples in a mini-batch, an integer scalar. 
* x:  the feature vectors of a mini-batch of data samples, a float torch tensor of shape (batch_size, p), each row x[i] is the feature vector of the i-th data sample in the mini-batch. 
* y:  the labels of a mini-batch of data samples, a torch integer vector of length batch_size. y[i,0] is the label of the i-th training sample, which can be 0 or 1. 
* m:  a logistic regression model (a PyTorch nn.Module), which is defined in "model.py" (LogisticRegression class), it includes the weights and bias in the linear layer. 
* z:  the linear logits on a mini-batch of data samples, a float torch tensor of shape (batch_size, 1), each row z[i,0] is the linear logit of the i-th data sample in the mini-batch. 
* L:  the average binary cross entropy loss on a mini-batch of training samples, a torch float scalar. 
* data_loader:  a PyTorch loader of a dataset, which is use to load a mini-batch of training samples at a time from a large dataset. 
* alpha:  the step-size parameter of gradient descent, a float scalar. 
* n_epoch:  the number of passes to go through the training dataset in the training process, an integer scalar. 
* optimizer:  a PyTorch optimizer (such as SGD, ADAM, RMSProp) to handle the gradient descent for parameters in the model (weights and bias). 
--------------------------------------------'''



