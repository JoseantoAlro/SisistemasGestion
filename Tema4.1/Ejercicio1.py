import pandas as pd
import datapane as dp

fichero_csv = "DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)

table = dp.Table(df)
data_table = dp.DataTable(df)

titulo = dp.HTML(
    '<p style="font-size:30px; text-align:center; color:#ffffff; background-color:#4d4d4d;">Informe de ventas</p>'
)

vendedores_julio = df[(df['Mes'] == 'Julio') & (df['Unidades'] > 500)]
tabla_julio = dp.DataTable(vendedores_julio)





filtro_limite = df[df['Unidades'] <= 300] #todos los que sean inferiores a 300

indice_max_importe = filtro_limite['Importe (€)'].idxmax() #el de mayor importe de la anterior seleccion

record_ventas = filtro_limite.loc[indice_max_importe] #todos los datos de esa fila


record_ventas = dp.Group(
    dp.BigNumber(
        heading=f"Récord: {record_ventas['Nombre']} ({record_ventas['Mes']})",
        value=f"{record_ventas['Importe (€)']}€",
        label="Máximo importe con menos de 300 unidades"
    ),
    columns=1
)



nombres_s = df[(df['Nombre'].str.startswith('S')) & (df['Mes'] == 'Agosto')] #todos los vendedores de agosto que empiezan por s

max_ventas_importe = nombres_s['Importe (€)'].idxmax() #el que mas vendió

max_ventas = nombres_s.loc[max_ventas_importe]

record_ventas_agosto = dp.Group(
    dp.BigNumber(
        heading=f"Récord: {max_ventas['Nombre']} ({max_ventas['Mes']})",
        value=f"{max_ventas['Importe (€)']}€",
        label="Máximo importe con menos de 300 unidades"
    ),
    columns=1
)





report = dp.Report(
    titulo,      # Ahora aparecerá el título arriba
    tabla_julio,
    record_ventas,
    record_ventas_agosto,
    data_table   # La tabla interactiva (opcional, si quieres mostrarla)
)
report.save(path='DI_U05_A02_05.html', open=True)
