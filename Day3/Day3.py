file = open('../inputDay3.txt', 'r')
f = file.readlines()

triangles = []

for line in f:
    triangle = []
    triangle.append(int(line[2:5].strip()))
    triangle.append(int(line[7:10].strip()))
    triangle.append(int(line[12:].strip()))
    triangles.append(triangle)

count = 0
for triangle in triangles:
    for i in triangle:
        print(i, end=" ")
    print()

    s1 = int(triangle[0])
    s2 = int(triangle[1])
    s3 = int(triangle[2])

    if (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1:
        count += 1

print(count)