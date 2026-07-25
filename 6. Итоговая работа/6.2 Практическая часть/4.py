s = input()

a, b = s.split(";")

new_a = a.replace(" ", "").lower()
new_b = b.replace(" ", "").lower()

print(sorted(new_a) == sorted(new_b))
