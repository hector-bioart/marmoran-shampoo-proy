# Diccionario de Datos: Estudio de Mercado y Análisis INCI (4.2)

Este directorio contiene las bases de datos crudas y tabuladas correspondientes al relevamiento comercial de 20 productos de higiene capilar. Estos datos sustentan la viabilidad y competitividad de las formulaciones de *Agave marmorata*.

## Catálogo de Archivos

| Archivo | Descripción del Contenido |
| :--- | :--- |
| `relevamiento_mixto_shampoo.csv` | Base de datos maestra. Contiene la lista de ingredientes completa (INCI), marca, tipo, tamaño y punto de venta. |
| `perfil_fisicoquimico_marcas.csv` | Matriz de clasificación que desglosa la función de cada ingrediente (tensioactivos, acondicionadores, conservantes, etc.) por marca. |
| `clasificacion_inci_ingredientes.csv` | Resumen cualitativo de las familias químicas identificadas y su impacto observado en el mercado. |
| `distribucion_composicion_quimica.csv` | Tabla de frecuencias absolutas y relativas (%) de los ingredientes predominantes en la muestra. |
| `frecuencia_componentes_activos.csv` | Datos procesados para el contraste directo (Brecha Tecnológica) entre el estándar industrial y las formulaciones propuestas. |
| `segmentacion_precio_volumen.csv` | Datos de competitividad económica, agrupando los productos por rangos de precio (MXN) y capacidad del envase (mL). |

## Glosario de Variables Clave
- **INCI:** Nomenclatura Internacional de Ingredientes Cosméticos.
- **Tensioactivos Aniónicos:** Principalmente sulfatos (SLES, SLS), utilizados como agentes de limpieza profunda.
- **Tensioactivos No Iónicos:** Alternativas de química verde y baja irritabilidad (ej. Coco-Glucoside).
- **Brecha Tecnológica:** Diferencia porcentual en el uso de ingredientes sintéticos (mercado) frente a alternativas naturales (fórmulas F).

## Notas de Uso
Los datos económicos (`segmentacion_precio_volumen.csv`) están expresados en Pesos Mexicanos (MXN) y corresponden al muestreo físico y electrónico realizado durante la fase de investigación.
