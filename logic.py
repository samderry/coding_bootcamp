monday = int(input("Enter how many cups of tea do you drink on a Monday: "))
tuesday = int(input("Enter how many cups of tea do you drink on a Tuesday: "))
wednesday = int(input("Enter how many cups of tea do you drink on a Wednesday: "))
thursday = int(input("Enter how many cups of tea do you drink on a Thursday: "))
friday = int(input("Enter how many cups of tea do you drink on a Friday: "))
saturday = int(input("Enter how many cups of tea you drink on a Saturday: "))
sunday = int(input("Enter how many cups of tea you drink on a Sunday: "))
total_weekly_tea = monday + tuesday + wednesday + thursday + friday + saturday + sunday
per_week = total_weekly_tea
average_day = per_week / 5
print(average_day)