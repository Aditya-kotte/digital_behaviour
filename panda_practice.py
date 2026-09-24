import pandas as pd
df = pd.read_csv('digital_behaviour.csv')
#sep = ','
#encoding = 'utf-8'
nrows = 400
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())
df["Instagram_Minutes"].mean()
df[["date", "Study_Minutes"]].describe()
float f = 0.1
print(f == 0.1) #difference between these two is that the first one is a float and the second one is a double. The double has more precision than the float, so it can represent numbers more accurately. In this case, the float 0.1 is not exactly equal to the double 0.1, so the comparison returns false.
df["Instagram_Minutes"].sum()
df["Instagram_Minutes"].max()
df["Instagram_Minutes"].mean()
val = df[df["Instagram_Minutes"] > 100]



