n = int(input())
x = input()

print("┌" + "─" * n + "┐")
print("│" + x.rjust(n) + "│")
print("└" + "─" * n + "┘")
