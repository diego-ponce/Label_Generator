import requests
from pprint import pprint
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os


root = tk.Tk()

root.title("Label Generator")

#Since I don't know where Paul will be keeping this file on his computer I want him to be able to select relase id's from his computer from a button
def open_ids():
    '''function for when the user clicks the "Find ID's" button. Five things happen
    1) A dialog box allows them to select a file with IDs
    2) The filename variable is updated (accessible through "filename.get()")
    3) The button text is updated with the filename selected
    4) The file is read in
    5) The contents of the file is added to a textbox which the user can edit
    '''
#######     1
    file = filedialog.askopenfilename(initialdir = "./", title= "Select Release ID", filetypes = (("text", "*.txt"),("all files", "*./")))

#######     2
#     my_label = Label(root, text= filename).pack()
#  insead update label like this:
    filename.set(file) # updates the StringVar called filename

#######     3
    findIDS['text'] = filename.get()

#######     4
    with open(filename.get()) as f:
        quote = f.read()

#######     5
    T.delete('1.0', END) # Delete whatever was in the textbox originally
    T.insert(tk.END, quote) # insert the filecontents
#     return my_label -- not needed

#not sure how to launch the file after finding it above. Don't love having a second button. Can't access file name as its in another function
def launch_ids():
    pass
#      f = open(location)
     #f.read()
     #print(f.read)


#I would like the third button to run the label generator program and open up the newly adjusted CSV.
def create_csv():
    pass


#os.startfile(text = filename)

canvas = tk.Canvas(root, height = 800, width = 600, bg ='#3492eb')
canvas.pack()

frame = tk.Frame(root, bg = '#F9F7F5')
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

trash = PhotoImage(file = r"./images/trash_sml.png")
image = canvas.create_image(50, 50, anchor = NE, image = trash)

findIDS =tk.Button(frame, text="Find ID's", padx=100, pady=50, fg="white", bg="#3492eb", command=open_ids )
findIDS.pack(fill = X)

openFile =tk.Button(frame, text="open IDs", padx=100, pady=50, fg="white", bg="#3492eb", command=launch_ids)
openFile.pack(fill = X)

openCSV =tk.Button(frame, text="Create CSV", padx=100, pady=50, fg="white", bg="#3492eb", command=create_csv)
openCSV.pack(fill = X)

# added textbox for release IDs
S = tk.Scrollbar(frame)
T = tk.Text(frame, height=20, width=80)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Enter Release IDs here or click 'Find ID\'s' above to select a file of IDs"""
T.insert(tk.END, quote)

# things to add to make filename selected accessible to other functions in the window
filename = tk.StringVar() # declare a dynamic string variable to hold the filename
# filename.set("this") # set it to nothing until the filename is chosen by the user
# my_label = tk.Label(root, text=filename.get()) # create a label with the filename as it's text attribute
# my_label.pack()
root.mainloop()
