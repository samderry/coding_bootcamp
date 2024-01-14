restaurant_name = input("What is your favourite restaurant?: ")
string_fav = restaurant_name
print(string_fav)

favourite_number = int(input("What is your favourite number?: "))
int_fav = favourite_number
print(int_fav)

string_fav = int(restaurant_name)
print(string_fav)
# This won't work because the content of the string is not numerical so cannot be coverted to an integer