import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos ficticios
data = {
    "Trimestre": ["T1-2023", "T1-2023", "T1-2023", "T2-2023", "T2-2023", "T2-2023", "T3-2023", "T3-2023", "T3-2023", "T4-2023", "T4-2023", "T4-2023"],
    "Producto": ["Producto A", "Producto B", "Producto C", "Producto A", "Producto B", "Producto C", "Producto A", "Producto B", "Producto C", "Producto A", "Producto B", "Producto C"],
    "Cantidad Vendida": [100, 120, 90, 80, 110, 95, 75, 105, 125, 85, 70, 115],
    "Precio Unitario": [10.5, 12.0, 11.0, 9.5, 11.5, 10.0, 9.0, 10.0, 12.5, 10.0, 8.5, 11.0]
}

df = pd.DataFrame(data)

df['Total Vendido'] = df['Cantidad Vendida'] * df['Precio Unitario']

# 1. Calcular el total de ventas para cada trimestre del año.
df['Total Vendido'] = df['Cantidad Vendida'] * df['Precio Unitario']
ventas_por_trimestre = df.groupby('Trimestre')['Total Vendido'].sum().reset_index()
print("Total de Ventas por Trimestre:")
print(ventas_por_trimestre)

# 2. Identificar los productos más vendidos en términos de cantidad y en términos de ingresos generados en cada trimestre.
productos_mas_vendidos = df.groupby(['Trimestre', 'Producto'])[['Cantidad Vendida', 'Total Vendido']].max().reset_index()
print("\nProductos Más Vendidos en Cantidad y Total de Ventas:")
print(productos_mas_vendidos)

# 3. Realizar un análisis de tendencia para visualizar cómo las ventas totales han evolucionado a lo largo del año.
# Crear un gráfico de línea para mostrar la tendencia de ventas trimestrales
plt.figure(figsize=(10, 6))
plt.plot(ventas_por_trimestre['Trimestre'], ventas_por_trimestre['Total Vendido'], marker='o')
plt.title('Tendencia de Ventas Trimestrales')
plt.xlabel('Trimestre')
plt.ylabel('Total Vendido')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Calcular la media, mediana y desviación estándar de los precios unitarios de todos los productos vendidos en cada trimestre.
estadisticas_precio_unitario = df.groupby('Trimestre')['Precio Unitario'].agg(['mean', 'median', 'std']).reset_index()
print("\nEstadísticas de Precios Unitarios por Trimestre:")
print(estadisticas_precio_unitario)

# 5. Encontrar el trimestre con el mayor ingreso total y el trimestre con el menor ingreso total.
trimestre_mayor_ingreso = ventas_por_trimestre.loc[ventas_por_trimestre['Total Vendido'].idxmax()]
trimestre_menor_ingreso = ventas_por_trimestre.loc[ventas_por_trimestre['Total Vendido'].idxmin()]
print("\nTrimestre con Mayor Ingreso Total:")
print(trimestre_mayor_ingreso)
print("\nTrimestre con Menor Ingreso Total:")
print(trimestre_menor_ingreso)