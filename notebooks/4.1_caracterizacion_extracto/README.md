# Guía de Ejecución: Scripts de Caracterización Fisicoquímica (4.1)

Este directorio contiene los scripts en Python utilizados para la visualización de los datos crudos obtenidos en la caracterización inicial del extracto.

## Entorno de Ejecución
- Los scripts están diseñados para ejecutarse localmente usando Python (probados en VS Code).
- **Dependencias necesarias:** `matplotlib`, `numpy`. (Ver `requirements.txt` en la raíz del repositorio).
- **Nota de datos:** Actualmente, los scripts contienen los datos integrados (hardcoded) para facilitar su ejecución rápida sin dependencias de rutas de archivos.

## Catálogo de Scripts y Relación con la Tesis

| Script | Descripción y Salida | Ubicación en Tesis |
| :--- | :--- | :--- |
| `4.1a_grafica_ph.py` | Genera un gráfico de barras con barras de error para el pH (media ± desviación estándar). | **Capítulo 4 (Resultados):** Figura 4.1.2 |
| `4.1b_grafica_sdt_ce.py` | Genera un gráfico de barras comparativo entre los Sólidos Disueltos Totales (SDT) y la Conductividad Eléctrica. | **Anexo B:** Scripts de procesamiento de datos |

## Instrucciones de Uso
Para generar las gráficas, ejecuta los scripts desde la terminal apuntando a este directorio:
```bash
python 4.1a_grafica_ph.py
python 4.1b_grafica_sdt_ce.py
