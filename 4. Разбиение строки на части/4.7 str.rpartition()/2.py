s = input()

p = s.rpartition(".")

print(p[0] if p[0] else s)
