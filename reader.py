import pandas


def cypher_code(file, sheet):
    data = pandas.read_excel(file, sheet_name=sheet)
    return data

#
# if __name__ == '__main__':
#     i = input()
#     k = cypher_code(i)
#     print(k)
#     data = pandas.read_excel('C:/Users/annas/Downloads/Telegram Desktop/output.xlsx', sheet_name='Sheet1')
