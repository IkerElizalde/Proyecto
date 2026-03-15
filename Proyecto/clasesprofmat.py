class Profesor:
    def __init__(self, nombre, cedula, correo, materiaspermitidas, materias=None):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.materiaspermitidas = materiaspermitidas

        if materias is not None:
            self.materias = materias
        else:
            self.materias = []
        self.secciones_asignadas = 0 

    def agregarmateria(self, codigo):
        if codigo not in self.materias:
            self.materias.append(codigo)
            return True
        return False

    def eliminarmateria(self, codigo):
        if codigo in self.materias:
            self.materias.remove(codigo)
            return True
        return False

    def __str__(self):
        return f"Prof: {self.nombre} | CI: {self.cedula} | Límite: {self.materiaspermitidas}"

class Materia:
    def __init__(self, codigo, nombre, nrosecciones=0):
        self.codigo=codigo
        self.nombre=nombre
        self.nrosecciones=nrosecciones
    
    def modificar(self, nuevo_nrosec):
        self.nrosecciones=nuevo_nrosec

    def __str__(self):
        return f"Materia: {self.nombre} ({self.codigo}) | Secciones necesarias: {self.nrosecciones}"
    
