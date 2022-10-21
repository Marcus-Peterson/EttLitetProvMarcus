from dictionary1 import dictionary
from dictionary1 import fyll_på



assert dictionary == {"nyckel1" : "värde1", "nyckel2" : "värde2"}

fyll_på()
assert dictionary == {"nyckel1" : "värde1", "nyckel2" : "värde2",
"nyckel3" : "värde3", "nyckel4" : "sista" }