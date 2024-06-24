file = open('inputDay9.txt', 'r')
f = file.readlines()


def decompress(string):
    final_length = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            marker = ''
            i += 1
            while string[i] != ')':
                marker = marker + string[i]
                i += 1
            i += 1
            length = int(marker.split('x')[0])
            count = int(marker.split('x')[1])
            repeated = ''
            for x in range(length):
                repeated = repeated + string[i]
                i += 1
            final_length += count * decompress(repeated)
        else:
            i += 1
            final_length += 1
    return final_length


wholeInput = "".join(f).replace(' ', '').replace('\n', '')

print(decompress(wholeInput))
print(decompress("(3x3)XYZ"))
