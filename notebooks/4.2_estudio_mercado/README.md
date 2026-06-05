# Guía de Ejecución: Scripts de Estudio de Mercado (4.2)

Este directorio contiene los scripts en Python desarrollados para procesar los datos del relevamiento comercial y generar las visualizaciones que fundamentan la viabilidad técnica y económica del champú formulado.

## Entorno de Ejecución
- Los scripts están programados para leer los archivos `.csv` correspondientes ubicados en el directorio [`/data/4.2_estudio_mercado/`](../../data/4.2_estudio_mercado/).
- *(Nota: Las librerías y el entorno virtual necesarios para ejecutar este código se encuentran detallados en la documentación principal en la raíz del repositorio).*

## Catálogo de Scripts y Salidas

> **Relación con el documento:** Todas las visualizaciones generadas por estos scripts están referenciadas directamente en el documento del reporte, en la sección **"4.2 Análisis del estudio de mercado y selección de insumos y en el Anexo B"**.

| Script | Propósito del Análisis | Visualización Generada (`/results/`) |
| :--- | :--- | :--- |
| [`4.2a_frecuencia_ingredientes.py`](./4.2a_frecuencia_ingredientes.py) | Analiza y grafica la presencia porcentual de las diferentes categorías químicas (sulfatos, sales, betainas) en la muestra comercial. | [`barras_frecuencia_mercado.png`](../../results/4.2_estudio_mercado/barras_frecuencia_mercado.png) |
| [`4.2b_brecha_tecnologica.py`](./4.2b_brecha_tecnologica.py) | Genera una comparativa que contrasta el uso de ingredientes sintéticos del estándar industrial frente a las formulaciones propuestas. | [`barras_comparativa_brecha.png`](../../results/4.2_estudio_mercado/barras_comparativa_brecha.png) |
| [`4.2c_analisis_volumen.py`](./4.2c_analisis_volumen.py) | Procesa la distribución de los formatos de envase para identificar el tamaño de mayor preferencia por el consumidor. | [`pie_distribucion_envases.png`](../../results/4.2_estudio_mercado/pie_distribucion_envases.png) |
| [`4.2d_segmentacion_precios.py`](./4.2d_segmentacion_precios.py) | Clasifica la muestra en segmentos económicos para ubicar el producto en el rango de gama media-especializada. | [`barras_precios_mercado.png`](../../results/4.2_estudio_mercado/barras_precios_mercado.png) |

## Instrucciones de Uso
Para reproducir las gráficas del análisis de mercado, ejecuta los scripts de manera secuencial desde la terminal:

```bash
python 4.2a_frecuencia_ingredientes.py
python 4.2b_brecha_tecnologica.py
python 4.2c_analisis_volumen.py
python 4.2d_segmentacion_precios.py