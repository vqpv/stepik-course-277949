s = input()

p_1 = s.rpartition("+")
p_2 = s.rpartition("-")

if p_1[-1].isdigit():
    print(f"Доход {p_1[-1]} марок")
elif p_2[-1].isdigit():
    print(f"Расход {p_2[-1]} марок")
