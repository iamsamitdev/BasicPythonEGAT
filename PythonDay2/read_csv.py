import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/demo_data.csv')

# print(data)

filteredData = data[data.Edition == 1988]
filteredData.Sport.value_counts().plot()
plt.show()