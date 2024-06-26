class Disc:
    def __init__(self, num, positions, offset):
        self.num = num
        self.positions = positions
        self.offset = offset

    def is_free(self, time):
        return (time + self.num + self.offset) % self.positions == 0


discs = []
discs.append(Disc(1, 13, 11))
discs.append(Disc(2, 5, 0))
discs.append(Disc(3, 17, 11))
discs.append(Disc(4, 3, 0))
discs.append(Disc(5, 7, 2))
discs.append(Disc(6, 19, 17))
discs.append(Disc(7, 11, 0))

i = -1
valid = False
while not valid:
    i += 1
    valid = True
    for disc in discs:
        if not disc.is_free(i):
            valid = False
            break


print(i)
