# Funciones de preprocesamiento de datasets
import pandas as pd
from sklearn.preprocessing import StandardScaler

def limpiar_datos(df):
    return df.dropna()

def codificar_categoricas(df):
    return pd.get_dummies(df)

def escalar_numericas(df):
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

