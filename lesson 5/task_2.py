# -*- coding: utf-8 -*-
import json
import re
from collections import defaultdict
from typing import List  # Для Python версий < 3.9

def extract_emails(text: str) -> List[str]:
    """
    Извлекает email-адреса из переданного текста.

    :param text: Строка, в которой нужно искать email-адреса.
    :return: Список найденных email-адресов (в нижнем регистре), либо пустой список.
    """
    # Регулярное выражение для поиска email-адресов
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    # Поиск всех совпадений
    emails = re.findall(email_pattern, text)

    # Приведение к нижнему регистру и удаление дубликатов
    return sorted(set(email.lower() for email in emails))

# Словарь для хранения email-адресов по ИНН
emails_by_inn = defaultdict(set)

# Загрузка данных из JSON-файла
with open('1000_efrsb_messages.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

emails_by_inn = {}

# Обработка каждой записи
for item in data:
    inn = item.get('publisher_inn')
    msg_text = item.get('msg_text', '')

    if inn and msg_text:
        emails_by_inn[inn] = extract_emails(msg_text)

# Сохранение результата в JSON-файл
with open('emails.json', 'w', encoding='utf-8') as f:
    json.dump(emails_by_inn, f, ensure_ascii=False, indent=2)
