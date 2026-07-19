nums = input().split(".")

result = ""

if len(nums) == 4:
    b_nums = []
    for n in nums:
        if n.isdigit():
            if int(n) in range(0, 256):
                b_nums.append(format(int(n), "b"))
            else:
                break
                result = "Некорректный IP-адрес"
        else:
            break
            result = "Некорректный IP-адрес"
    if len(b_nums) == 4:
        result = f"{b_nums[0].zfill(8)}.{b_nums[1].zfill(8)}.{b_nums[2].zfill(8)}.{b_nums[3].zfill(8)}"
    else:
        result = "Некорректный IP-адрес"
else:
    result = "Некорректный IP-адрес"

print(result)
