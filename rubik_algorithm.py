"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program implements a variety of needed algorithms to
    assist with solving the cube.
"""
from rotate_tools import *

def right_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the r/u/r'/u' algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["R", "U", "R'", "U'"]
    run_algorithm(cur_cube, algo_moves)

def short_right_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the r/u/r' algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["R", "U", "R'"]
    run_algorithm(cur_cube, algo_moves)

def left_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the l'/u'/l/u algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["L'", "U'", "L", "U"]
    run_algorithm(cur_cube, algo_moves)

def short_left_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the l'/u'/lalgorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["L'", "U'", "L"]
    run_algorithm(cur_cube, algo_moves)

def white_top_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the f/r/u/r'/f/f algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["F", "R", "U", "R'", "F", "F"]
    run_algorithm(cur_cube, algo_moves)

def left_second_layer(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the u'/l'/u'/l/u/y'/r/u/r' algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["U'", "L'", "U'", "L", "U", "Y'", "R", "U", "R'"]
    run_algorithm(cur_cube, algo_moves)

def right_second_layer(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the u/r/u/r'/u'/y/l'/u'/l algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["U", "R", "U", "R'", "U'", "Y", "L'", "U'", "L"]
    run_algorithm(cur_cube, algo_moves)

def yellow_line_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the f/r/u/r'/u'/f' algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["F", "R", "U", "R'", "U'", "F'"]
    run_algorithm(cur_cube, algo_moves)

def yellow_l_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the f/r/u/r'/u'/r/u/r'/u'/f' algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    algo_moves = ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"]
    run_algorithm(cur_cube, algo_moves)

def final_edge_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the r/u/r'/u/r/u'/u'/r'/u algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    # rotates the cube in r, u, r', u, r, u', u', r', u
    algo_moves = ["R", "U", "R'", "U", "R", "U'", "U'", "R'", "U"]
    run_algorithm(cur_cube, algo_moves)

def final_corner_algorithm(cur_cube):
    '''
    This function rotates the cube 4 times in specific directions
        to create the u/r/u'/l'/u/r'/u'/l algorithm.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    # rotates the cube in u, r, u', l', u, r', u', l
    algo_moves = ["U", "R", "U'", "L'", "U", "R'", "U'", "L"]
    run_algorithm(cur_cube, algo_moves)

def run_algorithm(cur_cube, cube_moves):
    '''
    This function will run all of the moves in a given algorithm and display
        the moves on the GUI.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cube_moves: An array of strings each representing a move in the
            algorithm.
    '''
    for move in cube_moves:
        # checks what move to run
        if move == "U":
            u_rotation(cur_cube, False)
        elif move == "U'":
            u_rotation(cur_cube, True)
        elif move == "R":
            r_rotation(cur_cube, False)
        elif move == "R'":
            r_rotation(cur_cube, True)
        elif move == "F":
            f_rotation(cur_cube, False)
        elif move == "F'":
            f_rotation(cur_cube, True)
        elif move == "B":
            b_rotation(cur_cube, False)
        elif move == "B'":
            b_rotation(cur_cube, True)
        elif move == "L":
            l_rotation(cur_cube, False)
        elif move == "L'":
            l_rotation(cur_cube, True)
        elif move == "D":
            d_rotation(cur_cube, False)
        elif move == "D'":
            d_rotation(cur_cube, True)
        elif move == "X":
            x_rotation(cur_cube, False)
        elif move == "X'":
            x_rotation(cur_cube, True)
        elif move == "Y":
            y_rotation(cur_cube, False)
        elif move == "Y'":
            y_rotation(cur_cube, True)
        elif move == "Z":
            z_rotation(cur_cube, False)
        elif move == "Z'":
            z_rotation(cur_cube, True)
        cur_cube.draw_window(False, (255, 255, 255), move)