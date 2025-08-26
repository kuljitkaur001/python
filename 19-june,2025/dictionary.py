# for only keys 
print("for printin valus only")
dict={"name " :  "kuljit",
    "age " : "21",
    "sub " : "b"}
for i in dict:
    print(i)

# for only values 
print("acessign only values using for loop ")
dict={"name " :  "kuljit",
    "age " : "21",
    "sub " : "b"}
for i in dict:
    print(dict[i])

# printing whole dictionary ..
print("taking whole dictioanry using items function ")
dict={"name " :  "kuljit",
    "age " : "21",
    "sub " : "b"}
for i in dict.items():
    print(i)


print(dict.items())