file = open('inputDay4.txt', 'r')
f = file.readlines()
test = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""


def get_checksum(string):
    return string[len(string) - 6: len(string) - 1]


def get_id(string):
    return int(string[len(string) - 10: len(string) - 7])


def get_highest(string: str):
    string = string[:len(string) - 11].replace('-', '')

    highest_list = []
    for i in range(5):
        appeared = []
        highest_char = '@'
        for char in string:
            if char not in appeared:
                appeared.append(char)
                if string.count(char) > string.count(highest_char):
                    highest_char = char
                elif string.count(char) == string.count(highest_char) and char < highest_char:
                    highest_char = char
        highest_list.append((highest_char, string.count(highest_char)))
        #print(f'{highest_char}: {string.count(highest_char)}')
        string = string.replace(highest_char, '')
    return highest_list


def validate(string):
    highest_list = get_highest(string)
    checksum = get_checksum(string)
    for i in range(5):
        char = checksum[i]
        count = string.count(char) - 1
        correct_char = highest_list[i][0]
        correct_count = highest_list[i][1]
        if not (count == correct_count and char == correct_char):
            return False
    return True


def cipher(string: str):
    num = get_id(string)
    string = string[:len(string) - 11].replace('-', '')

    for i in range(num):
        for j in range(len(string)):
            s = list(string)
            if s[j] == 'z':
                s[j] = 'a'
            else:
                s[j] = chr(ord(s[j]) + 1)
            string = "".join(s)
    return string


sum = 0
for line in f:
    name = line.strip()
    if validate(name):
        sum += get_id(name)
        if ("northpole" in cipher(name)):
            print(name)
            print(cipher(name))

