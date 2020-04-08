import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
for contact in contacts_list:
    pattern_1 = re.compile(r"(\+7|8)?\s*(\(|)(\d+)(\)|)\s*(\d+)[\s-]?(\d+)?[\s-]?(\d+)( |)(\(|)(доб\.)?( |)(\d+)?(\))?")
    replacer_1 = r"\3\5\6\7 \10\12"
    version_1 = pattern_1.sub(replacer_1, contact[5])
    pattern_2 = re.compile(r"(\d{3})(\d{3})(\d{2})(\d{2})( доб.\d{4})?( )?")
    replacer_2 = r"+7(\1)\2-\3-\4\5"
    result = pattern_2.sub(replacer_2, version_1)
    contact[5] = result
    # print(contact[5])

for contact in contacts_list:
    split_string = re.split(r" ", contact[0])
    if len(split_string) == 2:
        contact[0] = split_string[0]
        contact[1] = split_string[1]
    if len(split_string) == 3:
        contact[0] = split_string[0]
        contact[1] = split_string[1]
        contact[2] = split_string[2]

    split_string_2 = re.split(r" ", contact[1])
    if len(split_string_2) == 2:
        contact[1] = split_string_2[0]
        contact[2] = split_string_2[1]

contacts_list_final = []


def make_contacts_great_again():
    contacts_list.sort()
    number = 0
    for contact in contacts_list:
        if number == 0:
            number += 1
        if number > 0:
            if contact[0] == contacts_list[number - 1][0] and contact[1] == contacts_list[number - 1][1]:
                if len(contact[2]) <= len(contacts_list[number - 1][2]):
                    contact[2] = contacts_list[number - 1][2]

                if len(contact[3]) <= len(contacts_list[number - 1][3]):
                    contact[3] = contacts_list[number - 1][3]

                if len(contact[4]) <= len(contacts_list[number - 1][4]):
                    contact[4] = contacts_list[number - 1][4]

                if len(contact[5]) <= len(contacts_list[number - 1][5]):
                    contact[5] = contacts_list[number - 1][5]

                if len(contact[6]) <= len(contacts_list[number - 1][6]):
                    contact[6] = contacts_list[number - 1][6]

                del contacts_list[number - 1]
                number -= 1
            else:
                number += 1


make_contacts_great_again()
print(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
