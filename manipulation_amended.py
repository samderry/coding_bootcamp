user_sentence = input("Enter a sentence: ")

print(user_sentence)

str_manip = user_sentence
print(len(str_manip))

last_letter = str_manip[-1]

print(last_letter)

print(str_manip.replace(last_letter, "@"))





print(str_manip[-3::][::-1])

print(str_manip[0:3] + str_manip[-2::])