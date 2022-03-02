"""

@author: MyLaptop

"""
import string 
def longestWord(s):
    #remove punctuation
    for ch in string.punctuation:
        s = s.replace(ch, '')
    #split text into word  
    words = s.split()

    #search for the longest word
    count = 0    
   
    for word in words: 
        if len(word) > count: 
            count = len(word) 
            res = word
    
    #return the longest result word
    return ("the longest word in "+ "-" + s + "-" +" is " + res + " with "+ str(len(res)) +" character")


 #it works in console
text = "Les sanglots longs des violons de l’automne blessent mon cœur d’une langueur monotone. Tout suffocant et blˆeme, quand sonne l’heure, je me souviens des jours anciens et je pleure."
longestWord(text)

