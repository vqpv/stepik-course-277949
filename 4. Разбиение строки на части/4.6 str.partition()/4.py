s = input()

p = s.partition("=")

print("Нет значения" if not p[-1] else p[-1])
