"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program gives the functions to rotate the cube F, F',
    R, R', U, U', B, B', L, L', D, D', X, X', Y, Y', Z and Z' whenever the
    designated button is clicked on the bottom of the screen. It will also
    create a randomly scrambled cube whenever the Scramble button is clicked.
"""
import random

def f_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the F or F' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    top_face = get_bottom(cur_cube.top)
    right_face = get_left(cur_cube.right)
    left_face = get_right(cur_cube.left)
    bottom_face = get_top(cur_cube.bottom)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(top_face, right_face, 3)
        swap_squares(bottom_face, left_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(bottom_face)
        rotate_color(top_face)
        rotate_face(cur_cube.front, False)
    else:
        swap_squares(top_face, left_face, 3)
        swap_squares(bottom_face, right_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(left_face)
        rotate_color(right_face)
        rotate_face(cur_cube.front, True)

def r_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the R or R' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    front_face = get_right(cur_cube.front)
    top_face = get_right(cur_cube.top)
    bottom_face = get_right(cur_cube.bottom)
    back_face = get_left(cur_cube.back)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(front_face, bottom_face, 3)
        swap_squares(top_face, back_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(back_face)
        rotate_color(bottom_face)
        rotate_face(cur_cube.right, False)
    else:
        swap_squares(front_face, bottom_face, 3)
        swap_squares(top_face, back_face, 3)
        swap_squares(front_face, back_face, 3)
        # rotates the colors to the correct positions
        rotate_color(back_face)
        rotate_color(top_face)
        rotate_face(cur_cube.right, True)

def u_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the U or U' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    front_face = get_top(cur_cube.front)
    left_face = get_top(cur_cube.left)
    right_face = get_top(cur_cube.right)
    back_face = get_top(cur_cube.back)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(left_face, front_face, 3)
        swap_squares(front_face, right_face, 3)
        swap_squares(right_face, back_face, 3)
        rotate_face(cur_cube.top, False)
    else:
        swap_squares(right_face, back_face, 3)
        swap_squares(front_face, right_face, 3)
        swap_squares(left_face, front_face, 3)
        rotate_face(cur_cube.top, True)

def b_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the B or B' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    top_face = get_top(cur_cube.top)
    left_face = get_left(cur_cube.left)
    right_face = get_right(cur_cube.right)
    bottom_face = get_bottom(cur_cube.bottom)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(left_face, top_face, 3)
        swap_squares(bottom_face, right_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(left_face)
        rotate_color(right_face)
        rotate_face(cur_cube.back, False)

    else:
        swap_squares(top_face, right_face, 3)
        swap_squares(bottom_face, left_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(top_face)
        rotate_color(bottom_face)
        rotate_face(cur_cube.back, True)

def l_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the L or L' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    front_face = get_left(cur_cube.front)
    bottom_face = get_left(cur_cube.bottom)
    top_face = get_left(cur_cube.top)
    back_face = get_right(cur_cube.back)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(bottom_face, back_face, 3)
        swap_squares(front_face, top_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(top_face)
        rotate_color(back_face)
        rotate_face(cur_cube.left, False)
    else:
        swap_squares(top_face, back_face, 3)
        swap_squares(front_face, bottom_face, 3)
        swap_squares(top_face, bottom_face, 3)
        # rotates the colors to the correct positions
        rotate_color(back_face)
        rotate_color(bottom_face)
        rotate_face(cur_cube.left, True)

def d_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the D or D' rotation depending
        on which button the user clicked.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # gets the initial squares that will be swapped
    front_face = get_bottom(cur_cube.front)
    back_face = get_bottom(cur_cube.back)
    left_face = get_bottom(cur_cube.left)
    right_face = get_bottom(cur_cube.right)
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(right_face, back_face, 3)
        swap_squares(front_face, right_face, 3)
        swap_squares(left_face, front_face, 3)
        rotate_face(cur_cube.bottom, False)
    else:
        swap_squares(left_face, front_face, 3)
        swap_squares(front_face, right_face, 3)
        swap_squares(right_face, back_face, 3)
        rotate_face(cur_cube.bottom, True)

def x_rotation(cur_cube, is_prime):
    '''
    This will either move the cube up in the x direction.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    if not is_prime:
        # swaps the squares in the correct order
        swap_squares(cur_cube.top.tiles, cur_cube.front.tiles, 9)
        swap_squares(cur_cube.front.tiles, cur_cube.bottom.tiles, 9)
        swap_squares(cur_cube.bottom.tiles, cur_cube.back.tiles, 9)
        rotate_face(cur_cube.right, False)
        rotate_face(cur_cube.left, True)
        # moves square to correct position
        swap_face(cur_cube.back)
        swap_face(cur_cube.bottom)
    else:
        # swaps the squares in the correct order
        swap_squares(cur_cube.bottom.tiles, cur_cube.back.tiles, 9)
        swap_squares(cur_cube.front.tiles, cur_cube.bottom.tiles, 9)
        swap_squares(cur_cube.top.tiles, cur_cube.front.tiles, 9)
        rotate_face(cur_cube.right, True)
        rotate_face(cur_cube.left, False)
        # moves square to correct position
        swap_face(cur_cube.back)
        swap_face(cur_cube.top)

def y_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the y direction.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    # swaps the squares in the correct order
    if not is_prime:
        swap_squares(cur_cube.left.tiles, cur_cube.front.tiles, 9)
        swap_squares(cur_cube.right.tiles, cur_cube.back.tiles, 9)
        swap_squares(cur_cube.front.tiles, cur_cube.back.tiles, 9)
        rotate_face(cur_cube.top, False)
        rotate_face(cur_cube.bottom, True)
    else:
        swap_squares(cur_cube.front.tiles, cur_cube.back.tiles, 9)
        swap_squares(cur_cube.right.tiles, cur_cube.back.tiles, 9)
        swap_squares(cur_cube.left.tiles, cur_cube.front.tiles, 9)
        rotate_face(cur_cube.top, True)
        rotate_face(cur_cube.bottom, False)

def z_rotation(cur_cube, is_prime):
    '''
    This will either move the cube in the z direction.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_prime: A boolean representing if the prime rotation was clicked.
    '''
    if not is_prime:
        # swaps the squares in the correct order
        swap_squares(cur_cube.left.tiles, cur_cube.right.tiles, 9)
        swap_squares(cur_cube.left.tiles, cur_cube.bottom.tiles, 9)
        swap_squares(cur_cube.top.tiles, cur_cube.right.tiles, 9)
        rotate_face(cur_cube.right, False)
        rotate_face(cur_cube.bottom, False)
        rotate_face(cur_cube.left, False)
        rotate_face(cur_cube.top, False)
        rotate_face(cur_cube.front, False)
        rotate_face(cur_cube.back, True)
    else:
        # swaps the squares in the correct order
        swap_squares(cur_cube.top.tiles, cur_cube.right.tiles, 9)
        swap_squares(cur_cube.left.tiles, cur_cube.bottom.tiles, 9)
        swap_squares(cur_cube.left.tiles, cur_cube.right.tiles, 9)
        rotate_face(cur_cube.right, True)
        rotate_face(cur_cube.bottom, True)
        rotate_face(cur_cube.left, True)
        rotate_face(cur_cube.top, True)
        rotate_face(cur_cube.front, True)
        rotate_face(cur_cube.back, False)


def get_top(face):
    '''
    This will get the top three squares of a given face on the cube.
    Parameters:
        face: An object that contains all the information for a single face.
    Return Type:
        Returns an array containing the three squares.
    '''
    first_tile = face.tiles[0]
    second_tile = face.tiles[1]
    third_tile = face.tiles[2]
    cur_tiles = [first_tile, second_tile, third_tile]
    return cur_tiles

def get_bottom(face):
    '''
    This will get the bottom three squares of a given face on the cube.
    Parameters:
        face: An object that contains all the information for a single face.
    Return Type:
        Returns an array containing the three squares.
    '''
    first_tile = face.tiles[6]
    second_tile = face.tiles[7]
    third_tile = face.tiles[8]
    cur_tiles = [first_tile, second_tile, third_tile]
    return cur_tiles

def get_right(face):
    '''
    This will get the right three squares of a given face on the cube.
    Parameters:
        face: An object that contains all the information for a single face.
    Return Type:
        Returns an array containing the three squares.
    '''
    first_tile = face.tiles[2]
    second_tile = face.tiles[5]
    third_tile = face.tiles[8]
    cur_tiles = [first_tile, second_tile, third_tile]
    return cur_tiles

def get_left(face):
    '''
    This will get the left three squares of a given face on the cube.
    Parameters:
        face: An object that contains all the information for a single face.
    Return Type:
        Returns an array containing the three squares.
    '''
    first_tile = face.tiles[0]
    second_tile = face.tiles[3]
    third_tile = face.tiles[6]
    cur_tiles = [first_tile, second_tile, third_tile]
    return cur_tiles

def swap_squares(first_squares, second_squares, index):
    '''
    This will swap three of the colors from one face with three colors
        of another face on the cube to represent a rotation.
    Parameters:
        first_squares: An array of three objects which each represent a
            square on the cube.
        second_squares: An array of three objects which each represent a
            square on the cube.
        index: An integer representing the number of tiles to be swapped.
    '''
    for index in range(index):
        first_color = first_squares[index].tile_color
        second_color = second_squares[index].tile_color
        first_squares[index].tile_color = second_color
        second_squares[index].tile_color = first_color

def rotate_face(cur_face, is_left):
    '''
    This will completely rotate a given face either to the left or to
        the right.
    Parameters:
        cur_face: An object that contains all the information for a
            single face.
        is_left: A boolean value representing weather to rotate the face to
            the left or to the right.
    Return Type:
        Returns an array containing the three squares.
    '''
    # rotates the face to the left
    if is_left:
        # swaps the corner pieces
        swap_squares([cur_face.tiles[0]], [cur_face.tiles[6]], 1)
        swap_squares([cur_face.tiles[2]], [cur_face.tiles[8]], 1)
        swap_squares([cur_face.tiles[0]], [cur_face.tiles[8]], 1)
        # swap the edge pieces
        swap_squares([cur_face.tiles[1]], [cur_face.tiles[3]], 1)
        swap_squares([cur_face.tiles[5]], [cur_face.tiles[7]], 1)
        swap_squares([cur_face.tiles[1]], [cur_face.tiles[7]], 1)
    # rotates the face to the right
    else:
        # swaps the corner pieces
        swap_squares([cur_face.tiles[0]], [cur_face.tiles[8]], 1)
        swap_squares([cur_face.tiles[2]], [cur_face.tiles[8]], 1)
        swap_squares([cur_face.tiles[0]], [cur_face.tiles[6]], 1)
        # swap the edge pieces
        swap_squares([cur_face.tiles[1]], [cur_face.tiles[7]], 1)
        swap_squares([cur_face.tiles[5]], [cur_face.tiles[7]], 1)
        swap_squares([cur_face.tiles[1]], [cur_face.tiles[3]], 1)

def rotate_color(squares):
    '''
    This will swap the first and third color of an array of three squares.
    Parameters:
        squares: An array of three objects which each represent a
            square on the cube.
    '''
    # gets the colors to be swapped
    first_color = squares[0].tile_color
    second_color = squares[2].tile_color
    # swaps the colors
    squares[0].tile_color = second_color
    squares[2].tile_color = first_color

def swap_face(cur_face):
    '''
    This will swap all the colors of the face to represent the
        cub being flipped over.
    Parameters:
        cur_face: An object that contains all the information for a
            single face.
    '''
    # gets the squares that will be swapped
    top_squares = get_top(cur_face)
    bottom_squares = get_bottom(cur_face)
    middle_squares = [cur_face.tiles[3], cur_face.tiles[4], cur_face.tiles[5]]
    # swaps all the squares to the correct positions
    swap_squares(top_squares, bottom_squares, 3)
    rotate_color(top_squares)
    rotate_color(middle_squares)
    rotate_color(bottom_squares)

def scramble_cube(cur_cube):
    '''
    This will use randomly generated numbers to select movements in the
        cube so that the cube will be randomly scrambled.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    '''
    # determines amount of times to turn the cube
    number_turns = random.randint(20, 30)
    for index in range(number_turns):
        random_turn = random.randint(1, 12)
        # chooses a random movement based on the random number
        if random_turn == 1:
            f_rotation(cur_cube, False)
        if random_turn == 2:
            f_rotation(cur_cube, True)
        if random_turn == 3:
            r_rotation(cur_cube, False)
        if random_turn == 4:
            r_rotation(cur_cube, True)
        if random_turn == 5:
            u_rotation(cur_cube, False)
        if random_turn == 6:
            u_rotation(cur_cube, True)
        if random_turn == 7:
            b_rotation(cur_cube, False)
        if random_turn == 8:
            b_rotation(cur_cube, True)
        if random_turn == 9:
            l_rotation(cur_cube, False)
        if random_turn == 10:
            l_rotation(cur_cube, True)
        if random_turn == 11:
            d_rotation(cur_cube, False)
        if random_turn == 12:
            d_rotation(cur_cube, True)