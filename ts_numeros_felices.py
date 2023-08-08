def main():
    nueva_iteracion = True
    while nueva_iteracion:
        identificar_numero()
        nueva_iteracion = preguntar_iteracion()
        print("\n")
    print("Fin.")

def identificar_numero():
    numero = leer_numero()
    feliz = escribir_iteraciones(numero)
    resultado = "Es un número feliz :D" if feliz else "No es un número feliz :("
    print(resultado)
    
def leer_numero():
    entrada = ""
    while entrada.isnumeric() == False:
        entrada = input("Ingrese un número: ")
    retorno = int(entrada)
    if retorno < 0:
        retorno *= -1
    return retorno

def escribir_iteraciones(numero):
    resultados = []
    while numero != 1:
        resultado = sumar_cuadrados(numero)
        for elemento in resultados:
            if elemento == resultado:
                print('\nCiclo a partir de: '+str(resultado)+'\n')
                return False
        resultados.append(numero)
        numero = resultado
    return True

def sumar_cuadrados(numero):
    num_cadena = str(numero)
    feedback = ''
    resultado = 0
    contador = 0
    while contador < len(num_cadena):
        numero = int(numero)
        feedback += num_cadena[contador]+'²'
        feedback += ' = ' if contador == len(num_cadena)-1 else ' + '
        resultado += (numero%10)**2
        numero /= 10
        contador += 1
    feedback += str(resultado)
    print(feedback)
    return resultado
    
def preguntar_iteracion():
    entrada = ''
    while True:
        entrada = input('¿Otra vez?: [S/N] ')
        entrada = entrada.lower()
        if entrada == 's':
            return True
        elif entrada == 'n':
            return False
        else:
            print('Entrada no válida\n')
