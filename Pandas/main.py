import pandas as pd
import numpy as np

s = pd.Series([1, 3, 4, np.nan, 44, 1])
print(s)

dates = pd.date_range('2016', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df1)

df2 = pd.DataFrame({'a': np.arange(4, 2, -1)})
print(df2)
print(df['b'])
print(df[0:2])
print(df.loc[:, ['a', 'b']])

print(df.iloc[:2, :1])

print(df.ix[:3, ['a', 'c']])
print(df[df.a > 0])
