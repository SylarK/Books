#str.capitalize() - the first letter is capitalized

var1 = 'lord king'
var1.capitalize()

#str.casefold() - it's a kind of lower(), but more agressive.

var2 = '&@&*#!*###  cCCSSSPsoa'
var2.casefold()

#str.upper()

#str.lower() - ever letters is lowed

var3 = 'STAR WARS'
var3.lower()

#str.center(width, [fillchar]) - centered in a string of length width
var4 = 'Services.msc'
var4.center(50, '-')

#str.count()

#str.encode(enconding='utf-8', errors='strict') - return a encoded version of the string as a byte objects.
var5 = 'password'
var5.encode() 

#str.endswith(suffix) - Return true with the string ends with the specific suffix

#str.index(sub)

#str.find(sub)

#str.isalnum() - Return true with all carac is alphanumeric
#str.isalpha()
#str.isascii()
#str.isdecimal()
#str.isdigit()
#str.isidentifier()
#str.islower()
#str.isnumeric()

#str.replace(old, new[, count])

var6 = 'The spirit come'
print(var6.replace('The','A'))

#str.split() - Return a list of word in the string, using sep a delimiter string

var7 = 'Lower, Hipster, Hacker moon'
print(var7.split(','))
print(var7.split(' '))






