# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:30:02 2022

@author: pulle
"""

from tkinter import*
import random

root=Tk()
root.title("Gifts")
root.geometry("500x500")
root.configure(background = 'lightblue')

label1 = Label(root)
label2 = Label(root)


label1["text"]="Listed_items: ['bottle', 'Tiffin', 'ID Card', 'Chocolates', 'Chips', 'Tickets', 'Hanky']"

def bag_contents():
    random_list = random.sample(range(0, 7),1)
    label2["text"]="Put Item Number " + str(random_list) + " In Bag"

label1.place(relx=0.5, rely=0.4, anchor=CENTER)

btn = Button(root, text="Which item to put in bag?",command = bag_contents,bg="orange",fg="white")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label2.place(relx=0.5, rely=0.6, anchor=CENTER)


root.mainloop()