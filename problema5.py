# Nombre: Carlos Arturo Suarez Valencia
# Grupo: 213022_79
# Programa: Ingeniería de Sistemas
# Autoría: Código fuente de autoría propia
# Problema 5 - Fase 5 - Control de horas trabajadas

def calcular_jornada(
    horas_lunes,
    horas_martes,
    horas_miercoles,
    horas_jueves,
    horas_viernes
):


    total_horas = (
        horas_lunes
        + horas_martes
        + horas_miercoles
        + horas_jueves
        + horas_viernes
    )

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


def main():

    print("==============================================")
    print(" CONTROL DE HORAS TRABAJADAS DEL EQUIPO")
    print("==============================================")

    matriz_recursos = [

        ["Carlos", 8, 8, 8, 8, 8],

        ["María", 9, 8, 9, 8, 9],

        ["Juan", 7, 8, 7, 8, 7],

        ["Ana", 10, 9, 9, 8, 9]

    ]

    print("\nRESULTADOS\n")

    for recurso in matriz_recursos:

        nombre_recurso = recurso[0]

        horas_lunes = recurso[1]
        horas_martes = recurso[2]
        horas_miercoles = recurso[3]
        horas_jueves = recurso[4]
        horas_viernes = recurso[5]

        total_horas, clasificacion = calcular_jornada(
            horas_lunes,
            horas_martes,
            horas_miercoles,
            horas_jueves,
            horas_viernes
        )

        print("----------------------------------------------")
        print(f"Nombre del recurso : {nombre_recurso}")
        print(f"Total de horas     : {total_horas}")
        print(f"Clasificación      : {clasificacion}")

    print("----------------------------------------------")


if __name__ == "__main__":
    main()