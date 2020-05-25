#q1
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for files in range (len(filenames)):
  if "hpp" in filenames[files][3:]:
    newfilenames.append(filenames[files][:-2])
  else:
    newfilenames.append(filenames[files])
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


#q2
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # Create the pig latin word and add it to the list
    say+=word[1:]+word[0]+"ay "
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


#q3
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for m in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if m >= value:
                result += letter
                m-= value
            else:
                result+="-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

#q5
def group_list(group, users):
    result = ""
    if len(group)!=0:
        result += group+":"
    if len(users)!=0:
        result += " "+users[0]
    if len(users)>1:
        for x in users[1:]:
            result += ", "+x
    return result

# Testing
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print (group_list("Users",""))

#q6
def guest_list(guests):
  count = 0
  if count < 1:
	  for guest in guests:
		  name,age,job=guest
		  print("{} is {} years old and works as {}".format(name,age,job))
		  count =count +1
	

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
