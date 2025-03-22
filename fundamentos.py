# suma = 10 + 2
# print(f"Suma es {suma}")

# edad = 15
# if edad >= 18:
#     print("Entras a la pary")
# elif edad >= 15:
#     print("Entras a la pary pero no tomas")
# else:
#     print("No entras a la pary")

# edad = 13

# while edad < 18:
#     print("eres menor de edad")
#     edad += 1


# def suma(a: int, b: int) -> int:
#     return a + b


# print(suma(3, 4.2))


# def odd_count(n):
#     contador = 0
#     for i in range(n):
#         print(i % 2)
#         if 1 % 2 == 1:
#             contador += 1

#     return contador


# print(odd_count(15))
# def digital_root(n):
#     resultado = 0
#     for i in str(n):
#         resultado += int(i)

#     print(resultado)
#     # print(len(str(resultado)))

#     if len(str(resultado)) >= 2:
#         return digital_root(resultado)
#     else:
#         return resultado


# print(digital_root(942))
# strng = "abcd"
# for i in range(len(strng)):
#     print(strng[i:] + strng[:i])
# POO
"""
POO
1. Clase
2. Instanciar
3. Objeto
4. Método
    4.1 Método constructor (crear atributos)
5. Atributo
6. Self (referencia a uno mismo)
"""


class Course:
    # metodo constructor
    # nos permite definir los atributos de la clase
    def _init_(self, name="Python"):
        self.name = name
        self.students = []

    # metodo1
    def add_student(self, name, last_name, age, grade):
        student = {"name": name, "last_name": last_name, "age": age, "grade": grade}
        self.students.append(student)

    # metodo2
    def print_students(self):
        for student in self.students:
            print(student)


# creando una instancia de la clase Course
course1 = Course()
print(course1.name)
course1.add_student("John", "Doe", 14, 9)
course1.print_students()

print("-" * 20)
course2 = Course("Javascript")
print(course2.name)
course2.add_student("Jane", "Smith", 13, 8)
course2.print_students()
