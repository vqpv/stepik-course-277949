s = input()

p_1 = s.partition("@")
p_2 = p_1[-1].partition(".")

print(p_1[0])
print(p_2[0])
print(p_2[-1])
