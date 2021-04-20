import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

le = LabelEncoder()
df = pd.read_excel('products.xlsx')
df['Urbanizacion'] = df['Sector'].apply(lambda x: x.split(',')[0])
df['Construccion_mt'] = df['Construccion'].str.replace(',', '')
df['Construccion_mt'] = df['Construccion_mt'].str.replace(' ', '')
df['Construccion_mt'] = df['Construccion_mt'].str.replace('mt', '')
df['Construccion_mt'] = df['Construccion_mt'].astype('int')
df['Moneda'] = df['Precio'].str.slice(stop=3)
df['Valor'] = df['Precio'].str.slice(start=4)
df['Valor'] = df['Valor'].str.replace(',', '')
df['Valor'] = df['Valor'].astype('int')
df.loc[df['Moneda'] == 'RD$', 'Valor'] = df['Valor'] / 58.50

df['Urbanizacion_ID'] = le.fit_transform(df['Urbanizacion'])
df['Moneda_ID'] = le.fit_transform(df['Moneda'])
df['Tipo_Propiedad_ID'] = le.fit_transform(df['Tipo Propiedad'])

df.to_excel('productsETL.xlsx', index=False)
print(df.corrwith(df['Valor']))

scaler = StandardScaler()
X = df[['Construccion_mt', 'Baños', 'Habitaciones', 'Tipo_Propiedad_ID', 'Moneda_ID']].values
y = df['Valor'].values
X = scaler.fit_transform(X)

model = DecisionTreeRegressor(max_depth=8)


scores = cross_val_score(model, X, y, cv=5)
print('Cross split mean: ', scores.mean())
print('Cross split: ', scores)
model.fit(X, y)


values_predict = [[90, 1, 2, 0, 0]]
scaled = scaler.transform(values_predict)
pred = model.predict(scaled)
print('Values to predict', values_predict)
print('Values to predict scaled: ', scaled)
print('Result: ', pred)
