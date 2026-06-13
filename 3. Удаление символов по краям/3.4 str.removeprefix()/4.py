n = int(input())

files = []

for _ in range(n):
    files.append(input())

prefix = ""

a, b = files[0][0], files[1][0]
c = 0

while a == b:
    prefix += a
    c += 1
    a, b = files[0][c], files[1][c]

for file in files:
    print(file.removeprefix(prefix))
