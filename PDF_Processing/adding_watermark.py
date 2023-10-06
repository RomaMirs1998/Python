import PyPDF2

pdf_without_watermark = PyPDF2.PdfFileReader(open("super.pdf","rb")) # to read the pdf file without watermark

pdf_with_watermark = PyPDF2.PdfFileReader(open("wtr.pdf","rb")) # to read the pdf file with watermark

output = PyPDF2.PdfFileWriter() # to write a new pdf file

for i in range(pdf_without_watermark.getNumPages()): # to loop through all the pages of the pdf file without watermark
    page = pdf_without_watermark.getPage(i) # to get the page
    page.mergePage(pdf_with_watermark.getPage(0)) # to merge the page with the watermark
    output.addPage(page) # to add the page to the new pdf file

    with open("watermarked_output.pdf","wb") as file: # to write the new pdf file
        output.write(file) # to write the new pdf file

print("All done!")