# adding cars to a database: e.g make, colour, type
# asking users for input
# stays in memory only while program is running

# Make a database to store the data entered
car_db = []
car_id = 0

# Ask the user to start the car database, otherwise quit
answer = input("Would you like to access the car database? Y/N ")

# Loop this
while answer == "Y":
    #If the database has cars in it, show the amount of cars inside database then print out cars
    if car_db:
        print(f"\nCars in Database: {len(car_db)}\n")
        for car in car_db:
            print(f"Car {car['id']}\nMake: {car['make']}\nModel: {car['model']}\nYear: {car['year']}\n")
    car_id = car_id + 1

    # User input
    # 1. ask user for make
    car_make = input("What is the make of the car? ")

    # 2. ask user for model
    car_model = input("What is the model? ")

    # 3. ask for year
    car_year = input("What is the year? ")

    # 4. put it into a dictionary
    car = {
        "id": car_id,
        "make": car_make,
        "model": car_model,
        "year": car_year}
    
    #print(car)
    #print(id(car)) # id is the location in memory

    # add new car to the database
    car_db.append(car)