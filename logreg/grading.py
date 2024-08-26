
import pytest 
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

print('------- Problem 1 (60 points) --------')
total_points = test_function(1, "test_compute_z", 5,total_points)
total_points = test_function(1, "test_compute_dz_db", 5,total_points)
total_points = test_function(1, "test_compute_dz_dw", 5,total_points)
total_points = test_function(1, "test_compute_L", 5,total_points)
total_points = test_function(1, "test_compute_dL_dz", 5,total_points)
total_points = test_function(1, "test_compute_dL_db", 5,total_points)
total_points = test_function(1, "test_compute_dL_dw", 5,total_points)
total_points = test_function(1, "test_backward", 5,total_points)
total_points = test_function(1, "test_update_b", 5,total_points)
total_points = test_function(1, "test_update_w", 5,total_points)
total_points = test_function(1, "test_train", 5,total_points)
total_points = test_function(1, "test_predict", 5,total_points)




print('------- Problem 2 (20 points) --------')
total_points = test_function(2, "test_compute_z", 5,total_points)
total_points = test_function(2, "test_compute_L", 5,total_points)
total_points = test_function(2, "test_update_parameters", 5,total_points)
total_points = test_function(2, "test_train", 5,total_points)




print('------- Problem 3 (20 points) --------')
total_points = test_function(3, "test_compute_z", 5,total_points)
total_points = test_function(3, "test_compute_L", 5,total_points)
total_points = test_function(3, "test_update_parameters", 5,total_points)
total_points = test_function(3, "test_train", 5,total_points)


print('****************************')
print(f'** Total Points: {total_points} / 100  **')
print('****************************')

