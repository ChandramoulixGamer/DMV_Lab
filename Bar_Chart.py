import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Company.csv")
# Sort by rating
df_sorted = df.sort_values(by="Rating", ascending=False)

plt.figure()
plt.bar(df_sorted["Company"], df_sorted["Rating"])
plt.xticks(rotation=45)
plt.xlabel("Company")
plt.ylabel("Rating")
plt.title("Company Ratings")
plt.tight_layout()
plt.show()