from tkinter import *
from reader import cypher_code
from main import Statistics


import matplotlib.pyplot as plt


def main():
    text = cypher_code()
    data = text['YearsExperience'].tolist()
    math = Statistics(data, len(data))
    print(f'{math.table_interval}. Excess:{math.excess}. Asy:{math.asymmetry}. Dis:{math.dispersion}.Ave:{math.average_value}')


def bar_chart():
    data = cypher_code()
    plt.hist(data['YearsExperience'].tolist(), bins=[0, 10, 20])
    plt.ylabel('some numbers')
    plt.show()


def window_drive():
    window = Tk()
    window.title("Maths")
    window.geometry('1000x800')
    fig = bar_chart()
    lbl = Label(window, text="Привет")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)
    window.mainloop()


if __name__ == '__main__':
    # main()
    bar_chart()
    # window_drive()
