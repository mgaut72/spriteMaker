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

# loop through all the images in the folder to determine the dimensions
# of our spritesheet
for sprt in os.listdir("./img/"):
    img = Image.open("./img/" + sprt)

    if (max_width < img.size[0]):
        max_width = img.size[0]

    total_height += img.size[1]



sheet = Image.new("RGBA", (max_width, total_height))


y_loc = 0


fd = open('sprite_definitions.txt', 'w')


# add each sprite to the total sheet
for sprt in os.listdir("./img/"):
    img = Image.open("./img/" + sprt)

    fd.write(sprt + "\nUpper Left X: 0\nUpper Left Y: " + str(y_loc)
            + "\nWidth: " + str(img.size[0]) + "\nHeight: "
            + str(img.size[1]) + "\n\n")

    sheet.paste(img,(0,y_loc))
    y_loc += img.size[1]















