# Base de Datos: Propiedades Fisicoquímicas, Reológicas y de Desempeño (4.4)

Este directorio contiene los registros experimentales cuantitativos correspondientes a la evaluación instrumental de las formulaciones de champú a base de *Agave marmorata*.

## Catálogo de Archivos

| Archivo | Descripción del Contenido |
| :--- | :--- |
| [`resultados_estabilidad.csv`](./resultados_estabilidad.csv) | Evaluaciones fisicoquímicas (como pH y conductividad) registradas a lo largo de los periodos de prueba para determinar la estabilidad térmica y física. |
| [`resultados_reologia.csv`](./resultados_reologia.csv) | Mediciones instrumentales de la viscosidad aparente y el comportamiento de flujo de las diferentes variantes del gel. |
| [`resultados_espuma.csv`](./resultados_espuma.csv) | Registros de las pruebas de desempeño sobre la capacidad espumante y la retención volumétrica generada por las saponinas. |

## Vinculación Estructural y Metodológica

- **Relación con el documento:** Los datos aquí tabulados son el soporte empírico central para los apartados **"4.4 Evaluación de propiedades reológicas, fisicoquímicas y de desempeño"** y **"4.5 Análisis estadístico y validación de la formulación óptima"** del documento.
- **Análisis Estadístico:** Estos archivos `.csv` están formateados para ser consumidos y procesados automáticamente mediante Análisis de Varianza (ANOVA y pruebas Tukey). 

> **Nota de Navegación:** Para auditar los scripts en Python que realizan la validación estadística de estos datos, diríjase al directorio correspondiente: 
> 🔗 [`/notebooks/4.4_propiedades_fisicoquimicas/`](../../notebooks/4.4_propiedades_fisicoquimicas/)