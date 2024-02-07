import pandas as pd

# Зчитування даних з Data.csv
df = pd.read_csv('Data.csv')

# Функції для обробки ціни та виділення числового значення, розбиття на місто та район
def extract_price(price):
    if 'грн.' in price:
        return int(''.join(filter(str.isdigit, price)))
    else:
        return None

def split_city_district(city):
    city_parts = city.split(', ')
    if len(city_parts) == 2:
        return city_parts[0], city_parts[1]
    else:
        return city_parts[0], None

# Застосування функцій до відповідних стовпців
df['Ціна'] = df['Ціна'].apply(extract_price)
df[['Місто', 'Район']] = df['Місто'].apply(split_city_district).apply(pd.Series)

# Запис результату в новий документ Data2.csv
df.to_csv('Data2.csv', index=False)