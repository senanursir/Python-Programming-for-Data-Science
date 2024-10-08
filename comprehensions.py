# COMPREHENSIONS

# LIST COMPREHENSIONS:
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 2 / 100 + x

[new_salary(salary * 2)if salary < 3000 else new_salary(salary) for salary in salaries]

print(new_salary(1000))
#


# [for salary in salaries]
# [salary * 2 for salary in salaries] # 2000, 4000, 6000, 8000, 10000
# salary
print([salary * 2 for salary in salaries if salary < 3000]) # 2000 4000
print([salary * 2  if salary < 3000 else salary * 0 for salary in salaries])  # [2000, 4000, 0, 0, 0]
print([new_salary(salary * 2)if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]) # [2040.0, 4080.0, 612.0, 816.0, 1020.0]
#


students = ["Ayse", "Sena", "Buse", "Meryem"]
students_no = ["Ayse", "Buse", ]

print([student.lower() if student in students_no else student.upper() for student in students])
# ['ayse', 'SENA', 'buse', 'MERYEM']

print([student.lower() if student not in students_no else student.upper() for student in students])
# ['AYSE', 'sena', 'BUSE', 'meryem']
#


# DICT COMPREHENSİONS:
dict = {'a': 1,
        'b': 2,
        'c': 3,
        'd': 4}

print({k: v ** 2 for (k, v) in dict.items()})   # {'a': 1, 'b': 4, 'c': 9, 'd': 16}
print({k.upper(): v for (k, v) in dict.items()})   # {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print({k.upper(): v ** 2 for (k, v) in dict.items()})   # {'A': 1, 'B': 4, 'C': 9, 'D': 16}
#


# MULAKAT SORUSU:

numbers = range(10)

#new_dict = {}

# for n in numbers:
    # if n % 2 == 0:
         # new_dict[n] = n ** 2  # sayının kendisini key bölümüne, karesini value kısmına ekliyoruz.
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# with dict comprehension:
new_dict = {n: n ** 2 for n in numbers if n % 2 == 0}
print(new_dict) # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}







