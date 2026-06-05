# Scripts de Análisis Estadístico y Automatización (4.4)

Este directorio contiene las rutinas en Python desarrolladas para la automatización del procesamiento de datos analíticos, la ejecución de pruebas estadísticas inferenciales y el renderizado de gráficos de control de la formulación óptima (**F4**) frente al estándar comercial y sus iteraciones experimentales previas.

## Contenido del Directorio

### 1. [`ANOVA_resultados_reologia.py`](./ANOVA_resultados_reologia.py)
* **Propósito**: Evalúa las propiedades mecánicas y de flujo de los fluidos obtenidos en laboratorio.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv)
* **Análisis Estadístico**: 
  * Unifica réplicas experimentales (corrección de lotes de diseño) bajo el bloque definitivo F4.
  * Ejecuta un Análisis de Varianza (**ANOVA unifactorial**, α = 0.05) para las variables de *Densidad* (**g/mL**), *Tiempo de flujo* (**s**) y *Viscosidad absoluta* (**mPa·s**).
  * Aplica la prueba post-hoc de **Tukey HSD** para contrastar la hipótesis de similitud con el estándar industrial.
* **Gráficas Generadas (`/results/`)**: `grafica_densidad.png`, `grafica_tiempo_flujo.png`, `grafica_viscosidad.png`.

### 2. [`ANOVA_resultados_estabilidad.py`](./ANOVA_resultados_estabilidad.py)
* **Propósito**: Monitorea el comportamiento cinético del Potencial de Hidrógeno (pH) en almacenamiento.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv)
* **Análisis Estadístico**: 
  * Modela de forma independiente el estado basal (`ph_inicial` en el Día 0) y el estado final tras el ensayo de estabilidad acelerada (`ph_final` a los 120 días).
  * Determina mediante ANOVA y Tukey HSD la significancia de las variaciones térmicas y temporales sobre la matriz coloidal.
* **Gráficas Generadas (`/results/`)**: `grafica_ph_inicial.png`, `grafica_ph_final.png`. *(Nota: Nombres sujetos al procesamiento dinámico de variables).*

### 3. [`ANOVA_resultados_espuma.py`](./ANOVA_resultados_espuma.py)
* **Propósito**: Cuantifica las propiedades interfaciales y la capacidad tensioactiva del sistema base biodegradable.
* **Entrada**: [`../../data/4.4_propiedades_fisicoquimicas/resultados_espuma.csv`](../../data/4.4_propiedades_fisicoquimicas/resultados_espuma.csv)
* **Análisis Estadístico**: 
  * Analiza la capacidad espumante inmediata (`altura_espuma`) y la resistencia mecánica de las burbujas ante el colapso temporal (`colapso_espuma`).
  * Evalúa la variabilidad mediante ANOVA y Tukey para validar el desempeño interfacial frente a los sulfatos comerciales.
* **Gráficas Generadas (`/results/`)**: `grafica_altura_espuma.png`, `grafica_colapso_espuma.png`.

---

## Arquitectura del Código y Reproducibilidad

Los scripts están diseñados bajo principios de software robusto para garantizar su ejecución en cualquier entorno:
- **Rutas Dinámicas:** Utilizan la librería `os` para trazar rutas relativas a la raíz del repositorio, eliminando dependencias de rutas locales absolutas.
- **Limpieza de Datos Autónoma:** Los scripts están programados para omitir encabezados en blanco, corregir codificaciones (`latin-1`) y estandarizar nombres de variables de forma transparente para el usuario.
- **Reporte en Consola:** Durante la ejecución, se imprime un resumen ejecutivo del ANOVA y una validación booleana clara (ÉXITO / NOTA) de la comparación específica entre la fórmula "F4" y el "Comercial".

---

## Estándar de Visualización Gráfica

Todos los módulos exportan visualizaciones normalizadas con la librería `Seaborn` y `Matplotlib` utilizando la siguiente arquitectura de control:
1. **Barras de Media**: Representación del desempeño promedio de cada tratamiento.
2. **Barras de Error**: Intervalos calculados a partir de la desviación estándar analítica (SD).
3. **Línea de Control Industrial**: Una línea horizontal discontinua roja (`plt.axhline`) que delimita el valor promedio del champú comercial. Si las barras de error de la formulación F4 cruzan o alcanzan esta línea, se valida visualmente el empate estadístico corroborado por la prueba de Tukey HSD ($p > 0.05$).

---

## Requisitos del Entorno

Para ejecutar los análisis, se requiere un entorno con Python 3.x y las siguientes dependencias científicas:

```bash
pip install pandas scipy statsmodels seaborn matplotlib