# PdfToPng
a simple python script to convert pdf files into png files.
Script uses PyMuPDF library. You need to install it before using the script:
pip install PyMuPDF

Replace '/path/to/your/pdf/files/' and '/path/to/save/images/' with the paths to your PDF files and where you want to save the images, respectively.

This code will create a PNG image for each page in each PDF, and the images will be saved with the format filename_page{pagenumber}.png. For example, if there's a PDF called document1.pdf with three pages, it will create document1_page0.png, document1_page1.png, and document1_page2.png.

! do not use \ for image path. The backslash \ is an escape character in Python strings, meaning it is used to introduce special character sequences. For example, \n is a newline, and \t is a tab. If you want a literal backslash in a string, you have to escape it by using \\. You can use "/" or "\\" for file paths.
