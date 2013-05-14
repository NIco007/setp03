def cuenta_palabras(diccionario,cantidad):
    
    
    if(len(diccionario)>0):
        algo, numero = diccionario.popitem()
        cantidad = cantidad + numero
        return cuenta_palabras(diccionario,cantidad) 
    else:
        return cantidad




cantidad = 0 
diccionario = {"hola":5 , "coma":6, "poasa":20,"vaca":20} # este diccionario lo tome como ejemplo para saber si funcionaba.

print("La cantidad de palabras totales dentro del diccionario son ", cuenta_palabras(diccionario,cantidad))