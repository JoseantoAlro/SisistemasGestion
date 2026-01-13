import pandas as pd
import datapane as dp

fichero_csv = "DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)

table = dp.Table(df)
data_table = dp.DataTable(df)

datos_diciembre = df[df['Mes'] == 'Diciembre']
unidades_diciembre = datos_diciembre['Unidades'].sum()

datos_noviembre = df[df['Mes'] == 'Noviembre']
unidades_noviembre = datos_noviembre['Unidades'].sum()

unidades = dp.BigNumber(
    heading='Unidades totales en diciembre',
    value=unidades_diciembre,
    change=unidades_diciembre - unidades_noviembre,
    is_upward_change=unidades_diciembre > unidades_noviembre
)

titulo = dp.HTML(
    '<p style="font-size:30px; text-align:center; color:#ffffff; background-color:#4d4d4d;">Informe de ventas</p>'
)
texto = dp.Text("**Puedes descargar el fichero con los datos del informe.**")

report = dp.Report(
    titulo,      # Ahora aparecerá el título arriba
    unidades,    # El número grande
    texto,       # El texto en negrita
    data_table   # La tabla interactiva (opcional, si quieres mostrarla)
)
report.save(path='DI_U05_A02_05.html', open=True)
