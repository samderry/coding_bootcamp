qual_time = int(input("Please tell us your qualifying time in minutes: "))
time = qual_time

if time <= 100:
    print("You win provincial colours!")
elif 101 <= time < 106:
    print("You win provincial half colours!")
elif 106 <= time < 111:
    print("You win a provincial scroll!")
else:
    print("You haven't won an award.")