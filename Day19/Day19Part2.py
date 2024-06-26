elf_count = 3005290
elves = [i + 1 for i in range(elf_count)]


index = 0
while len(elves) > 1:
    count = len(elves)
    index_across = index + int(count / 2)
    if index_across >= count:
        index_across -= count
    else:
        index += 1
    elves.pop(index_across)
    count -= 1
    if index >= count:
        index = 0
    if count % 1000 == 0: print(count)


print(elves)


