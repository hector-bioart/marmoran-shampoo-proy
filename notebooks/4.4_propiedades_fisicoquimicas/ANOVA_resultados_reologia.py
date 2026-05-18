import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import os
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def analizar_reologia_repositorio():
    # 1. CONFIGURACIÓN DE RUTAS DINÁMICAS
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Subimos dos niveles desde 'notebooks/4.4_...' para llegar a la raíz del proyecto
    ruta_raiz = os.path.abspath(os.path.join(directorio_actual, '../../'))
    
    # Definimos rutas absolutas basadas en la raíz
    ruta_csv = os.path.join(ruta_raiz, 'data/4.4_propiedades_fisicoquimicas/resultados_reologia.csv')
    output_dir = os.path.join(ruta_raiz, 'results/4.4_propiedades_fisicoquimicas')
    
    if not os.path.exists(ruta_csv):
        print(f"❌ Error: No se encontró el archivo base en: {ruta_csv}")
        return
        
    os.makedirs(output_dir, exist_ok=True)

    # 2. CARGA Y LIMPIEZA TOTAL DEL ARCHIVO DE REOLOGÍA
    # skiprows=2 salta el espacio en blanco superior del Excel original
    df = (pd.read_csv(ruta_csv, skiprows=2, encoding='latin-1')
          .dropna(axis=1, how='all'))
    
    # Renombrado forzado para asegurar compatibilidad total
    df.columns = ['Formulacion', 'Replica', 'Densidad', 'Tiempo_flujo', 'Viscosidad']
    
    # Agrupamos las réplicas que se guardaron como F5 y F6 bajo la etiqueta correcta (F4)
    df['Formulacion'] = df['Formulacion'].replace({'F5': 'F4', 'F6': 'F4'})

    # Diccionario de variables con sus respectivas unidades
    variables = {
        'Densidad': 'g/mL', 
        'Tiempo_flujo': 's', 
        'Viscosidad': 'mPa.s'
    }

    print("\n" + "="*65)
    print("   ANÁLISIS ESTADÍSTICO DE PROPIEDADES REOLÓGICAS (ANOVA + TUKEY)")
    print("="*65)

    for var, unidad in variables.items():
        # 3. CÁLCULO ESTADÍSTICO (ANOVA de un factor)
        grupos = [g[var].values for _, g in df.groupby('Formulacion')]
        f_stat, p_valor = stats.f_oneway(*grupos)
        
        nombre_impreso = var.replace("_", " ").title()
        status = '✅' if p_valor < 0.05 else '⚠️'
        
        print(f"\n{status} {nombre_impreso.upper()}:")
        print(f"   F-valor = {f_stat:.2f}")
        print(f"   p-valor = {p_valor:.2e}")

        # 4. PRUEBA POST-HOC (TUKEY HSD)
        if p_valor < 0.05:
            print("   📊 Post-hoc Tukey HSD (Comparación Múltiple):")
            tukey = pairwise_tukeyhsd(endog=df[var], groups=df['Formulacion'], alpha=0.05)
            
            # Filtramos los datos para evaluar específicamente la similitud con el Comercial
            datos_tukey = tukey.summary().data[1:]
            for fila in datos_tukey:
                g1, g2, reject = fila[0], fila[1], fila[6]
                if (g1 == 'Comercial' and g2 == 'F4') or (g1 == 'F4' and g2 == 'Comercial'):
                    print("   --- Comparación Clave ---")
                    if not reject:
                        print(f"   ✔️ ÉXITO: NO existe diferencia significativa entre Comercial y F4.")
                    else:
                        print(f"   ❌ NOTA: Sí existe diferencia significativa entre Comercial y F4.")
        print("-" * 40)

        # 5. GENERACIÓN Y GUARDADO DE GRÁFICAS
        plt.figure(figsize=(8, 5))
        sns.set_style("whitegrid")
        
        # Mapeo explícito con 'hue' para evitar advertencias de depreciación
        sns.barplot(x='Formulacion', y=var, data=df, hue='Formulacion', 
                    palette='viridis', legend=False, errorbar='sd', capsize=.1)
        
        # Línea de control del estándar comercial
        promedio_com = df[df.Formulacion == 'Comercial'][var].mean()
        plt.axhline(promedio_com, color='red', linestyle='--', label=f'Comercial ({promedio_com:.2f})')
        
        plt.title(f'Análisis de {nombre_impreso} por Formulación')
        plt.ylabel(f'{nombre_impreso} ({unidad})')
        plt.xlabel('Muestra')
        plt.legend()
        
        # Guardado en la carpeta de resultados del repositorio
        nombre_img = f'grafica_{var.lower()}.png'
        plt.savefig(os.path.join(output_dir, nombre_img), dpi=300, bbox_inches='tight')
        plt.close()

    print(f"\n📊 Proceso completado. Gráficas exportadas con éxito a:\n   {output_dir}\n")

if __name__ == "__main__":
    analizar_reologia_repositorio()