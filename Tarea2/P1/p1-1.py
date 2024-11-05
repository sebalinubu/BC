import sys
from read import read

nombre_archivo = sys.argv[1]

primera_columna, restantes = read(nombre_archivo)

print("Primeros 5 numeros de la primera columna:", primera_columna[:5])

if isinstance(restantes, list) and all(isinstance(col, list) for col in restantes):
    print("Primeros 5 numeros de la segunda columna:", restantes[0][:5])
    print("Primeros 5 numeros de la tercera columna:", restantes[1][:5])
else:
    print("Primeros 5 numeros de la segunda columna:", restantes[:5])
