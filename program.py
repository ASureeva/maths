from reader import cypher_code
from main import Statistics
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from create_answer import cr_answer
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
import numpy as np


matplotlib.use('TkAgg')


def main(file, sheet, table_name):
    text = cypher_code(file, sheet)
    # data = text['YearsExperience'].tolist()
    data = text[table_name].tolist()
    math = Statistics(data, len(data))
    return math


def window_drive():
    ww = tk.Tk()
    ww.geometry('700x400')
    ww.state('zoomed')
    ww.title("Maths")

    frame1 = tk.Frame()
    frame1.pack(side=tk.LEFT)
    link_l = tk.Label(ww, text="Укажите ссылку к файлу, где лежат данные", width=10)
    link_l.pack(padx=20, pady=5)
    link = tk.Entry(ww)
    link.pack(padx=10, pady=10)

    sheet_l = tk.Label(text="Напишите название таблицы", width=10)
    sheet_l.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)
    sheet_name = tk.Entry(ww, show=None)
    sheet_name.pack(fill=tk.BOTH, padx="0", pady="6")

    table_l = tk.Label(text="Напишите название столбца", width=10)
    table_l.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)
    table_name = tk.Entry(ww, show=None)
    table_name.pack(fill=tk.BOTH, padx="15", pady="6")

    t = tk.Text(ww, height=20)
    ff = Figure(figsize=(6, 6), dpi=100)
    xx = ff.add_subplot(111)
    rects1 = xx.bar([0], [0], 1)
    canvas = FigureCanvasTkAgg(ff, master=ww)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)

    def insert_point():
        t.delete("1.0", "end")
        t.pack()
        var = link.get()
        var_2 = sheet_name.get()
        var_3 = table_name.get()
        math = main(var, var_2, var_3)
        t.insert('insert', cr_answer(math))
        data = math.data
        print(data)
        xx.clear()
        canvas.get_tk_widget().delete(canvas.get_tk_widget().find_all())
        # ff = Figure(figsize=(6, 6), dpi=100)
        # xx = ff.add_subplot(111)
        ind = math.lis
        rects1 = xx.bar(ind, data, math.length)
        # canvas = FigureCanvasTkAgg(ff, master=ww)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT)

    b1 = tk.Button(ww, text='insert point', width=15, padx="15", pady="6",
                    height=2, command=insert_point)
    b1.pack()

    ww.mainloop()


if __name__ == '__main__':
    window_drive()
