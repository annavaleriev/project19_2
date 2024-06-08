# х = "1000000"
# х1 = int(х)
# y = '{0:,}'.format(х1).replace(',', ' ')
# print(y)


def change_str_to_int(number_str):
    to_int = int(number_str)
    return '{0:,}'.format(to_int).replace(',', ' ')


х2 = "1000000"
number = change_str_to_int(х2)
print(number)

