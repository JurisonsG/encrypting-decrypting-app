import tkinter as tk
from functions import window, closeWindow
from encrypt import encrypt
from decrypt import decrypt

root = tk.Tk()
window(root, 700, 400, "Main menu")

mainTitleLabel = tk.Label(root, text="Welcome to the encryption and decryption program", font=("Arial", 20))
mainTitleLabel.pack(pady=10)

choiceLabel = tk.Label(root, text="Please choose an option:", font=("Arial", 16))
choiceLabel.pack(pady=10)

encryptButton = tk.Button(root, text="Encrypt", font=("Arial", 16), command=lambda: encrypt(root))
encryptButton.pack(pady=10)

decryptButton = tk.Button(root, text="Decrypt", font=("Arial", 16), command=lambda: decrypt(root))
decryptButton.pack(pady=10)

closeButton = tk.Button(root, text="Close", font=("Arial", 16), command=lambda: closeWindow(root))
closeButton.pack(pady=10)

root.mainloop()
