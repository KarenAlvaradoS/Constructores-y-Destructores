class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        Inicializa los atributos nombre y edad.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre} ha sido creada.")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Realiza tareas de limpieza (si aplica).
        """
        print(f"Persona {self.nombre} ha sido eliminada.")

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# Eliminar las instancias manualmente (opcional)
del persona1
del persona2
