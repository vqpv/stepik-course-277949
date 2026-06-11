username = input()

username = username.removeprefix("@").lower()

print(f"https://t.me/{username}")
