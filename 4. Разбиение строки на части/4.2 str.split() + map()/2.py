s = input()

lst = s.split()

X, Y, Z = map(float, lst[1:])

print(f"Смещение: X={X + 5}, Y={Y + 5}, Z={Z + 5}")
