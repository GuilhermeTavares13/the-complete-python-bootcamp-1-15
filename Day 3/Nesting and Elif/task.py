print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))
    if age >= 18:
        print("You must pay $12.00")
    elif 12 <= age < 18:
      print("You must pay $7.00")
    else:
        print("You must pay $5.00")
else:
    print("Sorry you have to grow taller before you can ride.")
