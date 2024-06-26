def extend_data(data: str):
    a = data
    b = data[::-1]
    b = b.replace('1', 'x').replace('0', '1').replace('x', '0')
    return a + '0' + b


def check_sum(data):
    while len(data) % 2 == 0:
        check = ''
        for i in range(0, len(data), 2):
            #print(i)
            if data[i] == data[i + 1]:
                check += '1'
            else:
                check += '0'
        data = check
    return data


req_length = 35651584
string = "10001001100000001"

while len(string) < req_length:
    string = extend_data(string)
string = string[0: req_length]

print(check_sum(string))
