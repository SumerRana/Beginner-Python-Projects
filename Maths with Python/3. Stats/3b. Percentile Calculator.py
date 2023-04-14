import pandas as pd

df = pd.read_csv(r'C:\Users\SumerRana\Desktop\Projects\pythonProject\Maths with Python\3. Stats\StudentsPerformance.csv')

# mean1 = df['Value'].mean()
df = df.drop(columns=["race/ethnicity","lunch"])
df['Overall %age'] = (df['math score'] + df['reading score'] + df['writing score'])/3

pclist = df['Overall %age'].tolist()
asclist = sorted(pclist)
# print(asclist)

percentile = ((asclist.index(99.0))/len(asclist))*100
print(f'The percentile is {percentile}')