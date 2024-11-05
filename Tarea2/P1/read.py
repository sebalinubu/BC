import pandas as pd

def read(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    
    num_columnas = df.shape[1]
    
    primera_columna = df.iloc[:, 0].tolist()
    
    segunda_columna = []
    tercera_columna = []
    
    if num_columnas == 2:
        segunda_columna = df.iloc[:, 1].tolist()
        return primera_columna, segunda_columna
    elif num_columnas == 3:
        segunda_columna = df.iloc[:, 1].tolist()
        tercera_columna = df.iloc[:, 2].tolist()
        return primera_columna, [segunda_columna, tercera_columna]
    else:
        return [], []