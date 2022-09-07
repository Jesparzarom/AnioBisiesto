# Autor Juan Esparza R.
# Archivo de funciones a exportar

from tabulate import tabulate as tabla
from datetime import datetime as fecha


def anio_actual():
    year = fecha.today().year
    return year


# Para calcular si el año es bisiesto(True) o no(False).
def isYearLeap(year):
    rest1, rest2 = (year % 4 == 0), (year % 100 != 0)
    rest3, rest4 = (year % 400 == 0), (year % 100 == 0)
    if rest1 and rest4 and rest3:
        return True
    elif rest1 and rest2:
        return True
    else:
        return False


# Otras funciones desactivadas.
'''
# para calcular los días de cada mes tomando en cuenta si es o no bisiesto
def daysInMonth(year, month):
    if (month == 1 or month == 3 or month == 5
            or month == 7 or month == 8
            or month == 10 or month == 12):
        days = 31
        return days

    elif (month == 2 or month == 4 or month == 6
          or month == 9 or month == 11):
        if (month == 2) and (isYearLeap(year) is True):
            days = 29
        elif (month == 2) and (isYearLeap(year) is False):
            days = 28
        else:
            days = 30
        return days

    else:
        return None
'''


# Resultado en calendario de los días si es o no bisiesto
def resultado(year):
    mes = ["MES", "Ene", "Feb", "Mar", "Abr", "May", "Jun",
           "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    dias = ["DIAS", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isYearLeap(year) is True:  # Si el año es bisiesto
        dias[2] = 29  # Se remplazan 28 dias por 29 dias en febrero.
        calendar = tabla([dias],
                         headers=mes,
                         tablefmt="fancy_grid")
        print('\n', f"AÑO: {year}".center(105, "•"))
        print(calendar)
        print(f"Es un año bisiesto, "
              f"por lo que el mes de febrero del {year} tiene un día más (28+1): 29 días".center(105, " "))
        print("•" * 105)

    elif isYearLeap(year) is False:  # Si el año no es bisiesto
        calendar = tabla([dias],
                         headers=mes,
                         tablefmt="fancy_grid")
        print('\n', f" AÑO: {year} ".center(105, "•"))
        print(calendar)
        print(f"No es un año bisiesto, "
              f"por lo que el mes de febrero del {year} tiene 28 días".center(105, " "))
        print("•" * 105)


def usuario():  # Función que devuelve la opción 1 ingresada por el usuario.
    print("•" * 105)
    print(
            "a) ¿Este año es año bisiesto?".ljust(35)
            + "b) ingresar un año y ver si es bisiesto".center(30)
            + "c) Salir del programa".rjust(29)
    )
    print("•" * 105)
    opcion = input("Ingresar opción ► ")
    return opcion


def si_no():  # Función con la opcion 2
    opcion2 = input("\nSeguir... ¿si/no? ► ".rjust(52))
    if opcion2 == "si" or opcion2 == "SI":
        return True
    else:
        return False


def portada():
    print("•" * 105)
    print("                                                                                         \n"
          "            .______    __       _______. __   _______      _______..___________.  ______   \n"
          "            |   _  \  |  |     /       ||  | |   ____|    /       ||           | /  __  \  \n"
          "            |  |_)  | |  |    |   (----`|  | |  |__      |   (----``---|  |----`|  |  |  | \n"
          "            |   _  <  |  |     \   \    |  | |   __|      \   \        |  |     |  |  |  | \n"
          "            |  |_)  | |  | .----)   |   |  | |  |____ .----)   |       |  |     |  `--'  | \n"
          "            |______/  |__| |_______/    |__| |_______||_______/        |__|      \______/  \n"
          "                                                                                 \n"
          "        ")
