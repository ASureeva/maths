import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
e = tk.Entry(window, show="*")
# Указывает, что введенный текст будет замаскирован знаком «*»
# e = tk.Entry(window, show=None)
# Вы можете отменить режим маски, установив для него значение None

e.pack()

def insert_point():
    var = e.get()  # Получить введенное значение
    t.insert('insert', var)  # Ввод с позиции указателя


def insert_end():
    var = e.get()
    t.insert('end', var)  # Введите с конца
    # t.insert (2.2, var) # Ввод из третьей строки и третьего столбца


b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)  # Означает два символа в высоту
t.pack()

window.mainloop()