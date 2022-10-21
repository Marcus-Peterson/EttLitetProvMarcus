from dictionary3 import lista_alla_värden

dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}

assert lista_alla_värden(dictionary) == ["värde1", "värde2"]

dictionary.update({"nyckel3" : "värde3", "nyckel4" : "värde4" })

assert lista_alla_värden(dictionary) == ["värde1", "värde2", "värde3", "värde4"]


