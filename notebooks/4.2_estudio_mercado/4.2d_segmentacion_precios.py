import matplotlib.pyplot as plt

# Etiquetas con el signo de pesos escapado para evitar errores de formato
labels = ['Menores a \$100', '\$100 a \$200', 'Mayores a \$200']
sizes = [20, 60, 20]
colors = ['#ffe0b2', '#fb8c00', '#e65100'] # Escala de naranjas

plt.figure(figsize=(7, 7))

# El parámetro autopct coloca el porcentaje, las etiquetas (labels) llevan los signos $
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=(0, 0.1, 0), shadow=True,
        textprops={'fontsize': 12})

plt.tight_layout()
plt.savefig('4.2.2_Pastel_Precios_Corregido.png', dpi=300)
plt.show()

