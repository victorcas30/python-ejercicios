import pandas as pd
import matplotlib.pyplot as plt

#pip pandas
#pip install matplotlib

data = {
    "Mes": ["01-2023", "02-2023", "03-2023", "04-2023", "05-2023", "06-2023", "07-2023", "08-2023", "09-2023", "10-2023", "11-2023", "12-2023"],
    "Producto": ["Producto A", "Producto B", "Producto A", "Producto C", "Producto B", "Producto A", "Producto C", "Producto A", "Producto B", "Producto A", "Producto C", "Producto B"],
    "Cantidad Vendida": [100, 120, 90, 0, 110, 95, 75, 105, 500, 85, 20, 115],
    "Precio Unitario": [10.5, 12.0, 11.0, 9.5, 11.5, 10.0, 9.0, 10.0, 12.5, 10.0, 8.5, 11.0],
    "Valor Total": [1050.0, 1440.0, 990.0, 0.0, 1265.0, 950.0, 675.0, 1050.0, 6250.0, 850.0, 220.0, 1265.0],
}

df = pd.DataFrame(data)

# 1. Calcular el total de ventas (ingresos totales) para cada mes del año
df['Mes'] = pd.to_datetime(df['Mes'], format='%m-%Y')
df['Ingresos'] = df['Cantidad Vendida'] * df['Precio Unitario']
ventas_mensuales = df.groupby(df['Mes'].dt.strftime('%B-%Y'))['Ingresos'].sum().reset_index()

# 2. Identificar los productos más vendidos en cantidad e ingresos
productos_mas_vendidos_cantidad = df.groupby('Producto')['Cantidad Vendida'].sum().idxmax()
productos_mas_vendidos_ingresos = df.groupby('Producto')['Ingresos'].sum().idxmax()

# 3. Realizar un análisis de tendencia
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

# 4. Calcular media, mediana y desviación estándar de precios unitarios
media_precio = df['Precio Unitario'].mean()
mediana_precio = df['Precio Unitario'].median()
desviacion_precio = df['Precio Unitario'].std()

# 5. Encontrar el mes con el mayor ingreso total y el mes con el menor ingreso total
mes_max_ingreso = ventas_mensuales.loc[ventas_mensuales['Ingresos'].idxmax()]['Mes']
mes_min_ingreso = ventas_mensuales.loc[ventas_mensuales['Ingresos'].idxmin()]['Mes']

print("1. Total de Ventas Mensuales:")
print(ventas_mensuales)

print("\n2. Producto más vendido en cantidad:", productos_mas_vendidos_cantidad)
print("   Producto más vendido en ingresos:", productos_mas_vendidos_ingresos)

print("\n4. Estadísticas de Precios Unitarios:")
print("   Media:", media_precio)
print("   Mediana:", mediana_precio)
print("   Desviación Estándar:", desviacion_precio)

print("\n5. Mes con Mayor Ingreso Total:", mes_max_ingreso)
print("   Mes con Menor Ingreso Total:", mes_min_ingreso)

# Mostrar el gráfico
plt.show()