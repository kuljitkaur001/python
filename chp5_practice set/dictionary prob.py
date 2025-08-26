# create an empty dictionary . allow 4 frineds to enter their fav language  as value and  use key as their name. asue that the names are unique 

d = { }

name = input("\n enter your name : ")
lang = input("\n enter your language ")

d.update({name: lang})
name = input("\n enter your name : ")
lang = input("\n enter your language ")

d.update({name: lang})
name = input("\n enter your name : ")
lang = input("\n enter your language ")

d.update({name: lang})
name = input("\n enter your name : ")
lang = input("\n enter your language ")

d.update({name: lang})

print(d)
