# Scripts de Análisis Estadístico y Automatización (Sección 4.4)

Este directorio contiene las rutinas en Python desarrolladas para la automatización del procesamiento de datos analíticos, la ejecución de pruebas estadísticas inferenciales y el renderizado de gráficos de control de la formulación óptima (**F4**) frente al estándar comercial y sus iteraciones experimentales previas.

## Contenido del Directorio

### 1. `ANOVA_resultados_reologia.py`
* **Propósito**: Evalúa las propiedades mecánicas y de flujo de los fluidos obtenidos en laboratorio.
* **Entrada**: `data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv`
* **Análisis Estadístico**: 
  * Unifica réplicas experimentales bajo el bloque definitivo de diseño.
  * Ejecuta un Análisis de Varianza (**ANOVA unifactorial**, $\alpha = 0.05$) para las variables de *Densidad* ($g/mL$), *Tiempo de flujo* ($s$) y *Viscosidad absoluta* ($mPa\cdot s$).
  * Aplica la prueba post-hoc de **Tukey HSD** para contrastar la hipótesis de similitud con el estándar industrial.
* **Gráficas Generadas**: `resultado_densidad.png`, `resultado_tiempo_flujo.png`, `resultado_viscosidad.png`.

### 2. `ANOVA_resultados_estabilidad.py`
* **Propósito**: Monitorea el comportamiento cinético del Potencial de Hidrógeno ($pH$) en almacenamiento.
* **Entrada**: `data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv`
* **Análisis Estadístico**: 
  * Modela de forma independiente el estado basal (`ph_inicial` en el Día 0) y el estado final tras el ensayo de estabilidad acelerada (`ph_final` a los 120 días).
  * Determina mediante ANOVA y Tukey HSD la significancia de las variaciones térmicas y temporales sobre la matriz coloidal.
* **Gráficas Generadas**: `estabilidad_ph_inicial.png`, `estabilidad_ph_final.png`.

### 3. `ANOVA_resultados_espuma.py`
* **Propósito**: Cuantifica las propiedades interfaciales y la capacidad tensioactiva del sistema base biodegradable.
* **Entrada**: `data/4.4_propiedades_fisicoquimicas/resultados_espuma.csv`
* **Análisis Estadístico**: 
  * Analiza la capacidad espumante inmediata (`altura_espuma`) y la resistencia mecánica de las burbujas ante el colapso temporal (`colapso_espuma`).
  * Evalúa la variabilidad mediante ANOVA y Tukey para validar el desempeño interfacial frente a los sulfatos comerciales.
* **Gráficas Generadas**: `espuma_altura_espuma.png`, `espuma_colapso_espuma.png`.

---

## Estándar de Visualización Gráfica

Todos los módulos exportan visualizaciones normalizadas con la librería `Seaborn` y `Matplotlib` utilizando la siguiente arquitectura de control:
1. **Barras de Media**: Representación del desempeño promedio de cada tratamiento.
2. **Barras de Error**: Intervalos calculados a partir de la desviación estándar analítica ($SD$).
3. **Línea de Control Industrial**: Una línea horizontal discontinua roja (`plt.axhline`) que delimita el valor del champú comercial. Si las barras de error de la formulación F4 cruzan esta línea, se valida visualmente el empate estadístico de la prueba de Tukey HSD ($p > 0.05$).

---

## Requisitos del Entorno

Para garantizar la reproducibilidad del análisis, se requiere un entorno con Python 3.x y las siguientes dependencias científicas:

```bash
pip install pandas scipy statsmodels seaborn matplotlib
