import pandas as pd
import numpy as np
data = pd.read_csv('C:/Users/vchar/Downloads/Automobile_data.csv')
#print(data)
df = data[['company','price']][data.price == data['price'].max()]
#print(df)
car_manu = data.groupby('company')
toyota_df = car_manu.get_group('toyota')
print(toyota_df)