
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

print('------- Problem 1 (25 points) --------')
total_points = test_function(1, "test_hello_page", 5,total_points)
total_points = test_function(1, "test_rand_page", 5,total_points)
total_points = test_function(1, "test_vote", 5,total_points)
total_points = test_function(1, "test_create_template", 5,total_points)
total_points = test_function(1, "test_load_template", 5,total_points)




print('------- Problem 2 (20 points) --------')
total_points = test_function(2, "test_sample_pair", 5,total_points)
total_points = test_function(2, "test_facemash", 10,total_points)
total_points = test_function(2, "test_vote", 5,total_points)




print('------- Problem 3 (25 points) --------')
total_points = test_function(3, "test_compute_EA", 5,total_points)
total_points = test_function(3, "test_compute_EB", 5,total_points)
total_points = test_function(3, "test_update_RA", 5,total_points)
total_points = test_function(3, "test_update_RB", 5,total_points)
total_points = test_function(3, "test_compute_ratings", 5,total_points)




print('------- Problem 4 (30 points) --------')
total_points = test_function(4, "test_load_G", 5,total_points)
total_points = test_function(4, "test_load_teams", 5,total_points)
total_points = test_function(4, "test_compute_elo", 10,total_points)
total_points = test_function(4, "test_merge_team", 5,total_points)
total_points = test_function(4, "test_rank_teams_Elo", 5,total_points)


print('****************************')
print(f'** Total Points: {total_points} / 100  **')
print('****************************')

