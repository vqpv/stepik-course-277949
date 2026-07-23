replacement_table = input()
text = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for i in text.lower():
    if i in alphabet:
        result += replacement_table[alphabet.find(i)]
    else:
        result += i

print(result)
