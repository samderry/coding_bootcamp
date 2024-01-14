sum = 0
count = 0
while True:
    num = int(input("Enter a number: " ))
    if num == -1:
        break 
    sum += num
    count += 1

avg = sum / count
print("The average is: " + str(avg))


















