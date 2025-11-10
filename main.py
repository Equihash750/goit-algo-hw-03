from datetime import datetime
import random
import re

def get_days_from_today(date):
    """
    Обчислює кількість днів між заданою датою та поточною датою.
    """
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Задан неверный формат даты. Используйте YYYY-MM-DD"
    date_now = datetime.today()
    date_diff = date_now - date_obj
    return date_diff.days

def get_numbers_ticket(min, max, quantity):
    """
    Генерує список унікальних випадкових чисел для лотерейного квитка.
    """
    ticket_list = random.sample(range(min, max), quantity)
    return ticket_list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


def normalize_phone(phone_number):
    """
    Приводить номер телефону до формату +380XXXXXXXXX.
    Видаляє зайві символи, додає код країни якщо потрібно.
    """
    clean_numb = re.sub(r"\D", '', phone_number)
    if not clean_numb.startswith("+"):
        if clean_numb.startswith("380"):
            clean_numb = "+" + clean_numb
        else:
            clean_numb = "+38" + clean_numb
    return clean_numb

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)