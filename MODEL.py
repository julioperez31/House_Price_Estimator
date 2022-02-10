'''import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

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


values_predict = [[52, 1, 1, 0, 1]]

scaled = scaler.transform(values_predict)
pred = model.predict(scaled)
print('Values to predict', values_predict)
print('Values to predict scaled: ', scaled)
print('Result: ', pred)

scaler = StandardScaler()
X = df[['Construccion_mt', 'Baños', 'Habitaciones', 'Tipo_Propiedad_ID', 'Moneda_ID']].values
y = df['Valor'].values
X = scaler.fit_transform(X)

model = DecisionTreeRegressor(max_depth=8)


scores = cross_val_score(model, X, y, cv=5)
print('Cross split mean: ', scores.mean())
print('Cross split: ', scores)
model.fit(X, y)'''

