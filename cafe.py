# create a list of menu items
menu = ["cake", "pasty", "tart", "muffin"]

# create 2 dictionaries - 1 for stock and 1 for price
stock = {"cake": 5, "pasty": 4, "tart": 9, "muffin": 3}
price = {"cake": 3.5, "pasty": 4.25, "tart": 6.0, "muffin": 3.2}

# create a variable for a running total
total_value = 0.0

# get each of items on menu
for item in menu:
 
    # calculate value of stock for menu item
    item_value = (stock[item] * price[item])
    
    # calculate running total of stock value
    total_value += item_value

print("The total value of the stock is: " + str(total_value))
