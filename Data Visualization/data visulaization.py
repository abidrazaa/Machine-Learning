import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show


data = pd.read_csv("data.csv")


data_pie = data["province"].value_counts().rename_axis("province").reset_index(name="province_count")
plt.figure(figsize=(10,10))
plt.pie(data_pie.province_count, labels=data_pie.province, startangle=90, autopct="%.1f%%")
plt.title("Provinces")
plt.show()


