# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip_addresses(ip_addresses):
    ping = []
    notping = []
    for ip in ip_addresses:
        check = subprocess.run(f"ping {ip}")
        if check.returncode == 0:
            ping.append(ip)
        else:
            notping.append(ip)
            
    return (ping, notping)

if __name__ == "__main__":
    data = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    result = ping_ip_addresses(data)
    print(result)

