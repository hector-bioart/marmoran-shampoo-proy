import matplotlib.pyplot as plt

labels = ['400 mL (Estándar)', '650-750 mL (Valor)', 'Otros (200mL / >1L)']
sizes = [40, 25, 35]
colors = ['#1565c0', '#43a047', '#b0bec5'] # Azul, Verde, Gris

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=(0.05, 0, 0)) # Resalta el de 400ml

plt.tight_layout()
plt.savefig('4.2.2_Pastel_Volumen.png', dpi=300)
plt.show()
