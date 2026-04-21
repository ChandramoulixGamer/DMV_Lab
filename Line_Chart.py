import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Company.csv")

df_sorted = df.sort_values(by="Employees", ascending=False)

plt.figure()
plt.plot(df_sorted["Company"], df_sorted["Employees"], marker='o')
plt.xticks(rotation=45)
plt.xlabel("Company")
plt.ylabel("Employees Count")
plt.title("Employees Count by Company")
plt.tight_layout()
plt.show()