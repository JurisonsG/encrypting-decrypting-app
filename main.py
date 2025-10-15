import tkinter as tk
from functions import window, closeWindow
from DES_encryption import DES_encryption
from AES_encryption import *

root = tk.Tk()
window(root, 900, 400, "Main menu")

mainTitleLabel = tk.Label(root, text="Welcome to the DES and AES encryption and decryption program", font=("Arial", 20))
mainTitleLabel.pack(pady=10)

choiceLabel = tk.Label(root, text="Please choose an option:", font=("Arial", 16))
choiceLabel.pack(pady=10)

DESButton = tk.Button(root, text="DES", font=("Arial", 16), command=lambda: DES_encryption(root))
DESButton.pack(pady=10)


AESButton = tk.Button(root, text="AES", font=("Arial", 16), command=lambda: AES_encryption(root))
AESButton.pack(pady=10)

closeButton = tk.Button(root, text="Close", font=("Arial", 16), command=lambda: closeWindow(root))
closeButton.pack(pady=10)

root.mainloop()
