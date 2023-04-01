import pandas as pd
df = pd.read_csv('california_housing_test.csv')
print(df.head())

print(df.shape)

print(df.dtypes)

print(df.isnull().sum())

print(df[df['median_income'] < 2]['median_house_value'])

print(df[['longitude', 'latitude']])

print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])

print(df['median_house_value'].min())

print(df['median_house_value'].max())

print(df[df['median_income'] == 3.1250]['median_house_value'].max())

print(df['population'][df['median_house_value']
      == df['median_house_value'].min()].max())