import tkinter as tk
from tkinter import messagebox
from functions import *
from DESfunctions import triple_des_encrypt
from DES_decryption import DES_decryption

def DES_encryption(root):

    page = tk.Toplevel(root)
    window(page, 500, 700, "DES encryption")

    title = tk.Label(page, text="DES Encryption", font=("Arial", 20))
    title.pack(pady=10)

    key1Label = tk.Label(page, text="Enter 1. encryption key:", font=("Arial", 16))
    key1Label.pack(pady=10)

    key1Input = tk.Entry(page, font=("Arial", 16))
    key1Input.pack(pady=10)

    key2Label = tk.Label(page, text="Enter 2. encryption key:", font=("Arial", 16))
    key2Label.pack(pady=10)

    key2Input = tk.Entry(page, font=("Arial", 16))    
    key2Input.pack(pady=10)

    key3Label = tk.Label(page, text="Enter 3. encryption key:", font=("Arial", 16))
    key3Label.pack(pady=10)

    key3Input = tk.Entry(page, font=("Arial", 16))    
    key3Input.pack(pady=10)

    textLabel = tk.Label(page, text="Enter text:", font=("Arial", 16))
    textLabel.pack(pady=10)

    TextInput = tk.Entry(page, font=("Arial", 16))
    TextInput.pack(pady=10)

    def encription():
        key1 = key1Input.get()
        key2 = key2Input.get()
        key3 = key3Input.get()
        text = TextInput.get()

        if not key1 or not key2 or not key3 or not text:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        encrypted_text = triple_des_encrypt(text.encode(), key1.encode(), key2.encode(), key3.encode())

        createFile(bytes_to_bitstring(encrypted_text), "DES_encrypted.txt")

    encryptButton = tk.Button(page, text="Encrypt", font=("Arial", 16), command=encription)
    encryptButton.pack(pady=10)

    decryptionButton = tk.Button(page, text="Decrypt", font=("Arial", 16), command=lambda: DES_decryption(page))
    decryptionButton.pack(pady=10)

    closeWindowButton = tk.Button(page, text="Close this window", font=("Arial", 16), command=lambda: closeWindow(page))
    closeWindowButton.pack(pady=10)
