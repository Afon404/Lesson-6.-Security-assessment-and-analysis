import nmap

# Создаем объект nmap.PortScanner
nm = nmap.PortScanner()

# Сканируем хост 127.0.0.1 на порты с 22 по 443
nm.scan('127.0.0.1', '22-443')

# Выводим команду, которую использовали для сканирования
print(f"Команда nmap: {nm.command_line()}")

# Выводим информацию о сканировании
print(f"Информация о сканировании: {nm.scaninfo()}")

# Получаем список всех обнаруженных хостов
hosts = nm.all_hosts()
for host in hosts:
    print(f"----------------------------------------------------")
    print(f"Хост: {host} ({nm[host].hostname()})")
    print(f"Состояние: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        print(f"----------")
        print(f"Протокол: {proto}")
        ports = nm[host][proto].keys()
        ports.sort()
        for port in ports:
            print(f"Порт: {port}\tСостояние: {nm[host][proto][port]['state']}")

# Экспортируем результаты в CSV-файл
print(nm.csv())
