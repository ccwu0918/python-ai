# play()函數的定義
def play(b, t):
    print("玩", t, "次", b, "元的遊戲")
    result = b * t
 
    return result

price = int(input("玩多少錢的遊戲==> ")) # 輸入整數值 
t = int(input("玩多少次遊戲==> "))       # 輸入整數值 

total = play(price, t)        # 呼叫函數 

print("總計的金額是:", total)  # 顯示總金額
