import pandas as pd;
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv");

df["Date"] = pd.to_datetime(df['Date'])
albany_df = df[ df['region'] == "Albany"]
albany_df = albany_df.set_index("Date")


albany_df["AveragePrice"].rolling(25).mean().plot()

albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()

print(albany_df)

df['region'].values.tolist()

print(set(df['region'].unique()))

df['region'].unique()

graph_df = pd.DataFrame()

for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region'] == region]
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])
"""
plt.xlabel('Date')
plt.ylabel('AveragePrice')

plt.show()
"""