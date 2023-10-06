import PyPDF2
import sys


if __name__ =="__main__":
    #get all argumments from the command line
    inputs = sys.argv[1:] # to get all the arguments except the first one which is the name of the file
    # print(inputs) # to print all the arguments
    def pdf_combiner(pdf_list):
        merger = PyPDF2.PdfFileMerger() # to merge pdf files
        for pdf in pdf_list: # to loop through all the pdf files
            print(pdf)
            merger.append(pdf) # to append all the pdf files
        merger.write("super.pdf") # to write the new pdf file

    pdf_combiner(inputs)

print("All done!")