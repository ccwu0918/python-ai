target = 38
guess = 1
while True:               # while無窮迴圈
    guess = int(input("請輸入猜測的數字(1~100) => "))
    if target == guess:   # if條件敘述
        break             # 跳出迴圈
    if guess > target:    # if/else條件敘述 
        print("數字太大!")
    else:
        print("數字太小!")
print("猜中數字 = ", target)
