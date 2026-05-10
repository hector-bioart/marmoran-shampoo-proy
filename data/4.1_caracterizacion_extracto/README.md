# Datos de Caracterización Fisicoquímica (4.1)

Este directorio contiene los datos crudos y procesados correspondientes a la caracterización fisicoquímica inicial del extracto. 

## Estructura de Archivos

- `parametros_fisicoquimicos.csv`: Tabla con las mediciones por triplicado (R1, R2, R3), promedios y desviaciones estándar.

## Diccionario de Datos

Las variables medidas en el archivo CSV incluyen:

| Parámetro | Unidad | Descripción |
| :--- | :--- | :--- |
| **pH** | Adimensional | Medición de la acidez del extracto. |
| **Densidad** | g/mL | Relación masa/volumen del extracto acuoso estabilizado. |
| **Conductividad eléctrica** | µS/cm | Capacidad del medio para conducir corriente (indicador de iones disueltos). |
| **Sólidos Disueltos Totales (SDT)** | ppm | Concentración de sustancias disueltas en el extracto. |

## Notas de Procesamiento
- Los valores de **Promedio** y **Desviación Estándar** fueron redondeados a cifras significativas coherentes con la precisión de los instrumentos de medición.
- Para reproducir el análisis estadístico de estos datos, referirse a los scripts ubicados en `/notebooks/4.1_caracterizacion_extracto/`.

