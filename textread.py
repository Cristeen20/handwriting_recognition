import pytesseract

import tkinter
import tkinter.messagebox
from tkinter import * 
from tkinter.ttk import *
  
from tkinter.filedialog import askopenfile 
from PIL import ImageTk,Image
from PIL import Image

root = Tk()
root.title('Answer Paper Evaluation')


def open1():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/Cristeena/Desktop/s8proj", title="Select A File",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    
    img = Image.open(root.filename)
    
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    print(result)
    Label(root,text=result).pack()
# write text in a text file and save it to source path    
    with open('abc.txt',mode='w') as file:      
      
                 file.write(result) 
                 print(result) 
    



#print(img)
   
                 
my_btn = Button(root,text="Open File", command=open1)
my_btn.pack()

root.mainloop()
