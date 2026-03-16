from apihandler import APIHandler
from clasesprofmat import *

class Bloques:
    def __init__(self, dia, horainicio, horafin, codigo):
        self.dia = dia
        self.horainicio = horainicio
        self.horafin = horafin
        self.codigo = codigo
        self.salonesocupados = 0 

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
    def __init__(self, limitesalones=30):
        self.profesores = [] 
        self.materias = []  
        self.secciones = []  
        self.limitesalones = limitesalones
        self.bloquesdisp = []
        self.cargarbloques()

    def cargarbloques(self):
        datosbloques = [
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
        
        for d, hi, hf, cod in datosbloques:
            nuevobloque = Bloques(d, hi, hf, cod)
            self.bloquesdisp.append(nuevobloque)

    
    def cargardatosapi(self):
        datosprofes, datosmaterias = APIHandler.descargardatos()

        if datosprofes is not None and datosmaterias is not None:
            for p in datosprofes:
                nuevoprofe = Profesor(
                    p['nombre'], 
                    p['cedula'], 
                    p['correo'], 
                    p['materiasper'], 
                    p['materias']
                )
                self.profesores.append(nuevoprofe)

            for m in datosmaterias:
                nuevamat = Materia(
                    m['codigo'], 
                    m['nombre'], 
                    m['secciones']
                )
                self.materias.append(nuevamat)
            
            print(f"Se cargaron {len(self.profesores)} profesor/es y {len(self.materias)} materia/s.")
            return True
        else:
            print("Error: No se pudieron obtener los datos de la API.")
            return False
        

    def buscarprofesor(self, cedula):
        for p in self.profesores:
            if p.cedula == cedula:
                return p
        return None
    
    def buscarmateriacodigo(self, codigo):
        for m in self.materias:
            if m.codigo == codigo:
                return m
        return None

    def generarhorario(self, salonesdisp):
        self.secciones=[]
        for b in self.bloquesdisp:
            b.salonesocupados=0
        for p in self.profesores:
            p.seccionesasignadas=0

        seccionescreadas=0
        seccionesfallidas=0

        for materia in self.materias:
            if int(materia.nrosecciones)==0:
                continue
            for numseccion in range(1,int(materia.nrosecciones)+1):
                asignado=False
                for p in self.profesores:
                    if materia.codigo in p.materias and p.seccionesasignadas<p.materiaspermitidas:
                        for bloque in self.bloquesdisp:
                            if bloque.salonesocupados<salonesdisp:
                                libre=True
                                for s in self.secciones:
                                    if s.cedulaprof==p.cedula and s.horario.codigo==bloque.codigo:
                                        libre=False
                                        break
                                if libre:
                                    nuevasec=Seccion(materia.codigo, p.cedula, bloque, salon=bloque.salonesocupados+1)
                                    self.secciones.append(nuevasec)
                                    bloque.salonesocupados+=1
                                    p.seccionesasignadas+=1
                                    asignado=True
                                    seccionescreadas+=1
                                    break
                            if asignado:
                                break
                        if not asignado:
                            print(f"No se puede asignar {materia.nombre} (Seccion {numseccion})")
                            seccionesfallidas+=1

        print(f"Secciones creadas: {seccionescreadas}")
        if seccionesfallidas>0:
            print(f"Secciones fallidas: {seccionesfallidas}")
            
                            
                


    


