import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_student = "INSERT INTO students(name, second_name) VALUE(%s, %s)"
cursor.execute(insert_student, ('Сергей', 'Popov'))
id_student = cursor.lastrowid
print(id_student)

insert_books = '''INSERT INTO books(title, taken_by_student_id)
VALUES
    (%s, %s),
    (%s, %s),
    (%s, %s),
    (%s, %s)'''
books = ('White Book', id_student, 'Black Book', id_student, 'Green Book', id_student, 'Red Book', id_student)
cursor.execute(insert_books, books)

cursor.execute('SELECT id FROM books WHERE taken_by_student_id = %s', (id_student,))
id_books = [row['id'] for row in cursor.fetchall()]
print(id_books)

insert_group = "INSERT INTO `groups`(title, start_date, end_date) VALUES(%s, %s, %s)"
cursor.execute(insert_group, ('Первая', '12-2024', '12-2025'))
id_group = cursor.lastrowid
print(id_group)

student_in_group = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(student_in_group, (id_group, id_student))

insert_subjets = 'INSERT INTO subjets(title) VALUES(%s)'
subjets = ['Математика', 'Биология', 'Физика', 'История']
id_subjets = []

for title in subjets:
    cursor.execute(insert_subjets, (title,))
    id_subjets.append(cursor.lastrowid)
print(id_subjets)

insert_lessons = '''INSERT INTO lessons(title, subject_id)
VALUES(%s, %s)'''

lessons = [
    ('lesson_1', id_subjets[0]), ('lesson_2', id_subjets[0]),
    ('lesson_3', id_subjets[1]), ('lesson_4', id_subjets[1]),
    ('lesson_5', id_subjets[2]), ('lesson_6', id_subjets[2]),
    ('lesson_7', id_subjets[3]), ('lesson_8', id_subjets[3])
]

id_lessons = []
for title in lessons:
    cursor.execute(insert_lessons, title)
    id_lessons.append(cursor.lastrowid)
print(id_lessons)

insert_marks = '''INSERT INTO marks(value, lesson_id, student_id)
VALUES (%s, %s, %s)'''

marks = [
    (3, id_lessons[7], id_student), (4, id_lessons[6], id_student),
    (4, id_lessons[5], id_student), (5, id_lessons[4], id_student),
    (2, id_lessons[3], id_student), (3, id_lessons[2], id_student),
    (4, id_lessons[1], id_student), (1, id_lessons[0], id_student)
]
id_marks = []
for mark in marks:
    cursor.execute(insert_marks, mark)
    id_marks.append(cursor.lastrowid)
print(id_marks)

cursor.execute('''
SELECT m.student_id FROM marks m
JOIN students s ON
m.student_id = s.id
WHERE s.id = %s LIMIT 1''', (id_student,))
student_id_marks = cursor.fetchone()
print(student_id_marks['student_id'])

# 1. Все оценки студента
cursor.execute("SELECT value FROM marks WHERE student_id = %s", (id_student,))
print(cursor.fetchall())

# 2. Все книги, которые находятся у студента
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (id_student,))
print(cursor.fetchall())
#
# 3. Для вашего студента выведите всё
select_all = '''SELECT * FROM students s
JOIN marks m ON
m.student_id = s.id
JOIN `groups` g ON
s.group_id = g.id
JOIN books b ON
b.taken_by_student_id = s.id
JOIN lessons l ON
m.lesson_id = l.id
JOIN subjets sub ON
l.subject_id = sub.id
WHERE s.id = %s'''
cursor.execute(select_all, (id_student,))
print(cursor.fetchall())
db.commit()

db.close()
