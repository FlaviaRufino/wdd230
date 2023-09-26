import tkinter as tk
import random
import math 


def main():
    # Width and height of the scene in pixels
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Creating a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing
    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, etc.
    
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)

    draw_land(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)
    
    draw_moon(canvas, 100, 100)
    
    draw_cloud(canvas=canvas, left=400, top=220, right=500, bottom=300)
    draw_cloud(canvas=canvas, left=500, top=50, right=600, bottom=100)

    tree_center = scene_left + 600
    tree_top = scene_top + 250
    tree_height = 200
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 700
    tree_top = scene_top + 100
    tree_height = 350
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, left, top, right, bottom, grid_spacing):
    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i, fill="blue4")
    # canvas.create_rectangle(0, 0, 799, 599, fill="")

def draw_land(canvas, left, top, right, bottom, grid_spacing):
    # Draw horizontal lines
    for i in range(400, bottom, grid_spacing):
        canvas.create_line(left, i, right, i, fill="darkgreen")
    # canvas.create_rectangle(0, 474, 799, 599, fill="")

def draw_moon(canvas, moon_left, moon_top, scale=1, ray_count=10, fill="yellow2"):
    moon_width = 100 * scale 
    moon_height = 100 * scale 
    ray_length = 100 * scale 
    ray_width = 3 * scale 

    moon_right = moon_left + moon_width
    moon_bottom = moon_top + moon_height 
    moon_center_x = moon_left + (moon_width / 2)
    moon_center_y = moon_top + (moon_height / 2)

    canvas.create_oval(moon_left, moon_top, moon_right, moon_bottom, fill="yellow2", width=False)

def draw_cloud(canvas, left, top, right, bottom):
    upper_top = top - 50
    upper_bottom = bottom - 50
    lower_top = top + 50
    lower_bottom = bottom + 50

    for i in range(0, 4):
        canvas.create_oval(left, top, right, bottom, fill="lightBlue1", width=False)
        left -= 50
        right -= 50
    
    left = 380
    right = 480

    for i in range(0, 3):
        canvas.create_oval(left, upper_top, right, upper_bottom, fill="lightBlue1", width=False)
        left -= 50
        right -= 50

    left = 150
    right = 80

def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="green4")


# Call the main function.
main()