import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Загружаем данные из файла CSV
df_sales = pd.read_csv('../Продажи прогноз.csv')
# Создаем рабочий датафрейм с датами
df = pd.DataFrame({
        'dt': pd.date_range('2022-01-01', '2022-12-31'),
        'Sales': 0
    })
# Вводим фактические продажи за первые полгода
df['Sales'] = df_sales['Sales']

# Готовим данные для обучения модели
x = np.arange(181).reshape((-1, 1))
y = np.array([i for i in df['Sales']][:181])

# Создаем модель
model = LinearRegression()

# Обучение
model.fit(x, y)

# print(model.coef_)
# print(model.intercept_)
# Уравнение: y = 63775.12 + 317.37x

# Вычисляем линию тренда прошедшего периода
y_pred = model.predict(x)

# Прогноз будущего периода
# Готовим данные для прогнозирования
x_new = np.arange(181, 365).reshape((-1, 1))
# Прогнозирование
y_new = model.predict(x_new)

# Вставляем прогнозные данные в датафрейм
df.loc[181:, ['Sales']] = y_new
# Устанавливаем значения поля isPredict
df['isPredict'] = 0
df.loc[181:, ['isPredict']] = 1

# Сохраняем CSV
df.to_csv('Продажи прогноз new.csv', index=False)

print('Файл Продажи прогноз new.csv сохранен.')
