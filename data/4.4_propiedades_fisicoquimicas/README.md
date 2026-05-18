# Datos de Caracterización Fisicoquímica (Sección 4.4)

Este directorio contiene las bases de datos en formato crudo (`.csv`) obtenidas de los ensayos analíticos de laboratorio para la formulación optimizada (F4), sus iteraciones previas y el control comercial.

## Contenido del Directorio

* **`resultados_reologia.csv`**: Registro de tres réplicas experimentales para el estudio del comportamiento mecánico y de flujo de las muestras:
    * Densidad ($g/mL$)
    * Tiempo de flujo ($s$)
    * Viscosidad Absoluta ($mPa\cdot s$)
* **`resultados_estabilidad.csv`**: Mediciones del Potencial de Hidrógeno en dos bloques temporales para el control cinético de estabilidad coloidal:
    * pH inicial (Día 0)
    * pH final (Post-almacenamiento acelerado a los 120 días bajo 25 °C $\pm$ 3 °C)
* **`resultados_espuma.csv`**: Evaluación de propiedades interfaciales y capacidad tensioactiva de las muestras seleccionadas (Comercial, F1 y F4):
    * Altura inicial de la espuma ($cm$)
    * Tiempo de colapso estructural ($min$)

## Especificaciones Técnicas
Las matrices de datos se encuentran estructuradas en filas por réplica independiente y tratamiento. Utilizan codificación de caracteres `latin-1` y separadores de coma estándar, quedando validadas para su consumo automatizado por parte de los scripts estadísticos alojados en la carpeta raíz `/notebooks` del proyecto.
