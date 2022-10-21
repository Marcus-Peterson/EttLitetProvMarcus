from dictionary2 import lista_alla_nycklar

dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}

assert lista_alla_nycklar(dictionary) == ["nyckel1", "nyckel2"]

dictionary.update({"nyckel3" : "värde3", "nyckel4" : "värde4" })

assert lista_alla_nycklar(dictionary) == ["nyckel1", "nyckel2", "nyckel3", "nyckel4"]


