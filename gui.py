import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askdirectory
from renamer_v2 import runRenamer
from PIL import ImageTk, Image


#create window
window = tk.Tk()
window.geometry("600x400")
#window.resizable(False,False) #disables window resizing
window.title('Receipt Renamer')

#Content
label = tk.Label(window, text="Receipt Renamer",font=96).grid(row=0,column=1)
label = tk.Label(window, text="Set Folder Containing Files").grid(row=1,column=1)


#First file path
def open_filePath():
    path = askdirectory(title='Select Folder')
    if path:
        print(path)
    else:
        print("No folder selected.")
    ent1.delete(0,'end')
    ent1.insert(0, path)

filePath = tk.StringVar()
ent1=tk.Entry(window,font=40, width=40, textvariable=filePath)
ent1.grid(row=2,column=1)
b1=tk.Button(window,text="Select Folder",font=40,command=open_filePath)
b1.grid(row=2,column=2)


#Check box
intVar = tk.IntVar()
chk = tk.Checkbutton(window, text="Move?",variable=intVar)
chk.grid( row=3,column=1)


#Second file path
def open_movePath():
    path = askdirectory(title='Select Folder')
    if path:
        print(path)
    else:
        print("No folder selected.")
    ent2.delete(0,'end')    
    ent2.insert(0, path)


label = tk.Label(window, text="Set Folder To Move Files To").grid(row=4,column=1)
movePath = tk.StringVar()
ent2=tk.Entry(window,font=40, width=40, textvariable=movePath)
ent2.grid(row=5,column=1)
b2=tk.Button(window,text="Select Folder",font=40,command=open_movePath)
b2.grid(row=5,column=2)



#RUN BUTTON
def runPressed():
    moveBool = False
    if intVar.get() == 1:
        moveBool = True
    elif moveBool==False and ent2.get()!="" and ent1.get()!="":
        res = tk.messagebox.askquestion('Move?', 
                             'There is a path in the move path, do you want to move the files to this path?')
        if res == 'yes' :
            moveBool = True
        else:
            moveBool = False
    
    runRenamer(ent1.get()+'\\',ent2.get()+'\\',moveBool)
    
button = tk.Button(window, text='Run', width=40, command=runPressed).grid(row=6,column=1)

#Instructions
label = tk.Label(window, text="\n\n\nInstructions"+"\n\nSelect a folder containing only pdf files of scanned receipts"
                 +"\nThe algorithm is looking for only pdf files, all others will cause an error"
                 +"\nIf move is selected, successful renames will be moved to new folder"
                 +"\nBarcodes and pdfs can be in any orientation"
                 +"\nOnly the first page will be scanned",font=20).grid(row=7,column=1)

#keeps window open
window.mainloop()