# volume()函數的定義
def total(a, b, c):
    return a + b + c

r1 = total(1, 2, 3)       # 函式呼叫(位置參數)
r2 = total(b=2, c=3, a=1) # 函式呼叫(關鍵字參數)
print("總和 = ", r1)
print("總和 = ", r2)
