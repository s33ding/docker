import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

def read_file():
    fl = [file for file in os.listdir() if ".csv" in file][0]
    return pd.read_csv(fl)

def checking_missing_values(df):
    missing_values = df.isnull().sum()
    print("missing_values:")
    print(missing_values)

def normalizing_num_data(df, numeric_columns):
    # Inicializar o scaler
    scaler = MinMaxScaler()

    # Normalizar as colunas numéricas
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df

# doing the one-hot encoding for the categorical data
def one_hot_encoding(df, lst_cols):
    df = pd.get_dummies(df, columns=lst_cols)
    return df

def create_correlation_matrix(df):
    # Calcular a matriz de correlação
    correlation_matrix = df.corr()
    # Plotar um mapa de calor da matriz de correlação
    return  correlation_matrix 

def analysing_features(df, target_col):
    mtx = create_correlation_matrix(df)
    # Plotar um mapa de calor da matriz de correlação
    df = pd.DataFrame(mtx.loc[target_col])
    df = df.loc[df.index != target_col]
    df = df.sort_values(target_col)    
    df = df.sort_values(by=target_col, ascending=False)
    return df[df[target_col] > 0]

def ploting_correlation_matrix(correlation_matrix):
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
    plt.title('Matriz de Correlação')
    plt.show()
