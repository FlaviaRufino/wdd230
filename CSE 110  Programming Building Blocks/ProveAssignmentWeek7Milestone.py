from PIL import Image

image_snowscape = Image.open("snowscape.jpg")
image_penguin = image.open("penguin.jpg")

print(image_snowscape.size)
print(image_snowscape.format)
print(image_penguin.size)
print(image_penguin.format)

image_combined = image.new("RGB", image_snowscape.size)
(width, height) = image_snowscape.size
print(f"width: {width}")
print(f"height: {height}")

pixels_snowscape = image_snowscape.load()
pixels_penguin = image_penguin.load()

print(pixels_snowscape[235, 432])
print(pixels_penguin[348, 579])

pixels_snowscape[100, 50] = (500, 0, 170)
pixels_snowscape[200, 150] = (400, 0, 256)
pixels_snowscape[301, 207] = (300, 0, 315)
pixels_snowscape[422, 400] = (200, 0, 405)
pixels_snowscape[500, 350] = (100, 0, 530)

for y in range(237, 589):
    for x in range(7, 12):
        (r, g, b) = pixels_snowscape[x, y]
        if r != 50 and g != 34 and b!= 92 :  
            new_red = r + 20
            pixels_snowscape[x, y] = (r, g, new_red)

#image_snowscape.show()
image_snowscape.save("snowscape_penguin.jpg")
