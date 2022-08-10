"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program uses the the beginner method to solve any given
    Rubik's cube. This program solves the cube in 7 main steps which are to
    solve the white cross, white corners, second layer, yellow cross, final
    edges final, corner alignment then to rotate the corners to complete the
    solve.
"""
import pygame.time
from solver_tools import *
from rubik_helper import *
from solver_check import *

def correct_face(cur_cube):
    '''
    This will rotate the Rubik's cube so that the white face
        will be at the bottom of the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # gets the needed center colors
    top_color = cur_cube.top.tiles[4].tile_color
    front_color = cur_cube.front.tiles[4].tile_color
    left_color = cur_cube.left.tiles[4].tile_color
    right_color = cur_cube.right.tiles[4].tile_color
    back_color = cur_cube.back.tiles[4].tile_color
    # rotates to the correct face
    rotations = []
    if top_color == (255, 255, 255):
        rotations = ["X'", "X'"]
    if front_color == (255, 255, 255):
        rotations = ["X'"]
    if back_color == (255, 255, 255):
        rotations = ["X"]
    if left_color == (255, 255, 255):
        rotations = ["Z'"]
    if right_color == (255, 255, 255):
        rotations = ["Z"]
    # runs the moves
    run_algorithm(cur_cube, rotations)

def white_cross(cur_cube):
    '''
    This will rotate the Rubik's cube to create a white cross on the white
        face of the cube with the adjacent pieces to each piece of the
        cross being in their correct respective locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # runs until the white cross has been solved
    is_solved = white_cross_solved(cur_cube)
    while not is_solved:
        # checks for pieces in each layer
        all_edges = get_pieces(cur_cube, True)
        for index in range(len(all_edges)):
            cur_pieces = all_edges[index]
            found_piece = find_color_location(cur_pieces, (255, 255, 255))
            if found_piece != False:
                # solves the pieces in the top layers
                if index == 0:
                    solve_white_top(cur_cube, found_piece, "top")
                    break
                if index == 1:
                    solve_white_top(cur_cube, found_piece, "upper")
                    break
                # moves the white pieces into the top layer to be solved
                if index == 2:
                    move_white_up(cur_cube, found_piece, "lower")
                    break
                if index == 3:
                    move_white_up(cur_cube, found_piece, "left")
                    break
                if index == 4:
                    move_white_up(cur_cube, found_piece, "right")
                    break
                if index == 5:
                    # checks if the white cross needs to be fixed
                    white_cross = True
                    for square in cur_pieces:
                        if square.tile_color != (255, 255, 255):
                            white_cross = False
                    if white_cross:
                        fix_white_bottom(cur_cube, True)
                        break
        # checks if the white cross is completed
        is_solved = white_cross_solved(cur_cube)

def white_corners(cur_cube):
    '''
    This will rotate the Rubik's cube to have each piece with a
        white corner in its correct respective location.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # runs until the white cross has been solved
    is_solved = white_corners_solved(cur_cube)
    while not is_solved:
        # checks for pieces in each layer
        all_edges = get_pieces(cur_cube, False)
        for index in range(len(all_edges)):
            cur_pieces = all_edges[index]
            found_piece = find_color_location(cur_pieces, (255, 255, 255))
            if found_piece != False:
                # solves the piece if it is in the upper left or upper right
                if index == 0:
                    solve_upper_location(cur_cube, found_piece, "left")
                    break
                if index == 1:
                    solve_upper_location(cur_cube, found_piece, "right")
                    break
                if index == 2:
                    solve_white_corner_top(cur_cube, found_piece)
                    break
                if index == 3:
                    move_bottom_corner(cur_cube, found_piece, "left")
                    break
                if index == 4:
                    move_bottom_corner(cur_cube, found_piece, "right")
                    break
                if index == 5:
                    # checks if the white cross needs to be fixed
                    white_corners = True
                    for square in cur_pieces:
                        if square.tile_color != (255, 255, 255):
                            white_corners = False
                    if white_corners:
                        fix_white_bottom(cur_cube, False)
                        break
        # checks if the white face is completed
        is_solved = white_corners_solved(cur_cube)

def second_layer(cur_cube):
    '''
    This will primarily run two main algorithms to move the remaining
        corner pieces of the cube to their correct respective locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    is_solved = second_layer_solved(cur_cube)
    while not is_solved:
        needed_pieces = get_pieces(cur_cube, True)
        top_pieces = needed_pieces[0]
        upper_pieces = needed_pieces[1]
        # gets the four top pieces
        front_piece = [upper_pieces[0], top_pieces[3]]
        left_piece = [upper_pieces[1], top_pieces[1]]
        right_piece = [upper_pieces[2], top_pieces[2]]
        back_piece = [upper_pieces[3], top_pieces[0]]
        all_pieces = [front_piece, left_piece, right_piece, back_piece]
        found_piece = find_upper_piece(all_pieces)
        if found_piece != False:
            solve_upper_piece(cur_cube, found_piece)
        is_solved = second_layer_solved(cur_cube)
        if not is_solved and found_piece == False:
            get_upper_piece(cur_cube)

def yellow_cross(cur_cube):
    '''
    This will rotate the Rubik's cube and run one main algorithm to
        correctly get a yellow cross on the top layer of the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    is_solved = True
    cross_squares = face_edges(cur_cube.top)
    cross_colors = []
    # gets the color of each square
    for square in cross_squares:
        square_color = square.tile_color
        cross_colors.append(square_color)
        if square_color != YELLOW:
            is_solved = False
    # solves the yellow cross
    if not is_solved:
        yellow_pattern(cur_cube, cross_colors)


def final_edges(cur_cube):
    '''
    This will move each of the four remaining edge pieces to their correct
        locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    correct_pieces = find_matching_edge(cur_cube)
    while False in correct_pieces:
        # determines how many pieces are correct
        found_pieces = correct_pieces.count(True)
        # rotates cube to find the maximum amount of correct pieces
        while found_pieces < 2:
            u_rotation(cur_cube, False)
            cur_cube.draw_window(False, (255, 255, 255), "U")
            correct_pieces = find_matching_edge(cur_cube)
            found_pieces = correct_pieces.count(True)
        # solves the step
        if False in correct_pieces:
            solve_final_edge(cur_cube, correct_pieces)
        correct_pieces = find_matching_edge(cur_cube)


def correct_corner(cur_cube):
    '''
    This will move each of the four remaining corner pieces to their correct
        locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    correct_pieces = find_matching_corner(cur_cube)
    # runs until all corners have been solved
    while False in correct_pieces:
        solve_final_corner(cur_cube, correct_pieces)
        correct_pieces = find_matching_corner(cur_cube)

def final_solve(cur_cube):
    '''
    This will rotate the four corner pieces until each of them are correctly
        rotated to finish off the solve for the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # turns the cube to the opposite face
    x_rotation(cur_cube, True)
    cur_cube.draw_window(False, (255, 255, 255), "X'")
    x_rotation(cur_cube, True)
    cur_cube.draw_window(False, (255, 255, 255), "X'")
    # solves the final corners
    final_cube_solve(cur_cube)

def solve_cube(cur_cube):
    '''
    This will run all the functions to solve the cube which were created
        in the previous functions.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        '''
    correct_face(cur_cube)
    white_cross(cur_cube)
    white_corners(cur_cube)
    second_layer(cur_cube)
    yellow_cross(cur_cube)
    final_edges(cur_cube)
    correct_corner(cur_cube)
    final_solve(cur_cube)