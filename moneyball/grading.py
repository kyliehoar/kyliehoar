
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

print('------- Problem 1 (22 points) --------')
total_points = test_function(1, "test_compute_BA", 3,total_points)
total_points = test_function(1, "test_compute_OBP", 3,total_points)
total_points = test_function(1, "test_compute_B1", 3,total_points)
total_points = test_function(1, "test_compute_TB", 3,total_points)
total_points = test_function(1, "test_compute_SLG", 3,total_points)
total_points = test_function(1, "test_compute_runs", 3,total_points)
total_points = test_function(1, "test_compute_wins", 4,total_points)




print('------- Problem 2 (27 points) --------')
total_points = test_function(2, "test_dataframe", 3,total_points)
total_points = test_function(2, "test_load_csv", 3,total_points)
total_points = test_function(2, "test_save_csv", 3,total_points)
total_points = test_function(2, "test_filter_height", 3,total_points)
total_points = test_function(2, "test_group_sum", 3,total_points)
total_points = test_function(2, "test_merge", 3,total_points)
total_points = test_function(2, "test_sort_values", 3,total_points)
total_points = test_function(2, "test_divide", 3,total_points)
total_points = test_function(2, "test_insert_column", 3,total_points)




print('------- Problem 3 (24 points) --------')
total_points = test_function(3, "test_load_batting", 3,total_points)
total_points = test_function(3, "test_filter_batting", 3,total_points)
total_points = test_function(3, "test_group_batting", 3,total_points)
total_points = test_function(3, "test_merge_player", 3,total_points)
total_points = test_function(3, "test_filter_salary", 3,total_points)
total_points = test_function(3, "test_merge_salary", 3,total_points)
total_points = test_function(3, "test_filter_min_AB", 3,total_points)
total_points = test_function(3, "test_filter_max_salary", 3,total_points)




print('------- Problem 4 (27 points) --------')
total_points = test_function(4, "test_compute_players_BA", 4,total_points)
total_points = test_function(4, "test_rank_players_BA", 3,total_points)
total_points = test_function(4, "test_compute_players_OBP", 4,total_points)
total_points = test_function(4, "test_rank_players_OBP", 3,total_points)
total_points = test_function(4, "test_compute_players_1B", 3,total_points)
total_points = test_function(4, "test_compute_players_TB", 3,total_points)
total_points = test_function(4, "test_compute_players_SLG", 4,total_points)
total_points = test_function(4, "test_rank_players_SLG", 3,total_points)


print('****************************')
print(f'** Total Points: {total_points} / 100  **')
print('****************************')

