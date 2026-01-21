import pandas as pd
import datapane as dp

# Cargar los datos desde el CSV
df = pd.read_csv("DI_U05_A02_PP_E_01.csv")



#########    bid numbers comparando un año con el anterior    ##########

## sumatorio
db21 = df[df['Año']==2021]
ventas21 = db21['Ventas'].sum()

db20 = df[df['Año']==2020]
ventas20 = db20['Ventas'].sum()

db19 = df[df['Año']==2019]
ventas19 = db19['Ventas'].sum()

db18 = df[df['Año']==2018]
ventas18 = db18['Ventas'].sum()

db17 = df[df['Año']==2017]
ventas17 = db17['Ventas'].sum()


## vistas
cambio_anual20_21 = dp.BigNumber(
    heading='Ventas en 2021',
    value=ventas21,
    change=ventas21 - ventas20,
    is_upward_change=ventas21 > ventas20
)
cambio_anual19_20 = dp.BigNumber(
    heading='Ventas en 2020',
    value=ventas20,
    change=ventas20 - ventas19,
    is_upward_change=ventas20 > ventas19
)
cambio_anual18_19 = dp.BigNumber(
    heading='Ventas en 2019',
    value=ventas19,
    change=ventas19 - ventas18,
    is_upward_change=ventas19 > ventas18
)
cambio_anual17_18 = dp.BigNumber(
    heading='Ventas en 2018',
    value=ventas18,
    change=ventas18 - ventas17,
    is_upward_change=ventas18 > ventas17
)

componente1 = cambio_anual20_21
componente2 = cambio_anual19_20
componente3 = cambio_anual18_19
componente4 = cambio_anual17_18




#########    GRAFICO DE LINEAS    ##########

#años a filtrar
años_deseados = [2019, 2020, 2021]
df_filtrado = df[df["Año"].isin(años_deseados)]

# Agrupar los datos por año y sumar las ventas
ventas_anual = df_filtrado.groupby(["Año"], sort=False).sum(numeric_only=True)

# Crear el gráfico de líneas (Matplotlib a través de Pandas)
grafico_lineas_matplotlib = ventas_anual.plot(y="Ventas")

# Adaptar el gráfico para Datapane

componente5 = dp.Plot(grafico_lineas_matplotlib)


#########    GRAFICO DE BARRAS    ##########

# Agrupar los datos por Region y sumar los importes
ventas_region = df.groupby('Región', as_index=True)[["Ventas"]].sum(numeric_only=True)

# Crear el gráfico de barras (Pandas usa Matplotlib internamente) 
grafico_barras_matplotlib = ventas_region.plot.bar(legend=False)

figura_barras = grafico_barras_matplotlib.get_figure()

# Adaptar el gráfico para Datapane
componente7 = dp.Plot(figura_barras)



##grupos
componente_grupos =dp.Group(
    componente1, componente2, componente3, componente4,
    columns=2
)

## submenu selcet dentro de una pagina
select = dp.Select(blocks=[componente5, componente7, componente_grupos])

##paginas agrupando los anteriores elementos
paginas= dp.Report(
    dp.Page(
        title="Página 1",
        blocks=[componente_grupos]
    ),
    dp.Page(
        title="Página 2",
        blocks=[componente5]
    ),
    dp.Page(
        title="Página 3",
        blocks=[select]
    )
)


paginas.save(path='Álvarez_JoseAntonio.html', open=True)
