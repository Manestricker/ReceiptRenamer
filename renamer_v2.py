'''
Written by David Deltz 
For Toshiba International Corporation
July 2023
'''
from genericpath import isfile
import os
#import configparser
import shutil
from barcodeDocScanner import barcodeReader
import tkinter as tk

#To add config reading back, you must make it write to path and movePath
#reads in the data from the config file
#Config = configparser.ConfigParser()
#Config.read(r"config.ini")

#this function iterates through all of the pdf files in the folder selected
def runRenamer(path, movePath, MoveBool):
  newNames = []

  #This loop takes the files in and renames them based on the barcodes it was able to read
  i = 0
  doubleScanned = 0
  notScanned = 0
  succ = 0
  moved = 0
  for filename in os.listdir(path):
    newNames.append(barcodeReader(path+filename))
    if len(newNames[i]) == 0:
      notScanned += 1
      print("No barcodes were not scanned")
    elif len(newNames[i]) == 1:
      notScanned += 1
      print("1 barcode was not scanned. Found: ", newNames[i])
    elif newNames[i][0] == newNames[i][1]:
      doubleScanned += 1
      print("Double Scanned Barcode. Found: ", newNames[i])
    elif newNames[i][0] == "" or newNames[i][1] == "":
      notScanned += 1
      print("One or more barcodes were not scanned")
      #print(newNames[i])
    #if the 2nd number is smaller than the first, switch them  
    elif int(newNames[i][1]) <= int(newNames[i][0]):
      succ += 1
      os.rename(path+filename, path+str(newNames[i][1])+'_'+str(newNames[i][0])+'.pdf')
      if MoveBool:
        moved +=1
        extraStr = ""
        num = 0
        while os.path.isfile(movePath+str(newNames[i][1])+'_'+str(newNames[i][0])+extraStr+'.pdf'):
          #print("File exists", movePath+str(newNames[i][1])+'_'+str(newNames[i][0])+extraStr+'.pdf')
          extraStr ="_"+str(num)
          num += 1
        dest = shutil.move(path+str(newNames[i][1])+'_'+str(newNames[i][0])+'.pdf', movePath+str(newNames[i][1])+'_'+str(newNames[i][0])+extraStr+'.pdf')
  
    else:
      succ += 1
      os.rename(path+filename, path+str(newNames[i][0])+'_'+str(newNames[i][1])+'.pdf')
      if MoveBool:
        moved +=1
        extraStr = ""
        num = 0
        while os.path.isfile(movePath+str(newNames[i][0])+'_'+str(newNames[i][1])+extraStr+'.pdf'):
          #print("File exists")
        
          extraStr ="_"+str(num)
          num += 1
        dest = shutil.move(path+str(newNames[i][0])+'_'+str(newNames[i][1])+'.pdf', movePath+str(newNames[i][0])+'_'+str(newNames[i][1])+extraStr+'.pdf')
  
    i += 1
  tk.messagebox.showinfo("Information", "Succesfully Renamed: "+str(succ)+
                         "\nDouble Scanned: "+str(doubleScanned)
                         +"\nNot Scanned: "+str(notScanned)
                          +"\nFiles Moved: "+str(moved))


