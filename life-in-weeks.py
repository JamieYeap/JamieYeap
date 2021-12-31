# Input your age
age = input("What is your current age?")

# Calculating the remaining time in weeks, months, days 
year = 90 - int(age)
week = year * 52
month = year * 12
day = year * 365 

print(f"You have {day} days, {week} weeks, and {month} months left.") 
