#The "toc" dictionary represents the table of contents for a book. 
#Fill in the blanks to do the following: 
#1) Add an entry for Epilogue on page 39. 
#2) Change the page number for Chapter 3 to 24. 
#3) Display the new dictionary contents. 
#4) Display True if there is Chapter 5, False if there isn't.

#Solution:
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39
toc["Chapter 3"]=24
print(toc)
print('Chapter 5' in toc)
