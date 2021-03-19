str = input("enter the string")
vowels = 0
digits = 0
spaces = 0
consonants = 0
characters = 0
str = str.lower()
for i in range(0, len(str)):
 if (str[i] == "a" or str[i] == "e" or str[i] == "i" or str == "o" or str == "u"):
vowels = vowels + 1
elif((str[i]>='a' and str[i]<= 'z')):
consonants = consonants +1
elif( str[i]>='0' and str[i]<='9'):
digits = digits +1
elif(str[]== '  '):
space = space +1
else:
character = character +1
     print(' vowels')
     print('digits')
     print('consonants')
     print('space')
     print('character')
