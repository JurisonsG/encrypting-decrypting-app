import tkinter as tk
from tkinter import messagebox
from functions import *
from DESfunctions import triple_des_decrypt

def DES_decryption(root):

    page = tk.Toplevel(root)
    window(page, 500, 700, "DES decryption")

    title = tk.Label(page, text="DES Decryption", font=("Arial", 20))
    title.pack(pady=10)

    key1Label = tk.Label(page, text="Enter 1. decryption key:", font=("Arial", 16))
    key1Label.pack(pady=10)

    key1Input = tk.Entry(page, font=("Arial", 16))
    key1Input.pack(pady=10)

    key2Label = tk.Label(page, text="Enter 2. decryption key:", font=("Arial", 16))
    key2Label.pack(pady=10)

    key2Input = tk.Entry(page, font=("Arial", 16))    
    key2Input.pack(pady=10)

    key3Label = tk.Label(page, text="Enter 3. decryption key:", font=("Arial", 16))
    key3Label.pack(pady=10)

    key3Input = tk.Entry(page, font=("Arial", 16))    
    key3Input.pack(pady=10)

    textLabel = tk.Label(page, text="Enter bit text:", font=("Arial", 16))
    textLabel.pack(pady=10)

    TextInput = tk.Entry(page, font=("Arial", 16))
    TextInput.pack(pady=10)

    def decryption():
        key1 = key1Input.get()
        key2 = key2Input.get()
        key3 = key3Input.get()
        hex_text = TextInput.get()

        if not key1 or not key2 or not key3 or not hex_text:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            cipher_bytes = bitstring_to_bytes(hex_text)
        except ValueError:
            messagebox.showerror("Error", "Invalid hex input!")
            return

        try:
            decrypted_text = triple_des_decrypt(
                cipher_bytes,
                key1.encode(),
                key2.encode(),
                key3.encode()
            ).decode('utf-8')
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {e}")
            return

        createFile(decrypted_text, "DES_decrypted.txt")

    decryptButton = tk.Button(page, text="Decrypt", font=("Arial", 16), command=decryption)
    decryptButton.pack(pady=10)

    closeWindowButton = tk.Button(page, text="Close this window", font=("Arial", 16), command=lambda: closeWindow(page))
    closeWindowButton.pack(pady=10)
