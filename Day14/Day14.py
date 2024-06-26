import hashlib
salt = "jlmsuwbz"
test = "abc"


def get_triple(string: str):
    triple = ''
    for i in range(len(string) - 2):
        triple = string[i: i + 3]
        if triple[0] == triple[1] == triple[2]:
            return triple[0]
    return ''


keys_queue = []
keys = []
key_indices = []

i = -1
while len(keys) < 64:
    i += 1
    string = salt + str(i)
    result = hashlib.md5(string.encode()).hexdigest()

    for j in range(2016):
        result = hashlib.md5(result.encode()).hexdigest()

    triple_char = get_triple(result)
    if len(triple_char) > 0:
        keys_queue.append((triple_char, i + 1000))

    keys_to_remove = []
    for pair in keys_queue:
        if i > pair[1]:
            keys_to_remove.append(pair)
            continue
        if pair[1] - i != 1000 and pair[0] * 5 in result:
            keys.append(pair[0] * 5)
            key_indices.append(pair[1] - 1000)
            keys_to_remove.append(pair)
            print(len(keys))

    for key in keys_to_remove:
        keys_queue.remove(key)


print(i)
print(keys)
print(keys_queue)
print(sorted(key_indices))
print(len(key_indices))
print(key_indices[63])

