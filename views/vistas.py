from controllers.controlador import (ControladorAutor, ControladorBook, ControladorAlquiler, ControladorLector)

class VistaLector:

    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE LECTORES')
            print('(1) Registrar Lector (2) Listar Lectores')
            opcion = int(input('Ingrese la opción: '))
            if opcion == 1:
                while True:
                    try:
                        identificador = input("Ingresa el identificador del nuevo lector: ")
                        if ControladorLector.verificar_id(identificador):
                            break
                        else:
                            raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
                    except Exception as e:
                        print(f"error aqui: {str(e)}")
                ControladorLector.registrar_lector(identificador,input("Ingrese el nombre del nuevo lector: "))
            elif opcion == 2:
                ControladorLector.listar_lectores()
            else:
                break
    
    @staticmethod
    def ingreso_lector():
        nombre = input('ingres el nombre del libro: ')
        author = input('ingrese el nombre del author: ')
        nuevo_libro = ControladorBook.registrar_libro(
            {
                'nombre': nombre, 'author': author
            }
        )
        print(nuevo_libro)

    @staticmethod
    def listar_lectores():
        for b in ControladorBook.libros:
            print(b)

class VistaBook:

    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE REGISTRO DE LIBROS')
            print('(1) Registrar Autor (2) Registrar Editorial')
            opcion = int(input('ingrese el numero: '))
            if opcion == 1:
                ControladorAutor.registrar_autor(input("Ingrese nombre de Autor: "))
            elif opcion == 2:
                ControladorAutor.listar_autores() #AQUI DEBE IR LO DE EDITORIAL PARA REGISTRAR
            elif opcion == 3:
                VistaBook.ingreso_libro()
            elif opcion == 4:
                VistaBook.listar_libros()
            else:
                break

    @staticmethod
    def ingreso_libro():
        nombre = input('ingres el nombre del libro: ')
        author = input('ingrese el nombre del author: ')
        nuevo_libro = ControladorBook.registrar_libro(
            {
                'nombre': nombre, 'author': author
            }
        )
        print(nuevo_libro)

    @staticmethod
    def listar_libros():
        for b in ControladorBook.libros:
            print(b)

class VistaAlquiler:
    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print('\n')
            print('BIENVENIDO A LA SECCION DE ALQUILER DE LIBROS')
            print('QUE LIBRO DESEA ADQUIRIR?')
            print('presione 1 para adquirir un libro')
            print('escriba 2 para listar sus libros')
            print('escriba 3 para regresar')
            opcion = int(input('Ingrese un numero: '))
            if opcion == 1:
                VistaAlquiler.ingreso_alquiler()
            elif opcion == 2:
                VistaAlquiler._listar_libro()
            else:
                continuar = False

    @staticmethod
    def ingreso_alquiler():
        VistaAlquiler._ingreso_lector()
        VistaAlquiler._agregar_libro()

    @staticmethod
    def _ingreso_lector():
        nombre = input('Ingrese su nombre: ')
        dni = input('ingrese su DNI: ')
        nuevo_alquiler = ControladorAlquiler.registrar_alquiler(
            {
                'dni': dni,
                'lector': nombre
            }
        )
        print(f'\nBIENVENIDO: {nuevo_alquiler.lector}\n')

    @staticmethod
    def _agregar_libro():
        nombre_libro = input('Ingrese un libro de la libreria: ')
        fecha_de_hoy = input('Ingrese la fecha de hoy: ')
        fecha_de_entrega = input('Ingrese la fecha en el cual devolvera el libro: ')
        response = ControladorAlquiler.registrar_libro_a_lector(
            nombre_libro, fecha_de_hoy ,fecha_de_entrega
        )
        if response:
            print('Se añadio el libro')
        else:
            print('no se encontro el libro :(')

    @staticmethod
    def _listar_libro():
        for b in ControladorAlquiler.alquiler:
            print(b)


class VistaAplicacion:
    @staticmethod
    def iniciar():
        try:
            VistaAplicacion.bienvenida()
            VistaAplicacion.menu()
        except ValueError:
            print('no ingresaste un dato')
        except Exception as a:
            print(f'ocurrio un error aqui: {str(a)}')
        except KeyboardInterrupt:
            print('se detubo la app')

    @staticmethod
    def bienvenida():
        print('BIENVENIDO')

    @staticmethod
    def menu():
        while True:
            print('(1) Accede al Menú de Libros (2) Accede al Menú de alquiler (3) Accede al Menú de Lectores ')
            opcion = int(input('Ingresa la opción: '))
            if opcion == 1:
                VistaBook.menu()
            elif opcion == 2:
                VistaAlquiler.menu()
            elif opcion == 3:
                VistaLector.menu()
            else:
                break