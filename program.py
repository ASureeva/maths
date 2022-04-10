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
    result = [False, 0]
    text = cypher_code(file, sheet)
    if text[0]:
    # data = text['YearsExperience'].tolist()
        data = text[1][table_name].tolist()
        try:
            result[1] = Statistics(data, len(data))
            result[0] = True
        except Exception:
            print('не могу выполнить код')
    return result


def window_drive():
    ww = tk.Tk()
    ww.geometry('700x400')
    ww.state('zoomed')
    ww.title("Maths")

    frame1 = tk.Frame()
    frame1.pack()
    link_l = tk.Label(master=frame1, text="Укажите ссылку к файлу, где лежат данные", width=100)
    link_l.pack()
    link = tk.Entry(master=frame1, width=100)
    link.pack()

    frame2 = tk.Frame()
    frame2.pack()
    sheet_l = tk.Label(master=frame1, text="Напишите название таблицы", width=100)
    sheet_l.pack()
    sheet_name = tk.Entry(master=frame1, width=100)
    sheet_name.pack()

    frame3 = tk.Frame()
    frame3.pack()
    table_l = tk.Label(master=frame1, text="Напишите название столбца", width=100)
    table_l.pack()
    table_name = tk.Entry(master=frame1, width=100)
    table_name.pack()

    t = tk.Text(ww, height=20)
    ff = Figure(figsize=(6, 6), dpi=100)
    xx = ff.add_subplot(111)
    rects1 = xx.bar([0], [0], 1)
    canvas = FigureCanvasTkAgg(ff, master=ww)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)

    def insert_point():
        t.delete("1.0", "end")
        t.pack(side=tk.LEFT)
        var = link.get()
        var_2 = sheet_name.get()
        var_3 = table_name.get()
        math = main(var, var_2, var_3)
        if math[0]:
            t.insert('insert', cr_answer(math[1]))
            data = math[1].data
            xx.clear()
            canvas.get_tk_widget().delete(canvas.get_tk_widget().find_all())
            # ff = Figure(figsize=(6, 6), dpi=100)
            # xx = ff.add_subplot(111)
            ind = math[1].lis
            rects1 = xx.bar(ind, data, math[1].length)
            # canvas = FigureCanvasTkAgg(ff, master=ww)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.RIGHT)
        else:
            t.insert('insert', 'Не могу провести расчет.\n'
                               'Пожалуйста, проверьте ссылку на документ,\n'
                               'название таблицы, имя столбца или данные в таблице')

    b1 = tk.Button(master=frame1, text='Рассчитать', width=15, height=2, command=insert_point)
    b1.pack()

    ww.mainloop()


if __name__ == '__main__':
    window_drive()
