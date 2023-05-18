import os
import fitz  # PyMuPDF

# specify directory where the PDF files are
pdf_dir = 'path/to/pdf/folder/'

# specify directory where to save images
img_dir = 'path/to/image/folder/'

# ensure img_dir ends with '/'
if not img_dir.endswith('/'):
    img_dir += '/'

# make img_dir if not exist
os.makedirs(img_dir, exist_ok=True)

desired_dpi = 300  # specify your desired DPI here

# iterate over files in the pdf directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # open pdf file
        doc = fitz.open(pdf_dir + filename)
        # iterate over pages in the pdf
        for i in range(len(doc)):
            # render page to an image (you can specify resolution here)
            pix = doc[i].get_pixmap()
            # save image as a PNG
            img_file = img_dir + filename.rstrip('.pdf') + f'_page{i}.png'
            pix.save(img_file)

print("Conversion completed!")
