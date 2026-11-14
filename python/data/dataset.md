# Dataset

Conjunto cerrado de la etapa 3 de [plan_python.md](../../plan_python.md): golpe al parche (`PARCHE`), golpe al anillo (`ANILLO`) y sonido ambiente (`AMBIENTE`). Cada archivo tiene una sola clase, la de su carpeta.

El manifiesto es [particiones.csv](particiones.csv). Lo escribe `pruebas_py/5_particiones.py`. Una fila es una grabación, con su WAV y su `.raw`. Las ventanas de 480 muestras que salgan de ese archivo quedan en la misma partición.

El plan no fija la proporción. Este corte usa 60 % entrenamiento, 20 % validación y 20 % prueba, por clase, con semilla 1. Para 28 archivos, `round(28 × 0,20)` da 6 de validación y 6 de prueba. Para 20, da 4 y 4. El resto es entrenamiento.

| Clase | Entrenamiento | Validación | Prueba | Total |
| --- | --- | --- | --- | --- |
| `PARCHE` | 16 | 6 | 6 | 28 |
| `ANILLO` | 16 | 6 | 6 | 28 |
| `AMBIENTE` | 12 | 4 | 4 | 20 |
| Total | 44 | 16 | 16 | 76 |

La partición de prueba no se usa hasta la etapa 8. `amb_1.wav` no está en el manifiesto. Tampoco las cuatro tomas retiradas en [formato.md](../../pruebas_py/grabacion/formato.md).

La línea de base de scikit-learn queda para cuando la etapa 4 tenga un vector por ventana. Este archivo todavía no elige esa representación.
