# volume()函數的定義
def total(a, b, c):
    return a + b + c

r3 = total(1, c=3, b=2)   # 混合使用位置和關鍵字參數
r4 = total(1, 2, c=3)     # 混合使用位置和關鍵字參數
print("總和 = ", r3)
print("總和 = ", r4)
