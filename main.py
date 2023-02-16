from car_rental_input import get_rental_input
from car_rental_calculator import calculate_rental
from car_rental_ui import display_rental_summary

rental_code, rental_period, start_odometer, end_odometer = get_rental_input()
total_miles, base_charge, mile_charge, amt_due = calculate_rental(rental_code, rental_period, start_odometer, end_odometer)
display_rental_summary(total_miles, base_charge, mile_charge, amt_due)

