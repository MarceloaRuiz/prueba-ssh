from Paquete.modulo1 import Cliente
Cliente1 = Cliente("Juan", "profe@coder.com", 30, ["tecnologia", "moda", "farmacia"])
Cliente1.comprar("Laptop", "Wallmart")
print(Cliente1) # este print es para comprobar el metodo __str__
Cliente1.agregar_intereses("comida")
print(f"se han agregado intereses al cliente:{Cliente1.intereses}") #este print es para mostrar los intereses agregados al cliente

