import tkinter as tk
from tkinter import ttk
import requests
def get_exchange_rates():
    # Replace with your free API key from an exchange rate service provider
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]
def convert_currency():
    try:
        usd_amount = float(entry_amount.get())
        target_currency = combo_currency.get()
        rates = get_exchange_rates()
        converted_amount = usd_amount * rates[target_currency]
        label_result.config(text=f"{usd_amount} USD = {converted_amount:.2f} {target_currency}")
    except ValueError:
        label_result.config(text="Please enter a valid number")
# Create the main window
root = tk.Tk()
root.title("USD Currency Converter")

# Amount label and entry field
label_amount = tk.Label(root, text="Enter amount in USD:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# Dropdown menu for currency selection
label_currency = tk.Label(root, text="Select target currency:")
label_currency.pack()
combo_currency = ttk.Combobox(root)
combo_currency["values"] = list(get_exchange_rates().keys())
combo_currency.current(0)
combo_currency.pack()

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack()

# Label to display the conversion result
label_result = tk.Label(root, text="")
label_result.pack()

# Run the application
root.mainloop()
def refresh_rates():
    combo_currency["values"] = list(get_exchange_rates().keys())
    label_result.config(text="Rates updated")
button_refresh = tk.Button(root, text="Refresh Rates", command=refresh_rates)
button_refresh.pack()
