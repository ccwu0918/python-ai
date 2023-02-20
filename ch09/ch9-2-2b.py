import os.path as path
 
p = "C:\Python\ch09"
f = "ch9-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)
