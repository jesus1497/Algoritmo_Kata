from src.kata import (
    convierte_a_codigo,
    cuatro_palabras_a_codigo,
    letras_a_codigo,
    dos_palabras_a_codigo,
    tres_palabras_a_codigo,
)

# Usando pruebas


def test_convierte_a_codidog():
    assert convierte_a_codigo("Dunlin") == ("DUNL")
    assert convierte_a_codigo("Dovenkie") == ("DOVE")
    assert convierte_a_codigo("Ou") == ("OU")
    assert convierte_a_codigo("Gadwall") == ("GADW")
    assert convierte_a_codigo("American Wigeon") == ("AMWI")
    assert convierte_a_codigo("Eastern Meadowlark") == ("EAME")
    assert convierte_a_codigo("Eastern Screech-Owl") == ("EASO")
    assert convierte_a_codigo("Western Wood-Pewee") == ("WEWP")
    assert convierte_a_codigo("Red-tailed Hawk") == ("RTHA")
    assert convierte_a_codigo("White-winged Crossbill") == ("WWCR")
    assert convierte_a_codigo("Whip-poor-will") == ("WPWI")
    assert convierte_a_codigo("Black-crowned Night-Heron") == ("BCNH")
    assert convierte_a_codigo("American Swallow-tailed Kite") == ("ASTK")
    assert convierte_a_codigo("Northern Saw-whet Owl") == ("NSWO")


def test_letras_a_codigo():
    assert letras_a_codigo("Dunlin", 4) == ("DUNL")
    assert letras_a_codigo("Ou", 4) == ("OU")


def test_dos_palabras_a_codigo():
    assert dos_palabras_a_codigo("American Wigeon") == ("AMWI")
    assert dos_palabras_a_codigo("Eastern-Meadowlark") == ("EAME")


def test_tres_palabras_a_codigo():
    assert tres_palabras_a_codigo("Eastern Screech-Owl") == ("EASO")
    assert tres_palabras_a_codigo("Western Wood Pewee") == ("WWPE")
    assert tres_palabras_a_codigo("Red-tailed Hawk") == ("RTHA")
    assert tres_palabras_a_codigo("Whip-poor-will") == ("WPWI")


def test_cuatro_palabras_a_codigo():
    assert cuatro_palabras_a_codigo("American Swallow tailed kite") == ("ASTK")
    assert cuatro_palabras_a_codigo("Black-crowned Night-Heron") == ("BCNH")
    assert cuatro_palabras_a_codigo("Black crowned-Night-Heron") == ("BCNH")
    assert cuatro_palabras_a_codigo("Northern Saw-whet Owl") == ("NSWO")
    assert cuatro_palabras_a_codigo("Northern-Saw-whet Owl") == ("NSWO")
    assert cuatro_palabras_a_codigo("Black-crowned-Night-Heron") == ("BCNH")
