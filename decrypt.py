import tkinter as tk
from functions import window, closeWindow, chooseFile, createFile
from tkinter import messagebox
from decryption import cryptToText

file_text = ""

def decrypt(root):
    global file_text

    page = tk.Toplevel(root)
    window(page, 500, 400, "Dencryption")

    title = tk.Label(page, text="Dencryption", font=("Arial", 20))
    title.pack(pady=10)

    keyLabel = tk.Label(page, text="Enter decription key:", font=("Arial", 16))
    keyLabel.pack(pady=10)

    keyInput = tk.Entry(page, font=("Arial", 16))
    keyInput.pack(pady=10)

    fileNameLabel = tk.Label(page, text="Enter file name with extension:", font=("Arial", 16))
    fileNameLabel.pack(pady=10)

    fileNameInput = tk.Entry(page, font=("Arial", 16))
    fileNameInput.pack(pady=10)

    def FileHandle():
        global file_text
        file_text = chooseFile()
        if not file_text:
            messagebox.showerror("Error", "Fail could't be read!")
            return

        key = keyInput.get()
        fileName = fileNameInput.get()

        if not key:
            messagebox.showerror("Error", "Write encription key!")
            return
        if not fileName:
            messagebox.showerror("Error", "Write file name!")
            return

        decrypted_text = cryptToText(file_text, key)
        createFile(decrypted_text, fileName)
        messagebox.showinfo("Success", f"Result has been saved in a file: {fileName}")

    chooseFileButton = tk.Button(page, text="Choose file", font=("Arial", 16), command=FileHandle)
    chooseFileButton.pack(pady=10)

    closeWindowButton = tk.Button(page, text="Close this window", font=("Arial", 16), command=lambda: closeWindow(page))
    closeWindowButton.pack(pady=10)