import numpy as np
import matplotlib.pyplot as plt

# Clase Celda
class Celda:
    def __init__(self, estado=False):
        self.estado = estado

    def interactuar(self, vecinas_vivas):#reglas
        if self.estado:  
            if vecinas_vivas < 2 or vecinas_vivas > 3:
                return False 
            else:
                return True  
        else:  
            return vecinas_vivas == 3  

# Clase Grilla, 
class Grilla:
    def __init__(self, tamano, posiciones_vivas):
        # (Constructor)
        print("Inicializando la grilla...")
        self.tamano = tamano  
        self.contador = 0     

        self.celdas = [[Celda() for _ in range(tamano)] for _ in range(tamano)]
        self.celdas_siguiente = [[Celda() for _ in range(tamano)] for _ in range(tamano)]

        for x, y in posiciones_vivas:
            self.celdas[x][y].estado = True
        print("Grilla inicializada con tamaño:", tamano)

    def actualizar_celdas(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                self.celdas[i][j].estado = self.celdas_siguiente[i][j].estado
        print("Estados de las celdas actualizados")

    def visualizar(self):

        grid = np.array([[1 if celda.estado else 0 for celda in fila] for fila in self.celdas])
        plt.clf()  
        plt.imshow(grid, cmap="binary")  
        plt.title(f"Generación {self.contador}") 
        plt.draw()
        plt.pause(0.5) 

    def contar_vecinas_vivas(self, x, y):

        vecinas_vivas = 0
        for i in range(max(0, x - 1), min(self.tamano, x + 2)):
            for j in range(max(0, y - 1), min(self.tamano, y + 2)):
                # Evitamos contar la propia célula en (x, y)
                if (i, j) != (x, y) and self.celdas[i][j].estado:
                    vecinas_vivas += 1
        return vecinas_vivas

    def avanzar(self):
     
        print(f"Avanzando a la generación {self.contador + 1}...")
        hay_celulas_vivas = False  
        
        estado_actual = [[celda.estado for celda in fila] for fila in self.celdas]
        
        for i in range(self.tamano):
            for j in range(self.tamano):
                vecinas_vivas = self.contar_vecinas_vivas(i, j)
                nuevo_estado = self.celdas[i][j].interactuar(vecinas_vivas)
                self.celdas_siguiente[i][j].estado = nuevo_estado
                if nuevo_estado:
                    hay_celulas_vivas = True  
        
        self.actualizar_celdas()
        self.contador += 1  
        self.visualizar()  

        nuevo_estado_matriz = [[celda.estado for celda in fila] for fila in self.celdas]
        es_estacionario = nuevo_estado_matriz == estado_actual

        return hay_celulas_vivas and not es_estacionario

def leer_datos(archivo):
    with open(archivo, 'r') as f:
        lines = f.readlines()
    
    tamano = int(lines[0].strip())
    print(f"Tamaño de la grilla leído: {tamano}")
    
    posiciones_vivas = []
    for line in lines[1:]:
        x, y = map(int, line.strip().split(","))
        posiciones_vivas.append((x, y))
    print(f"Posiciones iniciales de celdas vivas: {posiciones_vivas}")
    
    return tamano, posiciones_vivas

if __name__ == "__main__":
    import sys
    archivo_datos = sys.argv[1]
    tamano, posiciones_vivas = leer_datos(archivo_datos)
    grilla = Grilla(tamano, posiciones_vivas)
    
    plt.figure(figsize=(6, 6))
    
    while grilla.avanzar():
        pass  
    
    plt.show()