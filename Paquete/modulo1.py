class Cliente:
    def __init__(self, nombre, mail, edad, intereses):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
        self.intereses = intereses
    def __str__(self):
        return f"Se ha creado al cliente {self.nombre}"

    lista_correo = []

    def comprar(self, articulo, tienda ):
        print(f"El cliente {self.nombre} ha comprado {articulo} en la tienda {tienda}.")
        print(f"Se le ha mandado un correo con su factura a {self.mail}")

    def agregar_intereses(self, intereses):
        self.intereses.append(intereses)
