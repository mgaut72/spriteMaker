"""

    INPUT:

        1)  no command line arguments.  This assumes that all
            images in a folder called 'img'  should
            be the same size.

            All images will be scaled down to the size of the
            smallest image in the folder, and combined into a
            spritesheet.

        2)  1... arguments.

            This assumes that the directories, whose names are
            passed as arguments, contain images of different
            size.  For each directory passed as an argument,
            scale all the images down to the size of the smallest
            image in that folder, then add that set to the
            spritesheet.

            proceed with the next folder, adding the sprites to a
            "new line" in the spritesheet

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

for sprt in os.listdir("./img/"):
    img = Image.open("./img/" + sprt)
    print ("opened the img" + sprt)
    #if (max_width < img.size[0]):
    #    max_width



