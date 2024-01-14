# create a while loop to continually ask the user to enter a number
# when user enters -1 program should stop
# at this point calculate the average  of the numbers excluding the -1 

print("Welcome to the average number calculator.")
print("Please type in whole numbers each time and as many times as you like, and then press enter to submit.")
print("If you enter -1, the average of your numbers will be calculated and then the program will end.")
print("Have fun!")
sum = 0
count = 0
while True:
    num = int(input("Enter a number: " ))
    if num == -1:
        break 
    sum += num
    count += 1


if count > 0:
    avg = sum / count
    print("The average of your numbers is: " + str(avg))
else:
    print("Average number calculator cancelled.")