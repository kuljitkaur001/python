# funtion , 

# takes user imput
# length = specified (12)
# capital =  2 lttr 
# numbers = 4
# sepecial chr =  2
# small letters: 4 apply if 

# we need 4 function 
# define function  oasswrd validate 
# give base conditions 
# at the the starting 
# 

def password_validate(Input):
    if (len(Input ) >= 12 ):
        print("valid")
         
        count = 0 
        for i in Input:
            if i.isupper():
                count +=1
            if count >=4:
                return True
        return False 
    
    elif(Input.)
    
    
        

    
    else:
        print("pasword must be conatain 12 characters ")

    

    

enter = input("enter the charcters of your password : ")
password_validate(enter)
