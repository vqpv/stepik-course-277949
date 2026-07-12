W = int(input())
L = int(input())
n = input()
c = input()

a = W // L
s_1 = "Игрок: " + n
s_2 = "Счет: " + c

print(s_1 + s_2.rjust(a - len(s_1)))
