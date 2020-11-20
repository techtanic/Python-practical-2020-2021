'''Write a python program to read the content of text file and display the total
number of consonants, vowels, upper case letters, lower case letters, digits
and special characters.'''

f = open("para.txt")
lines = f.readlines()
f.close()

vowels = ("a", "e", "i", "o", "u")

c, v, u, l, d, s = 0,0,0,0,0,0

for line in lines:
    line = line.split()
    for word in line:
        for char in word:

            if char.isalpha():
                if char in vowels:
                    v += 1
                if not char in vowels:
                    c += 1
                if char.isupper():
                    u += 1
                if char.islower():
                    l += 1
            if char.isdigit():
                d += 1
            if not char.isalnum():
                s += 1
print("No. of consonants =",c)
print("No. of vowels =",v)
print("No. of digits =",d)
print("No. of upper case =",u)
print("No. of lower case =",l)
print("No. of special =",s)

        