# find the 2nd largest number 
# firtsly sort the list
def largest(list1):
    n = len(list1)
    for i in range(len(list1)):
        for j in range(i+1, len(list1)): #this j is starting from 2nd index val 
            if list1[i]>list1[j]: # if first indexed val is greaterthan 2nd indexed val 
                list1[i],list1[j]=list1[j],list1[i] # swap , i is swapped with j, and j is swapped with i 
    print(list1[n-2])  #if n-1 , it will return the last val 6-1 = 5th index will be largesr , but n-2 , 6-2 = [4] th indexed val will ber the largest with ythe list is sort 



list12  = int(input("enter elemnt of list: "))
largest( [12,34,56,43,7,8] )