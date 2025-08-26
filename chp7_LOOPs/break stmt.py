# break statement 
# used for break the loop in between 

#break will kill the loop afteR BREAK STMT

for i in range(1,100):
    if (i==24):
        break  #this break stmt will break the sequence and exits the loop .... and prints only ythe number upt0 23
    print(i)

# continue statement 

for k in  range(1,10):
    if (k ==2): #this iteration will be skiped. loop wil iteretae the next automaticlly after skipping it 
        continue #2 will be skipped 
    print(k)
    
