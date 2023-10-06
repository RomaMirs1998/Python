import PyPDF2


#The standard way to open a file is:

with (open("dummy.pdf","rb")) as file : # rb = read binary -> to read pdf file in binary mode
    # print(file) -> without using PyPDF2
    reader = PyPDF2.PdfFileReader(file) # to read pdf file using PyPDF2 -> the PyPDF2.PdfFileReader() method takes a binary file as an argument
    print(reader.numPages)
    print(reader.getPage(0)) # to get the first page of the pdf file
    page = reader.getPage(0) # to get the first page of the pdf file
    print(page.rotateClockwise(180)) # to rotate the pdf file
    with open("tilt.pdf","wb") as new_file:
        writer = PyPDF2.PdfFileWriter() # to write a new pdf file
        writer.addPage(page) # to add the page to the new pdf file
        writer.write(new_file) # to write the new pdf file

