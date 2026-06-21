s = input()

lst = list(map(chr, (map(int, s.split()))))

print(*lst, sep="")
