import matplotlib.pyplot as plt
import numpy as np

# Datos
parametros = ['SDT (ppm)', 'Conductividad (mS/cm)']
valores = [1410, 1916.97]
errores = [163.97, 83.72]

x_pos = np.arange(len(parametros))

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(x_pos, valores, yerr=errores, align='center', alpha=0.7, color=['#4da6ff', '#ffcc00'], capsize=8)

ax.set_ylabel('Magnitud de Medición')
ax.set_xticks(x_pos)
ax.set_xticklabels(parametros)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
