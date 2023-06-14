import pandas as pd

data1 = {
    "a": [11, -2, 7],
    "b": [9, 0, 77],
    "c": [7, 33, 19]
}
data2 = [
            [11, 9, 7],
            [-2, 0, 33],
            [7, 77, 19]
]
df1 = pd.DataFrame(data1, index=[1, 2, 3])
df2 = pd.DataFrame(data2, index=[1, 2, 3], columns=["a", "b", "c"])

df3 = df1\
    .melt()\
    .rename(columns={
        'variable': 'var',
        'value': 'val'
    })\
    .sort_values('val', ascending=False)\

print(df3)
print(df3.describe())
# print(df3['val'].value_counts())
# print(df3.shape)
# print(df3['val'].nunique())
print(df2.describe())