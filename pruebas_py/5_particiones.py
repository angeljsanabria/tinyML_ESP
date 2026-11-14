# 5_particiones.py
# Etapa 3. Una fila por grabacion: clase y particion.
# Las ventanas de ese archivo quedan en la misma particion.
# Proporcion por clase: 60, 20 y 20 por ciento. Semilla fija.
#
# Entorno: PowerShell de Windows.
#   conda activate tinyml
#   cd pruebas_py
#   python 5_particiones.py
import csv
import random
from pathlib import Path

SEMILLA = 1
FRACCION_VALIDACION = 0.20
FRACCION_PRUEBA = 0.20
CLASES = ("parche", "anillo", "ambiente")
ETIQUETA = {"parche": "PARCHE", "anillo": "ANILLO", "ambiente": "AMBIENTE"}

raiz = Path(__file__).resolve().parents[1]
grabacion = raiz / "pruebas_py" / "grabacion"
salida = raiz / "python" / "data" / "particiones.csv"
salida.parent.mkdir(parents=True, exist_ok=True)

rng = random.Random(SEMILLA)
filas = []

for carpeta in CLASES:
    wavs = sorted((grabacion / carpeta).glob("*.wav"))
    pares = []
    for wav in wavs:
        raw = wav.parent / "outputs" / (wav.stem + ".raw")
        if not raw.is_file():
            raise FileNotFoundError(raw)
        pares.append((wav, raw))
    rng.shuffle(pares)
    n = len(pares)
    n_prueba = int(round(n * FRACCION_PRUEBA))
    n_validacion = int(round(n * FRACCION_VALIDACION))
    n_entrenamiento = n - n_validacion - n_prueba
    if min(n_entrenamiento, n_validacion, n_prueba) < 1:
        raise RuntimeError("particion vacia en %s" % carpeta)
    cortes = (
        ("entrenamiento", pares[:n_entrenamiento]),
        ("validacion", pares[n_entrenamiento : n_entrenamiento + n_validacion]),
        ("prueba", pares[n_entrenamiento + n_validacion :]),
    )
    for particion, grupo in cortes:
        for wav, raw in sorted(grupo, key=lambda par: par[0].name):
            filas.append(
                {
                    "clase": ETIQUETA[carpeta],
                    "particion": particion,
                    "wav": wav.relative_to(raiz).as_posix(),
                    "raw": raw.relative_to(raiz).as_posix(),
                }
            )

filas.sort(key=lambda fila: (fila["clase"], fila["particion"], fila["wav"]))
with salida.open("w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(
        archivo, fieldnames=("clase", "particion", "wav", "raw")
    )
    escritor.writeheader()
    escritor.writerows(filas)

print("salida:", salida.relative_to(raiz).as_posix())
print("semilla:", SEMILLA)
print("filas:", len(filas))
for clase in ("PARCHE", "ANILLO", "AMBIENTE"):
    for particion in ("entrenamiento", "validacion", "prueba"):
        cuenta = sum(
            1
            for fila in filas
            if fila["clase"] == clase and fila["particion"] == particion
        )
        print(clase, particion, cuenta)
