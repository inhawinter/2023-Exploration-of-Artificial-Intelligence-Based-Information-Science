import pandas as pd

df1 = pd.DataFrame({
    "a": [11, -2, 7],
    "b": [9, 0, 77],
    "c": [55, 33, 19]
     }, index=[1, 2, 3])

df2 = pd.DataFrame(
    [[11, 9, 55],
     [-2, 0, 33],
     [7, 77, 19]]
)

print(df1)
print(df2)
