# -*- coding: utf-8 -*-
"""
Este programa realiza una simulación de caminata aleatoria en 1D.
"""

from src import functions
import matplotlib.pyplot as plt

num_pasos = 1000
trayectoria = functions.caminata_aleatoria(num_pasos)

# Graficar la trayectoria
plt.plot(trayectoria)
plt.title("Caminata Aleatoria")
plt.xlabel("Pasos")
plt.ylabel("Posición")
plt.grid(True)
plt.show()
