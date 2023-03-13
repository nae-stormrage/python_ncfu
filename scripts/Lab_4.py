F = open("p4_data_15.csv")
header = F.readline().strip().split(',')

all_clients = []

print('-' * 20)
n_to_print = 10
summa_minus = 0
max_balance = 0
total_plus = 0
count_plus = 0
avg_plus = 0
summa_nalog_minus = 0

for line in F:
    data = line.strip().split(',')
    client = {}
    for i, key in enumerate(header):
        client[key] = data[i]

    client['Minus'] = float(client['Minus'][1:])
    client['Plus'] = float(client['Plus'][1:])
    client['Tax'] = float(client['Tax'][1:])
    all_clients.append(client)

    #Задание №1 - Суммарный расход по счетам клиентов, с пустым полем "email"
    if client['email'] == '': #Условие для поиска клиентов без email
        summa_minus += client['Minus'] #прибавление к переменной summa_minus число стоящее в поле "Minus", если условие было соблюдено.

    client['Minus'] = float(client['Minus'])
    client['Plus'] = float(client['Plus'])
    client['Tax'] = float(client['Tax'])

    #Задание №2 - Поиск клиента с самым большим балансом после уплаты налогов
    balance = client['Plus'] - client['Minus'] - client['Tax']
    max_balance = max(max_balance, balance)

    #Задание №3 - Поиск среднего дохода людей с положительным балансом
    if balance > 0:
        total_plus += client['Plus']
        count_plus += 1
        avg_plus = total_plus / count_plus

    #Задание №4 - Поиск суммы налогов людей с отрицательным балансом
    if balance < 0:
        summa_nalog_minus += client['Tax']


print('Задание №1 - Сумма всех расходов людей без email: ', summa_minus)
print('Задание №2 - Человек с максимальным балансом после вычета налога: ', client['LastName'] + ' ' + client['FirstName'], max_balance)
print('Задание №3 - Средний доход всех людей с положительным балансом:', avg_plus)
print('Задание №4 - Сумма налогов всех людей с отрицательным балансом', summa_nalog_minus)

