import pygame, sys

# First thing in any pygame program - initializes pygame's internal variables.
pygame.init()

# set up variables for the screen size in pixels
size = width, height = 640, 480

# initialize a window with the screen size you set
screen = pygame.display.set_mode(size)

# create a clock, which will be used to control the program's frame rate
clock = pygame.time.Clock()

# create variables to store location and size of a shape to draw on screen.
shape_position = (width / 2, height / 2)
shape_size = (100, 100)

# make a pygame.Rect variable for the shape:
shape_rect = pygame.Rect(shape_position, shape_size)

# RGB colors of the shapes to draw
shape_color = (142, 58, 60)
line_color = (51, 116, 48)
circle_color = (143, 122, 59)

# Circle
x = 320
y = 240
circle_pos = (x, y)

move_right = False
move_left = False
move_UP = False
move_down = False
# Game loop
x1 = 580
y1 = 480
x2 = 580
y2 = 200
while True:
    y = y + 1

    # tick forward at 60 frames per second
    clock.tick(60)

    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            sys.exit()
        # This event happens when a key is pressed.
        elif event.type == pygame.KEYDOWN:
            # This checks to see if the key that was pressed is the left arrow key.
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_UP:
                move_UP = True
            if event.key == pygame.K_DOWN:
                move_down = True
            # elif to continue
        # This event happens when a key is released
        elif event.type == pygame.KEYUP:
            # This checks to see if the key that was released is the left arrow key.
            if event.key == pygame.K_RIGHT:
                move_right = False
            # elif to continue
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_UP:
                move_left = False
            if event.key == pygame.K_UP:
                move_UP = False
            if event.key == pygame.K_DOWN:
                move_down = False
            # elif to continue
            # This event happens when a key is rele
            # elif to continue


    if move_right:
        # Extend this to be done with variables if there's more time.
        # Double division is required, as tuples for PyGame positions must
        # be an integer (int) value.
        x = x + 0

    if move_left:

        # Extend this to be done with variables if there's more time.
        # Double division is required, as tuples for PyGame positions must
        # be an integer (int) value.
        x = x - 0

    # Extension Question: should you use if or elif statements for the other movement options?


    if move_UP:
        # Extend this to be done with variables if there's more time.
        # Double division is required, as tuples for PyGame positions must
        # be an integer (int) value.
        y = y - 15
        move_UP = False
    if move_down:
        # Extend this to be done with variables if there's more time.
        # Double division is required, as tuples for PyGame positions must
        # be an integer (int) value.
        y = y + 0
    if x < 0:
        x = 0
    if x > 640:
        x = 640
    if y < 0:
        sys.exit("you died")
    if y > 480:
        sys.exit("you died")

    # Extension Question: should you use if or elif statements for the other movement options?
    # Fill the screen with a solid color.
    # Comment this out to "paint" a picture with player movement.
    screen.fill((50, 50, 100))

    # Fill a rectangular area with the shape color. This is the fastest way to draw rectangles to the screen.
    # screen.fill(shape_color, rect=shape_rect)

    # Draws a circle on the given surface, color, position, and radius.
    circle_pos = (x, y)
    pygame.draw.circle(screen, circle_color, circle_pos, 25)
    x1 = x1 - 1
    x2 = x2 - 1
    line_pos = (x1, y1)
    line_pos2 = (x2, y2)
    pygame.draw.line(screen, (0,255,0), line_pos, line_pos2, 15)
    if x > x1:
        if y > y1:

            sys.exit("you died")
    # Draws a line on the given surface, color, start position, end position, and line width in pixels.
    # This draws a line between the two shapes
    # pygame.draw.line(screen, line_color, circle_pos, shape_rect.center, 4)

    # At the end of each game loop, call pygame.display.flip() to update the screen with what you drew.
    pygame.display.flip()