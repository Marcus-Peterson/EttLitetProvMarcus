dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}
""" Skapa en funktion med namnet:
lista_alla_värden
returnerar alla nycklar som en lista från ett dict som ska anges som argument
Tips: Använd lämpligtvis for och metoden dict.values()
  """

def lista_alla_värden(dict_):
      return list(dict_.keys())


print(lista_alla_värden(dictionary))
