from controllers.controlador import (ControladorAutor, ControladorEditorial, ControladorLibro, ControladorLector, ControladorAlquiler)

class VistaLector:

    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE LECTORES')
            print('(1) Registrar Lector (2) Listar Lectores (3) Para retroceder al menu principal')
            opcion = int(input('Ingrese la opción: '))
            if opcion == 1:
                VistaLector.registro()
            elif opcion == 2:
                ControladorLector.listar_lectores()
            else:
                break
    
    @staticmethod
    def registro():
        while True:
            try:
                identificador = input("Ingresa su DNI: ")
                if ControladorLector.verificar_id(identificador):
                    break
                else:
                    raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
            except Exception as e:
                print(f"error aqui: {str(e)}")
        ControladorLector.registrar_lector(identificador,input("Ingrese el nombre del nuevo lector: "))


class VistaLibro:

    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE REGISTRO DE LIBROS')
            print('(1) Registrar Autor (2) Registrar Editorial (3) Registrar Libro (4) Ver libros (5) Para regresar al menu principal')
            opcion = int(input('ingrese el numero: '))
            if opcion == 1:
                VistaLibro.ingreso_autor()
            elif opcion == 2:
                VistaLibro.ingreso_editorial()
            elif opcion == 3:
                VistaLibro.ingreso_libro()
            elif opcion == 4:
                VistaLibro.listar_libros()
            else:
                break

    @staticmethod
    def ingreso_autor():
        nombre = input("Ingrese nombre de Autor: ")
        ControladorAutor.registrar_autor(nombre)

    @staticmethod
    def ingreso_editorial():
        nombre = input('Ingrese nombre de editorial: ')
        ControladorEditorial.registrar_editorial(nombre)

    @staticmethod
    def listar_libros():
        ControladorLibro.listar_libros()

    @staticmethod
    def ingreso_libro():
        try:
            while True:
                try:
                    identificador = input("Ingresa el ISBN del Libro: ")
                    if ControladorLibro.verificar_id(identificador):
                        break
                    else:
                        raise Exception("--- Ya existe el ISBN --- Por favor, ingrese uno diferente")
                except Exception as e:
                    print(f"error aqui: {str(e)}")
            libro = input('Ingrese el nombre del libro: ')
            while True:
                    VistaLibro.lista_editoriales()
                    while True:
                        try:
                            editorial = int(input("Ingrese el ID de la editorial: "))
                            if ControladorLibro.verificar_editorial(editorial):
                                break
                            else:
                                raise Exception("El ID del editorial no existe, ingrese uno de la lista")
                        except Exception as e:
                            print(f"{e}")
                    
                    while True:
                        VistaLibro.listado_autores()
                        try:
                            autor = int(input("Ingrese el ID del autor: "))
                            if ControladorLibro.verificar_autor(autor):
                                break
                            else:
                                raise Exception("El ID del autor no existe, ingrese uno de la lista")
                        except Exception as e:
                            print(f"{e}")
                    ControladorLibro.registrar_libro(identificador, libro, autor, editorial)
                    break
        except Exception as e:
            print(f"Error aqui: {str(e)}")
        except KeyboardInterrupt:
            print('se interrumpio la app')
        except ValueError:
            print('No puso un dato')

    @staticmethod
    def listado_autores():
        return ControladorAutor.listar_autores()

    @staticmethod
    def lista_editoriales():
        return ControladorEditorial.listar_editoriales()


class BorrowBook:

    @staticmethod
    def menu():
        print('presiona (1) si deseas aquirir un nuevo libro')
        opcion = int(input('alquile un libro: '))
        if opcion == 1:
            BorrowBook.borrow_book()

    @staticmethod
    def borrow_book():
        ControladorLector.listar_lectores()
        u_idenficador = (input("Ingresa el identificador del lector: "))
        VistaLibro.listar_libros()
        id_libro = input("Ingresa el ISBN del libro: ")
        fecha = input('ingrese la fecha de devolucion: ')
        ControladorAlquiler.borrow(id_libro,u_idenficador, fecha)
        print('Se añadio un nuevo libro!')

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
            print('Se detuvo la app')

    @staticmethod
    def bienvenida():
        print('BIENVENIDO')

    @staticmethod
    def menu():
        while True:
            print('(1) Accede al Menú de Libros (2) Accede al Menú de Lectores (3) Accede al Menú de alquiler  ')
            opcion = int(input('Ingresa la opción: '))
            if opcion == 1:
                VistaLibro.menu()
            elif opcion == 2:
                VistaLector.menu()
            elif opcion == 3:
                BorrowBook.menu()
            else:
                break