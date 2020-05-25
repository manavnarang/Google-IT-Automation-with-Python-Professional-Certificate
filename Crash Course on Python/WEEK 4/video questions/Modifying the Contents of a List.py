#The skip_elements function returns a list containing every other element from an input list, 
#starting with the first element. 
#Complete this function to do that, using the for loop to iterate through the input list.

#method-1
def skip_elements(elements):
  new_list = []
  for index,element in enumerate(elements):
    if index == 0:
      new_list.append(element)
    elif (index % 2) == 0: 
      new_list.append(element)
  return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


#method-2
def skip_elememts(elements):
  return elements[::2]
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
