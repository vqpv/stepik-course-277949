s = input()

items = s.split(", ")

print("Есть место" if len(items) <= 20 else "Инвентарь полон")
