"""
	Ingresa una lista a Ordenarse para ordenarla en ella misma
"""
def ordenamientoPorInsercion(unaLista):
	# Recorremos la lista desde al posicion 1 hasta el final
   for indice in range(1,len(unaLista)):
     valorActual = unaLista[indice] # nos ubicamos en la posicion actual del indice
     posicion = indice # Variable auxiliar para hacer el intercambio
     # Mientras la posicion sea mayor a 0 y el valor anterior en al lista sea mayor al actual HACEMOS
     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1] # Dezplaza el elemento a la psociion de la derecha 
         posicion = posicion-1 # actualizamos la posicion 

     unaLista[posicion]=valorActual # Coloca el elemento insertado