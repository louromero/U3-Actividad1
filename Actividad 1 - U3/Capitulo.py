class Capitulo:
    __titulo=''
    __cantidadPaginas=0

    def __init__(self, titulo,cantidadPaginas):
        self.__titulo=titulo
        self.__cantidadPaginas=cantidadPaginas

    def getTituloC(self):
        return self.__titulo

    def getPaginas(self):
        return self.__cantidadPaginas

    def mostrarCapitulo(self):
        print("\nCapitulo: {}\nCantidad de Paginas: {}".format(self.__titulo, self.__cantidadPaginas))

    def acumPaginas(self, acum):
        acum+=self.__cantidadPaginas
        return acum