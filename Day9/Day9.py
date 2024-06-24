file = open('inputDay9.txt', 'r')
f = file.readlines()


def remove_char_at(string, i, count):
    return string[:i] + string[i + count:]


def decompress(string):
    i = 0
    while i < len(string):
        if string[i] == '(':
            marker = ''
            string = remove_char_at(string, i, 1)
            while string[i] != ')':
                marker = marker + string[i]
                string = remove_char_at(string, i, 1)
            string = remove_char_at(string, i, 1)
            length = int(marker.split('x')[0])
            count = int(marker.split('x')[1])
            repeated = ''
            for x in range(length):
                repeated = repeated + string[i]
                i += 1
            for x in range(count - 1):
                string = string[:i] + repeated + string[i:]
                i += length
        else:
            i += 1
    return string


wholeInput = "".join(f).replace(' ', '').replace('\n', '')
decompressed = decompress(wholeInput)
print(decompressed)
print(len(decompressed))
print(decompress("A(1x5)BC"))
