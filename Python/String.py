import string

str="Yash veer Singh"    # create string

# accessing
print(str[2])

# Slicing
print(str[2:10])

# reverse
print(str[::-1])

# delete
print(str[:4]+str[5:])

# update
print(str[:4]+" veer "+str[5:])

# formating of string
print("{} {} {}".format("yash","veer","singh"))
print("{1} {0} {2}".format("yash","veer","singh"))
#print("{l} {f} {g}".format("yash","veer","singh"))

print("{0:b}".format(10))
print("{0:e}".format(12345.076))
print("{0:.2f}".format(1/6))

print("|{:<10}|{:^10}|{:>10}|".format("yash","veer","singh"))

print("teh value of %3.2f"%23)

# Built function
print(string.ascii_letters) #return all alphabets
print(string.ascii_lowercase) #return all lowercase alphabets
print(string.ascii_uppercase) #return all uppercase alphabets
print(string.digits) #return all digits
print(string.hexdigits) #return all hexadigits
#print(string.letters())
#print(string.lowercase)
print(string.octdigits) #return all octadigits
print(string.punctuation) #return all punctuation
print(string.printable) #return all symbols
print(str.endswith("gh")) # true or false
print(str.startswith("veer")) # true or false
print(str.isdigit()) # true or false
print(str.isalpha()) # true or false
print(str.isdecimal()) # true or false
print(str.index("ee")) # string index from right

print("\n".isspace()) # true or false
print(str.swapcase()) # true or false
print("\n".replace("veer","VEER")) # return new string
print(str.isalnum()) # true or false
print("\n".istitle()) # true or false

print(str.partition("veer")) # splits the string at the first occurrence of the separator and returns a tuple. 
print(str.rpartition("veer"))
print(str.isidentifier()) # Check whether a string is a valid identifier or not
print(len(str)) # return length of string
print(str.rindex("s")) # return index from right
print(max(str)) # return max elements
print(min(str)) # return min elements
print(str.splitlines()) # Returns a list of lines in the string.
print(str.capitalize()) # Return a word with its first character capitalized.
print(str.expandtabs()) # Expand tabs in a string replacing them by one or more spaces
print(str.find("ee")) # 
print(str.rfind("sh"))
print(str.lower())
print(str.upper())
print(str.split())
print(str.rsplit())
print(str.ljust(15))
print(str.rjust(20))
print(str.center(40))
print(str.zfill(12))
print(str.casefold())
print(str.encode())
print(str.maketrans(str,str,str))















