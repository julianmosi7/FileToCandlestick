import mplfinance as mpf
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import pandas as pd

from pandas import DatetimeIndex

root = tk.Tk()

def choose_file(event):
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open(file_path)



label = Label(root, text="Select an appropriate File:")
label.pack()
button = Button(None, text='Choose File')
button.pack()
button.bind('<Button-1>', choose_file)

root.mainloop()
