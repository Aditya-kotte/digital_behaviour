import pandas as pd
import numpy as np

df = pd.read_csv("digital_behaviour.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df[["Instagram_Minutes", "Study_Minutes"]].describe())
print(df["Instagram_Minutes"].mean())
print(df[["Date", "Study_Minutes"]].describe())

print(df["Instagram_Minutes"].sum())
print(df["Instagram_Minutes"].max())
print(df["Instagram_Minutes"].mean())

print(df[df["Instagram_Minutes"] > 100])
print(df[df["Study_Minutes"] > 180])

print(df[(df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] > 180)])

top_5_instagram = df.sort_values(by="Instagram_Minutes",ascending=False).head(5)
print(top_5_instagram)

top_5_study = df.sort_values(by="Study_Minutes",ascending=False).head(5)
print(top_5_study)

df["Total_Screen_Time"] = ( df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]
)

df["Screen_Hours"] = df["Total_Screen_Time"] / 60

df["Digital_Balance"] = ( df["Study_Minutes"] / df["Total_Screen_Time"])

df["Day_Type"] = "Normal"
df.loc[df["Total_Screen_Time"] > 300, "Day_Type"]="heavy"


app_totals = df[["Instagram_Minutes","YouTube_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]].sum()
print("Total app usage:")
print(app_totals)

print("Most used app:", app_totals.idxmax())

print("Heavy days:", (df["Day_Type"] == "Heavy").sum())

best_study_index = df["Study_Minutes"].idxmax()

print("Best study day:",df.loc[best_study_index, "Date"])

heaviest_screen = df["Total_Screen_Time"].idxmax()

print("Study time on heaviest screen day:",df.loc[heaviest_screen, "Study_Minutes"])


print( "Average Digital Balance:",df["Digital_Balance"].mean())

df.to_csv('Modih.csv')