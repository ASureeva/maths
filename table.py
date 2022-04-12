import tkinter as tk


def create_table(math):
    root = tk.Tk()
    root.geometry('800x500')
    table = math.table_interval
    height = math.count_int + 1
    table[math.count_int] = {
        'frequency': 'n',  # 0
        'frequency_funded': 'n нак.',  # 1
        'x': 'x среднее',  # 2
        'z': 'z',  # 3
        'z_two': 'z**2',  # 4
        'z_third': 'z**3',  # 5
        'z_fourth': 'z**4'  # 6
    }
    for element in table:
        table[element]['name_table'] = element + 1
    for i in range(height):
        width = 0
        for j in table[i]:
            b = tk.Label(master=root, text=table[i][j], height=3)
            b.grid(row=i, column=width)
            width += 1

    root.mainloop()


# if __name__ == '__main__':
    # table = {0: {'frequency': 5, 'frequency_funded': 5, 'x': 1.8834116666666667, 'z': -3.447011333333333,
    #      'z_two': 11.881887132128444, 'z_third': -40.95699960583424, 'z_fourth': 141.17924182063948},
    #  1: {'frequency': 9, 'frequency_funded': 14, 'x': 3.450235, 'z': -1.8801879999999995, 'z_two': 3.5351069153439982,
    #      'z_third': -6.6466656009467995, 'z_fourth': 12.496980902912957},
    #  2: {'frequency': 4, 'frequency_funded': 18, 'x': 5.017058333333333, 'z': -0.31336466666666674,
    #      'z_two': 0.09819741431511116, 'z_third': -0.030771600004383375, 'z_fourth': 0.009642732178173597},
    #  3: {'frequency': 4, 'frequency_funded': 22, 'x': 6.583881666666667, 'z': 1.253458666666667,
    #      'z_two': 1.5711586290417785, 'z_third': 1.969382400280536, 'z_fourth': 2.4685394376124408},
    #  4: {'frequency': 3, 'frequency_funded': 25, 'x': 8.150705, 'z': 2.8202820000000006, 'z_two': 7.953990559524003,
    #      'z_third': 22.43249640319548, 'z_fourth': 63.26596582099697},
    #  5: {'frequency': 5, 'frequency_funded': 30, 'x': 9.717528333333332, 'z': 4.3871053333333325,
    #      'z_two': 19.24669320576177, 'z_third': 84.43727041202789, 'z_fourth': 370.4351993567163}}

    # print(table[0])
    # for i in table[0]:
    #     print(i)
