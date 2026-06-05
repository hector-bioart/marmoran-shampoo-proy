# Scripts de Análisis Estadístico y Automatización (4.4)

Este directorio contiene las rutinas en Python desarrolladas para la automatización del procesamiento de datos analíticos, la ejecución de pruebas estadísticas inferenciales y el renderizado de gráficos comparativos del desempeño de las formulaciones frente al estándar comercial.

## Contenido del Directorio y Enlaces a Resultados

A continuación se detalla cada script y se enlaza directamente a la visualización gráfica (`/results/`) que genera como salida.

### 1. [`ANOVA_resultados_reologia.py`](./ANOVA_resultados_reologia.py)
* **Propósito**: Evalúa las propiedades mecánicas y de flujo de los fluidos obtenidos en laboratorio mediante ANOVA y prueba de Tukey HSD.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv)
* **Gráficas Generadas**: 
  * 🔗 [`grafica_densidad.png`](../../results/4.4_propiedades_fisicoquimicas/grafica_densidad.png)
  * 🔗 [`grafica_tiempo_flujo.png`](../../results/4.4_propiedades_fisicoquimicas/grafica_tiempo_flujo.png)
  * 🔗 [`grafica_viscosidad.png`](../../results/4.4_propiedades_fisicoquimicas/grafica_viscosidad.png)

### 2. [`ANOVA_resultados_estabilidad.py`](./ANOVA_resultados_estabilidad.py)
* **Propósito**: Monitorea el comportamiento cinético del Potencial de Hidrógeno (pH) para evaluar la estabilidad térmica y temporal de la matriz coloidal.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv)
* **Gráficas Generadas**: 
  * 🔗 [`estabilidad_ph_inicial.png`](../../results/4.4_propiedades_fisicoquimicas/estabilidad_ph_inicial.png)
  * 🔗 [`estabilidad_ph_final.png`](../../results/4.4_propiedades_fisicoquimicas/estabilidad_ph_final.png)

### 3. [`ANOVA_resultados_espuma.py`](./ANOVA_resultados_espuma.py)
* **Propósito**: Cuantifica las propiedades interfaciales y la capacidad tensioactiva (ANOVA y Tukey) frente a los sulfatos comerciales.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_espuma.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_espuma.csv)
* **Gráficas Generadas**: 
  * 🔗 [`espuma_altura_espuma.png`](../../results/4.4_propiedades_fisicoquimicas/espuma_altura_espuma.png)
  * 🔗 [`espuma_colapso_espuma.png`](../../results/4.4_propiedades_fisicoquimicas/espuma_colapso_espuma.png)

### 4. [`comparativo_diseño.py`](./comparativo_diseño.py)
* **Propósito**: Genera un gráfico de doble eje para contrastar directamente la evolución del desempeño interfacial entre la fórmula inicial (F1), la fórmula optimizada (F4) y el champú comercial.
* **Entrada**: Datos integrados estructuralmente en el código (*hardcoded*).
* **Gráfica Generada**: 
  * 🔗 [`analisis_comparativo_desempeño.png`](../../results/4.4_propiedades_fisicoquimicas/analisis_comparativo_desempeño.png)

---

## Arquitectura del Código y Reproducibilidad

Los scripts están diseñados bajo principios de software robusto para garantizar su ejecución en cualquier entorno:
- **Rutas Dinámicas:** Utilizan la librería `os` para trazar rutas relativas a la raíz del repositorio, eliminando dependencias de rutas locales absolutas.
- **Limpieza de Datos Autónoma:** Los scripts de la familia ANOVA están programados para omitir encabezados en blanco, corregir codificaciones y estandarizar nombres de variables automáticamente.
- **Trazabilidad Visual:** Todas las visualizaciones incluyen una línea de control que delimita el estándar comercial, permitiendo validar empates estadísticos visualmente sin requerir una inspección manual del código.

---

## Requisitos del Entorno

Para ejecutar los análisis, se requiere un entorno con Python 3.x y las siguientes dependencias científicas:

```bash
pip install pandas scipy statsmodels seaborn matplotlib numpy