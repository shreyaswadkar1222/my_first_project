import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x200")
root.configure(bg="black")

def time():
    string = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, 
                 font=('Arial', 60),   # Font family + size
                 background='black', 
                 foreground='yellow')

label.pack(anchor='center')

time()
root.mainloop()