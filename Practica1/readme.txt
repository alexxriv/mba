# Modelación y Simulación basada en Agentes 2024

## Integrantes
Alejandro Terrazas Rivera 421006692
Ángela Janín Ángeles Martínez 314201009

## Ejecución

Se recomienda utilizar virtualenv para instalar las dependencias

En caso de no tener virtualenv instalado, instalarlo con el siguiente comando
```bash
pip install virtualenv
```

### Instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



## Ejecutar el proyecto: Parte 2

La parte 2 de la práctica es un notebook de jupyter con el nombre 'automata.ipynb', utilizamos Visual Studio Code para ejecutarlo, pero se puede ejecutar en cualquier IDE que soporte notebooks de jupyter.

Tambien se puede ejecutar desde la terminal con el siguiente comando

```bash
jupyter notebook practica01.ipynb
```

El notebook será visible en el navegador web http://localhost:8888, se puede ejecutar cada celda de código con el botón de 'Run Cell' o con el atajo de teclado 'Shift + Enter'


Este es un ejemplo de una inicialización de un autómata con parámetros personalizados:

```python
# Ejercicio 1: Exploración
rule_number = 0
time_steps = 100
boundary_type = 'periodic'  # Opciones: 'fixed', 'periodic'
condition_type = 'random'  # Opciones: 'random', 'fixed', 'custom'
custom_state = None  # Usar sólo si condition_type es 'custom'

initial_state = initial_conditions(size, condition_type, custom_state)
grid = cellular_automaton(rule_number, initial_state, time_steps, boundary_type)
plot_grid(grid)
```

## Ejecutar el proyecto: Parte 3

La parte 3 de la practica es un script de python con el nombre 'game_of_life.py', se puede ejecutar desde la terminal con el siguiente comando

### Ejecutar Game of Life
```bash
python game_of_life.py
```

ó 

```bash
python3 game_of_life.py
```

### Ejecutar Gospers Glider Gun
```bash
python gospers_gun.py
```

ó 

```bash
python3 gospers_gun.py
```

### Ejecutar eater
```bash
python eater.py
```

ó 

```bash
python3 eater.py
```

