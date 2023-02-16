def validate_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def validate_rental_code_input(prompt):
    while True:
        value = input(prompt).upper()
        if value in ["B", "D", "W"]:
            return value
        else:
            print("Invalid input. Please enter 'B' for budget, 'D' for daily, or 'W' for weekly.")

def get_rental_input():
    rental_code = validate_rental_code_input("Enter rental code (B)udget, (D)aily, or (W)eekly: ")
    rental_period = validate_int_input("Enter rental period (number of days or weeks): ")
    start_odometer = validate_int_input("Enter starting odometer reading: ")
    end_odometer = validate_int_input("Enter ending odometer reading: ")
    return rental_code, rental_period, start_odometer, end_odometer
