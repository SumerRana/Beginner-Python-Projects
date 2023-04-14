import pandas as pd

df = pd.read_csv(r'data.csv')

mean1 = df['Value'].mean()

print(mean1)