f = open("F:\\python\\chp13_file handling.py\\rought.text", "r+")
f.write("this is prianka , a data scientist")
f.close()


g = open("F:\\python\\chp13_file handling.py\\rought.text", "r+")
print(g.read())
g.close()