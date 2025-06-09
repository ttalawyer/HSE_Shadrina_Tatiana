# -*- coding: utf-8 -*-
import json
import csv

# Шаг 1: Читаем значения из filter.txt
with open('traders.txt', 'r', encoding='utf-8') as f:
    filter_values = set(line.strip() for line in f if line.strip())

# Шаг 2: Загружаем JSON-данные
with open('traders.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Шаг 3: Фильтруем JSON по полю 'inn'
filtered_data = []

for item in data:
    if item.get('inn') in filter_values:
        filtered_data.append({
            "inn":item.get('inn'),
            "ogrn":item.get('ogrn'),
            "address":item.get('address')
        })

# Шаг 4: Сохраняем результат в CSV
with open('traders.csv', 'w', newline='', encoding='utf-8') as f:
    if filtered_data:
        fieldnames = filtered_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)
    else:
        print("Нет совпадающих записей.")
