# Loading the pyPdf Library
from pyPdf import PdfFileWriter, PdfFileReader

# Creating a routine that appends files to the output file
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

# Creating an object where pdf pages are appended to
output = PdfFileWriter()

for pdf in folder:
    # Appending two pdf-pages from two different files
    append_pdf(PdfFileReader(open(pdf,"rb")),output)

    # Writing all the collected pages to a file
    output.write(open("CombinedPages.pdf","wb"))
    output.write(open("../CombinedPages.pdf","wb"))
