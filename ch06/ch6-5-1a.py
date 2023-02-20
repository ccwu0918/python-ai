# add()函數的定義
def add(a, b):
    return a + b

x = int(input("請輸入第1個整數==> ")) # 輸入整數值 
y = int(input("請輸入第2個整數==> ")) # 輸入整數值 

total = add(x, y)              # 呼叫函數 
print("x=", x)
print("y=", y)
print("x + y加法總和=", total)  # 顯示總和
