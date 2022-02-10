import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# FOR THE WEB PAGE REMAX.COM
le = LabelEncoder()
df = pd.read_excel('products.xlsx')
df['Urbanizacion'] = df['Sector'].apply(lambda x: x.split(',')[0])
df['Construccion_mt'] = df['Construccion(mt)'].str.replace(',', '')
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
df['pagina'] = 'REMAX'

# FOR THE WEB PAGE SUPERCASAS.COM

def f_habitaciones(d):
    for i in d:
        if 'Habitaciones' in i:
            return int(i.replace('[<label><b>Habitaciones</b>: ',''))

def f_Baños(d):
    for i in d:
        if 'Baños' in i:
            return float(i.replace('<b>Baños</b>: ',''))

def f_Construccion(d):
    for i in d:
        if ('Construcción' in i or 'Solar' in i) and 'Condición' not in i:
            return re.sub(r'(<b>Solar</b>:|<b>Construcción</b>:)','',i)

df_sc = pd.read_excel('products_sc.xlsx')
df_nn = df_sc[~(df_sc['Precio'].isna())]

df_nn['Tipo Propiedad'] = df_nn['Tipo Propiedad'].replace({r'^<div class="type">':'', r'</div>$':''}, regex=True)
df_nn['Sector'] = df_nn['Sector'].replace({r'^<div class="title1">':'', r'</div>$':''}, regex=True)
df_nn['Precio'] = df_nn['Precio'].replace({r'^<div class="title2">':'', r'</div>$':''}, regex=True)
df_nn['Habitaciones'] = df_nn['Datos generales'].str.split('</label>, <label>').apply(lambda x: f_habitaciones(x))
df_nn['Baños'] = df_nn['Datos generales'].str.split('</label>, <label>').apply(lambda x: f_Baños(x))
df_nn['Construccion'] = df_nn['Datos generales'].str.split('</label>, <label>').apply(lambda x: f_Construccion(x))
df_nn['Urbanizacion']=df_nn['Sector']
df_nn['Construccion_mt'] = df_nn['Construccion'].str.replace('Mt2', '')
df_nn.astype({'Construccion_mt': 'int32'})
df_nn['Moneda'] = df_nn['Precio'].apply(lambda x: x.split(' ')[1])
df_nn['valor'] = df_nn['Precio'].apply(lambda x: int(x.split(' ')[2].replace(',','')))
df_nn['Urbanizacion_ID'] = le.fit_transform(df_nn['Urbanizacion'])
df_nn['Moneda_ID'] = le.fit_transform(df_nn['Moneda'])
df_nn['Tipo_Propiedad_ID'] = le.fit_transform(df_nn['Tipo Propiedad'])
df_nn['pagina'] = 'SUPERCASAS'

df_f = df.append(df_nn)
df_f.to_excel('propiedades.xlsx')