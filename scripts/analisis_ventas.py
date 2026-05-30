
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
ventas_totales = df["monto"].sum()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
      .sum()
      .idxmax()
)

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Convertir fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Ventas por mes
ventas_mes = (
    df.groupby(df["fecha"].dt.month)["monto"]
      .sum()
)

print("\nVentas por mes:")
print(ventas_mes)

# Crear gráfico
plt.figure(figsize=(8,4))
ventas_mes.plot(marker="o")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto")
plt.grid(True)

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("\nGráfico guardado en resultados/grafico_ventas.png")
