
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
# Total Points: 5.0
# ***********  Method: choose_a_move  (Class: RandomPlayer) **************** 
# Total Points: 5.0

total_points = test_function(1, "test_RandomPlayer_choose_a_move_tictactoe", 1.0,total_points)
total_points = test_function(1, "test_RandomPlayer_choose_a_move_othello", 1.5,total_points)
total_points = test_function(1, "test_RandomPlayer_choose_a_move_othello_run_game", 1.5,total_points)
total_points = test_function(1, "test_RandomPlayer_choose_a_move_GO", 1.0,total_points)

# Total Points: 0.0

# Total Points: 30.0
# ***********  Method: expand  (Class: MMNode) **************** 
# Total Points: 6.0

total_points = test_function(1, "test_MMNode_expand_tictactoe", 1.2,total_points)
total_points = test_function(1, "test_MMNode_expand_tictactoe2", 1.2,total_points)
total_points = test_function(1, "test_MMNode_expand_tictactoe3", 1.2,total_points)
total_points = test_function(1, "test_MMNode_expand_othello", 1.2,total_points)
total_points = test_function(1, "test_MMNode_expand_GO", 1.2,total_points)

# ***********  Method: build_tree  (Class: MMNode) **************** 
# Total Points: 9.0

total_points = test_function(1, "test_MMNode_build_tree_tictactoe", 1.8,total_points)
total_points = test_function(1, "test_MMNode_build_tree_tictactoe2", 1.8,total_points)
total_points = test_function(1, "test_MMNode_build_tree_othello", 1.8,total_points)
total_points = test_function(1, "test_MMNode_build_tree_othello2", 1.8,total_points)
total_points = test_function(1, "test_MMNode_build_tree_GO", 1.8,total_points)

# ***********  Method: compute_v  (Class: MMNode) **************** 
# Total Points: 15.0

total_points = test_function(1, "test_MMNode_compute_v_terminal", 3.75,total_points)
total_points = test_function(1, "test_MMNode_compute_v_children", 3.75,total_points)
total_points = test_function(1, "test_MMNode_compute_v_optimal", 3.75,total_points)
total_points = test_function(1, "test_MMNode_compute_v_othello", 3.75,total_points)

# Total Points: 15.0
# ***********  Method: choose_optimal_move  (Class: MiniMaxPlayer) **************** 
# Total Points: 7.5

total_points = test_function(1, "test_MiniMaxPlayer_choose_optimal_move_tictactoe", 3.75,total_points)
total_points = test_function(1, "test_MiniMaxPlayer_choose_optimal_move_othello", 3.75,total_points)

# ***********  Method: choose_a_move  (Class: MiniMaxPlayer) **************** 
# Total Points: 7.5

total_points = test_function(1, "test_MiniMaxPlayer_choose_a_move_tictactoe", 3.75,total_points)
total_points = test_function(1, "test_MiniMaxPlayer_choose_a_move_game", 3.75,total_points)






file_submit.write('problem2.py') 

print('------- Problem 2 (50 points) --------')
# Total Points: 40.0

# ***********  Method: sample  (Class: MCNode) **************** 
# Total Points: 4.0

total_points = test_function(2, "test_MCNode_sample_tictactoe", 2.0,total_points)
total_points = test_function(2, "test_MCNode_sample_terminal", 0.8,total_points)
total_points = test_function(2, "test_MCNode_sample_othello", 1.2,total_points)

# ***********  Method: expand  (Class: MCNode) **************** 
# Total Points: 8.0

total_points = test_function(2, "test_MCNode_expand_tictactoe", 4.0,total_points)
total_points = test_function(2, "test_MCNode_expand_othello", 4.0,total_points)

# ***********  Method: backprop  (Class: MCNode) **************** 
# Total Points: 8.0

total_points = test_function(2, "test_MCNode_backprop_tictactoe", 8.0,total_points)

# ***********  Method: compute_UCB  (Class: MCNode) **************** 
# Total Points: 4.0

total_points = test_function(2, "test_MCNode_compute_UCB_tictactoe", 4.0,total_points)

# ***********  Method: select_a_child  (Class: MCNode) **************** 
# Total Points: 4.0

total_points = test_function(2, "test_MCNode_select_a_child_tictactoe", 4.0,total_points)

# ***********  Method: selection  (Class: MCNode) **************** 
# Total Points: 8.0

total_points = test_function(2, "test_MCNode_selection_root", 1.6,total_points)
total_points = test_function(2, "test_MCNode_selection_onelevelchild", 4.0,total_points)
total_points = test_function(2, "test_MCNode_selection_twolevelchild", 2.4,total_points)

# ***********  Method: build_tree  (Class: MCNode) **************** 
# Total Points: 4.0

total_points = test_function(2, "test_MCNode_build_tree_tictactoe", 4.0,total_points)

# Total Points: 10.0

# ***********  Method: choose_optimal_move  (Class: MCTSPlayer) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_MCTSPlayer_choose_optimal_move_tictactoe", 3.0,total_points)
total_points = test_function(2, "test_MCTSPlayer_choose_optimal_move_othello", 2.0,total_points)

# ***********  Method: choose_a_move  (Class: MCTSPlayer) **************** 
# Total Points: 5.0

total_points = test_function(2, "test_MCTSPlayer_choose_a_move_tictactoe", 2.0,total_points)
total_points = test_function(2, "test_MCTSPlayer_choose_a_move_play_with_AI", 2.0,total_points)
total_points = test_function(2, "test_MCTSPlayer_choose_a_move_othello", 1.0,total_points)



file_submit.close()
print('****************************')
print(f'** Total Points: {round(total_points)} / 100  **')
print('****************************')
print('If you are good with this grade, you could submit the zip file "submission.zip" as your final submission in canvas')

