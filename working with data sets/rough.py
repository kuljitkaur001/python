import pandas as pd
from tabulate import tabulate

# Step 1: Display settings to show full table structure
pd.set_option("display.max_columns", None)     # Show all columns
pd.set_option("display.width", None)            # Wide output (adjustable)
# pd.set_option("display.expand_frame_repr", False)  # Prevent wrapping

# Step 2: Load CSV
ed = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\fifa_eda.csv")

# Step 3: Show table using tabulate (only first 10 or 20 rows for readability)
print(tabulate(ed.head(20), headers="keys", tablefmt="grid"))
 

 