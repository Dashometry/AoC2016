grid = ["^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."]
row_length = len(grid[0])
current_row = 0
rows = 400000
safe_count = 0

for i in range(rows - 1):
    new_row = ''
    for j in range(row_length):
        tile1 = ''
        tile2 = ''
        tile3 = ''
        if j - 1 == -1:
            tile1 = '.'
        else:
            tile1 = grid[i][j - 1]

        tile2 = grid[i][j]

        if j + 1 == row_length:
            tile3 = '.'
        else:
            tile3 = grid[i][j + 1]

        if (tile1 == tile2 and tile1 != tile3) or (tile2 == tile3 and tile1 != tile2):
            new_row += '^'
        else:
            new_row += '.'

    grid.append(new_row)


for row in grid:
    safe_count += row.count('.')
    #print(row)

print(safe_count)