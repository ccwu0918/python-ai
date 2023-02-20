# play()函數的定義
def play(b):
    print("玩一次", b, "元的遊戲")

price = int(input("第1次玩多少錢的遊戲==> ")) # 輸入整數值 
play(price)    # 第1次呼叫函數
price = int(input("第2次玩多少錢的遊戲==> ")) # 輸入整數值 
play(price)    # 第2次呼叫函數
print("結束玩遊戲...")