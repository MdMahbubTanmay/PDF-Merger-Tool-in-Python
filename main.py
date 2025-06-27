import os
from PyPDF2 import PdfMerger
filePath= "F:/DeveloperTools/Python Learning/PDFS"

PdfList = []
for i in os.listdir(filePath):
    if i.endswith(".pdf"):
        PdfList.append(i)
PdfList.sort()
print(PdfList)
PdfHandel = PdfMerger()
for i in PdfList:
    PdfHandel.append(f"{filePath}/{i}")


PdfHandel.write(f"{filePath}/Mixed.pdf")
PdfHandel.close()