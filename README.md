<div align="center">

# 🥤 Monster vs Red Bull

**Clasificador de imágenes con fine-tuning de ResNet-18**

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)
![uv](https://img.shields.io/badge/uv-managed-DE5FE9)

Laboratorio 14 · Inteligencia Artificial (USS-ICIFH001) · Universidad San Sebastián

</div>

---

## 📌 Descripción

Un modelo que mira una foto y responde si hay una lata de **Monster**, una de **Red Bull**, o **ninguna de las dos** (por ejemplo, un vaso de agua). Parte de una ResNet-18 pre-entrenada en ImageNet y la ajusta (fine-tuning) con fotos tomadas por nosotros.

| Clase | Qué contiene |
|---|---|
| `monster` | Latas de Monster Energy, de distintos sabores y colores |
| `redbull` | Latas de Red Bull, de distintos sabores y colores |
| `ninguna` | Vasos, botellas, otras bebidas, objetos y fondos sin lata |

**Criterio de etiquetado:** la clase es la marca de la lata visible. Si aparecen latas de ambas marcas, o la marca no se distingue, la foto se descarta.

## 👥 Integrantes

- Mathias Carrera
- Bastian Contreras

## 🗂️ Estructura

```
lab_14/
├── clasificador.ipynb   # entrenamiento, evaluación y matriz de confusión
├── reducir_fotos.py     # reduce las fotos a 512 px
├── data/
│   ├── train/{monster,redbull,ninguna}/
│   └── test/{monster,redbull,ninguna}/
├── pyproject.toml
└── uv.lock
```

## 🚀 Cómo ejecutarlo

Requiere [uv](https://docs.astral.sh/uv/).

```bash
git clone <url-del-repo>
cd lab_14
uv sync
uv run jupyter lab
```

Luego abrir `clasificador.ipynb` y ejecutar todas las celdas.

## 📸 Agregar fotos

1. Dejar las fotos en `data/train/<clase>/` o `data/test/<clase>/`.
2. Reducirlas a 512 px:
   ```bash
   uv run python reducir_fotos.py
   ```

Requisitos del laboratorio: al menos 50 fotos propias por clase en `train` y 10 por clase en `test`.

## 🧠 Método

- **Modelo:** ResNet-18 con pesos de ImageNet, capa final reemplazada por 3 salidas.
- **Datos:** `ImageFolder`; 20 % de `train` para validación, separado por bloques de fotos consecutivas (evita gemelas de una misma ráfaga) y con semilla fija.
- **Aumento de datos:** recorte aleatorio, volteo horizontal y variación de color.
- **Entrenamiento:** PyTorch Lightning, Adam (lr 3e-4), 25 épocas, pesos por clase en la pérdida.
- **Evaluación:** exactitud y matriz de confusión sobre `data/test` (meta: ≥ 0,80).

## 📊 Resultados

| Clase | Entrenamiento | Test |
|---|---|---|
| `monster` | 63 | 15 |
| `redbull` | 82 | 15 |
| `ninguna` | 60 | 16 |

**Exactitud en test: 0,978** (45 de 46 fotos).

Matriz de confusión (filas: clase real, columnas: predicción):

| Real \ Predicho | monster | ninguna | redbull |
|---|---|---|---|
| **monster** | 15 | 0 | 0 |
| **ninguna** | 0 | 15 | 1 |
| **redbull** | 0 | 0 | 15 |

El único error es una foto de `ninguna` clasificada como Red Bull. Un primer intento con 10 épocas y pocas fotos de `ninguna` había dado 0,69.

**Limitaciones:** el test es pequeño (46 fotos), algunas fotos de Monster y Red Bull del test se parecen a las de entrenamiento, y todas se tomaron en pocos lugares con la misma mesa de fondo.

## 🤝 Flujo de trabajo en equipo

- Ramas cortas por tarea (`fotos-mathias`, `fotos-bastian`, `ajustes-modelo`) y *pull request* a `main`.
- No subir `.venv/` ni `log/` (ya están en `.gitignore`).
- Antes de entrenar: `git pull` y `uv sync`.
