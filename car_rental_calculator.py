def calculate_rental(rental_code, rental_period, start_odometer, end_odometer):
    budget_charge = 40.00
    daily_charge = 60.00
    weekly_charge = 190.00

    if rental_code == "B":
        base_charge = budget_charge * rental_period
    elif rental_code == "D":
        base_charge = daily_charge * rental_period
    else:
        base_charge = weekly_charge * rental_period

    total_miles = end_odometer - start_odometer

    if rental_code == 'B':
        mile_charge = total_miles * 0.25
    elif rental_code == 'D':
        average_day_miles = total_miles / rental_period
        if average_day_miles > 100:
            extra_miles = average_day_miles - 100
            mile_charge = extra_miles * 0.25
        else:
            mile_charge = 0
    else:
        average_week_miles = total_miles / rental_period
        if average_week_miles <= 900:
            mile_charge = (average_week_miles - 200) * 0.25
        else:
            mile_charge = 0
    amt_due = base_charge + mile_charge

    return total_miles, base_charge, mile_charge, amt_due
