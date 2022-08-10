"""
Author: Luke Laurie
Date: 5/27/2022
DESCRIPTION: This program starts by creating an displaying a solved Rubik's
    cube. It then allows the user to either click a scramble button to create
    a randomly scrambled cube or to manually input a cube by clicking on a
    color box then clicking on a tile. The cube can also be rotated by clicking
    one of the rotation boxes or solved by clicking on the solve box.
"""
import pygame
from rotate_tools import *
from cube_solver import *

pygame.font.init()
# creates rgb values for all the needed colors
WHITE = (255,255,255)
LIGHT_GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREY = (200, 200, 200)

# creates the window
WIDTH, HEIGHT = 630, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Solver")

WORD_FONT = pygame.font.SysFont("Arial", 20)
SOLVING_FONT = pygame.font.SysFont("Arial", 70)

class RubikCube:
    '''
    This class will use the faces created from the RubikFace class to create
        a Rubik's cube. This will both initialize the beginning board, and it
        will display the board on a GUI as well.
    The constructor will create six different objects where each object
        is one of the six faces of the cube. It will then store all of the
        objects in an array.
    Methods:
         draw_face(): Draws each of the squares for a given face
         is_collision(): Checks if the cursor collides with any of the
            tiles of the cube.
        is_valid(): Checks if the current cube is a valid cube.
        draw_window(): Displays the cube/buttons onto the GUI.
    '''
    def __init__(self):
        self.top = RubikFace("top")
        self.bottom = RubikFace("bottom")
        self.left = RubikFace("left")
        self.right = RubikFace("right")
        self.front = RubikFace("front")
        self.back = RubikFace("back")
        self.all_faces = [self.top, self.bottom, self.left,
                          self.right, self.front, self.back]
        self.color_boxes = create_colors()
        self.rotations = create_buttons()

    def draw_face(self, face):
        '''
        This draws each of the squares of a given face onto the GUI.
        Parameters:
            face: An object representing a single side of the cube
        '''
        # draws each of the nine squares.
        for tile in face.tiles:
            tile.draw_rect()

    def is_collision(self, cur_position):
        '''
        This iterates over all 54 squares of the cube and it checks if the
            cursor collides with any of them.
        Parameters:
            cur_position: A tuple of two integers representing the x/y
                coordinates of the cursor.
        Return Type:
            Either an object if there was a collision or a Boolean.
        '''
        # iterates through every tile
        for face in self.all_faces:
            for tile in face.tiles:
                # checks if location of the cursor collides with any tile
                if tile.cur_rect.collidepoint(cur_position):
                    return tile
        return False
    def is_valid(self):
        '''
        This iterates over all 54 squares of the cube and it checks if there
            is 6 of each color to determine if the cube is valid
        Return Type:
            A Boolean representing if the current cube s valid or not.
        '''
        # creates the counts for each color
        color_count = [0, 0, 0, 0, 0, 0]
        # check the color of each tile
        for face in self.all_faces:
            for tile in face.tiles:
                # adds to each color count
                if tile.tile_color == WHITE:
                    color_count[0] += 1
                if tile.tile_color == YELLOW:
                    color_count[1] += 1
                if tile.tile_color == RED:
                    color_count[2] += 1
                if tile.tile_color == BLUE:
                    color_count[3] += 1
                if tile.tile_color == GREEN:
                    color_count[4] += 1
                if tile.tile_color == ORANGE:
                    color_count[5] += 1
        # checks that each color count is 9
        for count in color_count:
            if count != 9:
                return False
        # the cube is valid
        return True

    def draw_window(self, collide, cur_color, solving_move):
        '''
        This draws each of the faces of the cube and the clickable
            buttons onto the GUI.
        Parameters:
            collide: A boolean value or object representing if a mouse is
                hovering over a square.
            cur_color: The RBG value of the selected color.
            solving_move: A string representing the current move in the
                solution.
        '''
        color_boxes = self.color_boxes
        rotations = self.rotations
        WIN.fill(WHITE)
        # draws the six faces of the cube
        for face in self.all_faces:
            self.draw_face(face)
        # draws the gray rectangle on the bottom of the screen
        bottom_rect = pygame.Rect(0, 450, 630, 180)
        pygame.draw.rect(WIN, GREY, bottom_rect)
        # displays the color options
        for color_box in color_boxes:
            pygame.draw.rect(WIN, color_box[1], color_box[0])
            pygame.draw.rect(WIN, BLACK, color_box[0], 1)
        # draws the rotation boxes
        x_location, y_location = 258, 493
        index = 1
        for rotation_box in rotations:
            pygame.draw.rect(WIN, rotation_box[1], rotation_box[0])
            pygame.draw.rect(WIN, BLACK, rotation_box[0], 1)
            # draws the text
            rotate_word = WORD_FONT.render(rotation_box[2], 1, BLACK)
            WIN.blit(rotate_word, (x_location, y_location))
            # changes coordinates for solve/scramble text
            if index == 12:
                y_location = 554
            if index == 13:
                y_location = 514
            # changes coordinates for x/y/z text
            if index == 14:
                y_location = 573
                x_location = 212
            if index >= 14:
                x_location += 45
            elif index % 2 == 0:
                x_location += 45
                y_location -= 40
            elif index % 2 == 1:
                y_location += 40
            index += 1
        # displays the possible color change of the tile
        if collide != False:
            display_rect = pygame.Rect(collide.x + 16, collide.y + 16, 20, 20)
            pygame.draw.rect(WIN, cur_color, display_rect)
        # displays the current rotation in the solver
        if solving_move == "Invalid Cube":
            rotate_word = SOLVING_FONT.render(solving_move, 1, RED)
            WIN.blit(rotate_word, (275, 65))
        elif solving_move != "":
            rotate_word = SOLVING_FONT.render(solving_move, 1, BLACK)
            WIN.blit(rotate_word, (395, 65))
            pygame.time.delay(500)
        pygame.display.update()

class RubikFace:
    '''
    This class will use the squares created from the RubikSquare class to create
        a single face of the Rubik's cube.
    The constructor will set the face to be at a specific x/y location and a
        specific color which changes based on the face.
    Methods:
         square_located(): Checks if a square is on the face
    '''
    def __init__(self, face):
        self.face = face
        self.x_location, self.y_location, self.color = get_location(self.face)
        self.tiles = create_face(self.x_location, self.y_location, self.color)

    def square_located(self, cur_square):
        '''
        This function determines if  square is located somewhere on the face.
        Parameters:
            cur_square: An object that contains all the information for a
                single square.
        Return Type:
            Returns a Boolean representing if the square was found.
        '''
        if cur_square in self.tiles:
            return True
        else:
            return False

class RubikSquare:
    '''
    This class will create a single square for the rubik's cube and
        hold information such as the color/location of the square.
    The constructor will create variables representing the current color of
        the square, the x/y location and the rect itself.
    Methods:
         draw_rect(): Draws the square onto the GUI
    '''
    def __init__(self, color, x, y):
        self.tile_color = color
        self.x = x
        self.y = y
        self.cur_rect = pygame.Rect(self.x, self.y, 40, 40)

    def draw_rect(self):
        '''
        This will draw the square onto the GUI with a black border
        '''
        pygame.draw.rect(WIN, self.tile_color, self.cur_rect)
        pygame.draw.rect(WIN, BLACK, self.cur_rect, 2)

    def get_coords(self):
        '''
        This function determines the coordinates of the square.
        Return Type:
            Returns a tuple representing the color of the square and two
            integers representing the x/y coordinates.
        '''
        return self.tile_color, self.x, self.y

def get_location(face):
    '''
    This will get the x/y location along with the starting color of
        the face.
    Parameters:
        face: A string representing the current face of the cube that
            information is needed for.
    Return Type:
        Returns two integers representing the x/y coordinates and a tuple
        representing the RGB value for the face.
    '''
    # gives the starting location/color for each of the faces
    if face == "top":
        x_location = 145
        y_location = 0
        color = YELLOW
    elif face == "bottom":
        x_location = 145
        y_location = 280
        color = WHITE
    elif face == "left":
        x_location = 5
        y_location = 140
        color = BLUE
    elif face == "right":
        x_location = 285
        y_location = 140
        color = GREEN
    elif face == "front":
        x_location = 145
        y_location = 140
        color = RED
    elif face == "back":
        x_location = 425
        y_location = 140
        color = ORANGE
    return x_location, y_location, color

def create_face(x_location, y_location, color):
    '''
    This will create nine separate rubik squares at a specific x/y
        coordinates to create a singular face of the cube.
    Parameters:
        x_location: An integer representing the x coordinate for the
            first square of the face.
        y_location: An integer representing the y coordinate for the
            first square of the face.
        color: A tuple representing the RGB value for the face.
    Return Type:
        Returns an array of the nine squares that make up the face.
    '''
    squares = []
    starting_x = x_location
    for index in range(3):
        # changes x/y to their correct locations
        x_location = starting_x
        y_location += 40
        for j in range(3):
            # creates the Rubik's tile at the correct x/y location
            new_tile = RubikSquare(color, x_location, y_location)
            x_location += 40
            squares.append(new_tile)
    return squares

def create_colors():
    '''
    This will create all the rects representing the color options
        the user can select and it stores the rects in an array.
    Return Type:
        Returns the array of rects.
    '''
    # creates the background color box
    background_box = [pygame.Rect(50, 486, 180, 118), WHITE]
    # creates the color selection option boxes
    yellow_box = (pygame.Rect(55, 493, 50, 50), YELLOW)
    red_box = (pygame.Rect(115, 493, 50, 50), RED)
    blue_box = (pygame.Rect(175, 493, 50, 50), BLUE)
    white_box = (pygame.Rect(55, 548, 50, 50), WHITE)
    green_box = (pygame.Rect(115, 548, 50, 50), GREEN)
    orange_box = (pygame.Rect(175, 548, 50, 50), ORANGE)
    color_boxes = [background_box, yellow_box, red_box, blue_box,
                   white_box, green_box, orange_box]
    return color_boxes

def create_buttons():
    '''
    This will create all the rects representing the clickable buttons
        the user can select and it stores the rects in an array.
    Return Type:
        Returns the array of rects.
    '''
    # creates the rotation buttons
    rotate_f = [pygame.Rect(245, 493, 35, 25), WHITE, "F"]
    rotate_f_prime = [pygame.Rect(245, 533, 35, 25), WHITE, "F'"]
    rotate_r = [pygame.Rect(290, 493, 35, 25), WHITE, "R"]
    rotate_r_prime = [pygame.Rect(290, 533, 35, 25), WHITE, "R'"]
    rotate_u = [pygame.Rect(335, 493, 35, 25), WHITE, "U"]
    rotate_u_prime = [pygame.Rect(335, 533, 35, 25), WHITE, "U'"]
    rotate_b = [pygame.Rect(380, 493, 35, 25), WHITE, "B"]
    rotate_b_prime = [pygame.Rect(380, 533, 35, 25), WHITE, "B'"]
    rotate_l = [pygame.Rect(425, 493, 35, 25), WHITE, "L"]
    rotate_l_prime = [pygame.Rect(425, 533, 35, 25), WHITE, "L'"]
    rotate_d = [pygame.Rect(470, 493, 35, 25), WHITE, "D"]
    rotate_d_prime = [pygame.Rect(470, 533, 35, 25), WHITE, "D'"]
    # creates the solve/scramble buttons
    solve_button = [pygame.Rect(515, 509, 92, 33), WHITE, "  Solve"]
    scramble_button = [pygame.Rect(515, 550, 92, 33), WHITE, "Scramble"]
    # creates the rotate buttons
    rotate_x = [pygame.Rect(245, 573, 35, 25), WHITE, "X"]
    rotate_x_prime = [pygame.Rect(290, 573, 35, 25), WHITE, "X'"]
    rotate_y = [pygame.Rect(335, 573, 35, 25), WHITE, "Y"]
    rotate_y_prime = [pygame.Rect(380, 573, 35, 25), WHITE, "Y'"]
    rotate_z = [pygame.Rect(425, 573, 35, 25), WHITE, "Z"]
    rotate_z_prime = [pygame.Rect(470, 573, 35, 25), WHITE, "Z'"]
    # adds the buttons to an array
    rotations = [rotate_f, rotate_f_prime, rotate_r, rotate_r_prime, rotate_u,
                 rotate_u_prime, rotate_b, rotate_b_prime, rotate_l,
                 rotate_l_prime, rotate_d, rotate_d_prime, solve_button,
                 scramble_button, rotate_x, rotate_x_prime, rotate_y,
                 rotate_y_prime, rotate_z, rotate_z_prime]
    return rotations

def color_clicked(current_colors, cur_position, cur_cube, color_select):
    '''
    This will check if any of the color options are selected and if so it
        will store the information in a variable.
    Parameters:
        current_colors: An array of rects representing the selectable
            color options.
        cur_position: A tuple representing the x/y coordinate of the cursor.
        cur_cube: An object representing the rubik's cube itself.
        color_select: A tuple representing the RGB value of the currently
            selected color.
    Return Type:
        Returns the tuple representing the currently selected color.
    '''
    for index in range(len(current_colors)):
        cur_button = current_colors[index][0]
        # checks if any of the color boxes were clicked
        if cur_button.collidepoint(cur_position) and index != 0:
            color_select = current_colors[index][1]
            # changes color of the background box
            current_colors[0][1] = color_select
    tile_clicked = cur_cube.is_collision(cur_position)
    if tile_clicked != False:
        # changes the color of the tile
        tile_clicked.tile_color = color_select
    return color_select

def button_clicked(all_buttons, cur_locations, cur_cube):
    '''
    This will check if any buttons on the bottom of the screen were
        clicked and if so it will call the appropriate function.
    Parameters:
        all_buttons: An array of rects representing the clickable buttons.
        cur_locations: An tuple representing the x/y coordinate of the cursor.
        cur_cube: An object representing the rubik's cube itself.
    Return Type:
        A string representing if the cube was a valid solve.
    '''
    for index in range(len(all_buttons)):
        cur_button = all_buttons[index][0]
        # runs a specific function for each button that is clicked
        if cur_button.collidepoint(cur_locations) and index == 0:
            f_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 1:
            f_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 2:
            r_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 3:
            r_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 4:
            u_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 5:
            u_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 6:
            b_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 7:
            b_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 8:
            l_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 9:
            l_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 10:
            d_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 11:
            d_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 12:
            valid_cube = cur_cube.is_valid()
            if valid_cube:
                solve_cube(cur_cube)
            else:
                return "Invalid Cube"
        elif cur_button.collidepoint(cur_locations) and index == 13:
            scramble_cube(cur_cube)
        elif cur_button.collidepoint(cur_locations) and index == 14:
            x_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 15:
            x_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 16:
            y_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 17:
            y_rotation(cur_cube, True)
        elif cur_button.collidepoint(cur_locations) and index == 18:
            z_rotation(cur_cube, False)
        elif cur_button.collidepoint(cur_locations) and index == 19:
            z_rotation(cur_cube, True)

def main():
    cur_cube = RubikCube()
    keep_running = True
    color_select, is_collide = WHITE, False
    valid_cube = ""
    # runs until the user exits out of the program
    while keep_running:
        cur_cube.draw_window(is_collide, color_select, valid_cube)
        for event in pygame.event.get():
            # determines the location of the cursor
            cur_position = pygame.mouse.get_pos()
            is_collide = cur_cube.is_collision(cur_position)
            # ends the program when the user exits out
            if event.type == pygame.QUIT:
                keep_running = False
                pygame.quit()
            # checks if the mouse is hovering over a button
            for button in cur_cube.rotations:
                if button[0].collidepoint(cur_position):
                    button[1] = LIGHT_GRAY
                else:
                    button[1] = WHITE

            if event.type == pygame.MOUSEBUTTONDOWN:
                # checks if a selection color is clicked
                color_select = color_clicked(cur_cube.color_boxes, cur_position, cur_cube, color_select)
                # checks if any remaining buttons are clicked
                valid_cube = button_clicked(cur_cube.rotations, cur_position, cur_cube)
                if valid_cube == None:
                    valid_cube = ""

if __name__ == main():
    main()