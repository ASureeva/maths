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
        self.m_third = self.create_m_third()
        self.m_fourth = self.create_m_fourth()
        self.asymmetry = self.create_a_third()
        self.excess = self.create_e_k()
        self.data = []
        self.lis = []
        self.histogram()

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
        if length * self.count_int == self.max - self.min:
            length += length*0.01/100
        return length

    def create_table_interval(self):
        for i in range(0, self.count_int):
            self.table_interval[i] = {
                'frequency': 0,  # 0
                'frequency_funded': 0,  # 1
                'x': 0,  # 2
                'z': 0,  # 3
                'z_two': 0,  # 4
                'z_third': 0,  # 5
                'z_fourth': 0  # 6
            }

    def create_n(self):
        step = 0
        accumulation = 0
        count_inter = self.min
        for i in range(0, self.count):
            if self.list[i] < step*self.length + self.min + self.length:
                self.table_interval[step]['frequency'] += 1  # первый элемент
                accumulation += 1
                self.table_interval[step]['frequency_funded'] = accumulation
            elif step != 5:
                step += 1
                self.table_interval[step]['frequency'] += 1  # первый элемент
                accumulation += 1
                self.table_interval[step]['frequency_funded'] = accumulation
                count_inter = count_inter + self.length

    def create_x(self):
        for i in range(0, self.count_int):
            self.table_interval[i]['x'] = ((i*self.length + self.min*2 + (i+1)*self.length)/2)  # третий элемент

    def search_average_value(self):
        average_value = 0
        for i in range(0, self.count_int):
            average_value += (self.table_interval[i]['frequency'] * (self.table_interval[i]['x'])) / self.count
        return average_value

    def create_z(self):
        for i in range(0, self.count_int):
            self.table_interval[i]['z'] = (self.table_interval[i]['x'] - self.average_value)  # четвертый элемент

    def create_all_z(self):
        self.create_z_degree(2, 'z_two')  # пятый элемент
        self.create_z_degree(3, 'z_third')  # шестой элемент
        self.create_z_degree(4, 'z_fourth')  # седьмой элемент

    def create_z_degree(self, degree, name_of_degree):
        for i in range(0, self.count_int):
            self.table_interval[i][name_of_degree] = self.table_interval[i]['z']**degree

    def create_dispersion(self):
        dispersion = 0
        for i in range(0, self.count_int):
            dispersion += self.table_interval[i]['frequency'] * (self.table_interval[i]['z_two']) / self.count
        return dispersion

    def create_root_of_dispersion(self):
        root = math.sqrt(self.dispersion)
        return root

    def search_fashion_line(self):
        marker = 0
        link_on_marker = 0
        for i in range(0, self.count_int):
            if self.table_interval[i]['frequency'] >= marker:
                marker = self.table_interval[i]['frequency']
                link_on_marker = i
        return link_on_marker

    def create_fashion(self):
        x_zero = (self.fashion_line*self.length + self.min)
        n_m = self.table_interval[self.fashion_line]['frequency']
        n_m_minus_one = self.table_interval[self.fashion_line - 1]['frequency']
        n_m_plus_one = self.table_interval[self.fashion_line + 1]['frequency']
        fashion = x_zero + ((n_m - n_m_minus_one)*self.length)/((n_m - n_m_minus_one) + (n_m - n_m_plus_one))
        return fashion

    def search_median_line(self):
        index = 1
        marker = self.list[self.count//2] + 1
        for i in range(self.count_int):
            if i*self.length + self.min <= marker < (i+1)*self.length + self.min:
                index = i
        return index

    def create_median(self):
        x_zero = self.median_line*self.length + self.min
        n_m_minus_one_nak = self.table_interval[self.median_line - 1]['frequency_funded']
        n_m = self.table_interval[self.median_line]['frequency']
        median = x_zero + ((0.5*self.count - n_m_minus_one_nak)*self.length) / n_m
        return median

    def create_m_third(self):
        m_third = 0
        for i in range(0, self.count_int):
            m_third += self.table_interval[i]['frequency'] * (self.table_interval[i]['z_third']) / self.count
        return m_third

    def create_m_fourth(self):
        m_fourth = 0
        for i in range(0, self.count_int):
            m_fourth += self.table_interval[i]['frequency'] * (self.table_interval[i]['z_fourth']) / self.count
        return m_fourth

    def create_a_third(self):
        a_third = self.m_third / self.root_of_dispersion**3
        return a_third

    def create_e_k(self):
        e_k = self.m_fourth / self.root_of_dispersion**4 - 3
        return e_k

    def histogram(self):
        for element in range(self.count_int):
            self.data.append(self.table_interval[element]['frequency']/self.count)
            self.lis.append(self.table_interval[element]['x'])


# if __name__ == '__main__':
#     list = [1.1, 1.3, 1.5, 2, 2.2, 2.9, 3, 3.2, 3.2, 3.7, 3.9, 4, 4, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6, 6.8, 7.1, 7.9,
#             8.2, 8.7, 9, 9.5, 9.6, 10.3, 10.5 ]
#     math = Statistics(list, 30)
#     print(f'{math.table_interval}. Excess:{math.excess}. Asy:{math.asymmetry}.
#     Dis:{math.dispersion}.Ave:{math.average_value}')
