user_sentence = input("Enter a sentence: ")

print(user_sentence)

str_manip = user_sentence
print(len(str_manip))

print(str_manip[-1])

print(str_manip.replace("e", "@"))

print(str_manip[-3::][::-1])

print(str_manip[0:3] + str_manip[-2::])