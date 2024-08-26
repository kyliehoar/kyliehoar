
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
import numpy as np
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
    Goal of Problem 1: Logistic Regression (with NumPy) (60 points)
    In this problem, we will implement the logistic regression method for binary classification problems using NumPy.
We will get familiar with gradient computation using the chain rule. 
We will use binary cross entropy as the loss function and stochastic gradient descent to train the model parameters.
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_z (5 points)--------------------
    Goal: (Value Forward Function 1) Given a logistic regression model with parameters w and b, compute the linear logit value on a data sample x. 
    ---- Inputs: --------
    * x: the feature vector of a data sample, a float numpy vector of length p.
    * w: the weights parameter of the logistic model, a float numpy vector of length p.
    * b: the bias value of the logistic model, a float scalar.
    ---- Outputs: --------
    * z: the logit value of the instance, a float scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_z(x, w, b):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    z = np.dot(w, x) + b
    #########################################
    return z

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_z
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_z
---------------------------------------------------------------'''



''' ---------Function: compute_dz_db (5 points)--------------------
    Goal: (Local Gradient 1.1) Suppose we are given a logistic regression model with parameters w and b. Suppose we have already computed the linear logit z(x) on a training sample x. Please compute the gradient of the linear logit z(x) with w.r.t. the bias b. 
    ---- Outputs: --------
    * dz_db: the partial gradient of logit z w.r.t. the bias b, a float scalar. It represents (d_z / d_b).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_dz_db():
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    dz_db = 1
    #########################################
    return dz_db

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_dz_db
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_dz_db
---------------------------------------------------------------'''



''' ---------Function: compute_dz_dw (5 points)--------------------
    Goal: (Local Gradient 1.2) Suppose we are given a logistic regression model with parameters w and b. Suppose we have already computed the linear logit z(x) on a training sample x. Please compute the partial gradients of the linear logit z(x)  w.r.t. the weights w. Here 'w.r.t.' represents 'with respect to'. 
    ---- Inputs: --------
    * x: the feature vector of a data sample, a float numpy vector of length p.
    ---- Outputs: --------
    * dz_dw: the partial gradients of the logit z w.r.t. the weights w, a numpy float matrix of shape (p by 1). It represents (d_z / d_w). The i-th element represents ( d_z / d_w[i]).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_dz_dw(x):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    dz_dw = x
    #########################################
    return dz_dw

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_dz_dw
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_dz_dw
---------------------------------------------------------------'''



''' ---------Function: compute_L (5 points)--------------------
    Goal: (Value Forward Function 2) Suppose we are given a logistic regression model and we have already computed the linear logit z(x) on a training sample x. Suppose the label of the training sample is y. Please compute the loss function of the logistic regression model on the training sample. 
    ---- Inputs: --------
    * z: the logit value of the instance, a float scalar.
    * y: the label of a data sample, an integer scalar value. The values can be 0 or 1.
    ---- Outputs: --------
    * L: the cross entropy loss value, a float scalar.
    ---- Hints: --------
    * You could use np.log(x) to compute the natural log of x. 
    * You could use np.exp(x) to compute the exponential of x. 
    * When computing exp(z), you need to be careful about an overflowing case. When the z is a large number (say 1000),  the computer can no longer store the result in a floating-point number. In this case, we may want to avoid computing exp(z) and assign the final result of L(x) directly. When z is very large (say 1000), 1+exp(z) will be very close to exp(z), so we can simplify the equation "log(1+exp(z))-yz" into   "log (exp(z)) - yz". Here log() and exp() cancel out, so we only have "z-yz" left, which is "z(1-y)". 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_L(z, y):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    # L = np.logaddexp(z,0)-y*z
    if z >= 1000:
        L = z*(1-y)
    else:
        L = np.log(1 + np.exp(z)) -y*z
    #########################################
    return L

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_L
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_L
---------------------------------------------------------------'''



''' ---------Function: compute_dL_dz (5 points)--------------------
    Goal: (Local Gradient 2) Suppose we are given a logistic regression model and we have already computed the logits z(x) on a training sample x. Suppose the label of the training sample is y. Please compute the gradient of the loss function (L) w.r.t. the linear logit (z) . 
    ---- Inputs: --------
    * z: the logit value of the instance, a float scalar.
    * y: the label of a data sample, an integer scalar value. The values can be 0 or 1.
    ---- Outputs: --------
    * dL_dz: the partial gradient of the loss function L w.r.t. the linear logit z, a float scalar value. It represents (d_L / d_z).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_dL_dz(z, y):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    if z < 1000:
        dL_dz = np.exp(z)/(1+np.exp(z)) - y
    else:
        dL_dz = 1-y
    #########################################
    return dL_dz

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_dL_dz
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_dL_dz
---------------------------------------------------------------'''



''' ---------Function: compute_dL_db (5 points)--------------------
    Goal: (Global Gradient 1) Suppose we are given a logistic regression model with parameters (w and b) and we have a training data sample (x,y).  Suppose we have already computed the local gradients on the data sample. Please compute the global gradient of the loss L w.r.t. bias parameter b using chain rule. 
    ---- Inputs: --------
    * dL_dz: the partial gradient of the loss function L w.r.t. the linear logit z, a float scalar value. It represents (d_L / d_z).
    * dz_db: the partial gradient of logit z w.r.t. the bias b, a float scalar. It represents (d_z / d_b).
    ---- Outputs: --------
    * dL_db: the partial gradient of the loss function L w.r.t. the bias b, a float scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_dL_db(dL_dz, dz_db):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    dL_db = dL_dz * dz_db
    #########################################
    return dL_db

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_dL_db
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_dL_db
---------------------------------------------------------------'''



''' ---------Function: compute_dL_dw (5 points)--------------------
    Goal: (Global Gradient 2) Suppose we are given a logistic regression model with parameters (w and b) and we have a training data sample (x,y).  Suppose we have already computed the local gradients on the data sample. Please compute the global gradient of the loss function L w.r.t. the weight parameters w using chain rule. 
    ---- Inputs: --------
    * dL_dz: the partial gradient of the loss function L w.r.t. the linear logit z, a float scalar value. It represents (d_L / d_z).
    * dz_dw: the partial gradients of the logit z w.r.t. the weights w, a numpy float matrix of shape (p by 1). It represents (d_z / d_w). The i-th element represents ( d_z / d_w[i]).
    ---- Outputs: --------
    * dL_dw: the partial gradient of the loss function L w.r.t. the weight vector w, a numpy float vector of length p.  The i-th element represents ( d_L / d_w[i]).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_dL_dw(dL_dz, dz_dw):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    dL_dw = dL_dz * dz_dw
    #########################################
    return dL_dw

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_compute_dL_dw
    (Mac /Linux): python3 -m pytest -v test_1.py::test_compute_dL_dw
---------------------------------------------------------------'''



''' ---------Function: backward (5 points)--------------------
    Goal: (Back Propagation) Suppose we are given a logistic regression model with parameters (w and b) and we have a training data sample (x) with label (y).  Suppose we have already computed the activation a(x) on the data sample in the forward-pass. Please compute the global gradients of the loss w.r.t. the parameters w and b on the data sample using back propagation. 
    ---- Inputs: --------
    * x: the feature vector of a data sample, a float numpy vector of length p.
    * y: the label of a data sample, an integer scalar value. The values can be 0 or 1.
    * z: the logit value of the instance, a float scalar.
    ---- Outputs: --------
    * dL_dw: the partial gradient of the loss function L w.r.t. the weight vector w, a numpy float vector of length p.  The i-th element represents ( d_L / d_w[i]).
    * dL_db: the partial gradient of the loss function L w.r.t. the bias b, a float scalar.
    ---- Hints: --------
    * Step 1: compute all the local gradients using the functions above. 
    * Step 2: use the local gradients to build global gradients for the parameters w and b. 
    * This problem can be solved using 4 line(s) of code. More lines are okay. ''' 

def backward(x, y, z):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    dL_dz = compute_dL_dz(z, y)
    dz_dw = compute_dz_dw(x)
    dL_dw = compute_dL_dw(dL_dz, dz_dw)
    dL_db = compute_dL_db(dL_dz, compute_dz_db())
    #########################################
    return dL_dw, dL_db

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_backward
    (Mac /Linux): python3 -m pytest -v test_1.py::test_backward
---------------------------------------------------------------'''



''' ---------Function: update_b (5 points)--------------------
    Goal: (Gradient Descent 1) Suppose we are given a logistic regression model with parameters (w and b) and we have a training data sample (x,y).  Suppose we have already computed the gradient of the loss w.r.t. the bias b on the data sample. Please update the bias parameter b using gradient descent. 
    ---- Inputs: --------
    * b: the bias value of the logistic model, a float scalar.
    * dL_db: the partial gradient of the loss function L w.r.t. the bias b, a float scalar.
    * alpha: the step-size parameter of gradient descent, a float scalar.
    ---- Outputs: --------
    * b: the bias value of the logistic model, a float scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def update_b(b, dL_db, alpha=0.001):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    b -= alpha * dL_db
    #########################################
    return b

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_update_b
    (Mac /Linux): python3 -m pytest -v test_1.py::test_update_b
---------------------------------------------------------------'''



''' ---------Function: update_w (5 points)--------------------
    Goal: (Gradient Descent 2) Suppose we are given a logistic regression model with parameters (w and b) and we have a training data sample (x,y).  Suppose we have already computed the partial gradients of the loss w.r.t. the parameters w on the data sample. Please update the weight parameter w using gradient descent. 
    ---- Inputs: --------
    * w: the weights parameter of the logistic model, a float numpy vector of length p.
    * dL_dw: the partial gradient of the loss function L w.r.t. the weight vector w, a numpy float vector of length p.  The i-th element represents ( d_L / d_w[i]).
    * alpha: the step-size parameter of gradient descent, a float scalar.
    ---- Outputs: --------
    * w: the weights parameter of the logistic model, a float numpy vector of length p.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def update_w(w, dL_dw, alpha=0.001):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    w -= alpha * dL_dw
    #########################################
    return w

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_update_w
    (Mac /Linux): python3 -m pytest -v test_1.py::test_update_w
---------------------------------------------------------------'''



''' ---------Function: train (5 points)--------------------
    Goal: (Training Logistic Regression) Given a training dataset X (features), Y (labels), train the logistic regression model using stochastic gradient descent: iteratively update the weights w and bias b using the gradients on each random data sample.  We repeat n_epoch passes over all the training instances. 
    ---- Inputs: --------
    * X: the feature matrix of training instances, a float numpy matrix of shape (n by p).
    * Y: the labels of training instance, a numpy integer vector of length n. The values can be 0 or 1.
    * alpha: the step-size parameter of gradient descent, a float scalar.
    * n_epoch: the number of passes to go through the training dataset in the training process, an integer scalar.
    ---- Outputs: --------
    * w: the weights parameter of the logistic model, a float numpy vector of length p.
    * b: the bias value of the logistic model, a float scalar.
    ---- Hints: --------
    * Step 1 compute the linear logit. 
    * Step 2 Back propagation: compute the gradients of w and b. 
    * Step 3 Gradient descent: update the parameters w and b using gradient descent. 
    * This problem can be solved using 4 line(s) of code. More lines are okay. ''' 

def train(X, Y, alpha=0.001, n_epoch=100):
    n,p = X.shape # n: the number training samples, p: the number of input features
    w, b = np.random.randn(p), 0. # initialize w randomly and b as 0
    for _ in range(n_epoch): # iterate through the dataset n_epoch times
        indices = np.random.permutation(n) # shuffle the indices of all samples
        for i in indices: # iterate through each random training sample (x,y)
            x=X[i] # the feature vector of the i-th random sample
            y=Y[i] # the label of the i-th random sample
            #########################################
            ## INSERT YOUR CODE HERE (5 points)
            z = compute_z(x, w, b)
            dL_dw, dL_db = backward(x, y, z)
            b = update_b(b, dL_db, alpha=alpha)
            w = update_w(w, dL_dw, alpha=alpha)
            #########################################
    return w, b

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_train
    (Mac /Linux): python3 -m pytest -v test_1.py::test_train
---------------------------------------------------------------'''



''' ---------Function: predict (5 points)--------------------
    Goal: (Using Logistic Regression) Given a trained logistic regression model with parameters w and b. Suppose we have a test sample x. Please use the logistic regression model to predict the label of x and the probability of the label of x being positive, i.e. the activation a(x). 
    ---- Inputs: --------
    * x: the feature vector of a data sample, a float numpy vector of length p.
    * w: the weights parameter of the logistic model, a float numpy vector of length p.
    * b: the bias value of the logistic model, a float scalar.
    ---- Outputs: --------
    * y: the label of a data sample, an integer scalar value. The values can be 0 or 1.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def predict(x, w, b):
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    # z = compute_z(x, w, b)
    sig = (1 / (1 + np.exp(-(np.dot(w, x) + b))))
    if sig >= 0.5:
        y = 1
    else:
        y = 0
    #########################################
    return y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
    (Windows OS): python -m pytest -v test_1.py::test_predict
    (Mac /Linux): python3 -m pytest -v test_1.py::test_predict
---------------------------------------------------------------'''




'''-------- TEST problem1.py file: (60 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
    (Windows OS): python -m pytest -v test_1.py
    (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* p:  the number of input features. 
* x:  the feature vector of a data sample, a float numpy vector of length p. 
* y:  the label of a data sample, an integer scalar value. The values can be 0 or 1. 
* w:  the weights parameter of the logistic model, a float numpy vector of length p. 
* b:  the bias value of the logistic model, a float scalar. 
* z:  the logit value of the instance, a float scalar. 
* a:  the activation value, a float scalar. 
* L:  the cross entropy loss value, a float scalar. 
* dL_dz:  the partial gradient of the loss function L w.r.t. the linear logit z, a float scalar value. It represents (d_L / d_z). 
* dz_dw:  the partial gradients of the logit z w.r.t. the weights w, a numpy float matrix of shape (p by 1). It represents (d_z / d_w). The i-th element represents ( d_z / d_w[i]). 
* dz_db:  the partial gradient of logit z w.r.t. the bias b, a float scalar. It represents (d_z / d_b). 
* dL_dw:  the partial gradient of the loss function L w.r.t. the weight vector w, a numpy float vector of length p.  The i-th element represents ( d_L / d_w[i]). 
* dL_db:  the partial gradient of the loss function L w.r.t. the bias b, a float scalar. 
* alpha:  the step-size parameter of gradient descent, a float scalar. 
* n_epoch:  the number of passes to go through the training dataset in the training process, an integer scalar. 
* n:  the number of data instance in the training set. 
* n_test:  the number of data instance in the test set. 
* X:  the feature matrix of training instances, a float numpy matrix of shape (n by p). 
* Y:  the labels of training instance, a numpy integer vector of length n. The values can be 0 or 1. 
* Ytest:  the predicted labels of test data samples, an integer numpy array of length ntest. Ytest[i] represents the predicted label on the i-th test sample. 
* P:  the predicted probabilities of test data samples to have positive labels, a float numpy vector of length n_test.  P[i] is a value is between 0 and 1, indicating the probability of the i-th data sample to have positive label. 
--------------------------------------------'''



