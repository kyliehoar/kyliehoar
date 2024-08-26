
import pytest 
import zipfile 
from pytest import ExitCode

#------------------------------------------
# AutoGrading of HW assignment
# How to run?  In the terminal, type:
#  (Windows OS) python grading.py
#  (Mac OS & Linux) python3 grading.py
#------------------------------------------

def test_function(pid,name, point,total_points):
    result = pytest.main(["--no-header","--tb=no",f"test_{pid}.py::{name}"])
    if result == ExitCode.OK:
        total_points += point
        print(f'*** Pass ({point} pt) --- {name}')
    else:
        print(f'*** Fail (0 / {point} pt) --- {name}')
    return total_points

total_points = 0
file_submit = zipfile.ZipFile('submission.zip','w')


file_submit.write('problem1.py') 

print('------- Problem 1 (50 points) --------')
# Total Points: 50.0

# ***********  Method: compute_zt  (Class: RNN) **************** 
# Total Points: 7.5

total_points = test_function(1, "test_RNN_compute_zt_value", 6.0,total_points)
total_points = test_function(1, "test_RNN_compute_zt_shape", 1.5,total_points)

# ***********  Method: compute_ht  (Class: RNN) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RNN_compute_ht_value", 4.0,total_points)
total_points = test_function(1, "test_RNN_compute_ht_shape", 1.0,total_points)

# ***********  Method: step  (Class: RNN) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RNN_step_value", 4.0,total_points)
total_points = test_function(1, "test_RNN_step_shape", 1.0,total_points)

# ***********  Method: compute_z  (Class: RNN) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RNN_compute_z_value", 5.0,total_points)

# ***********  Method: forward  (Class: RNN) **************** 
# Total Points: 7.5

total_points = test_function(1, "test_RNN_forward_value", 6.0,total_points)
total_points = test_function(1, "test_RNN_forward_shape", 1.5,total_points)

# ***********  Method: compute_L  (Class: RNN) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RNN_compute_L_value", 5.0,total_points)


# ***********  Method: train  (Class: RNN) **************** 
# Total Points: 10.0

total_points = test_function(1, "test_RNN_train_value", 10.0,total_points)

# ***********  Method: predict  (Class: RNN) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RNN_predict_value", 5.0,total_points)






file_submit.write('problem2.py') 

print('------- Problem 2 (50 points) --------')
# Total Points: 20.0
# ***********  Method: forward  (Class: ScaleDotProductScore) **************** 
# Total Points: 20.0

total_points = test_function(2, "test_ScaleDotProductScore_forward_shape", 6.0,total_points)
total_points = test_function(2, "test_ScaleDotProductScore_forward_value", 14.0,total_points)

# Total Points: 5.0

# ***********  Method: forward  (Class: SoftMax) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_SoftMax_forward_value", 5.0,total_points)

# Total Points: 10.0

# ***********  Method: forward  (Class: ScaleDotProductAttention) **************** 
# Total Points: 10.0

total_points = test_function(2, "test_ScaleDotProductAttention_forward_shape", 10.0,total_points)

# Total Points: 10.0

# ***********  Method: compute_qkv  (Class: AttentionHead) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_AttentionHead_compute_qkv_shape", 1.0,total_points)
total_points = test_function(2, "test_AttentionHead_compute_qkv_value", 4.0,total_points)

# ***********  Method: forward  (Class: AttentionHead) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_AttentionHead_forward_shape", 1.0,total_points)
total_points = test_function(2, "test_AttentionHead_forward_value", 4.0,total_points)

# Total Points: 5.0

# ***********  Method: forward  (Class: ResidualLayer) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_ResidualLayer_forward_shape", 5.0,total_points)



file_submit.close()
print('****************************')
print(f'** Total Points: {round(total_points)} / 100  **')
print('****************************')
print('If you are good with this grade, you could submit the zip file "submission.zip" as your final submission in canvas')

