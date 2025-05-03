# lesson_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# lesson_2
result = 'результат операции: 514'
num = result.split(':')
print(int(num[1]) + 10)

# lesson_3
students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)
print('Students', students, 'study these subjects:', subjects)
