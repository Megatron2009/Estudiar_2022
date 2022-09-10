import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Function ask aleatory questions and return the result
def hazPregunta(pregunta, respuesta, gResultado):
    print(str(gResultado[0]) + ","+ str(gResultado[1])+ ": " + pregunta)
    esFallo = False
    while True:
        try:
            respuestaDada = input('Respuesta: ').upper()
            # comparar respuesta dada con la respuesta correcta
            if respuesta == respuestaDada:
                # add +1 to gresultado(0)
                if not esFallo:
                    gResultado[0] += 1
                return gResultado
            else:
                esFallo = True
                gResultado[1] += 1
                print('ERROR: La respuesta correcta es ' + respuesta)
        except ValueError:
            print('RESPUESTA INVALIDA')

# function random select questions and answers from a list
def preguntaAleatoria( preguntas, respuestas, gResultado ):
    number = random.randint(0, len(preguntas)-1)
    question = preguntas[number]
    answer = respuestas[number]
    gResultado = hazPregunta(question, answer.upper(), gResultado)
    del preguntas[number]
    del respuestas[number]
    return preguntas, respuestas, gResultado


# function load text file questions and answers
def leerFichero( fichero ):
    preguntas = []
    respuestas = []
    #read lines from file with accents
    with open( fichero , 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea == '':
                continue
            pregunta, respuesta = linea.split('=')
            preguntas.append(pregunta)
            respuestas.append(respuesta)
    return preguntas, respuestas

# function list all txt files in path
def listarFicheros( ):
    ficheros = []
    numero = 0
    for fichero in os.listdir( ):
        if fichero.endswith('.txt'):
            ficheros.append(fichero)
            print( str( numero ) + ": " + fichero )
            numero = numero + 1
    return ficheros

# Funtion menu request what txt file to read from path
def menu( maximo ):
    # request number of file to read
    while True:
        try:
            numero = int(input('Selecciona un fichero: '))
            if numero < 0 or numero >= maximo:
                print('Introduce un numero entre 0 y ' + str(maximo - 1))
            else:
                break
        except ValueError:
            print('Introduce un numero entre 0 y ' + str(maximo - 1))
    
    return numero

# lista de preguntas y respuestas
gPreguntas = []
gRrespuestas = []

# Resultado de las preguntas
gResultado = [0,0]

gFicheros = listarFicheros( )
numeroFichero = menu( len( gFicheros ) )
gPreguntas, gRespuestas = leerFichero( gFicheros[numeroFichero] )

try:
    imagen = gFicheros[numeroFichero].replace('.txt', '.png')   
    # if file exist
    if os.path.isfile(imagen):
        # load image
        img = mpimg.imread(imagen)
        # plot image
        imgplot = plt.imshow(img)
        plt.show( block=False )
    else:
        imagen = gFicheros[numeroFichero].replace('.txt', '.jpg')   
        if os.path.isfile(imagen):
            # load image
            img = mpimg.imread(imagen)
            # plot image
            imgplot = plt.imshow(img)
            plt.show( block=False )
        else:
            print("Ejercicio sin IMAGENES")        
except:
    print("FALLO AL CARGAR IMAGEN")

totalPreguntas = len(gPreguntas)
while len(gPreguntas) > 0:
    gPreguntas, gRespuestas, gResultado = preguntaAleatoria(gPreguntas, gRespuestas, gResultado)
print("TU NOTA ES: " + str(gResultado[0]/totalPreguntas*10) )