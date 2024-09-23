import pandas as pd

# Cargar el dataset desde la URL
url = "https://raw.githubusercontent.com/jumafernandez/clasificacion_correos/main/tesis/data/02-01-correos-train-80.csv"
# url = "https://raw.githubusercontent.com/jumafernandez/clasificacion_correos/main/tesis/data/02-02-correos-test-20.csv"
df = pd.read_csv(url)

# Seleccionar solo las columnas 'consulta' y 'clase'
df_filtered = df[['consulta', 'clase']]

# Guardar el DataFrame filtrado en un nuevo archivo CSV
df_filtered.to_csv('data-test.csv', index=False)
