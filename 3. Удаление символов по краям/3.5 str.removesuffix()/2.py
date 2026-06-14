s = input()

s = s.removeprefix("/xp")
s = s.removesuffix(";")
s = s.strip()

print("+" if s.removeprefix("+").removeprefix("-").isdigit() else "-")
