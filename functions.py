import tkinter as tk
from tkinter import filedialog

def window(root, x, y, title):

    size = str(x) + "x" + str(y)

    root.geometry(size)

    root.title(title)

    root.config()

def closeWindow(root):
    root.destroy()

def chooseFile():

    path = filedialog.askopenfilename(title="Select your given file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if path:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        
        return text
