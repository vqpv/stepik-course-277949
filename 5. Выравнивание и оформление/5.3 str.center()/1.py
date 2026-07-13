s = input()

if len(s) > 20:
    print(s[:20])
else:
    print(s.center(20, "="))
