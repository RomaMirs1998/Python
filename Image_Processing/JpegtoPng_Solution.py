from PIL import Image
import sys
import os

if __name__ =="__main__":
    try:
        # get the first and second argument
        image_folder = sys.argv[1]
        output_folder = sys.argv[2]
    except IndexError:
        print("Please provide the source folder and destination folder")
        sys.exit(1)

    # check if new/ exists, if not create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # loop through the folder and convert the images to png
    for image in os.listdir(image_folder):

        try:
            act_image = Image.open(f".\\{image_folder}\\{image}") # .\\ is used to specify the current directory
            new_image=act_image.convert("RGB") # convert the image to RGB
            print(image[:-4])
            new_image.save(f".\\{output_folder}\\{image[:-4]}.png","png") # save the image as png
            print(f"converted {image} to png")
        except:
            print(f"Unable to convert {image} to png")

    print("All done!")


