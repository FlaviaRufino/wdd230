# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import tkinter as tk
import random
import math 

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_house(canvas, scene_width, scene_height)
    draw_bird(canvas, scene_width, scene_height)
    draw_picket(canvas, scene_width, scene_height)
    draw_glass_blade(canvas, scene_width, scene_height)
    draw_flower(canvas, scene_width, scene_height)
    draw_pebble(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

# # def draw_sky(canvas, scene_width, scene_height):
# #     """Draw the sky and all the objects in the sky."""
# #     draw_rectangle(canvas, 0, scene_height / 3,
# #         scene_width, scene_height, width=0, fill="sky blue")

#     # Draw a bird.
#     bird_center_x = 180
#     bird_top = 90
#     bird_height = 10
#     draw_bird(canvas, scene_width, scene_height)

# def draw_ground(canvas, scene_width, scene_height):
#     """Draw the ground and all the objects on the ground."""
#     draw_rectangle(canvas, 0, 0,
#         scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_bird(canvas, scene_width, scene_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    # Draw a House.
    house_right_x = 180
    house_bottom = 90
    house_height = 50
    draw_house(canvas, scene_width, scene_height, 10, 20,) 

    # Draw a picket.
    picket_right_x = 160
    picket_bottom = 110
    picket_height = 15
    draw_picket(canvas, scene_width, scene_height) 

    # Draw a glass blade.
    glass_blade_center_x = 175
    glass_blade_bottom = 90
    glass_blade_height = 17
    draw_glass_blade(canvas, scene_width, scene_height)

    # Draw a flower.
    flower_right_x = 165
    flower_bottom = 90
    flower_height = 7
    draw_flower(canvas, scene_width, scene_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


def draw_house(canvas, house_right_x, house_bottom, height, center_x, bottom):
    wall_width = height / 50
    wall_height = height / 150
    wall_left = center_x - wall_width / 2
    wall_right = center_x + wall_width / 2
    walll_top = bottom + wall_height

# def draw_bird(canvas, bird_center, bird_top, height):
#     bird_width = height / 4
#     bird_height = height / 15
#     bird_center = center_x - bird_width / 2
#     bird_left = center_x + bird_width / 2
#     bird_top = top + bird_height

# def draw_picket(canvas, picket_right_x, picket_bottom, height):
#     picket_width = height / 20
#     picket_height = height / 5
#     picket_left = center_x - picket_width / 2
#     picket_right = center_x + picket_width / 2
#     picket_top = bottom + picket_height

# def draw_grass_blade(canvas, glass_blade_center_x, glass_blade_bottom, blade_height):
#     glass_blade_width = height / 8
#     glass_blade_height = height / 4
#     glass_blade_left = center_x - glass_blade_width / 2
#     glass_blade_right = center_x + glass_blade_width / 2
#     glass_blade_top = bottom + glass_blade_height

# def draw_flower(canvas, flowers_right, flowers_botom, height):
#     flower_width = height / 3
#     flower_height = height / 6
#     flower_left = center_x - flower_width / 2
#     flower_right = center_x + flower_width / 2
#     flower_top = bottom + flower_height

# Call the main function so that
# this program will start executing.
main()
