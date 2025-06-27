import os #For folder operation
from PyPDF2 import PdfMerger #For Pdf Operation
filePath= "F:/DeveloperTools/Python Learning/PDFS"

PdfList = []
for i in os.listdir(filePath):
    if i.endswith(".pdf"):
        PdfList.append(i) #Joining in PdfList list
PdfList.sort() #To Decorate List

PdfHandel = PdfMerger()
for i in PdfList:
    PdfHandel.append(f"{filePath}/{i}")


PdfHandel.write(f"{filePath}/Mixed.pdf")
PdfHandel.close()
