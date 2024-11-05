import sys
import pandas as pd
import matplotlib.pyplot as plt

archivo_csv = sys.argv[1] 
archivo_salida = sys.argv[2]

df = pd.read_csv(archivo_csv)

primera_columna = df.iloc[:, 0].tolist()
num_columnas = df.shape[1]

if num_columnas == 2:
    segunda_columna = df.iloc[:, 1].tolist()
    
    plt.plot(primera_columna, segunda_columna, marker='o', linestyle='-')
    plt.xlabel("Tiempo")
    plt.ylabel("Posición")
    plt.title("Posición en función del Tiempo")
    plt.savefig(archivo_salida)
    plt.show()
    print(f"Gráfico 1D guardado en {archivo_salida}")

if num_columnas == 3:
    segunda_columna = df.iloc[:, 1].tolist()
    tercera_columna = df.iloc[:, 2].tolist()
    
    plt.scatter(segunda_columna, tercera_columna, c=primera_columna, cmap='viridis')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.colorbar(label="Valores de campo (Tiempo)")
    plt.title("Distribución en función de X e Y con el Tiempo como campo")
    plt.savefig(archivo_salida)
    plt.show()
    print(f"Gráfico 2D guardado en {archivo_salida}")