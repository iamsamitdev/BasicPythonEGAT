from cProfile import label
from dbpackage import ConnectMySQL as con
import pandas as pd
import matplotlib.pyplot as plt

# Connect Database
connection = con.connectdb()

# Read Data
df = pd.read_sql(
    "SELECT ship_name, freight FROM orders "
    "WHERE ship_country='USA' LIMIT 10", connection
)

# Plot graph
df.plot(kind="line", x="ship_name", y="freight", label="ship_name")
plt.show()
