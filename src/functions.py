# -*- coding: utf-8 -*-

import numpy as np

def caminata_aleatoria(num_pasos):
    posicion = 0
    trayectoria = [posicion]

    for _ in range(num_pasos):
        paso = np.random.choice([-1, 1])  # Paso aleatorio a la izquierda (-1) o a la derecha (1)
        posicion += paso
        trayectoria.append(posicion)

    return trayectoria
