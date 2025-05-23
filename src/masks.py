def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""

    if len(card_number) == 16 and card_number.isdigit():
        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'
    return 'Неправильный номер карты'


def get_mask_account(account: str) -> str:
    """Функция скрывающая полный номер счета"""

    if len(account) == 20 and account.isdigit():
        return f'**{account[-4:]}'
    return 'Неправильный номер счета'


def div(a, b):
    return a / b


print(get_mask_card_number("1234567812345678"))  # Должно вернуть замаскированный номер и записать в лог
print(get_mask_card_number("12345"))              # Должно вызвать исключение и записать в лог
print(get_mask_card_number("12345678123456AB"))   # Должно вызвать исключение и записать в лог
