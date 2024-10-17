import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest and compound interest
def calculate_interest():
    try:
        # Get input values
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        
        # Calculate simple interest
        simple_interest = (principal * rate * time) / 100

        # Calculate compound interest
        compound_interest = principal * (pow((1 + rate / 100), time)) - principal
        
        # Display the results
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")

# Create the main window
window = tk.Tk()
window.title("Interest Calculator App")

# Create and place input fields and labels
tk.Label(window, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Rate of Interest (%):").grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(window)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Time Period (Years):").grid(row=2, column=0, padx=10, pady=10)
time_entry = tk.Entry(window)
time_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to calculate interest
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()
