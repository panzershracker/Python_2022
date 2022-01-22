"""4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы.

Например:

>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
"""

employees = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

def thesaurus_adv(names_list):
    result = {x.split(' ')[1][0]:{} for x in names_list}

    for key in result.keys():

        for name in names_list:
            name_letter = name.split(' ')[0][0]
            last_name_letter = name.split(' ')[1][0]

            if last_name_letter == key:
                if name_letter not in result[key]:
                    result[key][name_letter] = [name]
                else:
                    result[key][name_letter].append(name)


    return result

print(thesaurus_adv(employees))
"""
out:
{
    'С': {
        'И': ['Иван Сергеев', 'Инна Серова'], 
        'А': ['Анна Савельева']
    }, 
    'А': {
        'П': ['Петр Алексеев']
    },
    'И': {
        'И': ['Илья Иванов']
    }
} 
"""

"""Как поступить, если потребуется сортировка по ключам?"""

print(dict(sorted(thesaurus_adv(employees).items())))