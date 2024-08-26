
'''------------Turn on Word Wrap Setting in Your Editor--------------
    NOTE: For better readability of the instructions, 
          please turn on the 'Word Wrap' setting in your editor. 
    HOW: For example, in the VS Code editor, click "Settings" in the menu, 
         then type "word wrap" in the search box of the settings, 
    choose "on" in the drop-down menu.
    TEST: If you can read this long sentence without scrolling your screen from left to right, it means that your editor's word wrap setting is on and you are good to go. 
------------------------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import torch as th
from torch import nn
import torch.nn.functional as F
#---------------------------------------------------------

#--------------------------
def Terms_and_Conditions():
    ''' 
      By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically copied your solution from your desktop computer to your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework and building your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other students about this homework, only discuss high-level ideas or use pseudo-code. Don't discuss about the solution at the code level. For example, two students discuss about the solution of a function (which needs 5 lines of code to solve) and they then work on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences (variable names are different). In this case, the two students violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Note: We may use the Stanford Moss system to check your code for code similarity. https://theory.stanford.edu/~aiken/moss/
      Historical Data: In one year, we ended up finding 25% of the students in that class violating one of the above terms and we handled ALL of these violations according to the WPI Academic Honesty Policy. 
    '''
    #*******************************************
    # CHANGE HERE: if you have read and agree with the term above, change "False" to "True".
    Read_and_Agree = True
    #*******************************************
    return Read_and_Agree
#--------------------------

# ---------------------------------------------------------
'''
    Goal of Problem 1: Recurrent Neural Network for Binary Time Sequence Classification (50 points)
    In this problem, you will implement the recurrent neural network for binary sequence classification problems.  Here we assume that each time sequence is assigned with one binary label.  For example, in audio classification, each time sequence is a short clip of audio recording, and the label of the sequence is either 0 (non-wake word) or 1 (wake word).  The goal of this problem is to learn the details of recurrent neural network by building RNN from scratch.  The structure of the RNN includes one recurrent layer repeating itself for l time steps and a fully-connected layer attached to the last time step of the recurrent layer to predict the label of a time sequence.  (Recurrent layer for time step 1)-> (Recurrent layer for time step 2) -> ...(Recurrent layer for time step t) -> (Fully connected layer) -> predicted label..
    
'''
# ---------------------------------------------------------

'''------------- Class: RNN (50.0 points) -------
    Build a reccurent neural network layer that can perform binary sequence classification 
'''

class RNN(nn.Module):
    #------------- Method: __init__  ------
    ''' Goal:     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * p: the dimension of input features for each time step of a time sequence, an integer scalar.
    * h: the number of neurons in the hidden states (or the activations of the recurrent layer), an integer scalar.
    * lr: the learning rate parameter of gradient descent, a float scalar.
    '''
    def __init__(self, p, h, lr=0.001):
        self.U = th.randn(p,h, requires_grad=True)
        self.V = th.randn(h,h, requires_grad=True)
        self.b_h = th.zeros(h, requires_grad=True)
        self.W = th.randn(h, requires_grad=True)
        self.b = th.zeros(1, requires_grad=True)
        self.optimizer = th.optim.SGD([self.U,self.V,self.b_h,self.W,self.b], lr=lr) # SGD optimizer
        
        
    #----------------------------------------------------------
    
    #------------- Method: compute_zt  ------
    ''' Goal: (Recurrent Layer: Linear Logits) Given a recurrent neural network layer with parameters weights U, V and biases b_h. We have a mini-batch of data samples xt at the t-th time step. Suppose we have already computed the hidden states h_(t-1) at the previous time step (t-1). Please compute the linear logits zt in the recurrent layer at the t-th time step on a mini-batch of data samples.    '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * xt: a mini-batch of time sequences at the t-th time step, a float torch tensor of shape (n, p). xt[k] represents the k-th time sequence in the mini-batch at the t-th time step.
    * ht_1: the hidden states (i.e., the activations of the recurrent layer) at the end of the (t-1)th time step, a float torch tensor of shape (n, h).
    ---- Outputs: --------
    * zt: the linear logits of the recurrent layer at the t-th time step on a mini-batch of time sequences,  a float torch tensor of shape (n, h).
    ---- Hints: --------
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def compute_zt(self, xt, ht_1):
        ##############################
        ## INSERT YOUR CODE HERE (7.5 points)
        zt = th.mm(xt, self.U) + th.mm(ht_1, self.V) + self.b_h
        ##############################
        return zt
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_compute_zt
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_compute_zt
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: compute_ht  ------
    ''' Goal: (Recurrent Layer: Tanh Activation) Given the linear logits zt of a recurrent layer at time step t, please use the element-wise hyperbolic tangent function to compute the activations h_(t) (also called hidden states) at time step t. Each element ht[i] is computed as tanh(zt[i]).     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * zt: the linear logits of the recurrent layer at the t-th time step on a mini-batch of time sequences,  a float torch tensor of shape (n, h).
    ---- Outputs: --------
    * ht: the hidden states (i.e., the activations of the recurrent layer) at the end of the t-th time step, a float torch tensor of shape (n, h).
    ---- Hints: --------
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def compute_ht(self, zt):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        ht = th.tanh(zt)
        ##############################
        return ht
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_compute_ht
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_compute_ht
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: step  ------
    ''' Goal: (Recurrent Layer: Step Forward) Given a recurrent neural network with parameters U, V and b_h and we have a mini-batch of data samples x_t at time step t. Suppose we have already computed the hidden state h_(t-1) at the previous time step t-1. Please compute the activations (also called hidden state) h_(t) of the recurrent layer for time step t.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * xt: a mini-batch of time sequences at the t-th time step, a float torch tensor of shape (n, p). xt[k] represents the k-th time sequence in the mini-batch at the t-th time step.
    * ht_1: the hidden states (i.e., the activations of the recurrent layer) at the end of the t-th time step, a float torch tensor of shape (n, h).
    ---- Outputs: --------
    * ht: the hidden states (i.e., the activations of the recurrent layer) at the end of the (t-1)th time step, a float torch tensor of shape (n, h).
    ---- Hints: --------
    * This problem can be solved using only 2 line(s) of code. More lines are okay.'''
    def step(self, xt, ht_1):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        zt = RNN.compute_zt(self, xt, ht_1)
        ht = RNN.compute_ht(self, zt)
        ##############################
        return ht
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_step
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_step
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: compute_z  ------
    ''' Goal: (Fully-Connected Layer: Linear Logit) Given the hidden state h_(t) of the recurrent neural network layer at time step t on a mini-batch of time sequences. Suppose the current time step t is the last time step (t=l) of the time sequences, please compute the linear logit z in the second layer (fully-connected layer) on the mini-batch of time sequences.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * ht: the hidden states (i.e., the activations of the recurrent layer) at the end of the t-th time step, a float torch tensor of shape (n, h).
    ---- Outputs: --------
    * z: the linear logits of the fully connected layer (2nd layer) of RNN on a mini-batch of data samples, a float torch vector of length n.
    ---- Hints: --------
    * Here we are assuming that the classification task is binary classification. So the linear logit z is a scalar on each time sequence in the mini-batch. 
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def compute_z(self, ht):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        z = th.matmul(ht, self.W) + self.b
        ##############################
        return z
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_compute_z
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_compute_z
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: forward  ------
    ''' Goal: (Forward Pass) Given a recurrent neural network with parameters U, V, b_h, W and b, and a mini-batch of time sequences x, where each time sequence has l time steps. Suppose the initial hidden states of the RNN before seeing any data are given as h_(t=0). Please compute the linear logits z of the RNN on the mini-batch of time sequences.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * x: a mini-batch of time sequences, a float torch tensor of shape (n, l, p). x[k,t] represents the k-th time sequence in the mini-batch at the t-th time step. 
    ---- Outputs: --------
    * z: the linear logits of the fully connected layer (2nd layer) of RNN on a mini-batch of data samples, a float torch vector of length n.
    ---- Hints: --------
    * Step 1 Recurrent Layer: apply the recurrent layer to each time step of the time sequences in the mini-batch.. 
    * Step 2 Fully-connected Layer: compute the linear logit z each time sequence in the mini-batch. . 
    * This problem can be solved using only 3 line(s) of code. More lines are okay.'''
    def forward(self, x):
        n,t,p = x.size()
        h = self.W.size(0)
        ht = th.zeros((n, h)) # initialize the hidden states as all zero
        ##############################
        ## INSERT YOUR CODE HERE (7.5 points)
        # ht = th.zeros(x.shape[0], self.b_h)  # Initialize hidden state at t=0
        for t in range(x.shape[1]):
            xt = x[:, t, :]  # Select the input at the current time step
            ht = th.tanh(th.mm(xt, self.U) + th.mm(ht, self.V) + self.b_h)

        # Step 2: Compute the linear logit z for each time sequence in the mini-batch.
        z = th.matmul(ht, self.W) + self.b
        ##############################
        return z
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_forward
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_forward
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: compute_L  ------
    ''' Goal: Given a recurrent neural network and suppose we have already computed the linear logits z in the second layer (fully-connected layer) in the last time step t on a mini-batch of training samples. Suppose the labels of the training samples are in y. Please compute the average binary cross-entropy loss on the mini-batch of training samples.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * z: the linear logits of the fully connected layer (2nd layer) of RNN on a mini-batch of data samples, a float torch vector of length n.
    * y: the binary labels of the time sequences in a mini-batch, a torch integer vector of length n. The value of each element can be 0 or 1.
    ---- Outputs: --------
    * L: the average binary cross entropy loss on a mini-batch of training samples, a torch float scalar.
    ---- Hints: --------
    * In our problem setting, the classification task is assumed to be binary classification (e.g., predicting 'wake word' or not) instead of multi-class classification (e.g., predicting different types of commands). So the loss function should be binary cross entropy loss instead of multi-class cross entropy loss.. 
    * This problem can be solved using only 1 line(s) of code. More lines are okay.'''
    def compute_L(self, z, y):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        L = F.binary_cross_entropy_with_logits(z, y.float(), reduction='mean')
        ##############################
        return L
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_compute_L
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_compute_L
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: update_parameters  ------
    ''' Goal: (Gradient Descent) Suppose we are given a recurrent neural network with parameters (U, V, bh, W and b) and we have a mini-batch of training data samples (x,y).  Suppose we have already computed the global gradients of the average loss L w.r.t. the parameters on the mini-batch of data samples. Assume that we have already created an optimizer for the parameters. Please update the parameter values using gradient descent. After the update, the global gradients of all the parameters should be set to zero.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    '''
    def update_parameters(self):
        self.optimizer.step()
        self.optimizer.zero_grad()
        
        
    #----------------------------------------------------------
    
    #------------- Method: train  ------
    ''' Goal: (Training Recurrent Neural Network) Given a training dataset X (time sequences), Y (labels) in a data loader, train the recurrent neural network using mini-batch stochastic gradient descent: iteratively update the parameters using the gradients on each mini-batch of random data samples.  We repeat n_epoch passes over all the training samples.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * data_loader: the PyTorch loader of a dataset
    * n_epoch: the number of passes to go through the training dataset in the training process, an integer scalar
    ---- Hints: --------
    * Step 1 Forward pass: compute the linear logits in the last layer z and the loss L. 
    * Step 2 Back propagation: compute the gradients of all parameters. 
    * Step 3 Gradient descent: update the parameters using gradient descent. 
    * This problem can be solved using only 4 line(s) of code. More lines are okay.'''
    def train(self, data_loader, n_epoch):
        for _ in range(n_epoch): # iterate through the dataset n_epoch times
            for mini_batch in data_loader: # iterate through the dataset with one mini-batch of random training samples (x,y) at a time
                x=mini_batch[0] # the feature vectors of the data samples in a mini-batch
                y=mini_batch[1] # the labels of the samples in a mini-batch
                ##############################
                ## INSERT YOUR CODE HERE (10.0 points)
                z = RNN.forward(self, x)
                L = RNN.compute_L(self, z, y)
                L.backward()
                self.optimizer.step()
                self.optimizer.zero_grad()
                pass 
                ##############################
        
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_train
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_train
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    
    #------------- Method: predict  ------
    ''' Goal: (Using RNN model)  Given a trained RNN model, suppose we have a mini-batch of test time sequences. Please use the RNN model to predict the labels.     '''
    '''---- Inputs: --------
    * self: a reference to the current instance of the class which is used to access properties of the instance.
    * x: a mini-batch of time sequences, a float torch tensor of shape (n, l, p). x[k,t] represents the k-th time sequence in the mini-batch at the t-th time step.
    ---- Outputs: --------
    * y_predict: the predicted labels of a mini-batch of time sequences, a torch integer vector of length n. y_predict[i] represents the predicted label on the i-th time sequence in the mini-batch. 
    ---- Hints: --------
    * This is a binary classification task. When a linear logit in z is >0, then the label should be predicted as 1, otherwise 0.. 
    * You could use the x>0 in PyTorch to convert a float tensor into a binary/boolean tensor using the element-wise operation (x[i]>0 returns True, otherwise return False).. 
    * You could use the x.int() in PyTorch to convert a boolean tensor into an integer tensor. . 
    * This problem can be solved using only 2 line(s) of code. More lines are okay.'''
    def predict(self, x):
        ##############################
        ## INSERT YOUR CODE HERE (5.0 points)
        z = RNN.forward(self, x)
        y_predict = (z > 0).int()
        ##############################
        return y_predict
        
    '''---------- Test This Method -----------------
    Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_1.py -m RNN_predict
        (Mac /Linux): python3 -m pytest -v test_1.py -m RNN_predict
    ---------------------------------------------------------------'''

    #----------------------------------------------------------
    

'''-------- TEST problem1.py file: (50 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_1.py
        (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''






