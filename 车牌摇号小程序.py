import string
import random

uppercase = string.ascii_uppercase
digits = string.digits

alphabet_ = uppercase + digits
print("请输入您该车所在省的简称及所在地代码")
area = input()
for number_of_times in range(1, 4):
    for numbers in range(1, 21):
        number_ = random.sample(alphabet_, 5)
        value = "".join(number_)
        if numbers % 5 == 0:
            print(f"{area}-{value}")
        else:
            print(f"{area}-{value}", end=" ")
    print(f"请选择您心仪的号码，若没有请输入NEXT刷新，您当前剩余刷新次数{3 - number_of_times}")
    choose = input()
    if (choose == "NEXT") & ((3 - number_of_times - 1) >= 0):
        print("刷新成功")
        continue
    else:
        print("输入错误或刷新次数不足")
        break
