from database.connection import Conexion


class Author:
    def __init__(self, author):
        self.author = author

    def insert_author(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO authors (author) values (%(author)s);",{ 
            'author' : self.author
        })
        conn.connection.commit()
        conn.connection.close()

    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nNombre: {r[1]}")

    def obtener_ids():
        ids = []
        conn = Conexion()
        conn.query("SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        return ids

    def __str__(self):
        return f"\nAuthor : {self.author}\n"
        
class Libro:
    def __init__(self, nombre, author):
        self.nombre = nombre
        self.author = author

    @staticmethod
    def buscar_libro(nombre, libros):
        resultado = None
        for libro in libros:
            if libro.nombre == nombre:
                resultado = libro
                break
        return resultado

    def __str__(self):
        return (
            "\n----------LIBRO-------------\n"
            f"\n Nombre del libro : {self.nombre}\n"
            f"\n nombre del author : {self.author}\n"
            "\n----------------------------\n"
            )

class Alquiler:
    def __init__(self, dni, lector):
        self.dni = dni
        self.lector = lector
        self.prestamo = []

    def añadir_libros(self, libro, fecha_hoy, fecha_entrega):
        self.prestamo.append(
            (libro, fecha_hoy, fecha_entrega)
        )

    def __str__(self):
        return (
            "\n---------------------------------------"
            f"\nSu DNI: {self.dni}\n"
            f"\nla persona: {self.lector}\n"
            f"\ndetalle: {self.prestamo}\n"
            "------------------------------------------"
        )

class User:

    def __init__(self,identifier,name):
        self.identifier = identifier
        self.name = name

    def insert_user(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO users (identifier,name) values (%(identifier)s,%(name)s);",{ 
            'identifier' : self.identifier,
            'name' : self.name
        })
        conn.connection.commit()
        conn.connection.close()

    def get_identifiers_list():
        lista = []
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        return lista

    def verify_id(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        if identifier not in lista:
            return True

    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\n")

    def __str__(self):
        return f"\nIdentificador: {self.identifier}, Nombre: {self.name}\n"

