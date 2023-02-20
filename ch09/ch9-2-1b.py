import os
 
path = os.getcwd() + "\\temp"
os.chdir(path)
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(path))
