#In Python, a dictionary can only hold a single value for a given key. 
#To workaround this, our single value can be a list containing multiple values. 
#Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
#Fill in the blanks to print a line for each item of clothing with each color, 
#for example: "red shirt", "blue shirt", and so on.

#Solution:

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key in wardrobe:
  for values in wardrobe[key]:
    print("{} {}".format(values,key))
