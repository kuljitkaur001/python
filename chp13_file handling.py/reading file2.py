f =  open("F:\\python\\chp13_file handling.py\\rought.text", "r+")
print(f.readlines())
print(f.seek(0))
f.close()