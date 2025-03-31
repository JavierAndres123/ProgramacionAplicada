#################LISTAS####################
###########################################
my_lista = ['Perro', 'Gato', 'Elefante', 'León', 'Tigre', 'Lobo']

print(my_lista)
print(type(my_lista))
print(my_lista[2])

print("my_lista size: ", len(my_lista))
print(my_lista[0:2])
print(my_lista[:2])

my_lista.append('Jirafa')      # Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Pantera')  # Inserta en una posición específica
print(my_lista)

my_lista.extend(['Zebra', 'Hipopótamo'])  # Concatena otra lista
print(my_lista)

print(my_lista.index('Gato'))

my_lista.remove('Zebra')  # Elimina un elemento
print(my_lista)

my_lista.insert(8, 'Zebra')
print(my_lista)

print(my_lista.pop())  # Elimina el último elemento y lo muestra
size = len(my_lista)
print("size = ", size)

my_lista_3 = my_lista * 3  # Multiplicación de lista
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_lista.sort()  # Ordena la lista alfabéticamente
print(my_lista)

my_NumList = [20, 15, 10, 5, 0, -5, -10, -15]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)

# Ordenando lista de mayor a menor
my_NumList.sort(reverse=True)
print("De menor a mayor: ", my_NumList)

#################TUPLAS####################
###########################################
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print("my_tupla: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])

# Evaluar si un elemento está contenido en la tupla
print('Perro' in my_tupla)
print(my_tupla.count('Perro'))

# Tupla con un solo elemento
my_tupla_unitaria = ('Jirafa',)
print(my_tupla_unitaria)

# Empaquetado de tupla
my_tupla = 'Carlos', 12, 6, 1995
print(my_tupla)

# Desempaquetado de tupla
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertir una tupla en una lista
my_lista2 = list(my_tupla)
print(my_lista2)