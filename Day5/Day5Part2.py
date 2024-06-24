import hashlib


def display_list(array):
    for char in array:
        print(char, end= ", ")
    print()


char_list = ['', '', '', '', '', '', '', '']
id = "uqwqemis"
password = ""
i = 0
while '' in char_list:
    string = id + str(i)
    result = hashlib.md5(string.encode()).hexdigest()
    if result[:5] == "00000" and result[5].isdigit():
        index = int(result[5])
        print(index)
        if index < 8 and char_list[index] == '':
            char_list[index] = result[6]
            display_list(char_list)
        print(result)
    i += 1

password = "".join(char_list)
print(password)
