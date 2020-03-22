import mplfinance as mpf
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import pandas as pd
from pandas import DatetimeIndex
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import os
import subprocess

root = tk.Tk()


def choose_file(event):
    #root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open(file_path)
    handle_candle(file)

dateg = []
timeg = []
def handle_candle(file):
    date = []
    open = []
    high = []
    low = []
    close = []
    value = []

    openCur = []
    highCur = []
    lowCur = []
    closeCur = []

    for x in file:
        parts = x.split(";")
        datetime_object = datetime.strptime(parts[0] + parts[1], '%d/%m/%Y%H:%M:%S')

        openCur.append(parts[2])
        highCur.append(parts[3])
        lowCur.append(parts[4])
        closeCur.append(parts[5])

        if datetime_object.minute == 0:
            dateg.append(parts[0])
            timeg.append(parts[1])
            date.append(datetime_object)
            open.append(openCur[0])
            high.append(max(highCur))
            low.append(min(lowCur))
            close.append(closeCur[len(closeCur)-1])
            value.append(parts[6])

            openCur.clear()
            highCur.clear()
            lowCur.clear()
            closeCur.clear()
    file.close()
    write_to_csv(date, dateg, timeg, open, high, low, close)


def print_chart(date, openl, high, low, close):

    df = pd.DataFrame(
        {'date': date,
         'Open': openl,
         'High': high,
         'Low': low,
         'Close': close
        })

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    #info: i tried to display the chart on the canvas on tkinter, but aparently doesn't work with mpffinance lib

    #iday = df.loc[:, '01/12/2019':'02/12/2019']
    #f = Figure(figsize=(5, 4), dpi=100)
    #a = f.add_subplot(111)
    #canvas = FigureCanvasTkAgg(f, master=root)
    #canvas.draw()
    #canvas.get_tk_widget().pack()

    mpf.plot(df, type='candle')


def write_to_csv(date, dateg, timeg, openl, high, low, close):

    rows = zip(dateg, timeg, openl, high, low, close)

    with open('stundenkerzen.csv', 'w', newline='') as result_file:
        wr = csv.writer(result_file, delimiter=';')
        for row in rows:
            wr.writerow(row)

    path = os.path.abspath('stundenkerzen.csv')
    finished = Label(root, text="Written to CSV! \n You can find the file under: \n" + path)
    finished.pack()

    #opening file/folder
    try:
        subprocess.Popen(f'explorer /select,"{path}"')
    except:
        print("oh..your're working on a mac..")
        subprocess.call(['open', path])

    print("Written to CSV!")

    print_chart(date, openl, high, low, close)


root.geometry("800x300")
label = Label(root, text="Select an appropriate File:")
label.pack()
button = Button(None, text='Choose File')
button.pack()
button.bind('<Button-1>', choose_file)
root.mainloop()
