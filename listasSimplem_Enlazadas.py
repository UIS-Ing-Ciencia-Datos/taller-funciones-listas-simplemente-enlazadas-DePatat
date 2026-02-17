# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

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
  #def insertarFinal()

  # Buscar elemento 
def buscarElemento(self, valor):
    actual = self.cabeza
    while actual != None:
      if actual == valor:
        print("True")
        return True
      actual = actual.siguiente
    print("False")
    return False

  # Contar elementos
def contarElementos(self, data):
    actual = self.cabeza
    cont = 0
    while actual != None:
      cont += 1
      actual = actual.siguiente
    print(f"Hay {cont} elementos en la lista")

#lista = ListaEnlazada()

valor = input("Ingrese un valor a insertar en la lista enlazada: \n Digite (salir) para no ingresar más elementos")

#if valor == "salir":
  #break

#else:
  #lista.insertar_final(valor)
  #print(f"El valor {valor} fue ingresado a la lista")

#buscarElemento(2, 4)