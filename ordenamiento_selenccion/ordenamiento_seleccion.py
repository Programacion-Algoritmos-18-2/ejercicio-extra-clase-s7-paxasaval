"""
    Ingresa una lista aordenarse en ella misma
"""
def ordenamientoPorSeleccion(unaLista):
    # iteramos la lista ingresada en el metodo
    for i in range(0, len(unaLista)-1):
        masPequenio = i  # primer indice del resto del arreglo(mas pequenio)
        # itera para buscar el indice dle elemento mas pequenio
        for indice in range(i + 1, len(unaLista)):
            if unaLista[indice] < unaLista[masPequenio]:
                masPequenio = indice
        intercambiar(unaLista, i, masPequenio)

def intercambiar(unaLista, primero, segundo):
       temp = unaLista[primero] # almacena el dato temporal
       unaLista[primero] = unaLista[segundo] # Sustituye primero con segundi
       unaLista[segundo] = temp # coloca el temproal segundo