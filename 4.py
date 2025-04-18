# import psycopg2
#
# class Student:
#     def __init__(self, name, surname, patronymic, group, grades, student_id):
#         self.student_id = student_id
#         self.name = name
#         self.surname = surname
#         self.patronymic = patronymic
#         self.group = group
#         self.grades = grades
#     def average_grades(self):
#         return sum(self.grades) / len(self.grades)
#     def dif(self):
#         return (f"ID: {self.student_id}\n"
#                 f"Name: {self.name}\n"
#                 f"Surname: {self.surname}\n"
#                 f"Patronymic: {self.patronymic}\n"
#                 f"Group: {self.group}\n"
#                 f"Grades: {self.grades}")
#
# def connect_to_db(dbname="postgres", user="postgres", password="Kirill266", host="localhost"):
#     conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
#     return conn
# def create_tables(conn):
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students2 (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(255),
#             surname VARCHAR(255),
#             patronymic VARCHAR(255),
#             groups INTEGER,
#             grades INTEGER[]
#         )
#     """)
#     conn.commit()
#     cursor.close()
# def add_student(conn, student):
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO students2 (name, surname, patronymic, groups, grades) VALUES (%s, %s, %s, %s, %s)",
#                    (student.name, student.surname, student.patronymic, student.group, student.grades))
#     conn.commit()
#     cursor.close()
# def get_all_students(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM students2")
#     students = []
#     for i in cursor.fetchall():
#         student = Student(i[1], i[2], i[3], i[4], i[5], i[0])
#         students.append(student)
#     cursor.close()
#     return students
# def get_student_by_id(conn, student_id):
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM students2 WHERE id = %s", (student_id,))
#     i = cursor.fetchone()
#     cursor.close()
#     if i:
#         return Student(i[1], i[2], i[3], i[4], list(i[5]), i[0])
#     else:
#         return None
# def update_student(conn, student):
#     cursor = conn.cursor()
#     cursor.execute("UPDATE students2 SET name = %s, surname = %s, patronymic = %s, groups = %s, grades = %s WHERE id = %s",
#                    (student.name, student.surname, student.patronymic, student.group, student.grades, student.student_id))
#     conn.commit()
#     cursor.close()
# def delete_student(conn, student_id):
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM students2 WHERE id = %s", (student_id,))
#     conn.commit()
#     cursor.close()
# def get_average_grade_by_group(conn, group):
#     cursor = conn.cursor()
#     cursor.execute("SELECT (grades::numeric[]) FROM students2 WHERE groups = %s", (group,))
#     average_grade = cursor.fetchone()[0]
#     cursor.close()
#     return average_grade
#
#
# conn = connect_to_db()
# if conn:
#     create_tables(conn)
#
#     student1 = Student("Кирилл", "Маментьев", "Евгеньевич", 643,[3,4,5,4],1)
#     add_student(conn, student1)
#
#     student2 = get_student_by_id(conn, 1)
#     print("\nStudent with ID 1:", student2)
#
#     if student2:
#         student2.grades = [3, 4, 5, 4]
#         update_student(conn, student2)
#
#         average_grade_643 = get_average_grade_by_group(conn, 643)
#         print(f"\nAverage grade for group 643: {average_grade_643}")
#
#         delete_student(conn, 2)
#
#     conn.close()
