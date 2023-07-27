from scrap import scrap
from json_gen import excel_a_json
from categories import cat_faltan


def main():
    while True:
        try:
            print("\n----BIENVENIDO----")
            print("1) Actualizar o Crear Excel")
            print("2) Crear JSON en base al Excel")
            print("3) Salir")
            choice = int(input("Eleccion: "))
        except:
            print("La opcion debe ser un numero entre 1 o 3")

        if 1 <= choice <= 3:
            if choice == 1:
                scrap()
                print("Finalizo la creacion/actualizacion del Excel")
                print(cat_faltan)

            if choice == 2:
                excel_a_json("tools.xlsx", "tools.json")

            if choice == 3:
                print("Adios")
                break
        else:
            print("El número está fuera del rango de 1 a 3.")


main()
