# Kata - Códigos de cuatro letras para las aves
# Optimización de Código


def convierte_a_codigo(texto):
    cadena_3_caracteres = 0
    longitud_texto = len(texto)
    for i in range(longitud_texto):
        valido = texto[i].find(" ") != -1
        valido_2 = texto[i].find("-") != -1
        if valido or valido_2:
            cadena_3_caracteres = cadena_3_caracteres + 1
    texto_con_1_caracter = cadena_3_caracteres == 1
    texto_con_2_caracteres = cadena_3_caracteres == 2
    texto_con_3_caracteres = cadena_3_caracteres == 3
    if texto_con_3_caracteres:
        return cuatro_palabras_a_codigo(texto)
    elif texto_con_2_caracteres:
        return tres_palabras_a_codigo(texto)
    elif texto_con_1_caracter:
        return dos_palabras_a_codigo(texto)
    limite_letras_palabra = 4
    return letras_a_codigo(texto, limite_letras_palabra)


def letras_a_codigo(palabras, limite_letras_palabra):
    return palabras[:limite_letras_palabra].upper()


def dos_palabras_a_codigo(palabras):
    caracter_guion = palabras.find("-")
    valido_guion = caracter_guion != -1
    if valido_guion:
        palabras = palabras.split("-")
    else:
        palabras = palabras.split()
    codigo = ""
    limite_letras_palabra = 2
    longitud_palabras = len(palabras)
    for i in range(longitud_palabras):
        codigo = codigo + letras_a_codigo(palabras[i], limite_letras_palabra)
    return codigo


def tres_palabras_a_codigo(palabras):
    caracter_guion = palabras.find(" ")
    valido_guion = caracter_guion != -1
    if valido_guion:
        palabras = palabras.split()
    else:
        palabras = palabras.split("-")
    codigo = ""
    longitud_palabras = len(palabras)
    rango_3 = longitud_palabras == 3
    rango_2 = longitud_palabras == 2
    for i in range(longitud_palabras):
        if rango_3:
            if i == 2:
                limite_letras_palabra = 2
                codigo = codigo + letras_a_codigo(palabras[i], limite_letras_palabra)
            else:
                limite_letras_palabra = 1
                codigo = codigo + letras_a_codigo(palabras[i], limite_letras_palabra)
        elif rango_2:
            validacion = palabras[i].find("-") == -1
            if validacion:
                limite_letras_palabra = 2
                codigo = codigo + letras_a_codigo(palabras[i], limite_letras_palabra)
            elif not validacion:
                auxiliar = palabras[i].split("-")
                longitud_auxiliar = len(auxiliar)
                limite_letras_palabra = 1
                for j in range(longitud_auxiliar):
                    codigo = codigo + letras_a_codigo(auxiliar[j], limite_letras_palabra)
    return codigo


def cuatro_palabras_a_codigo(palabras):
    palabras = palabras.split()
    codigo = ""
    longitud_palabras = len(palabras)
    limite_letras_palabra = 1
    for i in range(longitud_palabras):
        auxiliar = palabras[i].split("-")
        longitud_auxiliar = len(auxiliar)
        for j in range(longitud_auxiliar):
            codigo = codigo + letras_a_codigo(auxiliar[j], limite_letras_palabra)
    return codigo
