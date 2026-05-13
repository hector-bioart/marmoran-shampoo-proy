import matplotlib.pyplot as plt

# Datos de la Tabla 2
categorias = ['Sulfatos\n(Aniónicos)', 'Betaina\n(Anfóteros)', 'Acondic.\nSintéticos', 
              'Sal\n(NaCl)', 'Ácido\nCítrico', 'Benzoato\n(Preserv.)', 
              'Coco-Glucoside\n(No iónico)', 'Goma\nXantana']
frecuencias = [95, 85, 90, 75, 100, 75, 15, 15]

plt.figure(figsize=(10, 6))
bars = plt.bar(categorias, frecuencias, color='#455a64') # Gris azulado profesional

plt.ylabel('Presencia en etiquetas (%)')
plt.ylim(0, 115)

# Etiquetas de datos
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}%', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('4.2.1_Frecuencia_Mercado.png', dpi=300)
plt.show()

