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

cursor.execute('SELECT id FROM books ORDER BY id DESC LIMIT 4')
id_books = cursor.fetchall()
print(id_books)

insert_group = "INSERT INTO `groups`(title, start_date, end_date) VALUES(%s, %s, %s)"
cursor.execute(insert_group, ('Первая', '12-2024', '12-2025'))
id_group = cursor.lastrowid

student_in_group = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(student_in_group, (id_group, id_student))

insert_subjets = 'INSERT INTO subjets(title) VALUES(%s), (%s), (%s), (%s)'
subjets = ('Математика', 'Биология', 'Физика', 'История')
cursor.execute(insert_subjets, subjets)

cursor.execute('SELECT id FROM subjets ORDER BY id DESC LIMIT 4')
id_subjets = cursor.fetchall()
print(id_subjets)

insert_lessons = '''INSERT INTO lessons(title, subject_id)
VALUES(%s, %s)'''

lessons = [
    ('lesson_1', id_subjets[3]['id']), ('lesson_2', id_subjets[3]['id']),
    ('lesson_3', id_subjets[2]['id']), ('lesson_4', id_subjets[2]['id']),
    ('lesson_5', id_subjets[1]['id']), ('lesson_6', id_subjets[1]['id']),
    ('lesson_7', id_subjets[0]['id']), ('lesson_8', id_subjets[0]['id'])
]
cursor.executemany(insert_lessons, lessons)

cursor.execute('SELECT id FROM lessons ORDER BY id DESC LIMIT 8')
id_lessons = cursor.fetchall()
print(id_lessons)

insert_marks = '''INSERT INTO marks(value, lesson_id, student_id)
VALUES (%s, %s, %s)'''

marks = [
    (3, id_lessons[7]['id'], id_student), (4, id_lessons[6]['id'], id_student),
    (4, id_lessons[5]['id'], id_student), (5, id_lessons[4]['id'], id_student),
    (2, id_lessons[3]['id'], id_student), (3, id_lessons[2]['id'], id_student),
    (4, id_lessons[1]['id'], id_student), (1, id_lessons[0]['id'], id_student)
]
cursor.execute('SELECT id FROM marks ORDER BY id DESC LIMIT 8')
id_marks = cursor.fetchall()
print(id_marks)

cursor.execute('SELECT student_id FROM marks ORDER BY id DESC LIMIT 1')
student_id_marks = cursor.fetchone()
print(student_id_marks)

# 1. Все оценки студента
cursor.execute(f"SELECT value FROM marks WHERE student_id = {student_id_marks['student_id']}")
print(cursor.fetchall())

# 2. Все книги, которые находятся у студента
cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {student_id_marks['student_id']}")
print(cursor.fetchall())

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
cursor.execute(select_all, tuple({student_id_marks['student_id']}))
print(cursor.fetchall())
db.commit()


db.close()
