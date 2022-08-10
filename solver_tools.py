"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program implements a variety of functions to assist
    with solving the cube. The functions help with obtaining the location
    of each piece of the cube along with helping to set up the cube to be
    in the correct positions to run the needed algorithms.
"""
from rotate_tools import *
from rubik_algorithm import *

# creates the needed colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)


def adjacent_edge(cur_cube, cur_square):
    '''
    This function determines the adjacent edge to any given edge piece
        that is on the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cur_square: An object that contains all the information for a
            single square.
    Return Type:
        Returns an object that represents the square that is adjacent
        to the given tile.
    '''
    cur_face = find_face(cur_cube, cur_square)
    cur_edges = face_edges(cur_face)
    # finds the index that the piece is located
    piece_index = piece_location(cur_edges, cur_square)
    face_type = cur_face.face
    adjacent_face = surrounding_edges(cur_cube, face_type)
    # gets the adjacent top piece
    if piece_index == 0:
        adjacent_piece = adjacent_face[2]
    # gets the adjacent left piece
    elif piece_index == 1:
        adjacent_piece = adjacent_face[0]
    # gets the adjacent right piece
    elif piece_index == 2:
        adjacent_piece = adjacent_face[1]
    # gets the adjacent bottom piece
    elif piece_index == 3:
        adjacent_piece = adjacent_face[3]
    opposite_face = find_face(cur_cube, adjacent_piece)
    return [adjacent_piece, opposite_face]

def adjacent_corners(cur_cube, cur_square):
    '''
    This function determines the adjacent corners to any given edge piece
        that is on the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cur_square: An object that contains all the information for a
            single square.
    Return Type:
        Returns an object that represents the square that is adjacent
        to the given tile.
    '''
    cur_face = find_face(cur_cube, cur_square)
    cur_corners = face_corners(cur_face)
    # finds the index that the piece is located
    piece_index = piece_location(cur_corners, cur_square)
    face_type = cur_face.face
    adjacent_face = surrounding_corners(cur_cube, face_type)
    # gets the adjacent top piece
    if piece_index == 0:
        adjacent_pieces = adjacent_face[0]
    # gets the adjacent left piece
    elif piece_index == 1:
        adjacent_pieces = adjacent_face[1]
    # gets the adjacent right piece
    elif piece_index == 2:
        adjacent_pieces = adjacent_face[2]
    # gets the adjacent bottom piece
    elif piece_index == 3:
        adjacent_pieces = adjacent_face[3]
    opposite_face = find_face(cur_cube, adjacent_pieces[0])
    return [adjacent_pieces, opposite_face]

def get_pieces(cur_cube, is_edges):
    '''
    This function determines the edges or corners that are needed
        for each portion of the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        is_edges: A Boolean representing if the corners or edges are needed
    Return Type:
        Returns an array containing the four edges for all parts of the cube.
    '''
    # adds all the faces to an array
    cur_squares = [cur_cube.top, cur_cube.front, cur_cube.left, cur_cube.right,
                   cur_cube.back, cur_cube.bottom]
    first_squares = []
    second_squares = []
    third_squares = []
    fourth_squares = []
    all_squares = []
    for index in range(1, len(cur_squares) - 1):
        # gets the four edges of the face
        cur_face = cur_squares[index].tiles
        if is_edges:
            first_edge = cur_face[1]
            second_edge = cur_face[3]
            third_edge = cur_face[5]
            fourth_edge = cur_face[7]
        else:
            first_edge = cur_face[0]
            second_edge = cur_face[6]
            third_edge = cur_face[8]
            fourth_edge = cur_face[2]
        # checks if looking at the top or bottom face
        first_squares.append(first_edge)
        second_squares.append(fourth_edge)
        third_squares.append(second_edge)
        fourth_squares.append(third_edge)
    # adds all the found edges to the array
    if is_edges:
        all_squares.append(face_edges(cur_squares[0]))
        all_squares.append(first_squares)
        all_squares.append(second_squares)
        all_squares.append(third_squares)
        all_squares.append(fourth_squares)
        all_squares.append(face_edges(cur_squares[5]))
    else:
        all_squares.append(first_squares)
        all_squares.append(second_squares)
        all_squares.append(face_corners(cur_squares[0]))
        all_squares.append(third_squares)
        all_squares.append(fourth_squares)
        all_squares.append(face_corners(cur_squares[5]))
    return all_squares

def face_edges(cur_face):
    '''
    This function determines the four edges for any given face.
    Parameters:
        cur_cube: An object representing on given face on the current cube.
    Return Type:
        Returns an array containing the four edges for the given face.
    '''
    cur_edges = cur_face.tiles
    # gets the four edges
    first_edge = cur_edges[1]
    second_edge = cur_edges[3]
    third_edge = cur_edges[5]
    fourth_edge = cur_edges[7]
    edge_squares = [first_edge, second_edge, third_edge, fourth_edge]
    return edge_squares

def face_corners(cur_face):
    '''
    This function determines the four corners for any given face.
    Parameters:
        cur_cube: An object representing on given face on the current cube.
    Return Type:
        Returns an array containing the four corners for the given face.
    '''
    cur_edges = cur_face.tiles
    # gets the four corners
    first_edge = cur_edges[0]
    second_edge = cur_edges[2]
    third_edge = cur_edges[6]
    fourth_edge = cur_edges[8]
    edge_squares = [first_edge, second_edge, third_edge, fourth_edge]
    return edge_squares

def piece_location(cur_tiles, cur_piece):
    '''
    This function determines the index that a piece on the cube is
        located at.
    Parameters:
        cur_tiles: An array containing four squares from the cube.
        cur_piece: An object that contains all the information for a
            single square.
    Return Type:
        Returns an integer representing the found index.
    '''
    for index in range(len(cur_tiles)):
        # finds the index the piece is located at
        if cur_tiles[index] == cur_piece:
            return index

def surrounding_edges(cur_cube, type_face):
    '''
    This function determines the adjacent edge to every edge on a given
        face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        type_face: A string that represents the current face that information
            is needed for.
    Return Type:
        Returns an array containing the four adjacent squares on the cube.
    '''
    # gets all the squares adjacent to the left face
    if type_face == "left":
        left_piece = face_edges(cur_cube.back)[2]
        right_piece = face_edges(cur_cube.front)[1]
        top_piece = face_edges(cur_cube.top)[1]
        bottom_piece = face_edges(cur_cube.bottom)[1]
    # gets all the squares adjacent to the right face
    if type_face == "right":
        left_piece = face_edges(cur_cube.front)[2]
        right_piece = face_edges(cur_cube.back)[1]
        top_piece = face_edges(cur_cube.top)[2]
        bottom_piece = face_edges(cur_cube.bottom)[2]
    # gets all the squares adjacent to the front face
    if type_face == "front":
        left_piece = face_edges(cur_cube.left)[2]
        right_piece = face_edges(cur_cube.right)[1]
        top_piece = face_edges(cur_cube.top)[3]
        bottom_piece = face_edges(cur_cube.bottom)[0]
    # gets all the squares adjacent to the back face
    if type_face == "back":
        left_piece = face_edges(cur_cube.right)[2]
        right_piece = face_edges(cur_cube.left)[1]
        top_piece = face_edges(cur_cube.top)[0]
        bottom_piece = face_edges(cur_cube.bottom)[3]
    # gets all the squares adjacent to the top face
    if type_face == "top":
        left_piece = face_edges(cur_cube.left)[0]
        right_piece = face_edges(cur_cube.right)[0]
        top_piece = face_edges(cur_cube.back)[0]
        bottom_piece = face_edges(cur_cube.front)[0]
    # gets all the squares adjacent to the bottom face
    if type_face == "bottom":
        left_piece = face_edges(cur_cube.left)[3]
        right_piece = face_edges(cur_cube.right)[3]
        top_piece = face_edges(cur_cube.front)[3]
        bottom_piece = face_edges(cur_cube.back)[3]
    return [left_piece, right_piece, top_piece, bottom_piece]

def surrounding_corners(cur_cube, type_face):
    '''
    This function determines the adjacent corners to every corner on a given
        face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        type_face: A string that represents the current face that information
            is needed for.
    Return Type:
        Returns an array containing all the adjacent corners for every corner
        on the given face.
    '''
    top_corners = face_corners(cur_cube.top)
    bottom_corners = face_corners(cur_cube.bottom)
    left_corners = face_corners(cur_cube.left)
    right_corners = face_corners(cur_cube.right)
    front_corners = face_corners(cur_cube.front)
    back_corners = face_corners(cur_cube.back)
    # gets all the squares adjacent to the left face
    if type_face == "left":
        upper_left = [back_corners[1], top_corners[0]]
        upper_right = [front_corners[0], top_corners[2]]
        lower_left = [back_corners[3], bottom_corners[2]]
        lower_right = [front_corners[2], bottom_corners[0]]
    # gets all the squares adjacent to the right face
    if type_face == "right":
        upper_left = [front_corners[1], top_corners[3]]
        upper_right = [back_corners[0], top_corners[1]]
        lower_left = [front_corners[3], bottom_corners[1]]
        lower_right = [back_corners[2], bottom_corners[3]]
    # gets all the squares adjacent to the front face
    if type_face == "front":
        upper_left = [left_corners[1], top_corners[2]]
        upper_right = [right_corners[0], top_corners[3]]
        lower_left = [left_corners[3], bottom_corners[0]]
        lower_right = [right_corners[2], bottom_corners[1]]
    # gets all the squares adjacent to the back face
    if type_face == "back":
        upper_left = [right_corners[1], top_corners[1]]
        upper_right = [left_corners[0], top_corners[0]]
        lower_left = [right_corners[3], bottom_corners[3]]
        lower_right = [left_corners[2], bottom_corners[2]]
    # gets all the squares adjacent to the top face
    if type_face == "top":
        upper_left = [back_corners[1], left_corners[0]]
        upper_right = [back_corners[0], right_corners[1]]
        lower_left = [front_corners[0], left_corners[1]]
        lower_right = [front_corners[1], right_corners[0]]
    # gets all the squares adjacent to the bottom face
    if type_face == "bottom":
        upper_left = [front_corners[2], left_corners[3]]
        upper_right = [front_corners[3], right_corners[2]]
        lower_left = [back_corners[3], left_corners[2]]
        lower_right = [back_corners[2], right_corners[3]]
    return [upper_left, upper_right, lower_left, lower_right]

def find_face(cur_cube, cur_piece):
    '''
    This function determines which face that any given piece is located on.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cur_piece: An object that contains all the information for a
            single square.
    Return Type:
        Returns an object that represents the face that the tile was
        found on.
    '''
    # checks each face to see if the piece is located in it
    if cur_cube.top.square_located(cur_piece):
        return cur_cube.top
    if cur_cube.bottom.square_located(cur_piece):
        return cur_cube.bottom
    if cur_cube.left.square_located(cur_piece):
        return cur_cube.left
    if cur_cube.right.square_located(cur_piece):
        return cur_cube.right
    if cur_cube.front.square_located(cur_piece):
        return cur_cube.front
    if cur_cube.back.square_located(cur_piece):
        return cur_cube.back

def find_color_location(cur_pieces, cur_color):
    '''
    This function will determine if any pieces in a given array contains
        a specific color.
    Parameters:
        cur_pieces: An array of objects each representing a piece of
            the cube.
        cur_color: A tuple with 3 integers each representing a RGB value.
    Return Type:
        Returns an object that represents the found piece of the cube or
        a boolean if it was not found.
    '''
    for piece in cur_pieces:
        # compares each of the colors to see if they are the same
        if piece.tile_color == cur_color:
            return piece
    # if no piece was found
    return False

def move_correct_location(cur_cube, cur_color, center_color):
    '''
    This function will determine the rotations that are needed to match
        a given color to a specific face.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cur_color: A tuple with 3 integers each representing a RGB value.
        center_color: A tuple with 3 integers each representing a RGB value.
    '''
    movements = ""
    # cube movements if the center color is red
    if cur_color == RED:
        if center_color == BLUE:
            movements = "right"
        if center_color == GREEN:
            movements = "left"
        if center_color == ORANGE:
            movements = "left two"
    # cube movements if the center color is blue
    if cur_color == BLUE:
        if center_color == RED:
            movements = "left"
        if center_color == ORANGE:
            movements = "right"
        if center_color == GREEN:
            movements = "left two"
    # cube movements if the center color is green
    if cur_color == GREEN:
        if center_color == ORANGE:
            movements = "left"
        if center_color == RED:
            movements = "right"
        if center_color == BLUE:
            movements = "left two"
    # cube movements if the center color is orange
    if cur_color == ORANGE:
        if center_color == BLUE:
            movements = "left"
        if center_color == GREEN:
            movements = "right"
        if center_color == RED:
            movements = "left two"
    # rotates the cube
    if movements != "":
        cube_movements(cur_cube, movements)

def cube_movements(cur_cube, cube_move):
    '''
    This function will implement the rotations that are needed
        to move a piece from one face to another.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        cur_move: A string that represents the moves to be executed.
    '''
    # rotates the cube in the u direction
    moves = []
    if cube_move == "right":
        moves = ["U'"]
    if cube_move == "left":
        moves = ["U"]
    if cube_move == "left two":
        moves = ["U", "U"]
    run_algorithm(cur_cube, moves)

def face_rotate(cur_cube, face_piece):
    '''
    This function will implement the rotations that are needed
        to rotate the cube from one face to another
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        face_piece: An object representing a piece of the cube.
    '''
    move_face = find_face(cur_cube, face_piece).face
    # rotates the cube over the y axis
    moves = []
    if move_face == "left":
        moves = ["Y'"]
    if move_face == "right":
        moves = ["Y"]
    if move_face == "back":
        moves = ["Y'", "Y'"]
    run_algorithm(cur_cube, moves)

def find_piece(cur_cube, first_color, second_color):
    '''
    This function searches through the entirety of the cube to find
        a specific edge.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        first_color: A tuple containing 3 integers representing a RGB value.
        second_color: A tuple containing 3 integers representing a RGB value.
    Return Type:
        Returns an object representing the found piece.
    '''
    # creates all of the pieces
    top_pieces = face_edges(cur_cube.top)
    bottom_pieces = face_edges(cur_cube.bottom)
    left_pieces = face_edges(cur_cube.left)
    right_pieces = face_edges(cur_cube.right)
    front_pieces = face_edges(cur_cube.front)
    back_pieces = face_edges(cur_cube.back)
    all_pieces = [top_pieces, bottom_pieces, left_pieces, right_pieces,
                  front_pieces, back_pieces]
    # checks each piece to see if the color matches
    for face in all_pieces:
        for piece in face:
            adjacent_color = adjacent_edge(cur_cube, piece)[0].tile_color
            if piece.tile_color == first_color and adjacent_color == second_color:
                return piece

def find_corner_piece(cur_cube, first_color, second_color):
    '''
    This function searches through the entirety of the cube to find
        a specific corner.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
        first_color: A tuple containing 3 integers representing a RGB value.
        second_color: A tuple containing 3 integers representing a RGB value.
    Return Type:
        Returns an object representing the found piece.
    '''
    # creates all of the pieces
    top_pieces = face_corners(cur_cube.top)
    bottom_pieces = face_corners(cur_cube.bottom)
    left_pieces = face_corners(cur_cube.left)
    right_pieces = face_corners(cur_cube.right)
    front_pieces = face_corners(cur_cube.front)
    back_pieces = face_corners(cur_cube.back)
    all_pieces = [left_pieces, right_pieces, top_pieces, bottom_pieces,
                  front_pieces, back_pieces]
    # checks each piece to see if the color matches
    for face in all_pieces:
        for piece in face:
            adjacent_color = adjacent_corners(cur_cube, piece)[0][0].tile_color
            if piece.tile_color == first_color and adjacent_color == second_color:
                return piece

def find_matching_edge(cur_cube):
    '''
    This function searches through the upper layer of the cube to find
        which edges are in their correct locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        Returns an array of Booleans each representing if an edge is in
        it's correct respective location.
    '''
    correct_edges = []
    needed_faces = [cur_cube.front.tiles, cur_cube.right.tiles,
                    cur_cube.back.tiles, cur_cube.left.tiles]
    for face in needed_faces:
        # compares the colors to see if it is in its correct location
        upper_color = face[1].tile_color
        center_color = face[4].tile_color
        if upper_color == center_color:
            correct_edges.append(True)
        else:
            correct_edges.append(False)
    return correct_edges

def find_matching_corner(cur_cube):
    '''
    This function searches through the upper layer of the cube to find
        which corners are in their correct locations.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        Returns an array of Booleans each representing if an edge is in
        it's correct respective location.
    '''
    correct_edges = [True, True, True, True]
    # gets the needed center colors
    top_color = cur_cube.top.tiles[4].tile_color
    front_color = cur_cube.front.tiles[4].tile_color
    left_color = cur_cube.left.tiles[4].tile_color
    right_color = cur_cube.right.tiles[4].tile_color
    back_color = cur_cube.back.tiles[4].tile_color
    all_corners = surrounding_corners(cur_cube, "top")
    top_corners = face_corners(cur_cube.top)
    # checks if the upper left is solved
    top_left = [all_corners[0][0], all_corners[0][1], top_corners[0]]
    for corner in top_left:
        corner_color = corner.tile_color
        if corner_color != top_color and corner_color != back_color and \
        corner_color != left_color:
            correct_edges[0] = False
    # checks if the upper right is solved
    top_right = [all_corners[1][0], all_corners[1][1], top_corners[1]]
    for corner in top_right:
        corner_color = corner.tile_color
        if corner_color != top_color and corner_color != back_color and \
        corner_color != right_color:
            correct_edges[1] = False
    # checks if the lower left is solved
    bottom_left = [all_corners[2][0], all_corners[2][1], top_corners[2]]
    for corner in bottom_left:
        corner_color = corner.tile_color
        if corner_color != top_color and corner_color != front_color and \
        corner_color != left_color:
            correct_edges[2] = False
    # checks if the lower right is solved
    bottom_right = [all_corners[3][0], all_corners[3][1], top_corners[3]]
    for corner in bottom_right:
        corner_color = corner.tile_color
        if corner_color != top_color and corner_color != front_color and \
        corner_color != right_color:
            correct_edges[3] = False
    return correct_edges