import pandas as pd

data1 = {
    "a": [11, -2, 7],
    "b": [9, 0, 77],
    "c": [55, 33, 19]
}
data2 = [
            [11, 9, 55],
            [-2, 0, 33],
            [7, 77, 19]
]
df1 = pd.DataFrame(data1, index=[1, 2, 3])
df2 = pd.DataFrame(data2, index=[1, 2, 3], columns=["a", "b", "c"])

print(df2.iat[1, 0])
print(df2.iloc[1:3, 1:3])
print(df2.loc[2:3, 'b':'c'])

print(df1)
df3 = df1\
    .melt()\
    .rename(columns={
        'variable': 'var',
        'value': 'val'
    })\
    .sort_values('val', ascending=False)\
    .tail(6)\
    .query('val > 10')

print(df3)
print(df1.drop(columns=['b']))
print(df1)

