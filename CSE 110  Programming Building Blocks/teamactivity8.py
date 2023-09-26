
from PIL import Image

# Display to check if pillow install without error
print("The library is loaded correctly")

#Variable contain the image we will open
image_original = Image.open("cse110_images/beach.jpg")

# Assign the pixels image in the variable
pixels_original = image_original.load()


for x in range(100, 201):
    """
    This loop help us to display the RGB number with corresponding pixels of image
    and set a new color value for corresponding pixels.
    """
    for y in range(200, 505) :
        (r, g, b) = pixels_original[x, y]
    
        print(f"RGB number {r, g, b} corresponding to pixels {x, y}\n")
        
        pixels_original[x, y] = (r + x, y - g, b - x)
        print(f"Pixels {x, y} corresponding to pixels RGB values {(r + x, y - g, b - x)}\n")
        
# help to show image and observe the changed pixels.
image_original.show()

