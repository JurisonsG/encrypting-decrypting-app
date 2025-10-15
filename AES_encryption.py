import tkinter as tk
from AES_decryption import *
from tkinter import messagebox
from functions import window, closeWindow, createFile
from AESfunctions import *


def AES_encryption(root):
    page = tk.Toplevel(root)
    window(page, 500, 700, "AES Encryption")

    tk.Label(page, text="AES Encryption (128-bit)", font=("Arial", 20)).pack(pady=10)

    key_label = tk.Label(page, text="Enter 16-character key:", font=("Arial", 16))
    key_label.pack(pady=10)
    key_input = tk.Entry(page, font=("Arial", 16))
    key_input.pack(pady=10)

    text_label = tk.Label(page, text="Enter text:", font=("Arial", 16))
    text_label.pack(pady=10)
    text_input = tk.Entry(page, font=("Arial", 16))
    text_input.pack(pady=10)

    def encrypt_action():
        key = key_input.get().encode()
        plaintext = text_input.get().encode()
        if len(key) != 16:
            messagebox.showerror("Error", "Key must be exactly 16 bytes (128-bit)")
            return
        w = key_expansion(key)
        padded = pkcs7_pad(plaintext)
        cipher = b''.join(encrypt_block(padded[i:i+16], w) for i in range(0, len(padded), 16))
        createFile(cipher.hex(), "AES_encrypted.txt")

    tk.Button(page, text="Encrypt", font=("Arial", 16), command=encrypt_action).pack(pady=10)
    decryptionButton = tk.Button(page, text="Decrypt", font=("Arial", 16), command= lambda: AES_decryption(page))
    decryptionButton.pack(pady=10)
    tk.Button(page, text="Close", font=("Arial", 16), command=lambda: closeWindow(page)).pack(pady=10)
