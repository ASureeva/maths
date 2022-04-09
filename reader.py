import pandas


def cypher_code():
    # with open(file, "r", encoding="utf-8") as file_read:
    #     result = file_read.read()
    #     print(result)
    data = pandas.read_excel('C:/Users/annas/Downloads/Telegram Desktop/output.xlsx', sheet_name='Sheet1')

    # data.to_csv(index=False)
    # data = pandas.read_excel(file)
    return data

#
# if __name__ == '__main__':
#     i = input()
#     k = cypher_code(i)
#     print(k)
