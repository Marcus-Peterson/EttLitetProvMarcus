""" Skapa en funktion med namnet:
update_or_insert
 som tar emot 3 argument.
Det första argumentet som skickas kommer vara av typen dict
Det andra argument är nyckeln.
Det tredje argumentet är värdet.
Key:value/nyckelvärde ska uppdateras eller läggas in dict
Om nyckeln redan fanns i dict som skickades in
så ska metoden returnera strängen:
"Nyckeln fanns och fick ett nytt värde"
Om nyckeln inte fanns i dict som skickades in
så ska metoden returnera strängen:
"Nyckeln har lagts in med värdet"

Tips: metoden dict.get() kan vara bra att använda
   """

dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}

def update_or_insert(arg1,arg2,arg3):
       if arg2 in arg1:
             x = arg1.setdefault(arg2,arg3)
             return "Nyckeln fanns och fick ett nytt värde:",arg1
       elif arg2 not in arg1:
             x = arg1.setdefault(arg2,arg3)
             return "Nyckeln har lagts in med värde"


print(update_or_insert(dictionary, "nyckel3", "värde1"))
             

