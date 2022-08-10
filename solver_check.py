"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program has functions to check each of the seven steps to
    solve the cube to see if they have been completed or not.
"""
from solver_tools import *

def white_cross_solved(cur_cube):
    '''
    This function checks to see if the white cross has been completely
        solved on the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        Returns a Boolean representing if the cross is completed.
    '''
    white_edges = face_edges(cur_cube.bottom)
    for edge in white_edges:
        # checks if any colors on the cross are not white
        if edge.tile_color != (255,255,255):
            return False
        adjacent_piece, adjacent_face = adjacent_edge(cur_cube, edge)
        # finds the center piece of the adjacent tiles face
        middle_piece = adjacent_face.tiles[4]
        # checks if the adjacent piece is in the correct location
        if adjacent_piece.tile_color != middle_piece.tile_color:
            return False
    # The cross is completed
    return True

def white_corners_solved(cur_cube):
    '''
    This function checks to see if the white face has been completely
        solved on the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        Returns a Boolean representing if the face is completed.
    '''
    white_corners = face_corners(cur_cube.bottom)
    for edge in white_corners:
        # checks if any colors on the cross are not white
        if edge.tile_color != (255, 255, 255):
            return False
        front_corners = face_corners(cur_cube.front)
        back_corners = face_corners(cur_cube.back)
        left_corners = face_corners(cur_cube.left)
        right_corners = face_corners(cur_cube.right)
        # gets the color of each face
        front_face = cur_cube.front.tiles[4].tile_color
        back_face = cur_cube.back.tiles[4].tile_color
        left_face = cur_cube.left.tiles[4].tile_color
        right_face = cur_cube.right.tiles[4].tile_color
        # checks if the corners are in the correct location
        if front_corners[2].tile_color != front_face:
            return False
        if front_corners[3].tile_color != front_face:
            return False
        if back_corners[2].tile_color != back_face:
            return False
        if back_corners[3].tile_color != back_face:
            return False
        if left_corners[2].tile_color != left_face:
            return False
        if left_corners[3].tile_color != left_face:
            return False
        if right_corners[2].tile_color != right_face:
            return False
        if right_corners[3].tile_color != right_face:
            return False
        # the step is completed
        return True

def second_layer_solved(cur_cube):
    '''
    This function checks to see if the second layer has been completely
        solved on the cube.
    Parameters:
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        Returns a Boolean representing if the face is completed.
    '''
    all_faces = [cur_cube.front.tiles, cur_cube.left.tiles,
                 cur_cube.right.tiles, cur_cube.back.tiles]
    for face in all_faces:
        left_color = face[3].tile_color
        middle_color = face[4].tile_color
        right_color = face[5].tile_color
        # checks if any color do not match
        if left_color != middle_color or right_color != middle_color:
            return False
    # the step is completed
    return True