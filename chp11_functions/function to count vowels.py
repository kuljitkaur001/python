# Do you want to write a function that counts vowels in a string?
# in the case of finding use in operator .. 
def vowels(vow):
    count = 0 
    voww = ["a","e","i","o","u",]
    for i in vow:
        if i in voww: # this means that if any value of i is present tin vow list 
            count = count + 1
    return count

str = "hello world"
print("vowels in a strng : ", vowels(str)) 