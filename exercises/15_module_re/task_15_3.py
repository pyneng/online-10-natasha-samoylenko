# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint

def convert_ios_nat_to_asa(file_in_ios_nat, file_out_nat_asa):
#def convert_ios_nat_to_asa(file_in_ios_nat):
    template_nat_asa = [
    "object network LOCAL_",
    " host",
    " nat (inside,outside) static interface service tcp"
    ]

    regex = (
        r"\w+ \w+ \w+ \w+ \w+ \w+ " # ip nat inside source static tcp
        r"(?P<ip>[\d.]+) " # IP-Address
        r"(?P<tcp_src>\d+) " # tcp source
        r"interface \S+\d+ " # interface
        r"(?P<tcp_dst>\d+)" # tcp destination
    )

    with open(file_in_nat_ios) as src, open(file_out_nat_asa, "w") as dest:
    #with open(file_in_ios_nat) as src:
        result = []
        for line in src:
            match = re.finditer(regex, line)
            for m in match:
                print(m.group())
                ip_src = m.group("ip")
                tcp_src = m.group("tcp_src")
                tcp_dst = m.group("tcp_dst")
            for command in template_nat_asa:
                if "LOCAL_" in command:
                    result.append(f"{command}{ip_src}")
                elif "host" in command:
                    result.append(f"{command} {ip_src}")
                elif "service tcp" in command:
                    result.append(f"{command} {tcp_src} {tcp_dst}")
        result = "\n".join(str(i) for i in result)
        dest.write(result)

    return result

if __name__ == "__main__":
    output = convert_ios_nat_to_asa("cisco_nat_config.txt", "convert_ios_nat_to_asa.txt")
    pprint(output)
