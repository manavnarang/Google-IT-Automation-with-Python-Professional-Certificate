#Want to try some string methods yourself? Give it a go!

#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received,
#in upper case. 
#For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.





def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
