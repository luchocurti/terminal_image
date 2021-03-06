#! python3

'''
Usage: python terminal_image.py image_name.ext [character] [Image_width] [Image_height] [BW]
'''

# Import external modules:
from PIL import Image, ImageFilter
import os
import sys


# General definitions:
VERSION = "V1.0.4"
DEBUGGING = False

SUPPORTED_FILE_FORMATS = [".BMP", ".DIB", ".EPS", ".GIF", ".ICNS", ".ICO",
                          ".IM", ".JPEG", ".JPG", ".MSP", ".PCX", ".PNG",
                          ".PPM", ".SGI", ".SPIDER", ".TGA", ".TIFF", ".WEBP",
                          ".XBM"]

CHAR_DEFAULT = u"\u2588"    # Unicode Full Block
CHAR_BLACK = " "

MIN_CHAR_VAL = 32           # Char = Space
MAX_CHAR_VAL = 127          # Char = Delete

IMAGE_X_DEFAULT = 60
IMAGE_Y_DEFAULT = 30

HALF_SCALE = (256 // 2)     # The full scale uses 1 Byte deep
PIXEL_WIDTH = 2

EDIT_COMMAND = "\033["

STYLE_RESET = EDIT_COMMAND + "0m"
STYLE_BRIGHT = EDIT_COMMAND + "1m"

FORE_BLACK = EDIT_COMMAND + "30m"
FORE_RED = EDIT_COMMAND + "31m"
FORE_GREEN = EDIT_COMMAND + "32m"
FORE_YELLOW = EDIT_COMMAND + "33m"
FORE_BLUE = EDIT_COMMAND + "34m"
FORE_MAGENTA = EDIT_COMMAND + "35m"
FORE_CYAN = EDIT_COMMAND + "36m"
FORE_WHITE = EDIT_COMMAND + "37m"


# Get the color of the 8 possible saturated values:
def get_color(red, green, blue):
    """
    Function:   get_color(red, green, blue)
    Summary:    Get the color of the 8 possible saturated values
    Receive:    Red, green and blue values as booleans
    Return:     ASCII command to change the terminal color
    """

    if red and green and blue:
        return(FORE_WHITE)
    if red and green and not blue:
        return(FORE_YELLOW)
    if red and not green and blue:
        return(FORE_MAGENTA)
    if red and not green and not blue:
        return(FORE_RED)
    if not red and green and blue:
        return(FORE_CYAN)
    if not red and green and not blue:
        return(FORE_GREEN)
    if not red and not green and blue:
        return(FORE_BLUE)
    if not red and not green and not blue:
        return(FORE_BLACK)


# This is executed only when the file is used as a script:
def print_image(arg_list, directory):
    """
    Function:   print_image(arg_list, directory)
    Summary:    Display an image in the Command Prompt (CMD) as a matrix of text characters
    Receive:    arg_list = A list of the following arguments:
                    - "python"              # String
                    - "terminal_image.py"   # String - Name of the script
                    - "image_name.ext"      # String - Name of the image + its extension
                    - [character]           # An optional character
                    - [Image_width]         # An optional image width (number of characters)
                    - [Image_height]        # An optional image height (number of characters)
                    - [BW]                  # An optional to print the image in Black and White
                directory = A string representing the program directory
    Return:     0: If success / Not 0: A string (The error message)
    """

    # Show the correct order of the argument list:
    print(
        "\nList of Arguments: python terminal_image.py image_name.ext [character] [Image_width] [Image_height] [BW]\n")

    # Get the number of arguments received:
    arguments = len(arg_list)

    # Only for debugging purposes:
    if DEBUGGING:
        # Print the arguments received:
        print("Number of arguments: {0}".format(arguments))
        print("List of arguments: ")
        for index in range(arguments):
            print("\t> #{0} = {1}".format(index, arg_list[index]))
        print(" ")

    # Check if there is an image in the arguments:
    if arguments >= 2:
        # Get the name of the file:
        file_name = arg_list[1]

        # Check if the user enters an absolute or relative path:
        if file_name.startswith("/") or file_name.startswith("\\"):
            # Create the full absolute path of the file:
            file_path = os.path.join(os.path.abspath(os.sep), file_name)
        else:
            # Create the full relative path of the file:
            file_path = os.path.join(directory, file_name)

        # Check if the file exists:
        if os.path.isfile(file_path):
            # Get the extension of the file:
            root, extension = os.path.splitext(file_path)

            # Check if the file format is supported by Pillow:
            if extension.upper() in SUPPORTED_FILE_FORMATS:
                # Try to run the image processing:
                try:
                    # Open the image:
                    imageOriginal = Image.open(file_path)

                    # Create copies of the original image to manipulate them:
                    imageScaled = imageOriginal
                    imageBlackWhite = imageScaled

                    # Only for debugging purposes:
                    if DEBUGGING:
                        # Print the image attributes:
                        print("Original image attributes:")
                        print("------------------------- ")
                        print("File name:\t{0}".format(imageOriginal.filename))
                        print("Format:\t\t{0}".format(imageOriginal.format))
                        print("Mode:\t\t{0}".format(imageOriginal.mode))
                        print("Size:\t\t{0}".format(imageOriginal.size))
                        print("Width:\t\t{0} pixels".format(
                            imageOriginal.width))
                        print("Height:\t\t{0} pixels".format(
                            imageOriginal.height))
                        print("Palette:\t{0}".format(imageOriginal.palette))
                        print(" ")

                    # Set the character used to create the terminal image:
                    fillChar = CHAR_DEFAULT

                    # Check if the user wants to set a specific character:
                    if arguments >= 3:
                        # Get the value of the first character:
                        new_char_val = ord(arg_list[2][0])

                        # Check if it is a printable character:
                        if (new_char_val > MIN_CHAR_VAL) and (new_char_val < MAX_CHAR_VAL):
                            # Set the new desired character:
                            fillChar = arg_list[2][0]

                    # Set the width of the terminal image:
                    image_x_size = IMAGE_X_DEFAULT

                    # Check if the user set a specific width:
                    if arguments >= 4:
                        # Check if the value is a number:
                        if arg_list[3].isdigit():
                            # Check if the number is greater than zero:
                            if int(arg_list[3]) > 0:
                                # Get the new value:
                                image_x_size = int(arg_list[3])
                            else:
                                print("Warning: Image width must be greater than 0")
                        else:
                            print("Warning: The width of the image must be a number")

                    # Set the height of the terminal image:
                    image_y_size = IMAGE_Y_DEFAULT

                    # Check if the user set a specific height:
                    if arguments >= 5:
                        # Check if the value is a number:
                        if arg_list[4].isdigit():
                            # Check if the number is greater than zero:
                            if int(arg_list[4]) > 0:
                                # Get the new value:
                                image_y_size = int(arg_list[4])
                            else:
                                print(
                                    "Warning: Image height must be greater than 0")
                        else:
                            print(
                                "Warning: The height of the image must be a number")

                    # Scale the image to the new size:
                    imageScaled.thumbnail((image_x_size, image_y_size))

                    # Convert the image into Grayscale:
                    imageGrayScale = imageScaled.convert('LA')

                    # Only for debugging purposes:
                    if DEBUGGING:
                        # Display the modified image:
                        imageGrayScale.show()

                    # Check if the user wants to show the image in Black and White:
                    if (arguments >= 6) and (arg_list[5] == "BW"):
                        # Move over each row:
                        for row in range(imageGrayScale.height):
                            # Start from an empty string:
                            string = ""

                            # Move over each column:
                            for column in range(imageGrayScale.width):
                                # Read each pixel Grayscale value:
                                pixel_gray = imageGrayScale.getpixel((column, row))[
                                    0]

                                # Check if it has to print a character or a blank space:
                                if pixel_gray > HALF_SCALE:
                                    # Add the character to the string:
                                    string += (fillChar * PIXEL_WIDTH)
                                else:
                                    # Add a blank space to the string:
                                    string += (CHAR_BLACK * PIXEL_WIDTH)

                            # Print the whole row:
                            print(string)

                    # Default case - The image is shown in colors:
                    else:
                        # Enable the terminal to use VT100 Escape Sequence (colors):
                        os.system('')

                        # Move over each row:
                        for row in range(imageScaled.height):
                            # Start from an empty string:
                            string = ""

                            # Move over each column:
                            for column in range(imageScaled.width):
                                # Read the colors of the pixel:
                                red, green, blue = imageScaled.getpixel(
                                    (column, row))

                                # Saturate colors to 0/1 values:
                                red //= HALF_SCALE
                                green //= HALF_SCALE
                                blue //= HALF_SCALE

                                # Add color to the next character:
                                string += get_color(red, green, blue)

                                # Check if it has to print a character or a blank space:
                                if get_color(red, green, blue) is not FORE_BLACK:
                                    # Add brightness to the character:
                                    string += STYLE_BRIGHT

                                    # Add the character to the string:
                                    string += (fillChar * PIXEL_WIDTH)

                                # If the color is Black:
                                else:
                                    # Add a blank space to the string:
                                    string += (CHAR_BLACK * PIXEL_WIDTH)

                                # Disable the text style:
                                string += STYLE_RESET

                            # Print the whole row:
                            print(string)

                    # Close the image pointers:
                    imageOriginal.close()
                    imageScaled.close()
                    imageBlackWhite.close()

                    # Return the success value:
                    return(0)

                # Catch the exceptions:
                except Exception as e:
                    # Print the exception message:
                    print("Exception: {0}".format(e.__class__.__name__))

                    # Return an error message:
                    return("It is not possible to open the image")

            else:
                # Return an error message:
                return("The file format is not supported")

        else:
            # Return an error message:
            return("The image file does not exist")

    else:
        # Return an error message:
        return("Add the name of an image after the program name")


# Starting point - Check if the file is used as a Script:
if __name__ == "__main__":
    # Only for debugging purposes:
    if DEBUGGING:
        print(" ")
        print("Function print_image documentation: {0}".format(
            print_image.__doc__))
        print("Function get_color documentation: {0}".format(
            get_color.__doc__))

    # Call the "main" function and pass command line arguments as parameters:
    result = print_image(sys.argv, os.getcwd())

    # Check if there was an error:
    if result != 0:
        # Print the error:
        print("Error: {0}".format(result))


# The file is imported as a module:
else:
    print("Thanks for using terminal_image as a module")
