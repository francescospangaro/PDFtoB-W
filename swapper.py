import glob
import fitz
import os
from PIL import Image, ImageTk
from pprint import pprint

pdfs = glob.glob("*.pdf")
for pdf in pdfs:
	file = fitz.open(pdf)
	for page in file:
		pix = page.get_pixmap(matrix=fitz.Matrix(6.0, 6.0))
		pix.save("page-%i.jpeg" % page.number)
	images = glob.glob("*.jpeg")
	for image in images:
		img = Image.open(image)
		thresh = 200
		fn = lambda x : 255 if x > thresh else 0
		r = img.convert('L').point(fn, mode='1')
		r.save(image)
	images = [
			Image.open(image)
			for image in glob.glob("*.jpeg") 	
		]
	path = pdf[:(len(pdf)-4)] + "BW" + pdf[(len(pdf)-4):]
	images[0].save(
		path, "PDF", resolution = 100.0, save_all = True, append_images = images[1:]
	)
	images = glob.glob("*.jpeg")
	for i in images:
		os.remove(i)
