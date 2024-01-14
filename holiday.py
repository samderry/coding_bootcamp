# Create a calculator that works out the total holiday cost for a customer

# create a dictionary of holiday locations
location = {1: "Tokyo", 2: "Paris", 3: "Berlin"}
# create a dictionary of flight costs
flight_cost = {1: 700, 2: 300, 3: 400}

# create function to determine hotel cost
hotel_cost = lambda num_nights : num_nights * 200

# create function to determine plane cost
plane_cost = lambda city_flight : flight_cost[city_flight]

# create function to determine car rental cost
car_rental = lambda rental_days : rental_days * 50

# create function to determine the total holiday cost
holiday_cost = lambda hotel_cost, plane_cost, car_rental : hotel_cost + plane_cost + car_rental

print("Welcome to planning and booking your holiday for 2024. First we need a few details from you.\n")


while True:
    # Ask customer where they would like to go. 
    print("Please enter the number of location of where you would like to go (enter -1 to cancel):")
    for city_flight in location:
        print("  " + str(city_flight) + ". " + location[city_flight])

    # Get city flight choice from user
    try:
        city_flight = int(input(" > "))
    except:
        city_flight = 0

    # Check if user wishes to cancel or validate their choice
    if city_flight == -1:
        print("Calculator cancelled")
        break
    elif city_flight not in location:
        print("Invalid destination")
    else:
        print("You're off to " + location[city_flight])
        break 
print()

# Check if user has opted to cancel
if city_flight == -1:
    exit()

while True:
    # Get number of nights from user
    try: 
        num_nights = int(input("Enter number of nights you will be staying (enter -1 to cancel): "))
    except:
        num_nights = -2

    # Check if user wishes to cancel or validate their choice    
    if num_nights == -2:
        print("Invalid number of nights")
    elif num_nights == -1:
        print("Calculator cancelled")
        break
    else:
        print(f"You have chosen to stay {num_nights} nights.")
        break
print()

# Check if user has opted to cancel
if num_nights == -1:
    exit()

while True:
    # Get number of car rental days from user
    try: 
        rental_days = int(input("Enter number of days you would like to hire a car (enter -1 to cancel): "))
    except:
        rental_days = -2

    # Check if user wishes to cancel or validate their choice       
    if rental_days == -2:
        print("Invalid number of days")
    elif rental_days == -1:
        print("Calculator cancelled")
        break
    else:
        print(f"You have chosen to rent a car for {rental_days} days.")
        break
print()

# Check if user has opted to cancel
if rental_days == -1:
    exit()

print()

hotel_cost = hotel_cost(num_nights)
print(f"The cost of your hotel will be:      £{hotel_cost}")

plane_cost = plane_cost(city_flight)
print(f"The cost of your flight will be:     £{plane_cost}")

car_rental = car_rental(rental_days)
print(f"The cost of your car rental will be: £{car_rental}")

holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
print(f"\nThe total cost of your holiday will be an extortionate £{holiday_cost}\n")






