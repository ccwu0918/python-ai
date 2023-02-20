hour = int(input("請輸入24小時制==> ")) # 輸入整數值 

hour = hour-12 if hour >= 12 else hour  # 單行if/else條件敘述 

print("12小時制 =", hour)
