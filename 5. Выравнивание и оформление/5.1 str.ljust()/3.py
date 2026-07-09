s = input()
n = input()

print(s.ljust(20 - len(n), ".") + n)
