hp = int(input())
lvl = input()
hunger = int(input())

p_1 = ("♥" * (hp // 10)).ljust(10, "♡")
p_2 = lvl.center(10)
p_3 = ("●" * (hunger // 10)).ljust(10, "○")

print(p_1 + p_2 + p_3)
