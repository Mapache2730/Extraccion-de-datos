import pandas as pd

# Carga del archivo CSV
df = pd.read_csv('CDMX.csv', encoding='latin1')

# Eliminar espacios en los nombres de las columnas
df.columns = df.columns.str.strip()

# 1. Registros de 5 "host name" diferentes
if 'host name' in df.columns:
    hostnames_diferentes = df['host name'].drop_duplicates().head(5)
    print("Hostnames diferentes:", hostnames_diferentes)
else:
    print("Columna 'host name' no encontrada")

# 2. Registros de los host que se hallan unidos a Airbnb antes del año 2019
if 'join_date' in df.columns:
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')  # Convertir a fecha y manejar errores
    registros_antes_2019 = df[df['join_date'].dt.year < 2019]
    print("Registros antes de 2019:", registros_antes_2019)
else:
    print("Columna 'join_date' no encontrada")

# 3. Registros de los host que responden a más tardar en un día
if 'response_time' in df.columns:
    respuestas_1_dia = df[df['response_time'] == 'within a day']
    print("Respuestas a más tardar en un día:", respuestas_1_dia)
else:
    print("Columna 'response_time' no encontrada")

# 4. Registros que tienen al menos 5 accommodations
if 'accommodates' in df.columns:
    registros_5_accommodates = df[df['accommodates'] >= 5]
    print("Registros con al menos 5 accommodations:", registros_5_accommodates)
else:
    print("Columna 'accommodates' no encontrada")

# 5. Registros de los tipos de cuarto "entire home" y "private room"
if 'room_type' in df.columns:
    registros_tipo_cuarto = df[df['room_type'].isin(['Entire home/apt', 'Private room'])]
    print("Registros con tipo de cuarto 'entire home' o 'private room':", registros_tipo_cuarto)
else:
    print("Columna 'room_type' no encontrada")

# 6. Registros que a lo mucho cuenten con 4 camas
if 'beds' in df.columns:
    registros_max_4_camas = df[df['beds'] <= 4]
    print("Registros con a lo mucho 4 camas:", registros_max_4_camas)
else:
    print("Columna 'beds' no encontrada")

# 7. Registros que tengan 1 baño o sean superhost, pero con la condición de que todos sean instant_bookable
if 'bathrooms' in df.columns and 'superhost' in df.columns and 'instant_bookable' in df.columns:
    registros_bano_o_superhost_instant = df[
        ((df['bathrooms'] == 1) | (df['superhost'] == True)) & (df['instant_bookable'] == True)
    ]
    print("Registros con 1 baño o superhost e instant_bookable:", registros_bano_o_superhost_instant)
else:
    print("Faltan algunas columnas: 'bathrooms', 'superhost', o 'instant_bookable'")

# 8. Registros cuyo review_score_cleanliness sea menor de 3 y review_score_rating mayor de 3
if 'review_score_cleanliness' in df.columns and 'review_score_rating' in df.columns:
    registros_reviews = df[
        (df['review_score_cleanliness'] < 3) & (df['review_score_rating'] > 3)
    ]
    print("Registros con review_score_cleanliness menor de 3 y review_score_rating mayor de 3:", registros_reviews)
else:
    print("Faltan algunas columnas: 'review_score_cleanliness' o 'review_score_rating'")
