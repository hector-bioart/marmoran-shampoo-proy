import matplotlib.pyplot as plt
import numpy as np

# Datos comparativos
categorias = ['Sulfatos', 'Sal (NaCl)', 'Acondic. Sintéticos', 'Coco-Glucoside', 'Goma Xantana']
mercado = [95, 75, 90, 15, 15]
f_maguey = [0, 0, 0, 100, 100]

x = np.arange(len(categorias))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, mercado, width, label='Mercado Comercial', color='#90a4ae')
ax.bar(x + width/2, f_maguey, width, label='Formulación F (Maguey)', color='#2e7d32')

ax.set_ylabel('Frecuencia (%)')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
ax.set_ylim(0, 125)

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('4.2.2_Comparativa_F4.png', dpi=300)
plt.show()

