# This is a sample Python script.

"""
Нужно получить результат вида:
(номер телефона, ip-адрес, mac)
402 10.1.20.103 0800.23e1.eaba
"""

# файл с данными АТС
ATS_INPUT_FILE = "ats_out.txt"

# файл с данными от коммутатора
SWITCH_INPUT_FILE = "switch_out.txt"

def parse_ats_out():
    """
    парсим  данный файла вывода с АТС
    :return: list - список строк
    """
    with open(ATS_INPUT_FILE) as f:
        out = f.readlines()

        # убираем переносы строк
        return [i.replace('\n', '') for i in out]


def parse_switch_out():
    with open(SWITCH_INPUT_FILE) as f:
        out = f.readlines()
        return [i.replace('\n', '') for i in out]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ats_data = parse_ats_out()
    switch_data = parse_switch_out()

    for ats_line in ats_data:
        # находим IP в списке с АТС
        ip = ats_line.split()[1]

        # теперь для каждого найденного IP ищем строку в файле данных от коммутатора
        for switch_line in switch_data:
            if ip in switch_line:
                # находим mac
                mac = switch_line.split()[1]
                print(f"{ats_line} {mac}")




