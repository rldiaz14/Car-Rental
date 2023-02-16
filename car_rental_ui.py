import tkinter as tk
from car_rental_input import get_rental_input
from car_rental_calculator import calculate_rental

def display_rental_summary(total_miles, base_charge, mile_charge, amt_due):
    rental_summary.config(state=tk.NORMAL)
    rental_summary.delete("1.0", tk.END)
    rental_summary.insert(tk.END, f"Total Miles Driven: {total_miles}\n")
    rental_summary.insert(tk.END, f"Base Charge: ${base_charge:.2f}\n")
    rental_summary.insert(tk.END, f"Mileage Charge: ${mile_charge:.2f}\n")
    rental_summary.insert(tk.END, f"Amount Due: ${amt_due:.2f}\n")
    rental_summary.config(state=tk.DISABLED)

def calculate_button_clicked():
    rental_code, rental_period, start_odometer, end_odometer = get_rental_input()
    total_miles, base_charge, mile_charge, amt_due = calculate_rental(rental_code, rental_period, start_odometer, end_odometer)
    display_rental_summary(total_miles, base_charge, mile_charge, amt_due)

# Create the main window
window = tk.Tk()
window.title("Car Rental Calculator")

# Create the input labels and entry fields
rental_code_label = tk.Label(window, text="Rental Code:")
rental_code_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
rental_code_entry = tk.Entry(window)
rental_code_entry.grid(row=0, column=1, padx=5, pady=5)

rental_period_label = tk.Label(window, text="Rental Period:")
rental_period_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
rental_period_entry = tk.Entry(window)
rental_period_entry.grid(row=1, column=1, padx=5, pady=5)

start_odometer_label = tk.Label(window, text="Starting Odometer:")
start_odometer_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
start_odometer_entry = tk.Entry(window)
start_odometer_entry.grid(row=2, column=1, padx=5, pady=5)

end_odometer_label = tk.Label(window, text="Ending Odometer:")
end_odometer_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
end_odometer_entry = tk.Entry(window)
end_odometer_entry.grid(row=3, column=1, padx=5, pady=5)

# Create the summary label
rental_summary = tk.Text(window, height=6, width=30, state=tk.DISABLED)
rental_summary.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

