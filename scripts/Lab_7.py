import matplotlib.pyplot as plt
import csv

x = [] # Создали пустой список для х
y = [] # Создали пустой список для у

with open('p4_data_15.csv', 'r') as csvfile: # Открыли файл p4_data_15.csv
    plots = csv.reader(csvfile, delimiter=',') # Сохранили в переменную plots все данные из файла p4_data_15.csv
    next(plots) # Пропустили первую строку с заголовоком
    for row in plots:
        x_value = row[4].replace('$', '') # Убрали знак доллара в 4 колонке
        y_value = row[5].replace('$', '') # Убрали знак доллара в 5 колонке
        x.append(float(x_value)) # Добавляем значения в список х
        y.append(float(y_value)) # Добавляем значения в список y

# Создание линейного графика
plt.figure()
plt.plot(x)
plt.xlabel('x')
plt.title('Линейный график')

# Создание столбчатой диаграммы
plt.figure()
plt.bar(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Столбчатая диаграмма')

plt.show()