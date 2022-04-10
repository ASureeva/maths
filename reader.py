import pandas


def cypher_code(file, sheet):
    result = [False, 0]
    try:
        result[1] = pandas.read_excel(file, sheet_name=sheet)
        result[0] = True
    except Exception:
        print('не могу прочитать')
    return result

#
# if __name__ == '__main__':
#     i = input()
#     k = cypher_code(i)
#     print(k)
#     data = pandas.read_excel('C:/Users/annas/Downloads/Telegram Desktop/output.xlsx', sheet_name='Sheet1')
