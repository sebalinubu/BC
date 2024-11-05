import matplotlib.pyplot as plt

def plot1D(lista_x, lista_y, eje_x, eje_y):

    plt.plot(lista_x, lista_y, marker='o', linestyle='-')
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.title(f"{eje_y} en función de {eje_x}")
    plt.savefig("out1d.png") 
    plt.show()

def plot2D(lista_x, lista_y, lista_c, eje_x, eje_y):

    plt.scatter(lista_x, lista_y, c=lista_c, cmap='viridis')
    plt.xlabel(eje_x)
    plt.ylabel(eje_y)
    plt.colorbar(label="Valores de c (campo)")  
    plt.title(f"{eje_y} en función de {eje_x} con color como campo")
    plt.savefig("out2d.png")  
    plt.show()


