from tkinter import *
from reader import cypher_code
from main import Statistics


def main():
    text = cypher_code()
    math = Statistics(text, len(text))
    print(f'{math.table_interval}. Excess:{math.excess}. Asy:{math.asymmetry}. Dis:{math.dispersion}.Ave:{math.average_value}')


if __name__ == '__main__':
    main()


# def clicked():
#     lbl.configure(text="Я же просил...")
#
#
# window = Tk()
# window.title("Maths")
# window.geometry('1000x800')
# lbl = Label(window, text="Привет")
# lbl.grid(column=0, row=0)
# txt = Entry(window, width=10)
# txt.grid(column=1, row=0)
# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=2, row=0)
# window.mainloop()
