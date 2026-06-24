s = input()

lst = s.split("; ")

print("Команда 1:", ", ".join(lst[::2]))
print("Команда 2:", ", ".join(lst[1::2]))
