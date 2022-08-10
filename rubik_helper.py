"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program contains the functions to solve each of the more
    specific steps inside each of the general steps that are laid out
    in the cube_solver program.
"""
import pygame.time
from solver_tools import *
from rotate_tools import *
from rubik_algorithm import *

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

def solve_white_top(cur_cube, found_piece, location):
    '''
    This will move a given white piece that is in either the top or upper
        layer into the bottom layer to assist with solving the white cross.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_piece: An object representing a specific square of the cube.
        location: A string representing which layer the piece is located in.
    '''
    # gets the adjacent pieces
    adjacent = adjacent_edge(cur_cube, found_piece)
    adjacent_piece, adjacent_face = adjacent[0], adjacent[1]
    piece_color = adjacent_piece.tile_color
    if location == "top":
        center_color = adjacent_face.tiles[4].tile_color
    elif location == "upper":
        center_color = find_face(cur_cube, found_piece).tiles[4].tile_color
    # matches the top piece to its correct location.
    move_correct_location(cur_cube, piece_color, center_color)
    # gets the new piece
    if location == "top":
        new_piece = find_piece(cur_cube, piece_color, WHITE)
        # turns cube to the correct face
        face_rotate(cur_cube, new_piece)
        # moves piece into the cross
        f_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "F")
        f_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "F")
    elif location == "upper":
        new_piece = find_piece(cur_cube, WHITE, piece_color)
        # turns cube to the correct face
        face_rotate(cur_cube, new_piece)
        # moves piece into the cross
        white_top_algorithm(cur_cube)

def move_white_up(cur_cube, found_piece, movement):
    '''
    This will move a given white edge to the upper layer so that it can
        then be solved.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_piece: An object representing a specific square of the cube.
        movement: A string representing which layer the piece is located in.
    '''
    # turns cube to the correct face
    face_rotate(cur_cube, found_piece)
    # moves the piece to the top of the cube
    if movement == "left":
        short_left_algorithm(cur_cube)
    if movement == "right":
        short_right_algorithm(cur_cube)
    if movement == "lower":
        f_rotation(cur_cube, True)
        cur_cube.draw_window(False, (255, 255, 255), "F'")
        short_right_algorithm(cur_cube)

def solve_upper_location(cur_cube, found_piece, location):
    '''
    This will move a given white piece that is in either the upper left or
        upper right corner and it will move it into the bottom layer to
        assist with solving the white face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_piece: An object representing a specific square of the cube.
        location: A string representing which layer the piece is located in.
    '''
    # gets the adjacent pieces
    adjacent = adjacent_corners(cur_cube, found_piece)
    adjacent_piece, adjacent_face = adjacent[0][0], adjacent[1]
    piece_color = adjacent_piece.tile_color
    center_color = adjacent_face.tiles[4].tile_color
    move_correct_location(cur_cube, piece_color, center_color)
    # gets the new piece
    new_piece = find_piece(cur_cube, piece_color, WHITE)
    # rotates the cube to the correct face
    face_rotate(cur_cube, new_piece)
    # moves the piece into the white face
    if location == "left":
        short_right_algorithm(cur_cube)
    elif location == "right":
        short_left_algorithm(cur_cube)

def fix_white_bottom(cur_cube, is_edge):
    '''
    This will move a given white edge that is in a correct spot on the bottom
        layer to the top layer so that it can then be solved.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_edge: A boolean representing weather to fix the edges or corners.
    '''
    moving_faces = [cur_cube.front, cur_cube.left,
                    cur_cube.right, cur_cube.back]
    for face in moving_faces:
        # checks if each edge piece is successfully solved
        middle_square = face.tiles[4].tile_color
        if is_edge:
            bottom_square = face.tiles[7].tile_color
        else:
            bottom_square = face.tiles[6].tile_color
        if bottom_square != middle_square:
            # moves the piece to the top layer of the cube
            if is_edge:
                face_rotate(cur_cube, face.tiles[7])
                f_rotation(cur_cube, True)
                cur_cube.draw_window(False, (255, 255, 255), "F'")
                f_rotation(cur_cube, True)
                cur_cube.draw_window(False, (255, 255, 255), "F'")
            else:
                short_left_algorithm(cur_cube)


def solve_white_corner_top(cur_cube, found_piece):
    '''
    This will move a given white corner that is on the top layer of the
        cube and it will move it into the bottom layer to assist with
        solving the white face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_piece: An object representing a specific square of the cube.
        '''
    # gets the adjacent pieces
    adjacent = adjacent_corners(cur_cube, found_piece)
    adjacent_piece, adjacent_face = adjacent[0][1], adjacent[1]
    piece_color = adjacent_piece.tile_color
    center_color = adjacent_face.tiles[4].tile_color
    # moves the piece to the center with the same color as the other piece
    move_correct_location(cur_cube, piece_color, center_color)
    # gets the new piece
    new_piece = find_piece(cur_cube, piece_color, WHITE)
    # rotates the cube to the correct face
    face_rotate(cur_cube, new_piece)
    # checks if the main left algorithm is needed
    bottom_left_color = cur_cube.top.tiles[6].tile_color
    top_left_color = cur_cube.front.tiles[0].tile_color
    center_color = cur_cube.left.tiles[4].tile_color
    # moves the piece into the bottom layer
    if bottom_left_color == WHITE and top_left_color == center_color:
        left_algorithm(cur_cube)
        left_algorithm(cur_cube)
        left_algorithm(cur_cube)
    else:
        right_algorithm(cur_cube)
        right_algorithm(cur_cube)
        right_algorithm(cur_cube)

def move_bottom_corner(cur_cube, found_piece, location):
    '''
    This will move a given white corner piece that is in either the lower
        left or lower right corner and it will move it into the top layer to
        assist with solving the white face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_piece: An object representing a specific square of the cube.
        location: A string representing which layer the piece is located in.
    '''
    # turns cube to the correct face
    face_rotate(cur_cube, found_piece)
    # moves the piece out of the lower layer
    if location == "left":
        short_left_algorithm(cur_cube)
    elif location == "right":
        short_right_algorithm(cur_cube)

def solve_upper_piece(cur_cube, found_pieces):
    '''
    This will move a given edge piece on the upper layer into its correct
        respective location in the second layer.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_pieces: An array of objects representing specific squares
            of the cube.
    '''
    front_face = find_face(cur_cube, found_pieces[0])
    # gets the colors of all the pieces
    center_color = front_face.tiles[4].tile_color
    first_color = found_pieces[0].tile_color
    second_color = found_pieces[1].tile_color
    # moves the piece to the center with the same color as the other piece
    move_correct_location(cur_cube, first_color, center_color)
    # gets the new piece
    new_piece = find_piece(cur_cube, first_color, second_color)
    # rotates the cube to the correct face
    face_rotate(cur_cube, new_piece)
    # checks if the left or right algorithm is needed
    left_color = cur_cube.left.tiles[4].tile_color
    right_color = cur_cube.right.tiles[4].tile_color
    if second_color == left_color:
        left_second_layer(cur_cube)
    elif second_color == right_color:
        right_second_layer(cur_cube)

def find_upper_piece(top_pieces):
    '''
    This will check if there are any pieces in the upper layer that can
        be solved.
    Parameters:
        top_pieces: An array of objects representing specific squares
            of the cube.
    Return Type:
        A Boolean representing if the piece needed to be moved
    '''
    for piece in top_pieces:
        # gets the colors of all the pieces
        first_color = piece[0].tile_color
        second_color = piece[1].tile_color
        if first_color != YELLOW and second_color != YELLOW:
            return piece
    # no pieces to be solved in the upper layer
    return False

def get_upper_piece(cur_cube):
    '''
    This will move a given edge piece from the second layer into the
        upper layer so that it can then be solved
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    needed_pieces = get_pieces(cur_cube, True)
    left_pieces = needed_pieces[3]
    # finds the piece that needs to be moved
    for left_piece in left_pieces:
        adjacent = adjacent_edge(cur_cube, left_piece)[0]
        if left_piece.tile_color != YELLOW and adjacent.tile_color != YELLOW:
            # finds the color of the face the left piece is on
            left_piece_face = find_face(cur_cube, left_piece)
            center_color = left_piece_face.tiles[4].tile_color
            if left_piece.tile_color != center_color:
                break
    # rotates the cube to the correct face
    face_rotate(cur_cube, left_piece)
    # moves the piece to the upper layer
    left_second_layer(cur_cube)

def yellow_pattern(cur_cube, cross_colors):
    '''
    This will run specific algorithms to solve the yellow cross on
        the top of the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cross_colors: An array of objects representing specific squares
            of the cube.
    '''
    # horizontal line
    if cross_colors[1] == YELLOW and cross_colors[2] == YELLOW:
        yellow_line_algorithm(cur_cube)
    # vertical line
    elif cross_colors[0] == YELLOW and cross_colors[3] == YELLOW:
        y_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "Y")
        yellow_line_algorithm(cur_cube)
    # checks for any L shapes on the cross
    elif cross_colors[0] == YELLOW and cross_colors[1] == YELLOW:
        yellow_l_algorithm(cur_cube)
    elif cross_colors[0] == YELLOW and cross_colors[2] == YELLOW:
        y_rotation(cur_cube, True)
        yellow_l_algorithm(cur_cube)
    elif cross_colors[2] == YELLOW and cross_colors[3] == YELLOW:
        y_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "Y")
        y_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "Y")
        yellow_l_algorithm(cur_cube)
    elif cross_colors[1] == YELLOW and cross_colors[3] == YELLOW:
        y_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "Y")
        yellow_l_algorithm(cur_cube)
    else:
        yellow_line_algorithm(cur_cube)
        u_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "U")
        u_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "U")
        yellow_l_algorithm(cur_cube)

def solve_final_edge(cur_cube, found_edges):
    '''
    This will first rotate the cube to its correct face and then it will
        run an algorithm to solve the step.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_edges: An array of Booleans representing which pieces are in
            their correct locations.
    '''
    # rotates the cube to the correct face to run the algorithm
    moves = []
    if found_edges[0] == True and found_edges[1] == True:
        moves = ["Y'"]
    if found_edges[2] == True and found_edges[3] == True:
        moves = ["Y"]
    if found_edges[3] == True and found_edges[0] == True:
        moves = ["Y", "Y"]
    if found_edges[0] == True and found_edges[2] == True:
        moves = ["Y"]
    # runs the algorithm to solve the step
    run_algorithm(cur_cube, moves)
    final_edge_algorithm(cur_cube)

def solve_final_corner(cur_cube, found_corners):
    '''
    This will first rotate the cube to move each of the final corners to their
        correct respective locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        found_corners: An array of Booleans representing which pieces are in
            their correct locations.
    '''
    # moves the one correct piece to the bottom right corner
    moves = []
    if found_corners[0] == True:
        moves = ["Y", "Y"]
    elif found_corners[1] == True:
        moves = ["Y"]
    elif found_corners[2] == True:
        moves = ["Y'"]
    # runs the needed algorithm
    run_algorithm(cur_cube, moves)
    final_corner_algorithm(cur_cube)

def final_cube_solve(cur_cube):
    '''
    This will correctly solve the final four corners to finish the final step
        of solving the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # runs for each of the four remaining corners
    for index in range(4):
        while True:
            # determines if the corner has been solved
            bottom_corner = cur_cube.bottom.tiles[2].tile_color
            if bottom_corner == YELLOW:
                break
            right_algorithm(cur_cube)
        # turns to the next corner
        d_rotation(cur_cube, False)
        cur_cube.draw_window(False, (255, 255, 255), "D")