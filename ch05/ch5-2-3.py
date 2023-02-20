total = 0  
max_value = int(input("請輸入最大值==> ")) # 輸入整數值 

for i in range(1, max_value+1):    # for計數迴圈
    total = total + i
     
print("從1加至max的總和=", total)

