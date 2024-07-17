directions = "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"
directionList = directions.split(", ")
test = "R5, L5, R5, R3".split(", ")
xPos = 0
yPos = 0
direction = 0
visited = []
end = False
for i in directionList:
    if i[0] == 'R':
        direction += 1
    else:
        direction -= 1
    val = int(i[1:])
    for j in range(val):
        if (direction % 4) == 1:
            xPos += 1
        elif (direction % 4) == 2:
            yPos += 1
        elif (direction % 4) == 3:
            xPos -= 1
        else:
            yPos -= 1

        print(str(xPos) + " " + str(yPos))

        if (xPos, yPos) in visited:
            print(abs(xPos) + abs(yPos))
            end = True
            break
        else:
            visited.append((xPos, yPos))
    if end:
        break
