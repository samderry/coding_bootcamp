# create a string
str_1 = "Hello world"
# create empty string
new_str = ""
# use for loop to go through the loop along with the range of the length of list
for i in range(len(str_1)):
   if i % 2 == 0:
      #it returns the lowercase of the string when it is even
      new_str += str_1[i].lower()
   else:
      #it returns the uppercase of the string when it is odd
      new_str += str_1[i].upper()
#return the string after converting it into another case
print(new_str)



#create a string
sentence = "This is a sentence"
#split sentence into individual words
words = sentence.split()
i = 0
new_str = ""
#use for loop to process each word into upper and lower case
for word in words:
    if i % 2 == 0:
    #it returns the lowercase of the string when it is even
      new_str += word.lower()
    else:
      #it returns the uppercase of the string when it is odd
      new_str += word.upper()
    # each time going through the loop, move up to the next word
    i += 1
    # add in a space after each word in string
    new_str += " "
print(new_str.strip())

