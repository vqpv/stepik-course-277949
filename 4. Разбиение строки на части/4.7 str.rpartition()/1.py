s = input()

p = s.rpartition(".")

print("Имя:", p[0])
print("Разделитель:", p[1])
print("Расширение:", p[-1])
