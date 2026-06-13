s = input()

s = s.strip()
s = s.removeprefix("cmd:")
s = s.removesuffix(";")

print(s)
