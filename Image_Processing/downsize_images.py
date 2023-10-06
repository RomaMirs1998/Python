from PIL import Image

#open the image
image = Image.open("./Other_Images/astro.jpg")

#print image size
print(image.size) # (width, height)

#resize the image
#resize method will resize the image in place and it will not keep the aspect ratio of the image
new_image = image.resize((400, 400))
#save the new_image
new_image.save("austro_resize.jpg","jpeg")

#print image size
print(image.size)

#using thumbnail method to resize the image (thumbnail method will resize the image in place)
#thumbnail method will keep the aspect ratio of the image
# it is usefull when we want to resize the image for the web page or something like that
# it changes the height for a better aspect ratio but never the width of the image
image.thumbnail((400, 400))
#save the image
image.save("thumbnail.jpg","jpeg")

#print image size
print(image.size)



new_image.show()
image.show()