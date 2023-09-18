import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Lista para almacenar el número de celdas vivas en cada frame
live_cells_count = []

# Función para actualizar la cuadrícula
def update_grid(grid, periodic_boundary):
    # Copia de la cuadrícula original para actualizar celdas
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # Calcula la suma de los ocho vecinos usando la vecindad de Moore
            # Condiciones de frontera periódicas
            if periodic_boundary:
                total = int((grid[i, (j-1) % cols] + grid[i, (j+1) % cols] +
                             grid[(i-1) % rows, j] + grid[(i+1) % rows, j] +
                             grid[(i-1) % rows, (j-1) % cols] + grid[(i-1) % rows, (j+1) % cols] +
                             grid[(i+1) % rows, (j-1) % cols] + grid[(i+1) % rows, (j+1) % cols]))
            # Condiciones de frontera no periódicas
            else:
                total = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x, y = i + dx, j + dy
                        if 0 <= x < rows and 0 <= y < cols and not (dx == 0 and dy == 0):
                            total += grid[x, y]

            # Reglas del juego de la vida
            if grid[i, j] == 1:  # Celda viva
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:  # Celda muerta
                if total == 3:
                    new_grid[i, j] = 1

    return new_grid


def initialize_gosper_gun(grid):
    pattern = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    ])
    grid[1:11, 1:42] = pattern


# Tamaño de la cuadrícula
N = 100

# Inicializar cuadrícula con ceros
grid = np.zeros((N, N), dtype=int)

# Inicializar con un Gosper's Gun
initialize_gosper_gun(grid)

# Crear una figura y un conjunto de subtramas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Configurar la animación
def animate(frame):
    global grid
    ax1.clear()
    ax1.imshow(grid, cmap="gray")
    
    # Contar celdas vivas y agregar al registro
    live_count = np.sum(grid)
    live_cells_count.append(live_count)
    
    # Actualizar gráfico de celdas vivas
    ax2.clear()
    ax2.plot(live_cells_count, marker='o')
    ax2.set_title('Número de celdas vivas')
    ax2.set_xlabel('Frame')
    ax2.set_ylabel('Celdas vivas')
    
    # Mostrar el número actual de celdas vivas
    ax2.text(0.8, 0.9, f'Vivas: {live_count}', horizontalalignment='center', verticalalignment='center', transform=ax2.transAxes)
    
    grid = update_grid(grid, periodic_boundary=True)


ani = animation.FuncAnimation(fig, animate, frames=100)

plt.show()