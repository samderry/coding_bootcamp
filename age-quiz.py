num = int(input("Please enter your age: "))
if num >= 40:
    print("You're over the hill.")

num = int(input("Tell me your age: "))
age = num
print(age)

age = int(input("Please enter an age between 1 and 100: "))
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement")
elif age < 13:
    print("You qualify for the kiddie discount")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")