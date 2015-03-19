#Jorge A. García Gonález
#Python02 Cadenas de Palabras

#Abre el fichero pokemon.txt
def AbrirPokemon():
    fichero = open("pokemon.txt")
    lines = fichero.readlines()
    fichero.close()
    return lines
#Crea una lista con las palabras del fichero
def ObtenerPalabras(lines):
    palabras = []
    for i in lines:
        for palabra in i.split(" "):
               if(palabra != "\n"):
                    palabras.append(palabra)
    return palabras

#Crea las Cadenas de Palabras
def CreaCadena(i):
    Listadepokemon=ObtenerPalabras(Lista)
    CADENA=[]
    CADENA.append(Listadepokemon[i]) #Metemos en cadena la primera palabra
    numero = len(Listadepokemon)
    index=0
    for index in range(0,numero):#Bucle para reiniciar la busqueda
        for j in Listadepokemon:#Bucle para encontrar palabra valida para la cadena
            if(ComPalabra(Listadepokemon[i],j)):
                del Listadepokemon[i]#borramos la palabra que ya hemos seleccionado de la lista
                i = Listadepokemon.index(j)#Cambiamos la palabra que estamos comparando por la nueva encontrada
                CADENA.append(Listadepokemon[i])#Añadimos la nueva palabra a CADENA
                index=0#Reiniciamos el bucle
                break
    return CADENA

#Comprueba se la condicion para enlazar dos palabras
def ComPalabra(p1, p2):
    if(p1!=p2):
        return p1[len(p1)-1] == p2[0]
    else:
         return False
#MAIN


Lista=AbrirPokemon()
Palabras=ObtenerPalabras(Lista)
Totalpokemon = len(Palabras)
TamMax = 0 #Variable para ver cadena mas larga
for i in range(1,Totalpokemon): #Bucle para empezar la cadena por todas las palabras al menos una vez
    CADENA = CreaCadena(i)
    TAMAÑODECADENA = len(CADENA)
    if(TAMAÑODECADENA>TamMax):
        TamMax=len(CADENA)
        CADENAMASGRANDE=CADENA
print (CADENAMASGRANDE)