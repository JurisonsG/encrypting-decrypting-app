import tkinter as tk
from tkinter import messagebox
from functions import window, closeWindow, createFile
from AESfunctions import *

def AES_decryption(root):
    page = tk.Toplevel(root)
    window(page, 500, 700, "AES Decryption")

    tk.Label(page, text="AES Decryption (128-bit)", font=("Arial", 20)).pack(pady=10)

    key_label = tk.Label(page, text="Enter 16-character key:", font=("Arial", 16))
    key_label.pack(pady=10)
    key_input = tk.Entry(page, font=("Arial", 16))
    key_input.pack(pady=10)

    text_label = tk.Label(page, text="Enter HEX text:", font=("Arial", 16))
    text_label.pack(pady=10)
    text_input = tk.Entry(page, font=("Arial", 16))
    text_input.pack(pady=10)

    def decrypt_action():
        key = key_input.get().encode()
        hextext = text_input.get().strip()
        if len(key) != 16:
            messagebox.showerror("Error", "Key must be exactly 16 bytes (128-bit)")
            return
        try:
            cipher_bytes = bytes.fromhex(hextext)
        except:
            messagebox.showerror("Error", "Invalid HEX input")
            return
        w = key_expansion(key)
        decrypted = b''.join(decrypt_block(cipher_bytes[i:i+16], w) for i in range(0, len(cipher_bytes), 16))
        try:
            plaintext = pkcs7_unpad(decrypted).decode('utf-8')
        except:
            plaintext = str(pkcs7_unpad(decrypted))
        createFile(plaintext, "AES_decrypted.txt")

    tk.Button(page, text="Decrypt", font=("Arial", 16), command=decrypt_action).pack(pady=10)
    tk.Button(page, text="Close", font=("Arial", 16), command=lambda: closeWindow(page)).pack(pady=10)
