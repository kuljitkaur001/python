f = open("F:\\python\\chp13_file handling.py\\rought.text", "r+")
f.writelines(["hello\n","pyhon \n" ])
print(f.tell())
f.close()