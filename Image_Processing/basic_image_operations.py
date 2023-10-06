from PIL import Image, ImageFilter

#open the image
image = Image.open("./Pokedex/pikachu.jpg")

#filter the image
#filter method -> BLUR, SMOOTH, SHARPEN, EDGE_ENHANCE, FIND_EDGES, CONTOUR, EMBOSS, DETAIL .....etc
filteredImage = image.filter(ImageFilter.BLUR)
#save the filtered image
filteredImage.save("blur.png", "png")

# convert the image to Smoothing
filteredImage = image.filter(ImageFilter.SMOOTH)
#save the filtered image
filteredImage.save("smooth.png", "png")

# convert the image to Sharpen
filteredImage = image.filter(ImageFilter.SHARPEN)
#save the filtered image
filteredImage.save("sharpen.png", "png")

# convert the image to Edge Enhance
filteredImage = image.filter(ImageFilter.EDGE_ENHANCE)
#save the filtered image
filteredImage.save("edge_enhance.png", "png")

#convert the image to black and white
# convert Method -> L = black and white , RGB = color , RGBA = color with alpha channel (transparency)
filteredImage = image.convert("L")
#save the filtered image
filteredImage.save("grey.png", "png")

#roatet the image by 90 degree
filteredImage = image.rotate(90)
#save the filtered image
filteredImage.save("rotate.png", "png")

#resize the image
filteredImage = image.resize((300, 300))
#save the filtered image
filteredImage.save("resize.png", "png")

#crop the image
box = (100, 100, 400, 400)
filteredImage = image.crop(box)
#save the filtered image
filteredImage.save("crop.png", "png")


#get the image size
print(image.size)

#get the image format
print(image.format)

#show the image mode
print(image.mode)

# get all the attributes of the image
print(dir(image))

#show the filtered_image in a new window
filteredImage.show()
