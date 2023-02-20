# maxValue()函數的定義
def maxValue(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("請輸入第1個整數==> ")) # 輸入整數值 
y = int(input("請輸入第2個整數==> ")) # 輸入整數值 

result = maxValue(x, y)  # 呼叫函數 
print("x=", x)
print("y=", y)
print("最大值:", result) # 顯示最大值
