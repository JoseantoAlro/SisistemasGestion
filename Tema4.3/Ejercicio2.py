import pandas as pd
import datapane as dp

# Cargar los datos desde el CSV
df = pd.read_csv("DI_U05_A02_PP_E_01.csv")

#titulo
titulo = dp.HTML(
    '<p style="font-size:30px; text-align:center; color:#ffffff; background-color:#4d4d4d;">Informe de ventas</p>'
)


#########    GRAFICO DE SECTORES    ##########
# Agrupar por tipo y sumar (para obtener los totales)
ventas_vendedor = df.groupby("Tipo de producto")["Ventas"].sum()

# Crear el gráfico de sectores (tarta)
grafico_matplotlib = ventas_vendedor.plot.pie(
    y="Ventas",
    legend=False,
    ylabel="",
    figsize=(3,3),
)

# Adaptar el gráfico para Datapane
grafico_sectores_datapane = dp.Plot(grafico_matplotlib)


#########    GRAFICO DE LINEAS    ##########

#años a filtrar
años_deseados = [2019, 2020, 2021]
df_filtrado = df[df["Año"].isin(años_deseados)]

# Agrupar los datos por año y sumar las ventas
ventas_anual = df_filtrado.groupby(["Año"], sort=False).sum()

# Crear el gráfico de líneas (Matplotlib a través de Pandas)
grafico_lineas_matplotlib = ventas_anual.plot(y="Ventas")

# Adaptar el gráfico para Datapane
grafico_lineas_datapane = dp.Plot(grafico_lineas_matplotlib)


#########    GRAFICO DE BARRAS    ##########

# Agrupar los datos por Region y sumar los importes
ventas_region = df.groupby('Región', as_index=True)[["Ventas"]].sum()

# Crear el gráfico de barras (Pandas usa Matplotlib internamente) 
grafico_barras_matplotlib = ventas_region.plot.bar(legend=False)

figura_barras = grafico_barras_matplotlib.get_figure()

# Adaptar el gráfico para Datapane
grafico_barras_datapane = dp.Plot(figura_barras)






# Crear el informe Datapane
reporte = dp.Report(
    titulo,
    dp.Text("# Reparto de unidades vendidas por vendedor"),
    grafico_sectores_datapane,
    dp.Text("# Ventas de los dos últimos años"),
    grafico_lineas_datapane,
    dp.Text("# Ventas por región"),
    grafico_barras_datapane
)

# Guardar y abrir el informe
reporte.save("informe_reparto_unidades.html", open=True)