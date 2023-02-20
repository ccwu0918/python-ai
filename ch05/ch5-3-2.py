i = 1
total = 0  
max_value = int(input("請輸入最大值==> "))  # 輸入整數值 

while i <= max_value:     # while條件迴圈 
    total = total + i
    i = i + 1
     
print("從1加至max_value的總和=", total)
