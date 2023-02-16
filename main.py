import sys

#This project is about car rentals.
# The purpose this project was to give a estimate of how the rental is gonna cost.


rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

if rentalCode == "W":
    rentalPeriod = int(input("Number of Weeks Rented:\n"))
else:
    rentalPeriod = int(input("Number of Days Rented:\n"))

budget_Charge = 40.00
daily_Charge = 60.00
weekly_Charge = 190.00 #Charge base daily, Weekly and Budget

if rentalCode == "B":
    baseCharge = budget_Charge * rentalPeriod
elif rentalCode == "D":
    baseCharge = daily_Charge * rentalPeriod
else:
    baseCharge = weekly_Charge * rentalPeriod

    odoStart = int(input("Starting Odometer Reading:\n"))

    odoEnd = int(input("Ending Odometer Reading:\n"))

    totalMiles = int(odoEnd) - int(odoStart)

    if rentalCode == 'B': #miles charge is base on total miles
        mileCharge = totalMiles * 0.25

    if rentalCode == 'D': # mileage charge is based on Average miles
        averageDayMiles == totalMiles / rentalPeriod
        if averageDayMiles > 100:
            extraMiles = averageDayMiles - 100
            milesCharge = extraMiles * 0.25
        else:
            milesCharge = 0
    else:
        averageWeekMiles = totalMiles/rentalPeriod
        if averageWeekMiles > 900:
            milesCharge = 0
        else:
            milesCharge = (averageWeekMiles - 200) * 0.25
            amtDue = baseCharge + milesCharge

        print("Rental Summary")
        print("Rental Code: " + str(rentalCode))
        print("Rental Period: " + str(rentalPeriod))
        print("Starting Odometer: " + str(odoStart))
        print("Ending Odometer: " + str(odoEnd))
        print("Miles Driven: " + str(totalMiles))
        print('Amount Due:\t\t' + '$' + '%.2f' % amtDue)


