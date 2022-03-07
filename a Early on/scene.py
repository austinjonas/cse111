# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import math
import random
from cProfile import label
from pyexpat.errors import XML_ERROR_UNCLOSED_CDATA_SECTION
from turtle import right
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # draw_pine_tree(canvas, 550, 150, 250)
    draw_sky(canvas, scene_width, scene_height, 1)


    #draw stars
    draw_stars(canvas, scene_width, scene_height, 1, 300)


    # draw clouds
    diameter = 50
    space = 5
    interval = diameter + space
    x = 100
    y = 400
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 20, y - 5, x + diameter * 1.5, y + diameter * 1.5, fill = "white", outline = "white")
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 150, y - 80, x + diameter * 1.5, y + diameter * 1.5, fill = "white", outline = "white")
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 150, y - 5, x + diameter * 1.9, y + diameter * 1.9, fill = "white", outline = "white")
    
    

    #draw mountains, includes loop
    draw_mountains(canvas, 710, 170, 320)
    for x in range(50, 700, 50):
        over = x + 200
        draw_stubby_mountain(canvas, over, 180, 250)
    draw_mountains(canvas, 80, 180, 300)
    draw_oval(canvas, x + 200, y, x + 200, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 500, y - 5, x + diameter * 1.5, y + diameter * 1.5, fill = "white", outline = "white")
    draw_stubby_mountain(canvas, 600, 175, 278)
    draw_mountains(canvas, 680, 170, 320)
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 20, y - 5, x + diameter * 1.5, y + diameter * 1.5, fill = "white", outline = "white")
    draw_mountains(canvas, 300, 170, 325)
    draw_stubby_mountain(canvas, 483, 175, 278)
    draw_oval(canvas, x + 257, y, x + diameter, y + diameter, fill = "white", outline = "white")
    draw_oval(canvas, x + 20, y - 5, x + diameter * 1.5, y + diameter * 1.5, fill = "white", outline = "white")


    #draw ground    
    draw_ground(canvas, scene_width, scene_height / 3, 1)
    #draw_snowman(canvas, scene_width, scene_height, 10, 200, 200)
    

    #loop to draw forest
    
    for x in range(100, 700, 100):
        draw_pine_tree(canvas, x, 80, 80)
    draw_pine_tree(canvas, 100, 60, 150)
    draw_pine_tree(canvas, 700, 60, 150)

    # draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas) 


# Define your functions such as
# draw_sky and draw_ground here.
def draw_pine_tree(canvas, center_x, bottom, height):
    #draw trunk of tree
    trunk_width = height / 10
    trunk_height = height / 5
    left_trunk = center_x - (trunk_width / 2)
    bottom_trunk = bottom
    right_trunk = center_x + (trunk_width / 2)
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, 
    trunk_top, fill = "tan4")

    #draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - (skirt_width / 2)
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + (skirt_width / 2)
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x,
    peak_y, skirt_right, skirt_bottom, fill = "forestGreen")

def draw_mountains(canvas, center_x, bottom, height):
    #draw tall mountain
    mtn_base = height * .4
    mtn_left = center_x - (mtn_base / 2)
    mtn_bottom = bottom
    peak_x = center_x
    peak_y = bottom + height
    mtn_right = center_x + (mtn_base / 1.5)
    draw_polygon(canvas, mtn_left, mtn_bottom, peak_x, peak_y, 
    mtn_right, mtn_bottom, fill = "seashell4")

def draw_stubby_mountain(canvas, center_x, bottom, height):
    #draw stubby mountain
    mtn_base = height * .8
    mtn_left = center_x - (mtn_base / 2)
    mtn_bottom = bottom
    peak_x = center_x
    peak_y = bottom + height
    mtn_right = center_x + (mtn_base / 1.5)
    draw_polygon(canvas, mtn_left, mtn_bottom, peak_x, peak_y, 
    mtn_right, mtn_bottom, fill = "peachPuff4")



def draw_sky(canvas, width, height, interval):
    label_y = 1
    for x in range(interval, width, interval):
        draw_line(canvas, x, 1, x, height, fill = "purple4")
        # draw_line(canvas, x, 1, x, height, fill = "deepSkyBlue")


def draw_ground(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, 195, fill = "bisque4")


def draw_grid(canvas, width, height, interval):
   #draw vertical line
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    #draw horizontal line
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

def draw_stars(canvas, scene_width, scene_height, star_size, num_starts):
    for i in range(num_starts):
        x = random.randint(0, scene_width)
        y = random.randint(math.ceil(scene_height / 3), scene_height)
        draw_oval(canvas, x, y, x + star_size, y + star_size, fill = "black")

#def draw_snowman(canvas, scene_width, scene_height, circle_size, x, y):
    #draw_oval(canvas, x, y, circle_size, fill = "black")



# Call the main function so that
# this program will start executing.
main()