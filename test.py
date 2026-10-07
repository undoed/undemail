import tkinter as tk

def click():
    print("clikedboii")

wn = tk.Tk()
wn.config(background="#FFFFFF")
wn.geometry("500x500")

label = tk.Label(wn, text="Hello, world!", font=("Arial",10,"bold"), fg="green", relief="raised", bd=20, pady=10, padx=15)
label.pack()

button = tk.Button(text="test")
button.config(command=click)
button.config(font=("Arial", 40, "bold"))
button.pack()

wn.mainloop()