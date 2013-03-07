"""
    INPUT:
        no command line arguments.  This assumes that all
        images in a folder called 'img'  should
        be the same size.

    OUTPUT:

        a spritesheet, as well as a txt file containing all the
        size/location data for eacch sprite
"""

from PIL import Image
import os

# case where no command line args were passed
# look for a folder called img
max_width = 0
total_height = 0

imageList = [Image.open("./img/" + i) for i in os.listdir("./img/")]

# loop through all the images in the folder to determine the dimensions
# of our spritesheet
for img in imageList:

    if (max_width < img.size[0]):
        max_width = img.size[0]

    total_height += img.size[1]



sheet = Image.new("RGBA", (max_width, total_height))


y_loc = 0


fd = open('sprite_definitions.txt', 'w')


# add each sprite to the total sheet
for img in imageList:

    fd.write("Upper Left X: 0\nUpper Left Y: " + str(y_loc)
            + "\nWidth: " + str(img.size[0]) + "\nHeight: "
            + str(img.size[1]) + "\n\n")

    sheet.paste(img,(0,y_loc))
    y_loc += img.size[1]















