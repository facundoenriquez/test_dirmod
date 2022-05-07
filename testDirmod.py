
# Declaracion

secuencia_de_numeros = [
    [' '],  # Letra correspondientes al 0
    [],  # Letra correspondientes al 1
    ['a', 'b', 'c'],  # Letras correspondientes al 2
    ['d', 'e', 'f'],  # Letras correspondientes al 3
    ['g', 'h', 'i'],  # Letras correspondientes al 4
    ['j', 'k', 'l'],  # Letras correspondientes al 5
    ['m', 'n', 'o'],  # Letras correspondientes al 6
    ['p', 'q', 'r', 's'],  # Letras correspondientes al 7
    ['t', 'u', 'v'],  # Letras correspondientes al 8
    ['w', 'x', 'y', 'z'],  # Letras correspondientes al 9
]


def calcular_secuencia_de_numeros(mensaje):
    secuencia_total = ''

    # por cada letra dentro del mensaje
    for letra in mensaje:
        # recorro el array de numeros 
        for idx, numero in enumerate(secuencia_de_numeros):
            # veo a que numero corresponde la letra
            if letra in numero:
                # tomamos el indice donde se encuentra la letra en el array correspondiente al numero actual
                # para saber que cantidad de veces hay que presionar el numero
                cantidades_a_presionar = numero.index(letra) + 1
                # el numero a presionar seria el indice actual detro de secuencia_de_numeros
                numero_a_presionar = str(idx)
                if secuencia_total[-1:] == numero_a_presionar:
                    secuencia_total += ' '
                secuencia_total += cantidades_a_presionar * numero_a_presionar
                print("Letra: " + letra + " - Cantidades a presionar: " +
                      str(cantidades_a_presionar) + " - Numero: " + numero_a_presionar)

    return secuencia_total

######################################## MAIN ########################################

try:

    mensaje = str(
        input("Ingrese un mensaje para calcular su secuencia en numeros: "))

    mensaje = mensaje.strip()

    secuencia_total = calcular_secuencia_de_numeros(mensaje)

    print(secuencia_total)

except Exception as e:
    print(e)
