import pandas as pd
from tabulate import tabulate

# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", 200)
# pd.set_option("display.expand_frame_repr", False)
ed = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\fifa_eda.csv")
# print(tabulate(ed.head(12), headers = "keys", tablefmt= "grid"))

print(ed)
