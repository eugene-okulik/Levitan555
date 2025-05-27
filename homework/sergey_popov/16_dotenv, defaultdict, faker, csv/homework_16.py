import mysql.connector as mysql
import csv
import os
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
ev_file_path = os.path.join(file_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with (open(ev_file_path, newline='') as csv_file):
    file_data_csv = csv.reader(csv_file)
    data = []
    for row in file_data_csv:
        data.append(row)

data_tup = [tuple(item) for item in data]

data_in_db = '''
SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title,
    sub.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
    FROM students s
JOIN marks m ON
m.student_id = s.id
JOIN `groups` g ON
s.group_id = g.id
JOIN books b ON
b.taken_by_student_id = s.id
JOIN lessons l ON
m.lesson_id = l.id
JOIN subjets sub ON
l.subject_id = sub.id'''
cursor.execute(data_in_db)
list(cursor.fetchall())

csv_set = set(row for row in data_tup)
db_set = set(tuple(row) for row in data_in_db)
print(csv_set - db_set)
