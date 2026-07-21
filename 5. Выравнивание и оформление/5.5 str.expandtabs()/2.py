s = input()

s = s.replace("\\t", "\t")

print(s.expandtabs(16).count(" "))
