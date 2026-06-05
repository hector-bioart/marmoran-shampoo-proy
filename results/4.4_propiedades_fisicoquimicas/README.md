# Resultados Gráficos y Validación Visual (Sección 4.4 / 4.5)

Este directorio almacena las salidas de alta resolución (.png) generadas de manera automática por los scripts de análisis estadístico. Estas figuras constituyen el soporte visual y la evidencia experimental para la defensa del desempeño técnico de la formulación óptima (**F4**) frente al estándar comercial y las iteraciones previas del proyecto.

## Catálogo de Figuras y Variables Evaluadas

### 1. Propiedades Reológicas y de Flujo
* **[`grafica_densidad.png`](./grafica_densidad.png)**: Distribución de medias para la densidad volumétrica (**g/mL**). Muestra el ajuste interfacial del sistema.
* **[`grafica_tiempo_flujo.png`](./grafica_tiempo_flujo.png)**: Evaluación por método capilar (**s**) que mide indirectamente el rozamiento interno del fluido.
* **[`grafica_viscosidad.png`](./grafica_viscosidad.png)**: Cuantificación de la viscosidad absoluta (**mPa·s**). Evidencia la consistencia operativa de la F4 (2,153 mPa·s promedio) frente al control comercial.
* *Especificación Visual*: Renderizadas originalmente bajo la paleta de color `viridis` de Seaborn.

### 2. Cinética y Estabilidad del pH
* **[`estabilidad_ph_inicial.png`](./estabilidad_ph_inicial.png)**: Registro del Potencial de Hidrógeno basal (Día 0) inmediatamente posterior a la manufactura.
* **[`estabilidad_ph_final.png`](./estabilidad_ph_final.png)**: Evaluación del pH tras el ensayo de estabilidad acelerada (120 días a 25 °C ± 3 °C), demostrando la conservación del sistema coloidal.
* *Especificación Visual*: Renderizadas originalmente bajo la paleta de color `magma` de Seaborn.

### 3. Propiedades Interfaciales de la Espuma y Desempeño
* **[`espuma_altura_espuma.png`](./espuma_altura_espuma.png)**: Índice de generación e introducción de la fase gaseosa dispersa (**cm**).
* **[`espuma_colapso_espuma.png`](./espuma_colapso_espuma.png)**: Resistencia mecánica de la película líquida interfacial ante el colapso (**minutos**).
* **[`analisis_comparativo_desempeño.png`](./analisis_comparativo_desempeño.png)**: Gráfico de doble eje que contrasta de manera integrada la evolución del desempeño interfacial (altura de espuma y tiempo de colapso) entre las variantes F1, F4 y el control comercial.
* *Especificación Visual*: Renderizadas originalmente bajo la paleta de color `ocean` (para las pruebas analíticas individuales) para destacar propiedades de fluidos interfaciales.

---

## Interpretación de las Líneas de Control

Para asegurar una lectura rápida, homogénea y rigurosa por parte del sínodo evaluador, cada gráfica cuenta con los siguientes elementos de control de calidad de datos:

1. **Barras de Datos**: Representan los valores promedio reales calculados a partir de las réplicas de laboratorio.
2. **Bigotes de Variabilidad**: Indican la desviación estándar analítica (SD), haciendo transparente el error experimental inherente del proceso de medición.
3. **Línea Discontinua Roja (`plt.axhline`)**: Representa el valor promedio exacto del **Champú Comercial de Referencia**. 
   * *Criterio de Aceptación*: Si las barras de error de la formulación **F4** se intersectan o cruzan horizontalmente con la línea roja discontinua, se infiere visualmente el éxito estadístico (homogeneidad/empate técnico determinado por la prueba de Tukey HSD con un p > 0.05).

---

## Notas de Uso en la Memoria de Reporte de Residencia
- Las imágenes están exportadas con una resolución estándar óptima para impresión digital directa y escalado vectorial básico sin pérdida de nitidez en procesadores de texto (LaTeX / MS Word).
- Para auditar o reproducir el código en Python que generó automáticamente estas visualizaciones y exportó las métricas en consola, diríjase al directorio [`/notebooks/4.4_propiedades_fisicoquimicas/`](../../notebooks/4.4_propiedades_fisicoquimicas/).