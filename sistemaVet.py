import datetime 
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__medicamento= []

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n 


   
class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}

    def eliminarMedi(self,nombreMedicamento): 
        self:__medicamento.remove(nombreMedicamento) 

#Creamos los siguientes métodos tanto para el diccionario de caninos como de felinos 

    def verificarExisteCaninos(self,historia):
        if historia in self.__lista_caninos:
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        else: 
            return False

    def verificarExisteFelinos(self,historia):
        if historia in self.__lista_felinos:
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        else: 
            return False

    def verNumeroFelinos(self):
        return len(dict.keys(self.__lista_felinos))

    def verNumeroCaninos(self): 
        return len(dict.keys(self.__lista_caninos))

    def ingresarMascota(self,tipo,mascota):
        if tipo == 1:
            self.__lista_felinos[historia]=mascota
        elif tipo == 2:
            self.__lista_caninos[historia]=mascota

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_caninos: 
            a=self.lista_caninos[historia]
            return a.verFecha()
        elif historia in self.__lista_felinos: 
            a = self.lista_felinos[historia]
            return a.verFecha

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_caninos: 
            a=self.lista_caninos[historia]
            return a.verMedicamento()
        elif historia in self.__lista_felinos: 
            a = self.lista_felinos[historia]
            return a.verMedicamento()

    def eliminarMascota(self, historia):
        if historia in self.__lista_caninos: 
            a=self.lista_caninos[historia]
            del a
            return True
        elif historia in self.__lista_felinos: 
            a = self.lista_felinos[historia]
            del a
            return True  #eliminado con exito
        return False 
    
    def eliminarMedicamento(self, historia,nombreMedicamento): 
        if historia in self.__lista_caninos: 
            a=self.lista_caninos[historia]
            a.self.__medicamento.removed(nombreMedicamento)
            return True
        elif historia in self.__lista_felinos: 
            a=self.lista_felinos[historia]
            a.self.__medicamento.removed(nombreMedicamento)
            return True  #eliminado con exito
        return False 
        
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,d):
        self.__dosis = d 
        