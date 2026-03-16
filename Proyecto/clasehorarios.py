import csv
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
                # Combinamos Nombre y Apellido para no perder info
                nombre_completo = f"{p['Nombre']} {p['Apellido']}"
                nuevoprofe = Profesor(
                    nombre_completo, 
                    p['Cedula'], 
                    p['Email'], 
                    p['Max Carga'], 
                    p['Materias']
                )
                self.profesores.append(nuevoprofe)

            for m in datosmaterias:
                nuevamat = Materia(
                    m['Código'], 
                    m['Nombre'], 
                    m['Secciones'] 
                )
                self.materias.append(nuevamat)
            
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
        for p in self.profesores:
            p.seccionesasignadas = 0
        for b in self.bloquesdisp:
            b.salonesocupados = 0

        self.secciones = []
        seccionescreadas = 0
        fallasprofesor = {}
        fallassalon = {}

        for materia in self.materias:
            nro_necesario = int(materia.nrosecciones)
            for i in range(nro_necesario):
                asignada = False
                profes_aptos = []
                for p in self.profesores:
                    sabe_dar_materia = materia.codigo in p.materias
                    tiene_cupo = p.seccionesasignadas < p.materiaspermitidas
                    if sabe_dar_materia and tiene_cupo:
                        profes_aptos.append(p)
                if not profes_aptos:
                    if materia.nombre in fallasprofesor:
                        fallasprofesor[materia.nombre] += 1
                    else:
                        fallasprofesor[materia.nombre] = 1
                    continue
                for bloque in self.bloquesdisp:
                    if bloque.salonesocupados < salonesdisp:
                        for p in profes_aptos:
                            choque = False
                            for s in self.secciones:
                                if s.cedulaprof == p.cedula and s.horario.codigo == bloque.codigo:
                                    choque = True
                                    break 
                            if not choque:
                                nuevasec = Seccion(materia.codigo, p.cedula, bloque, salon=bloque.salonesocupados + 1)
                                self.secciones.append(nuevasec)
                                p.seccionesasignadas += 1
                                bloque.salonesocupados += 1
                                seccionescreadas += 1
                                asignada = True
                                break 
                    if asignada:
                        break 
                if not asignada:
                    if materia.nombre in fallassalon:
                        fallassalon[materia.nombre] += 1
                    else:
                        fallassalon[materia.nombre] = 1

        print(f"\nSecciones creadas: {seccionescreadas}")
        
        print("\nSecciones cerradas por falta de profesores:")
        if not fallasprofesor:
            print("Ninguna")
        else:
            for mat, cant in fallasprofesor.items():
                print(f"-{mat}: {cant} seccion(es)")

        print("\nSecciones no asignadas por falta de salones:")
        if not fallassalon:
            print("Ninguna")
        else:
            for mat, cant in fallassalon.items():
                print(f"-{mat}: {cant} seccion(es)")
            
                            
    def guardarhorario_csv(self,nombrearchivo):
        try:
            with open(nombrearchivo,mode='w',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                #Para los encabezados:
                writer.writerow(["Materia","Cedula_Profesor","Bloque_Codigo","Salon"])

                #Secciones generadas:
                for s in self.secciones:
                    writer.writerow([s.codigo],[s.cedulaprof],[s.horario.codigo],[s.salon])

            print(f"\n Horario guardado en {nombrearchivo}")

        except Exception as er:
            print(f"Se ha producido un error al guardar el archivo: {er}")

        def cargarhorario_csv(self,nombrearchivo):
            try:
                with open(nombrearchivo,mode='r',encoding='utf-8') as f:
                    reader= csv.DictReader(f)
                    self.secciones = []
                    
                    #Para reiniciar/resetear los contadores:

                    for b in self.bloquesdisp:
                        b.salonesocupados = 0
                    for p in self.profesores:
                        p.seccionesasignadas = 0
        
                    for row in reader:
                        codmat = row["Materia"]
                        cedulprof=int(row["Cedula_Profesor"])
                        codbloque=row["Bloque_Codigo"]
                        salon=int(row["Salon"])

                        #Para ubicar el objeto del bloque 
                        bloque_obj=None
                        for b in self.bloquesdisp:
                            if b.codigo == codbloque:
                                bloque_obj = b
                                break
                        
                        #Si sí existe, reconstruimos la sec
                        if bloque_obj is not None:
                            nueva_sec=Seccion(codmat,cedulprof,bloque_obj,salon)
                            self.secciones.append(nueva_sec)
                            bloque_obj.salonesocupados += 1

                            #Actualizacion secciones asignadas profe
                            prof = self.buscarprofesor(cedulprof)
                            if prof is not None:
                                prof.seccionesasignadas += 1

                print(f"\n Horario cargado desde: '{nombrearchivo}'")
                return True 
            

            except FileNotFoundError:
                print(f"\n Error: el archivo '{nombrearchivo}' no existe")
                return False
            except Exception as er:
                print(f"\n Error al cargar el archivo: {er}")
                return False


    




