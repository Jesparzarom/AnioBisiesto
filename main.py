# Autor Juan Esparza R.

from funciones import (resultado, usuario, portada, si_no, anio_actual)

portada()
bucle = True
while bucle:
    opcion = usuario()
    if opcion == "A" or opcion == "a":
        year = anio_actual()
        resultado(year)
        bucle = si_no()

    elif opcion == "B" or opcion == "b":
        year = int(input("Ingresa el año ► "))
        resultado(year)
        bucle = si_no()

    else:
        bucle = False
print("¡Hasta pronto!".center(105, "."))
