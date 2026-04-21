import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Company.csv")


# Take first 5 companies
df_top5 = df.head(5)

plt.figure()
plt.pie(df_top5["Year"], labels=df_top5["Company"], autopct='%1.1f%%')
plt.title("5 Companies Year Distribution")
plt.show()