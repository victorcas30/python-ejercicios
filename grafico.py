import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Mes": ["01-2023", "02-2023", "03-2023", "04-2023", "05-2023", "06-2023", "07-2023", "08-2023", "09-2023", "10-2023", "11-2023", "12-2023"],
    "Producto": ["Producto A", "Producto B", "Producto A", "Producto C", "Producto B", "Producto A", "Producto C", "Producto A", "Producto B", "Producto A", "Producto C", "Producto B"],
    "Cantidad Vendida": [100, 120, 90, 80, 110, 95, 75, 105, 125, 85, 70, 115],
    "Precio Unitario": [10.5, 12.0, 11.0, 9.5, 11.5, 10.0, 9.0, 10.0, 12.5, 10.0, 8.5, 11.0]
}

df = pd.DataFrame(data)

# Calcular el total vendido (cantidad * precio unitario)
df['Total Vendido'] = df['Cantidad Vendida'] * df['Precio Unitario']

# Convertir el campo "Mes" a tipo datetime
df['Mes'] = pd.to_datetime(df['Mes'], format='%m-%Y')

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Crear un gráfico de línea para mostrar la tendencia del total vendido
ax.plot(df['Mes'], df['Total Vendido'], marker='o', label='Total Vendido')

# Agregar etiquetas en cada punto del total vendido
for i, total in enumerate(df['Total Vendido']):
    ax.text(df['Mes'][i], total, f'{total:.2f}', ha='left', va='bottom')

# Configurar etiquetas y título del gráfico
ax.set_xlabel('Mes')
ax.set_ylabel('Total Vendido')
ax.set_title('Tendencia del Total Vendido Mensual')

# Ordenar el DataFrame por el campo "Mes"
df = df.sort_values('Mes')

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45)

# Mostrar una leyenda en el gráfico
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
