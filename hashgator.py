import tkinter as tk
from tkinter import messagebox as msg
from hashlib import sha256

def hashify():
    # calculate hash
    hash_var = sha256(entry_field.get().encode("utf-8")).hexdigest()
    hash_label = tk.Label(window, text="")
    hash_label.grid(row=1, column=0, columnspan=3)
    hash_label.configure(text=hash_var)
    print("SHA256: " + hash_var)

window = tk.Tk()
window.title("hashify")
window.geometry("650x100"),

entry_field = tk.Entry(window, width=55)
hash_button = tk.Button(window, text="Hash!", command=hashify)

entry_field.grid(row=0, column=0)
hash_button.grid(row=0, column=1)

window.mainloop()