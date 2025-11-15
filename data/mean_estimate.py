import pandas as pd

df = pd.read_csv("data/narvik.csv",comment='#')
df["pm25"] = (df["min"]+df["max"]+df["q1"]+df["q3"]+df["median"])/5

results = df[["date","pm25"]]
results.to_csv("data/narvik_mean.csv",index = False)

