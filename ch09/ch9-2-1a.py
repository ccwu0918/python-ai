import os
 
path = os.getcwd() + "\\temp"
print("目前工作路徑: ", os.getcwd())
print(path)
os.chdir(path)
print("chdir(): ", os.getcwd())
os.mkdir('newDir')
print("mkdir(): ", os.listdir(path))
