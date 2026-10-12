
try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age! Age cannot be negative.")
    elif age > 120:
        print("Invalid age! Please enter a valid age.")
    else:
        print("Your age is:", age)
        print("Age entered is correct.")

except ValueError:
    print("Invalid input! Please enter your age as a number.")
