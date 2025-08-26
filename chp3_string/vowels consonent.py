# seperating vowels and consonenest 
# take 2 empty strings , one for vowels  and one for consonnet
# if you using "range"  only then you can access the value from particular index, 
# either 

str = "hello world"
vowels = ["a", "e", "i", "o", "u", 'A',"B", "E", "I", "O", "U"]
vow = ""
consonent = ""
for i in str:
    if i in vowels:
        vow += i
    else:
        consonent += i
print("vowels ", vow)
print("consonent ", consonent)


 


