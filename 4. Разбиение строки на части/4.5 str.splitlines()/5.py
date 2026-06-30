lines = text.splitlines()

print(*(l for l in lines if l), sep="\n")
