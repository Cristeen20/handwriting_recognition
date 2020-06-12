# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 03:22:31 2020

@author: Cristeena
"""

import tkinter
import tkinter.messagebox
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
from PIL import ImageTk,Image

from google.cloud import vision
import io
import os


root = Tk() 
root.title("Answer sheet evaluator")
root.geometry('900x600')
root.resizable(width = True, height = True)

path=r"C:\Users\Cristeena\Desktop\s8proj\answer.PNG"


def open1():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/Cristeena/Desktop/s8proj", title="Select A File",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    
   
    credential_path =r"C:\Users\Cristeena\.spyder-py3\qwiklabs-gcp-01-481406de8cd5-dd024bfad853.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    client = vision.ImageAnnotatorClient()

    with io.open(root.filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
           # print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
               # print('Paragraph confidence: {}'.format(
                  #  paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    #print('Word text: {} (confidence: {})'.format(
                      #  word_text, word.confidence))
                    print(word_text,end=" ")
                    Label(root,text=word_text).pack()
                    #for symbol in word.symbols:
                       # print('\tSymbol: {} (confidence: {})'.format(
                           # symbol.text, symbol.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
    
    






        
    
"""Detects document features in an image."""

 

                 
my_btn = Button(root,text="Open File", command=open1)
my_btn.pack()       
root.mainloop()  
        

        