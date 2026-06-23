s = input()
N = int(input())
M = int(input())

lst = s.split("~")

print("\n".join(lst[N - 1:M]))
