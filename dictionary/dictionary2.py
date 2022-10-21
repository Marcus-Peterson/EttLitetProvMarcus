dictionary = {"nyckel1" : "värde1", "nyckel2" : "värde2"}
""" Skapa en funktion med namnet:
lista_alla_nycklar
returnerar alla nycklar som en lista från ett dict som ska anges som argument
Tips: Använd lämpligtvis for och metoden dict.keys()
  """

def lista_alla_nycklar():
      en_lista = list()
      for i in dictionary:
            en_lista.append(i)
      return en_lista

print(lista_alla_nycklar())
