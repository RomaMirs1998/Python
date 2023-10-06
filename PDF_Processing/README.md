# PDF Manipulation Tool

This project provides utilities to manipulate PDF files using the PyPDF2 library. You can add watermarks, rotate pages, and combine multiple PDFs into one.
Features:

   - Watermarking: Add watermark from one PDF to all the pages of another PDF.
   - Page Rotation: Rotate a page by 180 degrees.
   - PDF Combiner: Combine multiple PDFs into a single PDF.

How to Use:
## 1. Watermarking:

To watermark a PDF, place your PDF (super.pdf) and watermark (wtr.pdf) in the project directory. Run the script and the watermarked output will be saved as watermarked_output.pdf.

```python

import PyPDF2

pdf_without_watermark = PyPDF2.PdfFileReader(open("super.pdf","rb"))
pdf_with_watermark = PyPDF2.PdfFileReader(open("wtr.pdf","rb"))
output = PyPDF2.PdfFileWriter()

for i in range(pdf_without_watermark.getNumPages()):
    page = pdf_without_watermark.getPage(i)
    page.mergePage(pdf_with_watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf","wb") as file:
        output.write(file)

print("All done!")
```
## 2. Page Rotation:

To rotate the first page of a PDF by 180 degrees, place your PDF (dummy.pdf) in the project directory. Run the script and the rotated output will be saved as tilt.pdf.

```python

import PyPDF2

with (open("dummy.pdf","rb")) as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(180)
    
    with open("tilt.pdf","wb") as new_file:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(new_file)
```
## 3. PDF Combiner:

To combine multiple PDFs, run the script with the filenames of the PDFs you want to combine as command-line arguments. The combined PDF will be saved as super.pdf.

```python

import PyPDF2
import sys

if __name__ =="__main__":
    inputs = sys.argv[1:]

    def pdf_combiner(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write("super.pdf")

    pdf_combiner(inputs)

print("All done!")
```
Run the script using:

python script_name.py pdf1.pdf pdf2.pdf pdf3.pdf

Replace script_name.py with the name of your script and pdf1.pdf, pdf2.pdf, pdf3.pdf with the names of the PDFs you want to combine.
Dependencies:

    PyPDF2: A Pure-Python library built as a PDF toolkit.

To install the dependencies, run:

pip install PyPDF2

Contribution:

Feel free to fork this project and make your own changes. Pull requests are welcome!

Note: Always back up your original PDFs before using this tool to avoid unintended loss of data.