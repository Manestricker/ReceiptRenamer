'''
Written by David Deltz 
For Toshiba International Corporation
July 2023
'''
from pdf2image import convert_from_path
import os
import cv2
from pyzbar.pyzbar import decode

#This function takes the path of a pdf file and 
def barcodeReader(pdfFilePath):
    a = []
    #uses poppler library to convert the pdf into a PIL image
    pdfImage = convert_from_path(pdf_path=pdfFilePath, poppler_path = r"poppler-23.07.0\Library\bin")
    for count, page in enumerate(pdfImage):
        #creates temporary image file of the pdf
        page.save(f'out{count}.jpg', 'JPEG')
        #looks for the first barcode in image
        img = cv2.imread(r"out"+str(count)+".jpg") #read the jpg into openCV
        detectedBarcodes = decode(img) #give the openCV image object to Zbar, zbar will create a list of barcodes
        for barcode in detectedBarcodes: 
            if str(barcode.type) == 'CODE39': #only read CODE39 barcodes and some more filters below
                if len(str(barcode.data)) == 10:
                    a.append(str(barcode.data)[2:9])
                if len(str(barcode.data)) == 9:
                    a.append(str(barcode.data)[2:8])
                
        
        #removes temp file
        os.remove(r"out"+str(count)+".jpg")
    #check for no barcodes found
    if len(a) <= 1:
        return a
    if len(a[0]) < len(a[1]): #put the lowest value first. this is to get the output list in the format desired
        temp = a[1]
        a[1] = a[0]
        a[0] = temp
    return a
