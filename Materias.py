class Materia:
    #Precondiciones + precondiciones de los casos de uso
    #Atributos: encapsulamiento 
    __parcial1 = 0.0
    __parcial2 = 0.0
    __parcial3 = 0.0
    __calificacionFinal = 0.0

    #Metodos: 1 metodo por caso de uso
    # def nombreCasoUso(self, parametros(precondiciones separadas por comas))
    def calcularPromedioPonderado(self, parcial1, parcial2, parcial3):
        self.__parcial1 = parcial1
        self.__parcial2 = parcial2
        self.__parcial3 = parcial3
        self.__calificacionFinal = (self.__parcial1 * 0.2 + self.__parcial2 * 0.3 + self.__parcial3 * 0.5)
        return self.__calificacionFinal
