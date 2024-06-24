import hashlib

id = "uqwqemis"
password = ""
i = 0
while len(password) < 8:
    string = id + str(i)
    result = hashlib.md5(string.encode()).hexdigest()
    if result[:5] == "00000":
        password = password + result[5]
        print(result)
    i += 1


print(password)
