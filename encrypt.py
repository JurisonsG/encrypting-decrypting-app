import tkinter as tk
from functions import window, closeWindow, chooseFile
from encription import textToencrypt, createFile
from tkinter import messagebox

file_text = ""  # globāls mainīgais

def encrypt(root):
    global file_text

    page = tk.Toplevel(root)
    window(page, 500, 400, "Encryption")

    title = tk.Label(page, text="Encryption", font=("Arial", 20))
    title.pack(pady=10)

    keyLabel = tk.Label(page, text="Enter encription key:", font=("Arial", 16))
    keyLabel.pack(pady=10)

    keyInput = tk.Entry(page, font=("Arial", 16))
    keyInput.pack(pady=10)

    fileNameLabel = tk.Label(page, text="Enter file name with extension:", font=("Arial", 16))
    fileNameLabel.pack(pady=10)

    fileNameInput = tk.Entry(page, font=("Arial", 16))
    fileNameInput.pack(pady=10)

    def handleFile():
        global file_text
        file_text = chooseFile()
        if not file_text:
            messagebox.showerror("Error", "Fails netika nolasīts!")
            return

        # Nolasa atslēgu un faila nosaukumu tikai tad, kad poga nospiesta
        key = keyInput.get()
        fileName = fileNameInput.get()

        if not key:
            messagebox.showerror("Error", "Ievadi atslēgu!")
            return
        if not fileName:
            messagebox.showerror("Error", "Ievadi faila nosaukumu!")
            return

        encrypted_text = textToencrypt(file_text, key)
        createFile(encrypted_text, fileName)
        messagebox.showinfo("Success", f"Rezultāts saglabāts failā: {fileName}")

    chooseFileButton = tk.Button(page, text="Choose file", font=("Arial", 16), command=handleFile)
    chooseFileButton.pack(pady=10)

    closeWindowButton = tk.Button(page, text="Close this window", font=("Arial", 16), command=lambda: closeWindow(page))
    closeWindowButton.pack(pady=10)
