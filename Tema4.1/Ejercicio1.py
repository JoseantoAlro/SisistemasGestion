import pandas as pd
import datapane as dp

fichero_csv = "DI_U05_A02_PP_E_01.csv"
df = pd.read_csv(fichero_csv)

table = dp.Table(df)
data_table = dp.DataTable(df)

imagen = dp.Media(file='icono.jpg')

titulo = dp.HTML(
    '<p style="font-size:30px; text-align:center; color:#ffffff; background-color:#4d4d4d;">Informe de ventas</p>'
)

ventas_totales = df['Ventas'].sum()

ventas_anuales = df.groupby('Año')['Ventas'].sum().reset_index()
maximo_ventas = ventas_anuales['Ventas'].idxmax()
mejor_año = ventas_anuales.loc[maximo_ventas, 'Año']
valor_mejor_año = ventas_anuales.loc[maximo_ventas, 'Ventas']


total_ventas_final = dp.BigNumber(
    heading='Ventas totales',
    value= int(ventas_totales),

)

mejor_año_final =dp.BigNumber(
    heading='Año con msa ventas',
    value=int(mejor_año),
)

texto_descriptivo = dp.Text(
    "> **Justificación para la directiva:** Estos valores permiten evaluar el crecimiento histórico de la empresa "
    "además de identificar el año de mayor rendimiento, lo cual es crucial para aprender del mejor momento que se ha experimentado."
)

db21 = df[df['Año']==2021]
ventas21 = db21['Ventas'].sum()

db20 = df[df['Año']==2020]
ventas20 = db20['Ventas'].sum()


cambio_anual = dp.BigNumber(
    heading='Ventas en 2021',
    value=ventas21,
    change=ventas21 - ventas20,
    is_upward_change=ventas21 > ventas20
)

report = dp.Report(
    imagen,
    titulo,
    total_ventas_final,
    mejor_año_final,  
    texto_descriptivo, 
    cambio_anual,
    data_table   
)
report.save(path='DI_U05_A02_05.html', open=True)
