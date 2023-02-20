# bigger()函數定義: 回傳2個參數的最大值
def bigger(a, b):
    if a > b:
       return a, b
    else:
       return b, a
 
t = bigger(10, 30)    # 呼叫函數
c, d = bigger(10, 30)
print(t)
print(c, d)
print(type(t))
