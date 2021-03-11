# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей,
где ключи - взяты из первого списка, а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('R1', '12.4(24)T1', 'Cisco 3825'),
 ('R2', '15.2(2)T1', 'Cisco 2911')]

Функция должна вернуть такой список со словарями:
[{'hostname': 'R1', 'ios': '12.4(24)T1', 'platform': 'Cisco 3825'},
 {'hostname': 'R2', 'ios': '15.2(2)T1', 'platform': 'Cisco 2911'}]

Функция не должна быть привязана к конкретным данным или количеству
заголовков/данных в кортежах.

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - список data

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint
import re

headers = ["interface", "address", "status", "protocol"]

parsed_sh_ip_int_br = [
    ("FastEthernet0/0", "15.0.15.1", "up", "up"),
    ("FastEthernet0/1", "10.0.12.1", "up", "up"),
    ("FastEthernet0/2", "10.0.13.1", "up", "up"),
    ("FastEthernet0/3", "unassigned", "administratively down", "down"),
    ("Loopback0", "10.1.1.1", "up", "up"),
    ("Loopback100", "100.0.0.1", "up", "up"),
]


def convert_to_dict(list_keys, list_values):
    """
    Функция ожидает два аргумента:
    * list_keys - список с названиями полей
    * list_values - список кортежей со значениями

    Функция возвращает результат в виде списка словарей,
    где ключи - взяты из первого списка, а значения подставлены из второго.
    """
    result = []

    for data_list in list_values:
        dict_data = dict(zip(list_keys, data_list))

    return result


if __name__ == "__main__":
    print(convert_to_dict(headers, parsed_sh_ip_int_br))
