import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
from src.utils import browse_button
from src.classes.ReaderFiles import Files


path = browse_button()

files = Files(path)

fileNames = files.getFiles()

if len(fileNames) > 0:

    for file in fileNames:

        readFiles = files.readFile(file)
        if readFiles is not False:
            pass
