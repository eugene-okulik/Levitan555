# lesson_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# lesson_2
result_1 = 'результат операции: 42'
one_num = int(result_1[19:])
print(one_num + 10)

result_2 = 'результат операции: 514'
two_num = int(result_2[19:])
print(two_num + 10)

result_3 = 'результат работы программы: 9'
three_num = int(result_3[27:])
print(three_num + 10)

# lesson_3
students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)
print('Students', students, 'study these subjects:', subjects)
