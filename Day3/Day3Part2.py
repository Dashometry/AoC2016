file = open('../inputDay3.txt', 'r')
f = file.readlines()

triangles = []

for line in f:
    triangle = []
    triangle.append(int(line[2:5].strip()))
    triangle.append(int(line[7:10].strip()))
    triangle.append(int(line[12:].strip()))
    triangles.append(triangle)

trianglesNew = []
for col in range(3):
    i = 0
    triangleNew = []
    for row in triangles:
        if i != 0 and i % 3 == 0:
            trianglesNew.append(triangleNew)
            triangleNew = []
        triangleNew.append(triangles[i][col])
        i += 1
    trianglesNew.append(triangleNew)


count = 0
for triangle in trianglesNew:
    for i in triangle:
        print(i, end=" ")
    print()

    s1 = triangle[0]
    s2 = triangle[1]
    s3 = triangle[2]

    if (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1:
        count += 1

print(count)