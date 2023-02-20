import os
 
path = os.getcwd() + "\\temp"
os.chdir(path)
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(path))
os.remove("aa.txt")
print("remove(): ", os.listdir(path))
