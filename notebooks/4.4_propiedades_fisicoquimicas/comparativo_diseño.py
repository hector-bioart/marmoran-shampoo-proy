import matplotlib.pyplot as plt
import numpy as np

# 1. Datos
labels = ['F1', 'F4', 'Champú Comercial']
alturas = [0.433, 0.600, 0.500]
tiempos = [31.00, 33.33, 35.33]

x = np.arange(len(labels))
w = 0.35 # Ancho de barras

fig, ax1 = plt.subplots(figsize=(9, 5))
ax2 = ax1.twinx() # Segundo eje Y

# 2. Creación de barras
b1 = ax1.bar(x - w/2, alturas, w, label='Altura Inicial (cm)', color='#5dade2')
b2 = ax2.bar(x + w/2, tiempos, w, label='Tiempo de Colapso (min)', color='#58d68d')

# 3. Etiquetas sobre las barras (Mucho más limpio)
ax1.bar_label(b1, fmt='%.2f', padding=3)
ax2.bar_label(b2, fmt='%.1f', padding=3)

# 4. Configuración visual
ax1.set_xticks(x, labels)
ax1.set_ylabel('Altura de Espuma (cm)', color='#5dade2')
ax2.set_ylabel('Tiempo de Colapso (min)', color='#58d68d')
ax1.set_ylim(0, 0.8)
ax2.set_ylim(0, 45)

# 5. Título (no se le pone titulo) y leyenda
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.88)) # Leyenda unificada

plt.tight_layout()
plt.show()