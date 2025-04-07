class Saludo:

    def __init__(self,mensaje):
        self.mensaje= mensaje

        def Mostrarmensaje():
            print(self.mensaje)
saludo =Saludo("Hola mundo")
saludo.Mostrarmensaje()

