s = input()

lst = s.partition("# ")

print(f'"""{lst[-1].capitalize().rstrip(".")}."""')
print(lst[0])
