# write a program to accept marks of 6 students and display thme in a sorted manner
marks = [ ]

stu1 =  int(input("mark 1: "))
marks.append(stu1)

stu2 = int(input("mark 2: "))
marks.append(stu2)

stu3 = int(input("mark 3: "))
marks.append(stu3)

stu4 = int(input("mark 4: "))
marks.append(stu4)

stu5 = int(input("mark 5: "))
marks.append(stu5)

stu6 = int(input("mark 6: "))
marks.append(stu6)

print(sorted(marks))
