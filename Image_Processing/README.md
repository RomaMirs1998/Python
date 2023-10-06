# Image Processing with Python and PIL

This Project contains scripts and exercises related to image processing using the Python Imaging Library (PIL), a part of the Pillow library.

## Table of Contents
- [Exercise: Image Conversion](#exercise-image-conversion)
- [Basic Image Operations](#basic-image-operations)
- [Downsize Images](#downsize-images)

## Exercise: Image Conversion

**Goal:** Write a script that converts all images in a specified directory from their current format to PNG and saves them in another directory.

**Steps:**
1. Import the necessary libraries.
2. Ensure the script is being run as the main program.
3. Get the command line arguments. (Hint: The script should be run as `script_name.py source_directory destination_directory`).
4. Check if the destination directory exists; if not, create it.
5. Loop through each file in the source directory and:
   - Open the image using PIL.
   - Convert the image to RGB format.
   - Save the image with a PNG extension in the destination directory.
   - Print a message indicating the conversion was successful for each image.
6. Print a message once all images are converted.

> **Tip:** Use the PIL library from Pillow for image operations.

## Basic Image Operations

In this section, you'll learn basic operations you can perform on images, including:
- Filtering (e.g., BLUR, SMOOTH, SHARPEN, etc.)
- Conversion (e.g., to grayscale, RGB, etc.)
- Rotation and resizing
- Cropping
- Retrieving image attributes

Please refer to the provided script to see implementations of the operations above.

## Downsize Images

Downsizing images is a common task in image processing, especially for web applications. This section covers:
- Resizing images without preserving aspect ratio.
- Using the thumbnail method to resize images while preserving aspect ratio.
- Observing the changes in image dimensions after resizing.

For implementations and detailed comments, refer to the provided script in this section.

---

Feel free to explore the repository, run the scripts, and modify them to better understand the functionalities provided by PIL for image processing.