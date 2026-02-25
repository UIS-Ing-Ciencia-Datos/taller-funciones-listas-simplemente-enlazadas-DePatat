# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada
# ===========================================

# Importación de librerias
import time

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacia
    def vacio(self):
        if self.cabeza == None:
            print("Está vacia")
            return True
        else:
            print("Lista no vacia")
            return False

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    # Insertar al final
    def insertarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Insertar antes de un elemento x
    def insertarBeforeX(self, x, data):
        if self.cabeza is None:
          print("La lista se encuentra vacia")
          return
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data is x:
                break
            else:
                actual.siguiente
        if actual is None:
            print(f"El valor de {x} no pudo ser encontrado en la lista ")
            return
            time.sleep(1.25)

        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        print(f"El elemento {data} fue insertado antes del nodo {x} exitosamente.")
        time.sleep(1.5)
        self.mostrarLista()
        time.sleep(2)

    # Insertar después de un elemento x
    def insertarAfterX(self, x, data):
        actual = self.cabeza
        while actual is not None:
            if actual.data == x:

                break
            else:
                actual = actual.siguiente
        if actual is None:
            print(f"El elemento de {x} no existe en la lista actual")
            time.sleep(1.75)
            return
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        print(f"El elemento {data} fue insertado después del elemento {x} exitosamente.")
        time.sleep(2.25)

    # Eliminar el primero
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("La lista se encuentra vacia")
            time.sleep(1.5)
            return
        else:
            self.cabeza = self.cabeza.siguiente
            print(f"El primer elemento fue eliminado exitosamente")
            time.sleep(1.75)
            self.mostrarLista()
            time.sleep(2)

    # Eliminar último
    def eliminarUltimo(self):
        actual = self.cabeza
        if actual is None:
            print("La lista se encuentra vacia")
            time.sleep(1.5)
            return
        if actual.siguiente is None:
            actual = None
            print("El único elemento de la lista ha sido eliminado")
            time.sleep(1.5)
            self.mostrarLista()
            time.sleep(1.75)
            return
        else:
            while actual.siguiente.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = None
            print("El último elemento fue eliminado exitosamente")
            time.sleep(1.5)
            self.mostrarLista()
            time.sleep(2)

    # Buscar elemento
    def buscarElemento(self, valor):
        actual = self.cabeza
        while actual != None:
            # Se compara con actual.data, no con el objeto nodo
            if actual.data == valor:
                print(f"El elemento {valor} fue encontrado en la lista")
                time.sleep(2)
                return True
            actual = actual.siguiente
        print(f"El elemento {valor} no fue encontrado en la lista")
        time.sleep(2)
        return False

    # Contar elementos
    def contarElementos(self):
        actual = self.cabeza
        cont = 0
        while actual != None:
            cont += 1
            actual = actual.siguiente
        print(f"\nLa cantidad de elementos en la lista es de: ({cont})")

    # Mostrar lista
    def mostrarLista(self):
        actual = self.cabeza
        if actual is None:
            print("No hay ningún nodo en la lista")
            return
        else:
            print("Contenido de la lista:", end=" ")

        while actual != None:
            print(f"[{actual.data}]", end=" -> ")
            actual = actual.siguiente
        print("Null")


lista = ListaSE()

while True:
    print("\n ---Listas Enlazadas en Python---\n")
    print("1. Ingresar un nodo")
    print("2. Eliminar un nodo")
    print("3. Buscar un elemento en la lista")
    print("4. Contar los elementos de la lista")
    print("5. Salir del programa\n")
    option = int(input("Elija una opción: "))
    time.sleep(0.1)

    match option:

        case 1:
            time.sleep(.25)
            print("\n ---Ingreso de nodos a la lista---\n")
            print("1. Insertar el nodo al inicio")
            print("2. Insertar el nodo al final")
            print("3. Insertar el nodo antes de un elemento")
            print("4. Insertar el nodo después de un elemento")
            print("5. Salir al menu principal\n")
            option01 = int(input("Elija una opción: "))
            time.sleep(0.1)

            match option01:
                case 1:
                    value = input("\nDigite el contenido a introducir en el nodo: ")
                    if value == "":
                        print(
                            "El nodo no puede contener un valor nulo, por favor intentelo nuevamente."
                        )
                        time.sleep(1.5)
                    else:
                        lista.agregarInicio(value)
                        print(
                            f'El valor "{value}" fue ingresado al inicio de la lista exitosamente'
                        )
                        time.sleep(.75)
                        lista.mostrarLista()
                        time.sleep(2)

                case 2:
                    value = input("\nDigite el contenido a introducir en el nodo: ")
                    if value == "":
                        print(
                            "El nodo no puede contener un valor nulo, por favor intentelo nuevamente."
                        )
                        time.sleep(1.5)
                    else:
                        lista.insertarFinal(value)
                        print(
                            f'El valor "{value}" fue ingresado al final de la lista exitosamente'
                        )
                        time.sleep(.75)
                        lista.mostrarLista()
                        time.sleep(2)

                case 3:
                    print(
                        "\n ---Insertar el nodo antes de un elemento de la lista---\n"
                    )
                    lista.mostrarLista()
                    time.sleep(.25)
                    x = input("Ingrese el elemento ya existente en la lista: ")
                    value = input("Digite el contenido a introducir en el nuevo nodo: ")
                    if value == "":
                        print(
                            "El nodo no puede contener un valor nulo, por favor intentelo nuevamente."
                        )
                        time.sleep(1.5)
                    else:
                        lista.insertarBeforeX(x, value)

                case 4:
                    print(
                        "\n ---Insertar el nodo después de un elemento de la lista---\n"
                    )
                    lista.mostrarLista()
                    time.sleep(.25)

                    x = input("Ingrese el elemento ya existente en la lista: ")
                    value = input("Digite el contenido a introducir en el nuevo nodo: ")
                    if value == "":
                        print(
                            "El nodo no puede contener un valor nulo, por favor intentelo nuevamente."
                        )
                        time.sleep(1.5)
                    else:
                        lista.insertarAfterX(x, value)
                        lista.mostrarLista()
                        time.sleep(2)

                
                case 5:
                  print("Saliendo del al menú principal...")
                  time.sleep(0.5)

                case _:
                    print("\nOpción no valida. \n Por favor intentelo nuevamente")
                    time.sleep(1.75)

        case 2:
            print("\n1. Eliminar el primer nodo")
            print("2. Eliminar el último nodo")
            print("3. Salir al menu principal")
            try:
              option02 = int(input("Elija un opción: "))
            except ValueError:
              print("Por favor, ingrese un número válido.")
              time.sleep(1.5)
              continue

            match option02:
              case 1:
                lista.eliminarPrimero()
              case 2:
                lista.eliminarUltimo()
              case 3:
                print("Saliendo al menú principal...")
                time.sleep(.5)
              case _:
                print("\nOpción no valida. \n Por favor intentelo nuevamente")
                time.sleep(1.75)

        case 3:
            lista.mostrarLista()
            value = input("Ingrese el valor dentro de la lista que desea buscar: ")
            lista.buscarElemento(value)

        case 4:
            lista.contarElementos()
            time.sleep(1.75)

        case 5:
            print("Saliendo del programa...")
            time.sleep(0.5)
            break

        case _:
            print("\nOpción no valida. \n Por favor intentelo nuevamente")
            time.sleep(1.5)