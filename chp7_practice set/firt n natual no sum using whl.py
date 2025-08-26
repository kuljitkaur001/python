# sum of first natutal number using while

# when ever this kind of programs .... you need to initialize the val of sum with 1 

# and by default you need to take i = any number , in the case of while loop 
# do not use print stmt just after while 
# write increment statemnt .... in the while  (always incremnt using i )
# after completing while.. write print stmt out of the while  ....


number =  int(input("\n \n enter the numbr : "))

sum = 0
i = 1
while(i<=number):
    sum += i
    i += 1 #incremnt stmt 

print(sum)

    