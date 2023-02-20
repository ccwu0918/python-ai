import os.path as path
 
fname = path.realpath("ch9-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)

