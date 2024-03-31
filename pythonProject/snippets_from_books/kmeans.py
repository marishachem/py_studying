import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sqlalchemy import create_engine
# import matplotlib.pyplot as plt
from datetime import datetime

# Создаем подключение к базе данных
engine = create_engine('postgresql://bi:bi@bi9.spb.luxms.com/mi')
con = engine.connect()

# Извлекаем данные о магазинах из базы данных
sql = 'select * from custom.shops'
# Сохраняем данные в датафрейм
df = pd.read_sql(sql, con=engine)

# Создаем массив координат для кластеризации
coords = np.array(df[['shop_lat', 'shop_lon']]).reshape((-1, 2))

# Метод локтя для определения оптимального количества кластеров
# inertia = []
# for i in range(1, 21):
#     kmeans = KMeans(i)
#     kmeans.fit(coords)
#     inertia.append(kmeans.inertia_)
# x = [i+1 for i in range(20)]
# plt.xlabel("Кластеры")
# plt.ylabel("Сумма квадратов отклонений")
# plt.xticks(x)
# plt.grid(axis = 'x')
# plt.plot(x, inertia)

# Строим модель с кластерами в количестве от 2 до 8
for i in range(2, 9):
    kmeansi = KMeans(n_clusters=i)
    kmeansi.fit(coords)
    # Устанавливаем метки в датафрейме
    df['cluster' + str(i)] = kmeansi.labels_ + 1

    # сумма квадратов внутрикластерных расстояний
    # print(kmeans1.inertia_)
    # Метки кластеров
    # print(kmeans1.labels_)

# Сохраняем датафрейм в CSV
filename = 'clusters ' + datetime.now().strftime("%m_%d_%Y %H_%M_%S") + '.csv'
df.to_csv(filename, index=False)
print('Файл ' + filename + ' создан.')
