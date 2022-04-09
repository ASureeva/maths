import math


class Statistics():

    def __init__(self, list, count):
        self.count = count
        self.table_interval = {}
        self.count_int = self.count_interval()
        self.create_table_interval()
        self.list = list
        self.list.sort()
        self.min = self.search_min()
        self.max = self.search_max()
        self.length = self.length_interval()
        self.create_n()
        self.create_x()
        self.average_value = self.search_average_value()
        self.create_z()
        self.create_all_z()
        self.dispersion = self.create_dispersion()
        self.root_of_dispersion = self.create_root_of_dispersion()
        self.fashion_line = self.search_fashion_line()
        self.fashion = self.create_fashion()
        self.median_line = self.search_median_line()
        self.median = self.create_median()
        print(self.table_interval)
        self.m_third = self.create_m_third()
        self.m_fourth = self.create_m_fourth()
        self.asymmetry = self.create_a_third()
        self.excess = self.create_e_k()

    def search_min(self):
        min = self.list[0]
        return min

    def search_max(self):
        max = self.list[-1]
        return max

    def count_interval(self):
        count_int = 1 + 3.322*math.log(self.count, 10)
        return int(round(count_int))

    def length_interval(self):
        length = (self.max - self.min) / self.count_int
        # print(f'{length * self.count_int}--{self.max - self.min}')
        if length * self.count_int == self.max - self.min:
            length += length*10/100
        return length

    def create_table_interval(self):
        for i in range(0, self.count_int):
            self.table_interval[i] = [0, 0]

    def create_n(self):
        step = 0
        accumulation = 0
        count_inter = self.min
        for i in range(0, self.count):
            # print(i)
            # print(self.table_interval)
            # print(f'opopopop{self.list[i]}--{step*self.length + self.min + self.length}')
            if self.list[i] < step*self.length + self.min + self.length:
                # print(f'{self.list[i]}')
                self.table_interval[step][0] += 1  # первый элемент
                # print(f'cou---{self.table_interval[step][0]}---{step}')
                accumulation += 1
                self.table_interval[step][1] = accumulation
            elif step != 5:
                # print(f'{self.list[i]}')
                step += 1
                self.table_interval[step][0] += 1  # первый элемент
                # print(f'cou---{self.table_interval[step][0]}---{step}')
                accumulation += 1
                self.table_interval[step][1] = accumulation
                count_inter = count_inter + self.length

    def create_x(self):
        # print(f'{self.length}omg')
        for i in range(0, self.count_int):
            self.table_interval[i].append(((i)*self.length + self.min*2 + (i+1)*self.length)/2)  # третий элемент

    def search_average_value(self):
        average_value = 0
        for i in range(0, self.count_int):
            average_value += (self.table_interval[i][0] * (self.table_interval[i][2])) / self.count
        return average_value

    def create_z(self):
        print(self.average_value)
        for i in range(0, self.count_int):
            print(self.table_interval[i][2] - self.average_value)
            self.table_interval[i].append(self.table_interval[i][2] - self.average_value)  # четвертый элемент

    def create_all_z(self):
        self.create_z_degree(2)  # пятый элемент
        self.create_z_degree(3)  # шестой элемент
        self.create_z_degree(4)  # седьмой элемент

    def create_z_degree(self, degree):
        # print(self.table_interval)
        for i in range(0, self.count_int):
            # print(f'{degree} -- {self.table_interval[i]}')
            self.table_interval[i].append(self.table_interval[i][3]**degree)

    def create_dispersion(self):
        dispersion = 0
        for i in range(0, self.count_int):
            dispersion += self.table_interval[i][0] * (self.table_interval[i][2]) / self.count
        return dispersion

    def create_root_of_dispersion(self):
        root = math.sqrt(self.dispersion)
        return root

    def search_fashion_line(self):
        marker = 0
        link_on_marker = 0
        for i in range(0, self.count_int):
            # print(self.table_interval[i])
            # print(self.table_interval[i][0])
            if self.table_interval[i][0] >= marker:
                marker = self.table_interval[i][0]
                link_on_marker = i
        return link_on_marker

    def create_fashion(self):
        x_zero = (self.fashion_line*self.length + self.min)
        n_m = self.table_interval[self.fashion_line][0]
        n_m_minus_one = self.table_interval[self.fashion_line - 1][0]
        # print(self.fashion_line)
        n_m_plus_one = self.table_interval[self.fashion_line + 1][0]
        fashion = x_zero + ((n_m - n_m_minus_one)*self.length)/((n_m - n_m_minus_one) + (n_m - n_m_plus_one))
        return fashion

    def search_median_line(self):
        marker = self.count//2
        for i in range(self.count_int):
            if marker > i*self.length + self.min + self.length:
                index = i - 1
        return index

    def create_median(self):
        x_zero = self.median_line*self.length + self.min
        n_m_minus_one_nak = self.table_interval[self.median_line - 1][1]
        n_m = self.table_interval[self.median_line][0]
        median = x_zero + ((0.5*self.count - n_m_minus_one_nak)*self.length) / n_m
        return median

    def create_m_third(self):
        m_third = 0
        for i in range(0, self.count_int):
            m_third += self.table_interval[i][0] * (self.table_interval[i][5]) / self.count
        print(f'{m_third} m_third')
        return m_third

    def create_m_fourth(self):
        m_fourth = 0
        for i in range(0, self.count_int):
            m_fourth += self.table_interval[i][0] * (self.table_interval[i][6]) / self.count
        print(f'{m_fourth} m_fourth')
        return m_fourth

    def create_a_third(self):
        print(f'{self.root_of_dispersion} root ')
        print(f'{ self.root_of_dispersion**3} root 3')
        a_third = self.m_third / self.root_of_dispersion**3
        return a_third

    def create_e_k(self):
        print(f'{self.root_of_dispersion ** 4} root 4')
        e_k = self.m_fourth / self.root_of_dispersion**4 - 3
        return e_k


# if __name__ == '__main__':
    # list = [1.1, 1.3, 1.5, 2, 2.2, 2.9, 3, 3.2, 3.2, 3.7, 3.9, 4, 4, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6, 6.8, 7.1, 7.9,
    #         8.2, 8.7, 9, 9.5, 9.6, 10.3, 10.5 ]
    # math = Statistics(list, 30)
    # print(f'{math.table_interval}. Excess:{math.excess}. Asy:{math.asymmetry}. Dis:{math.dispersion}.Ave:{math.average_value}')
