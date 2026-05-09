# Estandarización de la formulación de champú con extracto de maguey pitzometl (*Agave marmorata*)

Este repositorio alberga la infraestructura de análisis de datos y validación estadística para el proyecto de investigación de Ingeniería Bioquímica: **"ESTANDARIZACIÓN DE LA FORMULACIÓN DE CHAMPÚ CON EXTRACTO DE MAGUEY PITZOMETL (AGAVE MARMORATA) DE LA REGIÓN DE ZAPOTITLÁN SALINAS PUEBLA."**.

## 🛠️ Tecnologías y Metodología
Para asegurar el rigor científico y la reproducibilidad de los resultados, se implementó un flujo de trabajo basado en ciencia de datos:

- **Lenguaje:** Python 3.x
- **Gestión de Datos:** `Pandas` y `NumPy` para la tabulación de resultados experimentales.
- **Visualización:** `Matplotlib` y `Seaborn` para la generación de gráficas de alta resolución (DPI 300) integradas en el reporte final.
- **Estadística Inferencial:** `SciPy` para la ejecución de pruebas de hipótesis (ANOVA de una vía) con un nivel de confianza del 95%.

## 📂 Estructura del Proyecto
- **/data**: Contiene los datos crudos del análisis de mercado (N=20) y los resultados de las pruebas fisicoquímicas por triplicado.
- **/media**: Contiene el registro fotográfico de la fase experimental. Sirve como evidencia visual de la metodología descrita en el Capítulo 3 y los resultados físicos del Capítulo 4.
- **/notebooks**: Scripts de Google Colab (.ipynb) que contienen la lógica de programación y procesamiento de datos.
- **/results**: Exportaciones de las figuras (Boxplots, diagramas de barras y pasteles) utilizadas en el Capítulo 4.

## 🔬 Transparencia Académica
El uso de este repositorio garantiza que cada gráfica y conclusión estadística presentada en la tesis tiene un respaldo algorítmico auditable, permitiendo la trazabilidad completa desde el dato crudo en el laboratorio hasta el resultado final.
