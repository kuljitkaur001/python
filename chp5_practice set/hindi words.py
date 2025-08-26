# write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up

hindi_words  = {"prikshrm"  :"hardwork",
                "prasshansa"  : "khushi", 
                "adhunik" : "moderan",
                "swasthya" : "health", 
                "nimrata" : "patience" }
print(hindi_words.items())

word = input("which word you want to find : ") #always use square brases when to access the from the dictionary 
print(hindi_words[word])



