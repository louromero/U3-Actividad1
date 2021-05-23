from ManejadorLibro import ManejadorLibro

def imprimir():
    print(" ")
    print("------------------------------MENU------------------------------")
    print("1. INGRESAR IDENTIFICADOR PARA MOSTRAR INFORMACION")
    print("2. INGRESE PALABRA PARA MOSTRAR TITULO O CAPITULO DONDE APARECE")
    print("0. SALIR")
    print("----------------------------------------------------------------\n")

def menu(manejador):
    band =True
    while band:
        imprimir()
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            identificador=int(input("\nIngrese identificador: "))
            manejador.buscarLibro(identificador)

        elif opcion == 2:
            palabra=input("\nIngrese palabra: ")
            manejador.buscarPalabra(palabra)

        elif opcion == 0:
            print("\nChau :)")
            band=False

        else:
            print("\nOpcion no valida.")

if __name__ == '__main__':
    manejador=ManejadorLibro()
    manejador.testLibros()
    print("\n-----------------LISTA DE LIBROS-------------------")
    manejador.mostrarLista()
    menu(manejador)