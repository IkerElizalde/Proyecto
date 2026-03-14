from apihandler import APIHandler
from clasesprofmat import *

class Bloques:
    def __init__(self, dia, horainicio, horafin, codigo):
        self.dia = dia
        self.horainicio = horainicio
        self.horafin = horafin
        self.codigo = codigo
        self.salones_ocupados = 0 

    def __str__(self):
        return f"{self.dia} ({self.horainicio} - {self.horafin})"
    
class Seccion:
    def __init__(self, codigo, cedulaprof, horario, salon=None):
        self.codigo=codigo
        self.cedulaprof=cedulaprof
        self.horario=horario
        self.salon=salon

    def __str__(self):
        if self.salon==None:
            return f"Materia: {self.codigo} | Profesor: {self.cedulaprof} | Horario: {str(self.horario)} | Salon: N/A"
        else:
            return f"Materia: {self.codigo} | Profesor: {self.cedulaprof} | Horario: {str(self.horario)} | Salon: {self.salon}"

class SistemaHorarios:
    def __init__(self, limite_salones=30):
        self.profesores = [] 
        self.materias = []  
        self.secciones = []  
        self.limite_salones = limite_salones
        self.bloques_disponibles = []
        self._cargar_bloques_maestros()

    def _cargar_bloques_maestros(self):
        datos_bloques = [
            ("Lunes y Miercoles", "7:00", "8:30", "LM_07:00"),
            ("Lunes y Miercoles", "8:45", "10:15", "LM_08:45"),
            ("Lunes y Miercoles", "10:30", "12:00", "LM_10:30"),
            ("Lunes y Miercoles", "12:15", "1:45", "LM_12:15"),
            ("Lunes y Miercoles", "2:00", "3:30", "LM_14:00"),
            ("Lunes y Miercoles", "3:45", "5:15", "LM_15:45"),
            ("Lunes y Miercoles", "5:30", "7:00", "LM_17:30"),
            ("Martes y Jueves", "7:00", "8:30", "MJ_07:00"),
            ("Martes y Jueves", "8:45", "10:15", "MJ_08:45"),
            ("Martes y Jueves", "10:30", "12:00", "MJ_10:30"),
            ("Martes y Jueves", "12:15", "1:45", "MJ_12:15"),
            ("Martes y Jueves", "2:00", "3:30", "MJ_14:00"),
            ("Martes y Jueves", "3:45", "5:15", "MJ_15:45"),
            ("Martes y Jueves", "5:30", "7:00", "MJ_17:30"),
        ]
        
        for d, hi, hf, cod in datos_bloques:
            nuevo_bloque = Bloques(d, hi, hf, cod)
            self.bloques_disponibles.append(nuevo_bloque)

    def buscar_profesor_por_cedula(self, cedula):
        for p in self.profesores:
            if p.cedula == cedula:
                return p
        return None
    
    def cargardatosapi(self):
        datos_profes, datos_materias = APIHandler.descargar_datos()

        if datos_profes is not None and datos_materias is not None:
            for p in datos_profes:
                nuevo_profe = Profesor(
                    p['nombre'], 
                    p['cedula'], 
                    p['correo'], 
                    p['materiasper'], 
                    p['materias']
                )
                self.profesores.append(nuevo_profe)

            for m in datos_materias:
                nueva_mat = Materia(
                    m['codigo'], 
                    m['nombre'], 
                    m['secciones']
                )
                self.materias.append(nueva_mat)
            
            print(f"Se cargaron {len(self.profesores)} profesores y {len(self.materias)} materias.")
            return True
        else:
            print("Error: No se pudieron obtener los datos de la API.")
            return False
        
    def buscar_materia_por_codigo(self, codigo):
        for m in self.materias:
            if m.codigo == codigo:
                return m
        return None
