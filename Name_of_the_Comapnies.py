import pandas as pd
df = pd.read_csv("Company.csv")

hq_names = df["Headquartrs"].unique()
print(hq_names)
