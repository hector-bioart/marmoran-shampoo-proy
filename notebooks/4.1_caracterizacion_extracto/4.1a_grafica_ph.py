import matplotlib.pyplot as plt

# Datos de la Tabla 5 - Parámetro: pH
labels = ['Extracto Agave marmorata']
ph_promedio = [4.03]
error_ph = [0.150] # Desviación estándar

plt.figure(figsize=(6, 8))
# Creamos la barra con el error
plt.bar(labels, ph_promedio, yerr=error_ph, capsize=10, color='#8eb382', edgecolor='#2d5a27', alpha=0.8)

# Configuración estética
plt.ylabel('Potencial de Hidrógeno (pH)', fontsize=12)
plt.ylim(0, 7) # Rango de pH para notar la acidez
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Añadir el valor exacto sobre la barra
for i, v in enumerate(ph_promedio):
    plt.text(i, v + 0.3, f'pH: {v}', ha='center', fontweight='bold')

plt.show()
