# Trabajo realizado por Garcia Gonzalez, Javier
#
def numeroNiveles(): # Funcion que guarda los niveles en el fichero niveles
    fichero = open("niveles.txt", "r")
    nivelesExistentes = (int)(fichero.readline().replace("\n",""))  # Variable que guarda la cantidad de niveles que hay en el fichero
    fichero.close() # Cierro el lector de niveles.txt
    return nivelesExistentes

def recogerRecords(): # Funcion que recoge los records existentes y los guarda en una lista
    fichero = open("records.txt", "r") # Abro y leo el fichero de records
    recordsPartida = [] # Declaro la lista para almacenar los ficheros

    for record in fichero:  # Recorro el fichero records para almacenar los records de cada nivel en una lista
        record=int(record)
        recordsPartida.append(record) # Añado a la lista el record que esta almacenado en el fichero
    fichero.close()  # Cierro el lector del fichero records.txt

    return recordsPartida # Devuelvo la lista de records

def crearTablero(coordenadasNivelElegido): # Funcion que crea el tablero con los bordes Funciona
    tablero=[] # Declaro una lista que creará el tablero

    # BORDE DEL TABLERO
    for i in range(24):# Filas 3*8
        tablero.append([])
        for j in range(40): # Columnas 5*8
            tablero[i].append("\u2592")

    for i in range(3,21): # Relleno de espacios en blanco el interior del tablero
        for j in range(5,35):
            tablero[i][j]=" "

    for i in range(int(coordenadasNivelElegido[1])*3,int(coordenadasNivelElegido[1])*3+3): # Salida
        for j in range(int(coordenadasNivelElegido[0])*5,int(coordenadasNivelElegido[0])*5+5):
            tablero[i][j]=" "


    return tablero # Devuelve el tablero

def cochesNivel(): # Funcion que me devuelve la lista con coches por cada nivel
    fichero=open("niveles.txt", "r")
    cochesLista = fichero.readlines()
    totalNiveles = numeroNiveles()  # Numero total de niveles que tiene el fichero
    coches=[] # Declaro una lista que me almacena los coches por nivel

    cochesLista.pop(0) # Quito el primer numero de la lista

    for i in range(len(cochesLista)):
       cochesLista[i]=cochesLista[i].replace("\n","") # Quito los saltos de línea del archivo para facilitar su lectura

    for i in range(totalNiveles):
        coches.append([])

    numero = (int)(cochesLista[0])  # Numero que de coches que tiene el primer nivel
    aux = 3

    for i in range(totalNiveles): # Extraigo los coches que hay por nivel a la lista coches que es multidimensional de modo que la posicion n de la lista tenga los coches del nivel n
        if i==totalNiveles-1:
            coches[i] = cochesLista[aux:len(cochesLista)]
        else:
            coches[i] = cochesLista[aux:aux + numero]
            aux = aux + numero + 3
            numero = (int)(cochesLista[aux - 3])
    fichero.close()
    return coches # Devuelvo la lista con los coches de cada nivel

def mostrarTablero(tablero): # Funcion que muestra el tablero
    for i in range(24):
        for j in range(40):
            print(tablero[i][j], end="")
        print()

def insertarCochesTablero(cochesNivelElegido): # Funcion que inserta los coches del nivel elegido al tablero
    letraMayuscula=64
    letraMinuscula=96
    COE="\u2500" # Lineas horizontales
    CNS="\u2502" # Lineas verticales
    CSE="\u250C" # Esquina superior izquierda
    CSO="\u2510" # Esquina superior derecha
    CNE="\u2514" # Esquina inferior izquierda
    CNO="\u2518" # Esquina inferior derecha


    for indice in range(len(cochesNivelElegido)): # Meto los coches en el tablero
        cocheActual=cochesNivelElegido[indice] # Voy cambiando de coche
        letraMayuscula += 1
        letraMinuscula += 1
        # Para insertarlos me fijo en los valores de su columna y fila para colocar las esquinas, letras y lineas.
        if (cocheActual[0]=="H"): # Si el coche es horizontal hago lo siguiente
            for i in range((int(cocheActual[2])) * 3, (int(cocheActual[2]) + 1) * 3):
                for j in range((int(cocheActual[1])) * 5, (int(cocheActual[1]) + int(cocheActual[3])) * 5):
                    if (i == (int(cocheActual[2])) * 3 and j == (int(cocheActual[1])) * 5):  # Esquina superior izquierda
                        tablero[i][j] = CSE
                    elif (i == (int(cocheActual[2]) + 1) * 3 - 1 and j == (int(cocheActual[1])) * 5):  # Esquina inferior derecha
                        tablero[i][j] = CNE
                    elif (i == (int(cocheActual[2]) + 1) * 3 - 1 and j == (int(cocheActual[1]) + int(cocheActual[3])) * 5 - 1):
                        tablero[i][j] = CNO
                    elif (i == (int(cocheActual[2])) * 3 and j == (int(cocheActual[1]) + int(cocheActual[3])) * 5 - 1):
                        tablero[i][j] = CSO
                    elif ((i == (int(cocheActual[2])) * 3 + 1 and j == (int(cocheActual[1])) * 5) or (i == (int(cocheActual[2])) * 3 + 1 and j == (int(cocheActual[1]) + int(cocheActual[3])) * 5 - 1)):
                        tablero[i][j] = CNS
                    elif (i == (int(cocheActual[2])) * 3 or i == (int(cocheActual[2]) + 1) * 3 - 1):
                        tablero[i][j] = COE
                    elif (i == (int(cocheActual[2])) * 3 + 1 and j == (int(cocheActual[1])) * 5 + 1):
                        tablero[i][j] = chr(letraMayuscula)
                    elif (i == i == (int(cocheActual[2])) * 3 + 1 and j == (int(cocheActual[1]) + int(cocheActual[3])) * 5 - 2):
                        tablero[i][j] = chr(letraMinuscula)
        elif (cocheActual[0]=="V"): # Si el coche es vertical hago lo siguiente
            for i in range((int(cocheActual[2])) * 3, (int(cocheActual[2]) + int(cocheActual[3])) * 3):
                for j in range((int(cocheActual[1])) * 5, (int(cocheActual[1]) + 1) * 5):
                    if (i == (int(cocheActual[2])) * 3 and j == (int(cocheActual[1])) * 5):
                        tablero[i][j] = CSE
                    elif (i == (int(cocheActual[2]) + int(cocheActual[3])) * 3 - 1 and j == (int(cocheActual[1])) * 5):
                        tablero[i][j] = CNE
                    elif (i == (int(cocheActual[2])) * 3 and j == (int(cocheActual[1]) + 1) * 5 - 1):
                        tablero[i][j] = CSO
                    elif (i == (int(cocheActual[2]) + int(cocheActual[3])) * 3 - 1 and j == (
                            int(cocheActual[1]) + 1) * 5 - 1):
                        tablero[i][j] = CNO
                    elif (j == (int(cocheActual[1])) * 5 or j == (int(cocheActual[1]) + 1) * 5 - 1):
                        tablero[i][j] = CNS
                    elif (i == (int(cocheActual[2])) * 3 or i == (int(cocheActual[2]) + int(cocheActual[3])) * 3 - 1):
                        tablero[i][j] = COE
                    elif (i == (int(cocheActual[2])) * 3 + 1 and j == (int(cocheActual[1])) * 5 + 2):
                        tablero[i][j] = chr(letraMayuscula)
                    elif (i == (int(cocheActual[2]) + int(cocheActual[3])) * 3 - 2 and j == (int(cocheActual[1])) * 5 + 2):
                        tablero[i][j] = chr(letraMinuscula)
    return tablero

def moverCochestTablero(movimientos, cochesNivelElegido): # Funcion que mueve los coches
    mayuscula=False
    cont=0
    auxMovimientos=""
    for indice in range(len(movimientos)):  # Recorro el string introducido por el usuario con los movimientos para hacer
        cocheActual = ""  # Reseteo el cocheActual
        seEjecuta = False  # Reseteo seEjecuta a False

        if (movimientos[indice].upper() == movimientos[indice]):  # Compruebo que sea mayuscula la letra asociada al movimiento
            mayuscula = True
        elif (movimientos[indice].lower() == movimientos[indice]):  # Compruebo que sea minuscula la letra asociadaa al movimiento
            mayuscula = False

        if (mayuscula == True):  # Compruebo que sea mayuscula la letra asociada al movimiento
            cocheActualInicial = cochesNivelElegido[ord(movimientos[indice]) - 65]  # Selecciono el coche
            if (cocheActualInicial[0] == "H"):  # Mayuscula Horizontal
                if (tablero[(int(cocheActualInicial[2]) * 3)][(int(cocheActualInicial[1])) * 5 - 1] == " "): # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True


                else:
                    print("El movimiento " + movimientos[indice]+ " no se puede realizar")
                    return cochesNivelElegido

                if (seEjecuta):  # Si no habia nada en esa direccion lo ejecuto
                    columna = int(cocheActualInicial[1]) - 1
                    for i in range(len(cocheActualInicial)):
                        if (i == 1):
                            cocheActual += str(columna)
                        else:
                            cocheActual += cocheActualInicial[i]

                    for i in range((int(cocheActual[2])) * 3, (int(cocheActual[2]) + 1) * 3):
                        for j in range((int(cocheActual[1])) * 5 + 1,
                                       (int(cocheActual[1]) + int(cocheActual[3])) * 5 + 5):
                            tablero[i][j] = " "

                    cochesNivelElegido[ord(movimientos[indice]) - 65] = cocheActual # Actualizo el valor del coche

            elif (cocheActualInicial[0] == "V"):  # Vertical Mayuscula
                if (tablero[(int(cocheActualInicial[2])) * 3 - 1][int(cocheActualInicial[1]) * 5] == " "): # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True

                else:
                    print("El movimiento " + movimientos[indice]+ " no se puede realizar")
                    return cochesNivelElegido

                if (seEjecuta):  # Si no habia nada en esa direccion lo ejecuto

                    fila = int(cocheActualInicial[2]) - 1
                    for i in range(len(cocheActualInicial)):
                        if (i == 2):
                            cocheActual += str(fila)
                        else:
                            cocheActual += cocheActualInicial[i]

                    for i in range((int(cocheActual[2])) * 3, (int(cocheActual[2]) + int(cocheActual[3])) * 3 + 3):
                        for j in range((int(cocheActual[1])) * 5, (int(cocheActual[1]) +1) * 5):
                            tablero[i][j] = " "

                    cochesNivelElegido[ord(movimientos[indice]) - 65] = cocheActual # Actualizo el valor del coche



        elif (mayuscula == False):  # Compruebo que sea minuscula la letra asociada al movimiento
            cocheActualInicial = cochesNivelElegido[ord(movimientos[indice]) - 97]

            if (cocheActualInicial[0] == "H"):  # Compruebo que sea horizontal
                if (tablero[(int(cocheActualInicial[2])) * 3][(int(cocheActualInicial[1]) + int(cocheActualInicial[3])) * 5] == " "):  # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True

                else:
                    print("El movimiento " + movimientos[indice]+ " no se puede realizar")
                    return cochesNivelElegido

                if (seEjecuta):  # Si no habia nada en la direccion a la que se va a mover
                    columna = int(cocheActualInicial[1]) + 1
                    for i in range(len(cocheActualInicial)):
                        if (i == 1):
                            cocheActual += str(columna)
                        else:
                            cocheActual += cocheActualInicial[i]

                    for i in range((int(cocheActual[2])) * 3, (int(cocheActual[2]) + 1) * 3):
                        for j in range((int(cocheActual[1])) * 5 - 5,(int(cocheActual[1]) + int(cocheActual[3])) * 5 - 1):
                            tablero[i][j] = " "

                    cochesNivelElegido[ord(movimientos[indice]) - 97] = cocheActual  # Actualizo el valor del coche

            elif (cocheActualInicial[0] == "V"):  # Minuscula y vertical

                if (tablero[((int(cocheActualInicial[2]) + int(cocheActualInicial[3]))) * 3 + 1  ][(int(cocheActualInicial[1])) * 5] == " "): # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True

                else:
                    print("El movimiento " + movimientos[indice]+ " no se puede realizar")
                    return cochesNivelElegido

                if (seEjecuta):
                    fila = int(cocheActualInicial[2]) + 1
                    for i in range(len(cocheActualInicial)):
                        if (i == 2):
                            cocheActual += str(fila)
                        else:
                            cocheActual += cocheActualInicial[i]

                    for i in range((int(cocheActual[2])) * 3 - 3, (int(cocheActual[2]) + int(cocheActual[3])) * 3):
                        for j in range((int(cocheActual[1])) * 5, (int(cocheActual[1]) +1) * 5):
                            tablero[i][j] = " "

                    cochesNivelElegido[ord(movimientos[indice]) - 97] = cocheActual  # Actualizo el valor del coche
        auxMovimientos+=movimientos[indice]
        cont=len(auxMovimientos)
    return cochesNivelElegido

def contadorMovimientos(movimientos, cochesNivelElegido):
    mayuscula = False
    cont = 0
    contador=0
    auxMovimientos = ""
    for indice in range(len(movimientos)):  # Recorro el string introducido por el usuario con los movimientos para hacer
        cocheActual = ""  # Reseteo el cocheActual
        seEjecuta = False  # Reseteo seEjecuta a False

        if (movimientos[indice].upper() == movimientos[indice]):  # Compruebo que sea mayuscula la letra asociada al movimiento
            mayuscula = True
        elif (movimientos[indice].lower() == movimientos[indice]):  # Compruebo que sea minuscula la letra asociadaa al movimiento
            mayuscula = False

        if (mayuscula == True):  # Compruebo que sea mayuscula la letra asociada al movimiento
            cocheActualInicial = cochesNivelElegido[ord(movimientos[indice]) - 65]  # Selecciono el coche
            if (cocheActualInicial[0] == "H"):  # Mayuscula Horizontal
                if (tablero[(int(cocheActualInicial[2]) * 3)][(int(cocheActualInicial[1])) * 5 - 1] == " "):  # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True
                else:
                    seEjecuta= False
                    contador+=1

            elif (cocheActualInicial[0] == "V"):  # Vertical Mayuscula
                if (tablero[(int(cocheActualInicial[2])) * 3 - 1][int(cocheActualInicial[1]) * 5] == " "):  # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True
                else:
                    seEjecuta= False
                    contador += 1


        elif (mayuscula == False):  # Compruebo que sea minuscula la letra asociada al movimiento
            cocheActualInicial = cochesNivelElegido[ord(movimientos[indice]) - 97]

            if (cocheActualInicial[0] == "H"):  # Compruebo que sea horizontal
                if (tablero[(int(cocheActualInicial[2])) * 3][(int(cocheActualInicial[1]) + int(cocheActualInicial[3])) * 5] == " "):  # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True
                else:
                    seEjecuta= False
                    contador+=1

            elif (cocheActualInicial[0] == "V"):  # Minuscula y vertical
                if (tablero[((int(cocheActualInicial[2]) + int(cocheActualInicial[3]))) * 3 + 1][(int(
                        cocheActualInicial[1])) * 5] == " "):  # Compruebo que a la direccion que se va a mover este vacio
                    seEjecuta = True
                else:
                    seEjecuta= False
                    contador+=1

        auxMovimientos += movimientos[indice]
        cont = len(auxMovimientos)-contador # Resto las veces que no se ejecuta
    return cont

def escribirRecords(cont, recordsPartida, nivelElegido): # Funcion que escribe en el fichero
    fichero = open("records.txt", "w")
    if (recordsPartida[0]==0): # Si la primera posicion es 0 la quito
        recordsPartida.pop(0)
    recordsPartida.append(cont)

    for i in range(len(recordsPartida)):
        fichero.write(str(recordsPartida[i])+"\n")
    fichero.flush()
    fichero.close()

def coordenadasSalida(): # Funcion que devuelve en listas las coordenadas de las salidas de cada nivel del fichero
    fichero=open("niveles.txt","r") # Abro el fichero
    cochesLista = fichero.readlines() # Creo una lista que contiene todas las lineas del fichero
    for i in range(len(cochesLista)):
        cochesLista[i] = cochesLista[i].replace("\n", "") # Quito los \n

    totalNiveles = int(cochesLista[0]) # Numero de niveles que hay en el fichero

    coordenadas = []

    for i in range(totalNiveles):
        coordenadas.append([]) # Añado dos listas dentro de la lista ya creada

    numeroCoches = (int)(cochesLista[1])
    aux = 3

    for i in range(totalNiveles):
        if (i == 0):
            coordenadas[i] = cochesLista[2:4]
        else:
            coordenadas[i] = cochesLista[2 + numeroCoches + 3:4 + numeroCoches + 3] # Guardo las filas y columnas como lista dentro de otra lista
        numero = numeroCoches
        numeroCoches = (int)(cochesLista[1 + 3 + numero])

    fichero.close() # Cierro el fichero
    return coordenadas # Devuelvo la lista que contiene las coordenadas respectivas a cada nivel


# Main
#

# Comienzo
nivelSinRecord=False
nivelElegido=1
continuado=False
cont=0
nivelesExistentes=numeroNiveles() # variable que almacena el numero de niveles que hay
while True:
    continuacion=""
    recordsPartida=recogerRecords() # Almacena los records que estan asociados a cada nivel
    nivelesConRecord = len(recordsPartida) # Variable que almacena los niveles que tienen record

    if (len(recordsPartida)==0):
        recordsPartida.append(0)
        escribirRecords(0, recordsPartida, nivelElegido-1)
    for i in range(len(recordsPartida)):
        if (recordsPartida[0]==0):
            nivelesConRecord=0

    if nivelesConRecord >= 1:
        while True:
            print(f"Elige un nivel (1-{nivelesConRecord + 1}): ",end="")  # Puede elegir desde 1 hasta el maximo nivel con record
            nivelElegido = int(input())  # Recojo el nivel elegido por el usuario

            if nivelElegido >= 1 and nivelElegido <= (nivelesConRecord + 1):  # Compruebo que esta dentro del intervalo
                break  # Si lo esta salgo del bucle
            else:
                print(f"Elige un nivel adecuado, entre 1 y {nivelesConRecord + 1}")
        if (len(recordsPartida)>=nivelElegido):
            print(f"NIVEL {nivelElegido} - RECORD {recordsPartida[nivelElegido - 1]} movimientos")  # Muestro que nivel ha elegido y el record de movimientos que tiene dicho nivel
        else:
            print(f"NIVEL {nivelElegido} - SIN RECORD")
            nivelSinRecord=True
    else:
        print(f"NIVEL {nivelElegido} - No hay records registrados")

    print()

    coches=cochesNivel() # Asigno a coches la lista que contiene los coches por nivel
    cochesNivelElegido=coches[nivelElegido-1] # Lista que contiene todos los coches del nivel elegido
    coordenadas=coordenadasSalida() # Lista que contiene las coordenadas
    coordenadasNivelElegido=coordenadas[nivelElegido-1] # Lista con las coordenadas de la salida

    tablero = crearTablero(coordenadasNivelElegido)  # Creo el tablero, bordes y relleno interior
    insertarCochesTablero(cochesNivelElegido)  # Funcion que inserta los coches en el tablero

    # Anteriormente se actualiza el tablero con insertar coches tablero
    mostrarTablero(tablero) # Muestra el tablero

    while True:
        print("Movimientos = ", end="")
        movimientos=input()
        cont += contadorMovimientos(movimientos, cochesNivelElegido) # Recojo el contador de movimientos validos
        cochesNivelElegido=moverCochestTablero(movimientos, cochesNivelElegido) # Cambio los valores dependiendo los movimientos que se introduzcan

        tablero=insertarCochesTablero(cochesNivelElegido)

        mostrarTablero(tablero) # Muestra el tablero

        if (tablero[int(coordenadasNivelElegido[1])*3][int(coordenadasNivelElegido[0])*5]!=" "): # Compruebo si hay algun coche en el la posicion objetivo
            print("ENHORABUENA, HA COMPLETADO EL NIVEL!")
            print("Movimientos: ", end="") # Muestro los movimientos
            print(f"{cont}  ", end="")
            if (nivelSinRecord):
                print("(NUEVO RECORD!)", end="")
                escribirRecords(cont, recordsPartida, nivelElegido-1)
            elif (cont<int(recordsPartida[nivelElegido-1]) or (int(recordsPartida[nivelElegido-1])==0)): # Si es menor guardo el dato en el fichero
                print("(NUEVO RECORD!)", end="")
                escribirRecords(cont, recordsPartida, nivelElegido-1)

            print()
            print("Desea pasar al siguiente nivel? [S/N]", end="")
            continuacion=input()
            if (continuacion=="N"):
                break
            elif (continuacion=="S"):
                continuado=True
                nivelesConRecord += 1
                nivelElegido+=1
                break
    if (continuacion=="N"): # Acabo la partica
        print("FINALIZO LA PARTIDA")
        break





