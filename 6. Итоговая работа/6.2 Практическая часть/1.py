s = input()
r = input()

if r == "нижний":
    print(s.lower())
elif r == "верхний":
    print(s.upper())
elif r == "заголовочный":
    print(s.title())
elif r == "противоположный":
    print(s.swapcase())
elif r == "первая заглавная":
    print(s.capitalize())
elif r == "жёсткий нижний":
    print(s.casefold())
else:
    print(s)
