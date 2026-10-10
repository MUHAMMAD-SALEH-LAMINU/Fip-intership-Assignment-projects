
import pandas as pd
import matplotlib.pyplot as plt

# Read the company sales dataset
data = pd.read_csv(r'C:\Users\kingsaleh\Downloads\company_sales_data.csv')

# Exercise 1: Total profit of all months using a line plot
plt.figure(figsize=(8, 5))
plt.plot(data["month_number"], data["total_profit"], marker="o")

plt.title("Total Profit of All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# Exercise 2: Bathing soap and facewash using subplots
plt.figure(figsize=(10, 6))

# First subplot: Facewash
plt.subplot(2, 1, 1)
plt.plot(data["month_number"], data["facewash"], marker="o", color="blue")
plt.title("Monthly Facewash Sales")
plt.ylabel("Units Sold")
plt.grid(True)

# Second subplot: Bathing soap
plt.subplot(2, 1, 2)
plt.plot(data["month_number"], data["bathingsoap"], marker="o", color="green")
plt.title("Monthly Bathing Soap Sales")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.grid(True)

plt.tight_layout()
plt.show()


