import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import os
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def analizar_estabilidad_repositorio():
    # 1. RUTAS DINÁMICAS DEL REPOSITORIO
    # Detectamos dónde está este script (notebooks/...)
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Subimos dos niveles para llegar a la raíz ('marmoran-shampoo-proy')
    ruta_raiz = os.path.abspath(os.path.join(dir_actual, '../../'))
    
    # Definimos las rutas exactas hacia los datos y los resultados
    ruta_csv = os.path.join(ruta_raiz, 'data/4.4_propiedades_fisicoquimicas/resultados_estabilidad.csv')
    output_dir = os.path.join(ruta_raiz, 'results/4.4_propiedades_fisicoquimicas')

    # Aseguramos que la carpeta de resultados exista
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(ruta_csv):
        print(f"❌ Error: No se encontró el archivo en {ruta_csv}")
        return

    # 2. CARGA DE DATOS
    # Nota: Aquí ya no usamos skiprows porque el archivo empieza directo en los encabezados
    df = pd.read_csv(ruta_csv, encoding='latin-1')
    
    # Limpiamos nombres de columnas por si tienen espacios (como 'Replica ')
    df.columns = df.columns.str.strip()
    
    # Renombramos para facilitar el manejo en el código
    # Se asume el orden: Formulación, Replica, ph_inicial, ph_final
    df.columns = ['Formulacion', 'Replica', 'ph_inicial', 'ph_final']

    # 3. VARIABLES A ANALIZAR
    variables = {
        'ph_inicial': 'Unidades de pH', 
        'ph_final': 'Unidades de pH'
    }

    print("\n" + "="*65)
    print("      ANÁLISIS DE ESTABILIDAD (pH INICIAL VS FINAL)")
    print("="*65)

    for var, unidad in variables.items():
        # ANOVA
        grupos = [g[var].values for _, g in df.groupby('Formulacion')]
        f_stat, p_valor = stats.f_oneway(*grupos)
        
        print(f"\nANÁLISIS DE: {var.upper()}")
        print(f"   F-valor = {f_stat:.2f}")
        print(f"   p-valor = {p_valor:.2e}")

        # 4. POST-HOC TUKEY
        if p_valor < 0.05:
            print("   📊 Diferencias detectadas. Ejecutando Tukey HSD...")
            tukey = pairwise_tukeyhsd(endog=df[var], groups=df['Formulacion'], alpha=0.05)
            
            # Comparación específica Comercial vs F4
            datos_tukey = tukey.summary().data[1:]
            for fila in datos_tukey:
                g1, g2, reject = fila[0], fila[1], fila[6]
                if (g1 == 'Comercial' and g2 == 'F4') or (g1 == 'F4' and g2 == 'Comercial'):
                    print("   --- Comparación Crítica (Comercial vs F4) ---")
                    if not reject:
                        print(f"   ✔️ El pH de F4 es ESTADÍSTICAMENTE IGUAL al Comercial.")
                    else:
                        print(f"   ❌ El pH de F4 es DIFERENTE al Comercial.")
        else:
            print("   ⚠️ No hay diferencias significativas entre ninguna fórmula.")

        # 5. GRÁFICA
        plt.figure(figsize=(8, 5))
        sns.set_style("whitegrid")
        
        sns.barplot(x='Formulacion', y=var, data=df, hue='Formulacion', 
                    palette='magma', legend=False, errorbar='sd', capsize=.1)
        
        promedio_com = df[df.Formulacion == 'Comercial'][var].mean()
        plt.axhline(promedio_com, color='red', linestyle='--', label=f'Comercial ({promedio_com:.2f})')
        
        plt.title(f'Distribución de {var}')
        plt.ylabel(unidad)
        plt.legend()
        
        # Guardado en la carpeta de resultados correcta
        nombre_img = f'estabilidad_{var}.png'
        plt.savefig(os.path.join(output_dir, nombre_img), dpi=300, bbox_inches='tight')
        plt.close()

    print(f"\n📊 Proceso terminado. Gráficas guardadas en:\n   {output_dir}\n")

if __name__ == "__main__":
    analizar_estabilidad_repositorio()