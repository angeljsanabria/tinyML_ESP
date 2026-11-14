# Formato de las grabaciones

Los 81 WAV de `pruebas_py/grabacion` cumplen el contrato de [audio_capture.md](../../python/docs/audio_capture.md). Todos son PCM sin compresión, 1 canal, 2 bytes por muestra y 16 000 Hz.

La duración no es fija, y eso entra en el plan: el proceso 1 mide el largo de cada archivo. Cada archivo tiene un solo sonido.

| Carpeta | Archivos | Duración |
| --- | --- | --- |
| `parche` | 30 | 1,15 s a 2,18 s |
| `anillo` | 30 | 1,34 s a 2,03 s |
| `ambiente` | 20 | 0,93 s a 2,12 s |
| `amb_1.wav` | 1, suelto en `grabacion` | 20,64 s |

Esas duraciones se midieron con los 30, 30 y 20 archivos. Después se retiraron cuatro tomas. Quedan 28 en `parche`, 28 en `anillo` y 20 en `ambiente`.

## Tomas retiradas

El WAV y el `.raw` de estas cuatro ya no están en las carpetas. El motivo salió de `pruebas_py/firma.ipynb`.

| Archivo | Motivo |
| --- | --- |
| `anillo-04` | Ruido antes del golpe. RMS previo 447, z 11,6. La mediana de la clase era 149. |
| `anillo-08` | Ruido antes del golpe. RMS previo 589, z 17,2. |
| `parche-19` | Golpe mucho más débil. Pico 1171, mediana de la clase 13319. |
| `parche-22` | Otro sonido después del golpe. El rebote llegó a 5497, con un pico de 11793. |
