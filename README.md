# Estandarización de la formulación de champú con extracto de maguey pitzometl (*Agave marmorata*)

Este repositorio alberga la infraestructura de análisis de datos, evidencia instrumental y validación estadística para el proyecto de investigación de Ingeniería Bioquímica: **"Estandarización de la formulación de champú con extracto de maguey pitzometl (Agave marmorata) de la región de Zapotitlán Salinas, Puebla."**

## 🛠️ Tecnologías y Metodología
Para asegurar el rigor científico y la reproducibilidad de los resultados, se implementó un flujo de trabajo basado en buenas prácticas de ciencia de datos:

- **Lenguaje:** Python 3.x (entorno de ejecución local).
- **Gestión de Datos:** `pandas` y `numpy` para la limpieza, tabulación y estructuración de los resultados experimentales.
- **Estadística Inferencial:** `scipy` y `statsmodels` para la automatización de pruebas de hipótesis (ANOVA unifactorial y prueba post-hoc de Tukey HSD) con un nivel de confianza del 95% ($\alpha = 0.05$).
- **Visualización:** `matplotlib` y `seaborn` para la generación de gráficas de alta resolución (DPI 300) y control de referencias comerciales integradas en el reporte final.

## 📂 Arquitectura del Repositorio
El proyecto está estructurado de manera modular para garantizar la trazabilidad desde el dato crudo hasta la conclusión científica. 

### Directorios Raíz
- 📁 **[`/data`](./data)**: Bases de datos tabulares (`.csv`), registros de iteraciones y diccionarios de variables.
- 📁 **[`/media`](./media)**: Catálogo de evidencia fotográfica sobre la metodología, pruebas instrumentales y comportamiento físico de las formulaciones.
- 📁 **[`/notebooks`](./notebooks)**: Módulo de scripts de automatización (`.py`) para el procesamiento estadístico y renderizado.
- 📁 **[`/results`](./results)**: Exportaciones gráficas finales utilizadas para la validación visual en el documento de tesis.

### Módulos de Investigación (Navegación Rápida)
La información dentro de cada directorio raíz está subdividida en las cuatro etapas críticas del proyecto:
* **[4.1 Caracterización del Extracto](./notebooks/4.1_caracterizacion_extracto):** Análisis fisicoquímico del jugo crudo estabilizado.
* **[4.2 Estudio de Mercado](./notebooks/4.2_estudio_mercado):** Relevamiento comercial, análisis INCI y brecha tecnológica.
* **[4.3 Diseño y Optimización](./data/4.3_diseno_optimizacion):** Registro cualitativo de la evolución de las variantes experimentales (F1 a F4).
* **[4.4 Propiedades Fisicoquímicas y Desempeño](./notebooks/4.4_propiedades_fisicoquimicas):** Validación estadística del producto final frente al estándar comercial.

*(Nota: Cada subdirectorio contiene su propio `README.md` con instrucciones específicas de uso y lectura).*

## ⚙️ Reproducibilidad del Entorno
Para auditar o ejecutar el código de este repositorio, se requiere instalar las dependencias científicas correspondientes:
```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn