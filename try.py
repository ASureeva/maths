# from tkinter import scrolledtext as tkst
# import numpy as np
# import matplotlib
# from reader import cypher_code
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import tkinter as tk
#
#
# matplotlib.use('TkAgg')
#
# def dummy():
#     return
#
#
# def bar_chart():
#     data = cypher_code()
#     plt.hist(data['YearsExperience'].tolist(), bins=6)
#     plt.ylabel('some numbers')
#     plt.show()
#
#
#
# ww = tk.Tk()
# ww.geometry('700x400')
# ww.state('zoomed')
#
# # datalst = [31, 41, 59, 26, 53, 58, 97, 96, 36]
# datalst = cypher_code()['YearsExperience'].tolist()
# ff = Figure(figsize=(6,6), dpi=100)
# xx = ff.add_subplot(111)
# ind = np.arange(len(datalst))
# rects1 = xx.bar(ind, datalst, 0.8)
# canvas = FigureCanvasTkAgg(ff, master=ww)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.RIGHT)

# butt1 = tk.Button(ww,text='Button 1',command=dummy, height=1,width=20,state='normal')
# butt1.place(x=12, y=2)
# butt2 = tk.Button(ww,text='Button 2',command=dummy, height=1,width=20,state='disabled')
# butt2.place(x=162, y=2)
# butt3 = tk.Button(ww,text='Button 3',command=dummy, height=1,width=10,state='disabled')
# butt3.place(x=320, y=100)
# butt4 = tk.Button(ww,text='Button 4',command=dummy, height=1,width=10,state='disabled')
# butt4.place(x=320, y=128)
# butt5 = tk.Button(ww,text='Button 5',command=dummy, height=1,width=10,state='disabled')
# butt5.place(x=320, y=156)
# butt6 = tk.Button(ww,text='Button 6',command=dummy, height=1,width=10,state='disabled')
# butt6.place(x=320, y=184)
# butt7 = tk.Button(ww,text='Button 7',command=dummy, height=1,width=12,state='disabled')
# butt7.place(x=420, y=394)
# butt8 = tk.Button(ww,text='Button 8',command=dummy, height=1,width=12,state='disabled')
# butt8.place(x=600, y=394)
#
# disp_txt1 = tkst.ScrolledText(ww, width=36, height=12, wrap=tk.WORD, state='disabled')
# disp_txt1.pack(fill=tk.BOTH)
# disp_txt1.place(x=410, y=100)
# disp_txt2 = tkst.ScrolledText(ww, width=36, height=5, wrap=tk.WORD, state='disabled')
# disp_txt2.pack(fill=tk.BOTH)
# disp_txt2.place(x=410, y=300)

# ww.mainloop()

print(29//2)