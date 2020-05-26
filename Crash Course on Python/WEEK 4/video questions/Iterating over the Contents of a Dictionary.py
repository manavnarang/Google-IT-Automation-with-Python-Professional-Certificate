#Now, it's your turn! Have a go at iterating over a dictionary!

#Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
#Remember that the items method returns a tuple of key, value for each element in the dictionary.

#Solution:

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animals,organ in cool_beasts.items():
    print("{} have {}".format(animals,organ))
