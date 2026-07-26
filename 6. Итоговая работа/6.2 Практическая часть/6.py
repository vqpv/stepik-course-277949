s = input()

result = False
s = s.replace(" ", "")
s = s.replace("--", "+")

if s.count("=") == 1:
    a, b = s.split("=")
    if a and b and b.lstrip("-").isdigit():
        if "+" in s and s.count("+") == 1:
            n_1, n_2 = a.split("+")
            if n_1.lstrip("-").isdigit() and n_2.lstrip("-").isdigit():
                result = True
        elif "*" in s and s.count("*") == 1:
            n_1, n_2 = a.split("*")
            if n_1.lstrip("-").isdigit() and n_2.lstrip("-").isdigit():
                result = True
        elif "/" in s and s.count("/") == 1:
            n_1, n_2 = a.split("/")
            if n_1.lstrip("-").isdigit() and n_2.lstrip("-").isdigit():
                result = True
        elif "-" in s:
            if s.count("-") == 1:
                n_1, n_2 = a.split("-")
            else:
                n_1, n_2 = a.lstrip("-").split("-")
            if n_1.lstrip("-").isdigit() and n_2.lstrip("-").isdigit():
                result = True

print(result)
