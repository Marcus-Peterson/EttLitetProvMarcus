from dictionary4 import update_or_insert


dictionary = {}
assert update_or_insert(dictionary, "nyckel1", "värde1") == "Nyckeln har lagts in med värdet"
assert dictionary == {"nyckel1" : "värde1"}
assert update_or_insert(dictionary, "nyckel1", "nyttvärde") == "Nyckeln fanns och fick ett nytt värde"
assert dictionary == {"nyckel1" : "nyttvärde"}
assert update_or_insert(dictionary, "nyckel2", "värde2") == "Nyckeln har lagts in med värdet"
assert dictionary == {"nyckel1" : "nyttvärde", "nyckel2" : "värde2"}
assert update_or_insert(dictionary, "nyckel2", "nyttvärde2") == "Nyckeln fanns och fick ett nytt värde"
assert dictionary == {"nyckel1" : "nyttvärde",  "nyckel2" : "nyttvärde2"}

