from clasehorarios import SistemaHorarios
from clasesprofmat import Profesor,Materia

#---------------------------------------------------------------------------------------------->

def menuprincipal():
  print("-------------------------")
  print("---Sistema de Horarios---")
  print("-------------------------")
  print("1. Crear listas en blanco")
  print("2. Descargar los datos de la API en Github")
  print("3. Cargar un horario en CSV")
  print("4. Salir del programa")

#---------------------------------------------------------------------------------------------->

def validarentrada(entrada):
  while True:
    val=input(entrada)
    if val.isdigit():
      return int(val)
    else:
      print("Entrada invalida. Por favor, ingrese un numero.")

#---------------------------------------------------------------------------------------------->

def modulos():
  print("-------------------------")
  print("---------Modulos---------")
  print("-------------------------")
  print("1. Modulo de Profesores")
  print("2. Modulo de Materias")
  print("3. Generacion de Horarios")
  print("4. Modificacion de Horarios")
  print("5. Volver al menu principal")

#---------------------------------------------------------------------------------------------->

def menuprofesores(sistema):
  while True:
    print("-------------------------")
    print("----Modulo Profesores----")
    print("-------------------------")
    print("1. Ver lista de profesores")
    print("2. Ver un profesor en especifico")
    print("3. Agregar un profesor")
    print("4. Eliminar un profesor")
    print("5. Modificar materias de un profesor")
    print("6. Volver a menu de modulos")
    option=validarentrada("Seleccione una opcion (1-6): ")
    if option==1:
      print("\n---------Lista de Profesores---------")
      if not sistema.profesores:
        print("No hay profesores registrados en el sistema")
      else:
        for p in sistema.profesores:
          print(p)
          print(f"Materias que dicta: {p.materias}")
    
    elif option == 2:
      print("\n-----Profesor en especifico-----")  
      ci=validarentrada("Ingrese la cédula a buscar: ")
      profe = sistema.buscarprofesor(ci)
      if profe is not None:
        print("\n---Detalles del profesor---")
        print(f"Nombre: {profe.nombre}")
        print(f"Cedula: {profe.cedula}")
        print(f"Correo: {profe.correo}")
        print(f"Limite de materias: {profe.materiaspermitidas}")
        print(f"Materias asignadas: {profe.materias}")

      else: 
        print("No se encontró ningún profesor con esa cedula registrada")


    elif option==3:
      print("\n---------Agregar Profesor---------")
      ci=validarentrada("Ingrese la cedula del profesor: ")
      if sistema.buscarprofesor(ci) is not None:
        print("Ya existe un profesor con esta cedula")
      else:
        nombre=input("Ingrese el nombre del profesor: ")
        correo=input("Ingrese el correo del profesor: ")
        limite=validarentrada("Ingrese el limite de materias permitidas (numero): ")
        nuevoprofesor=Profesor(nombre,ci,correo,limite)
        sistema.profesores.append(nuevoprofesor)
        print(f"El profesor, {nombre}, ha sido agregado satisfactoriamente")
    

    elif option==4:
      print("\n---------Eliminar Profesor---------")
      ci=validarentrada("Ingrese la cedula del profesor: ")
      profe=sistema.buscarprofesor(ci)
      if profe is not None:
        materiasenpeligro=[]
        for materia_codigo in profe.materias:
          otrosprofesoresdisponibles=0
          for p in sistema.profesores:
            if p != profe and materia_codigo in p.materias:
              otrosprofesoresdisponibles +=1
            
          if otrosprofesoresdisponibles == 0:
            materiasenpeligro.append(materia_codigo)
        
        if len(materiasenpeligro) > 0:
          print("¡Advertencia!")
          print(f"Al eliminar a este profesor, las siguientes materias quedarán sin nadie que las dicte: {materiasenpeligro} ")
          confirmacion=input("¿Deseas continuar con la acción? (si/no): ")
          if confirmacion == "no":
            print("Se ha cancelado la acción")
            continue

        sistema.profesores.remove(profe)
        print(f"El profesor, {profe.nombre}, ha sido eliminado")
      else:
        print("No hay profesor con esta cedula registrada")


    elif option==5:
      print("\n---------Modificar Materias de Profesor---------")
      ci=validarentrada("Ingrese la cedula del profesor: ")
      profe=sistema.buscarprofesor(ci)
      if profe is not None:
        print(f"El profesor seleccionado es: {profe.nombre}")
        print(f"Materias actuales: {profe.materias}")
        next=validarentrada("1. Agregar materia | 2. Eliminar materia")
        if next==1:
          codigo=input("Ingrese el codigo de la materia a agregar: ")
          if profe.agregarmateria(codigo):
            print("Materia agregada satisfactoriamente")
          else:
            print("El profesor ya tiene esta materia asignada")
        elif next==2:
          codigo=input("Ingrese el codigo de la materia a eliminar: ")
          if profe.eliminarmateria(codigo):
            print("Materia eliminada satisfactoriamente")
          else:
            print("El profesor no tenia esta materia asignada")
        else:
          print("Opcion invalida")
      else:
        print("No hay registro de la cedula ingresada")
    

    elif option==6:
      print("Regresando al menu de modulos")
      break
    
    else:
      print("Entrada invalida, se debe ingresar un numero del 1 al 6")

#---------------------------------------------------------------------------------------------->

def menumaterias(sistema):
  while True:
    print("-------------------------")
    print("Modulo Materias")
    print("-------------------------")
    print("1. Ver lista de materias")
    print("2. Ver detalles de una materia específica")
    print("3. Agregar una materia")
    print("4. Eliminar una materia")
    print("5. Modificar cantidad de secciones")
    print("6. Volver al menu de modulos")
    option=validarentrada("Seleccione una opcion (1-6): ")

    if option==1:
      print("\n---------Lista de Materias---------")
      if not sistema.materias:
        print("No hay materias registradas")
      else:
        for m in sistema.materias:
          print(m)

    elif option == 2:
      print("\n-----Materia especifica-----")  
      codigo=input("Ingrese el código de la materia a buscar: ")
      mater = sistema.buscarmateriacodigo(codigo)
      if mater is not None:
        print("\n---Detalles de la materia---")
        print(f"Código: {mater.codigo}")
        print(f"Nombre: {mater.nombre}")
        print(f"Secciones requeridas: {mater.nrosecciones}")

        profescapacitados = []
        for p in sistema.profesores:
          if mater.codigo in p.materias:
            profescapacitados.append(p.nombre)
          
        if profescapacitados:
          print(f"A continuación, los profesores capacitados: {profescapacitados}")
        else:
          print("No hay profesores capacitados asignados aquí")
      else:
        print("No se encontró ninguna materia con ese código")
    
    elif option==3:
      print("\n---------Agregar Materias---------")
      codigo=input("Ingrese el codigo de la materia: ")
      if sistema.buscarmateriacodigo(codigo) is not None:
        print("Ya existe una materia con este codigo")
      else:
        nombre=input("Ingresar nombre de la materia: ")
        secciones=validarentrada("Ingrese la cantidad de secciones necesarias (numero): ")
        nuevamateria=Materia(codigo,nombre,secciones)
        sistema.materias.append(nuevamateria)

    elif option==4:
      print("---------Eliminar Materias---------")
      codigo=input("Ingrese el codigo de la materia: ")
      materiaobj=sistema.buscarmateriacodigo(codigo)

      if materiaobj is not None:
        profesores_desempleados = []
        for p in sistema.profesores:
          if codigo in p.materias and len(p.materias)==1:
            profesores_desempleados.append(p.nombre)

        if len(profesores_desempleados) > 0:
          print("¡Advertencia!")
          print(f"Al eliminar esta materia, los siguientes profesores se quedarán sin materias que dictar: {profesores_desempleados}")
          confirmacion=input("¿Deseas continuar con la acción? (si/no): ")

          if confirmacion == "no":
            print("Se ha cancelado la acción")
            continue

        sistema.materias.remove(materiaobj)

        for p in sistema.profesores:
          if codigo in p.materias:
            p.eliminarmateria(codigo)

        print(f"La materia {materiaobj.nombre} ha sido eliminada")

      else:
        print("No hay alguna materia registrada con ese codigo")


    elif option==5:
      print("\n---------Modificar Seccion de Materias---------")
      codigo=input("Ingrese el codigo de la materia: ")
      materiaobj=sistema.buscarmateriacodigo(codigo)

      if materiaobj is not None:
        print(f"Materia seleccionada: {materiaobj.nombre} - ({materiaobj.codigo})")
        print(f"Secciones actuales: {materiaobj.nrosecciones}")
        nuevaseccion=validarentrada("Ingrese la nueva cantidad de secciones: ")

        if nuevaseccion == 0:
          print("¡Advertencia!")
          print("Si continuas, se fijará el numero de secciones en cero")
          confirmacion=input("¿Deseas continuar?(si/no): ")

          if confirmacion == "no":
            print("Se ha cancelado la acción")
            continue
        materiaobj.modificar(nuevaseccion)
        print("Se ha actualizado la cantidad de secciones")

      else:
        print("No hay alguna materia registrada con ese codigo")
    
    elif option==6:
      print("Volviendo al menu de modulos")
      break
    
    else:
      print("Entrada debe ser un numero del 1 al 6")

#---------------------------------------------------------------------------------------------->

def menumodulos(sistema):
  while True:
    modulos()
    option=validarentrada("Seleccione un modulo (1-5): ")
    if option==1:
      menuprofesores(sistema)
    elif option==2:
      menumaterias(sistema)


    elif option==3:
      print("\n----------------------------------")    
      print("---------Generar Horarios---------")
      print("----------------------------------")  


      if len(sistema.materias)== 0 or len(sistema.profesores)== 0:
        print("Error, debes cargar materias y profesores antes de generar el horario")
        continue


      salonesdisp=validarentrada("Ingrese la cantidad de salones disponibles en la universidad: ")
      if salonesdisp <= 0:
        print("Error. Número sin sentido")
        continue


      sistema.generarhorario(salonesdisp)
      if sistema.secciones:
        menuconsultashorario(sistema)
         
    elif option==4:
      print("\n---------Modificar Horarios---------")
      modificarhorarios(sistema)
     
    elif option==5:
      print("Volviendo al menu principal")
      break    
    else:
      print("Entrada invalida")

#---------------------------------------------------------------------------------------------->

def menuconsultashorario(sistema):
  while True:
    print("\n----------------------------------")    
    print("---------Generar horarios---------")
    print("----------------------------------")
    print("1. Ver el horario de una materia")
    print("2. Ver el horario de un profesor")
    print("3. Ver salones asignados a una hora")
    print("4. Modificar asignacion")
    print("5. Volver al menu anterior")
    op=validarentrada("Seleccione: ")
    if op==1:
      cod=input("Ingrese el codigo de la materia: ").upper()
      m=sistema.buscarmateriacodigo(cod)
      print(f"\nHorario para: {m.nombre}")
      for s in sistema.secciones:
        if s.codigo==cod:
          p=sistema.buscarprofesor(s.cedulaprof)
          print(f"-{s.horario} | Profe: {p.nombre} | Salon: {s.salon}")
        else:
          print("Materia no encontrada")
    elif op==2:
      ci=validarentrada("Ingrese la cedula del profesor: ")
      p=sistema.buscarprofesor(ci)
      if p:
        print("\nHorario para: {p.nombre}")
        for s in sistema.secciones:
          if s.cedulaprof==ci:
            m=sistema.buscarmateriacodigo(s.codigo)
            print(f"-{s.horario} | Materia: {m.nombre} | Salon: {s.salon}")
          else:
            print("Profesor no encontrado")
    elif op==3:
      print("\nBloques disponibles:")
      for i, b in enumerate(sistema.bloquesdisp):
        print(f"{i+1}. {b}")
      indice=validarentrada("Seleccione el numero del bloque: ")-1
      if 0<=indice<len(sistema.bloquesdisp):
        bloquesel=sistema.bloquesdisp[indice]
        print(f"\nOcupacion para {bloquesel}:")
        for s in sistema.secciones:
          m=sistema.buscarmateriacodigo(s.codigo)
          print(f"-Salon {s.salon}: {m.nombre}")
      else:
        print("Bloque invalido")
    elif op==4:
      modificarhorarios(sistema)
    elif op==5:
      print("Volviendo al menu principal")
      break
    else:
      print("Opcion invalida")

#---------------------------------------------------------------------------------------------->

def modificarhorarios(sistema):
  if not sistema.secciones:
    print("\nError: Aún no se han generado horarios. Ve a la opción 3 primero.")
    return


  print("\n--- Seleccionar Materia ---")
 
  codinsecs = []
  for s in sistema.secciones:
    if s.codigo not in codinsecs:
        codinsecs.append(s.codigo)


  for i in range(len(codinsecs)):
    cod = codinsecs[i]
    mat = sistema.buscarmateriacodigo(cod)
    print(f"{i+1}. {mat.nombre} ({cod})")


  funmat = validarentrada("Seleccione el número de la materia: ")
  if funmat < 1 or funmat > len(codinsecs):
    print("Opción inválida.")
    return


  selectcode = codinsecs[funmat-1]
  objmateria = sistema.buscarmateriacodigo(selectcode)


  print(f"\n--- Seleccionar Sección de {objmateria.nombre} ---")


  materiaseccs = []
  for s in sistema.secciones:
    if s.codigo == selectcode:
      materiaseccs.append(s)


  for i in range(len(materiaseccs)):
    sec = materiaseccs[i]
    prof = sistema.buscarprofesor(sec.cedulaprof)
    print(f"{i+1}. Horario: {sec.horario} | Profesor: {prof.nombre} | Salón {sec.salon}")


  funsecc = validarentrada("Seleccione el número de la sección a modificar: ")
  if funsecc < 1 or funsecc > len(materiaseccs):
    print("Opción inválida.")
    return


  secselect = materiaseccs[funsecc-1]
  profactual = sistema.buscarprofesor(secselect.cedulaprof)
  bloqueactual = secselect.horario


  print("\n--- Opciones de modificación ---")
  print("1. Cambiar el profesor de esta sección")
  print("2. Cambiar el horario de esta sección")
  funmod = validarentrada("Seleccione una opción (1 o 2): ")


  if funmod == 1:
    print(f"\nProfesores disponibles para clases {objmateria.nombre} en el horario {bloqueactual.codigo}:")
    profesoresdisp = []


    for p in sistema.profesores:
      if selectcode in p.materias and p.cedula != profactual.cedula:
          if p.seccionesasignadas < p.materiaspermitidas:
            ocupado = False
            for s in sistema.secciones:
              if s.cedulaprof == p.cedula and s.horario.codigo == bloqueactual.codigo:
                ocupado = True
                break
            if ocupado == False:
              profesoresdisp.append(p)


    if len(profesoresdisp) == 0:
      print("No hay profesores disponibles para este horario")
    else:
      for i in range(len(profesoresdisp)):
        pdisp = profesoresdisp[i]
        print(f"{i+1}. {pdisp.nombre} (CI: {pdisp.cedula})")


      funprof = validarentrada("Seleccione el número del nuevo profesor: ")
      if funprof >= 1 and funprof <= len(profesoresdisp):
        nuevoprof = profesoresdisp[funprof-1]


        secselect.cedulaprof = nuevoprof.cedula
        profactual.seccionesasignadas -= 1
        nuevoprof.seccionesasignadas += 1


        print(f"\n¡Éxito! Profesor cambiado a {nuevoprof.nombre}.")
      else:
        print("Opción inválida")


  elif funmod == 2:
    print("\nHorarios con salones disponibles: ")
    # Cambié sistema.salonesdisp a sistema.limitesalones asumiendo la variable de la clase Horarios
    limitesalones = sistema.limitesalones
    bloquesdisp = []


    for b in sistema.bloquesdisp:
      if b.salonesocupados < limitesalones and b.codigo != bloqueactual.codigo:
        bloquesdisp.append(b)


    if len(bloquesdisp) == 0:
      print("No hay otros horarios disponibles.")
    else:
      for i in range(len(bloquesdisp)):
        bdisp = bloquesdisp[i]
        print(f"({i+1}) {bdisp} (Ocupación: {bdisp.salonesocupados}/{limitesalones})")


      funbloque = validarentrada("Seleccione el número del nuevo horario: ")
      if funbloque >= 1 and funbloque <= len(bloquesdisp):
          nuevobloque = bloquesdisp[funbloque-1]


          print(f"\nProfesores disponibles para el nuevo horario: ")
          profdispbloque = []


          for p in sistema.profesores:
            if selectcode in p.materias:
              if p.cedula == profactual.cedula or p.seccionesasignadas < p.materiaspermitidas:
                ocupado = False
                for s in sistema.secciones:
                  if s.cedulaprof == p.cedula and s.horario.codigo == nuevobloque.codigo:
                    ocupado = True
                    break


                if ocupado == False:
                  profdispbloque.append(p)


          if len(profdispbloque) == 0:
            print("No hay profesores disponibles para este horario. Operación cancelada.")
          else:
            for i in range(len(profdispbloque)):
              pdisp = profdispbloque[i]
              print(f"{i+1}. {pdisp.nombre} (CI: {pdisp.cedula})")


            funprof2 = validarentrada("Seleccione el profesor que dará la clase: ")
            if funprof2 >= 1 and funprof2 <= len(profdispbloque):
              nuevoprof = profdispbloque[funprof2-1]


              bloqueactual.salonesocupados -= 1
              nuevobloque.salonesocupados += 1


              secselect.horario = nuevobloque
              secselect.salon = nuevobloque.salonesocupados


              if nuevoprof.cedula != profactual.cedula:
                  secselect.cedulaprof = nuevoprof.cedula
                  profactual.seccionesasignadas -= 1
                  nuevoprof.seccionesasignadas += 1


              print("\n¡Éxito! Horario actualizado correctamente.")
            else:
              print("Operación inválida.")
      else:
        print("Operación inválida.")
  else:
    print("Operación inválida.")


  print("\n------ Horario Resultante ------")
  for s in sistema.secciones:
      m = sistema.buscarmateriacodigo(s.codigo)
      p = sistema.buscarprofesor(s.cedulaprof)
      print(f"{s.horario} - {m.nombre} | Profesor: {p.nombre} | Salón: {s.salon}")

      


#---------------------------------------------------------------------------------------------->

def main():
  sistema=SistemaHorarios()
  while True:
    menuprincipal()
    option=validarentrada("Seleccione una opcion (1-4): ")
    if option==1:
      print("Lista en Blanco")
      sistema.profesores=[]
      sistema.materias=[]
      sistema.secciones=[]
      menumodulos(sistema)
   
    elif option==2:
      print("Cargando los datos del GitHub")
      if sistema.cargardatosapi():
        menumodulos(sistema)

    elif option==3:
      print("CSV")
      # Se debe pasar a cargar el horario
    elif option==4:
      print("Saliendo")
      break
    
    else:
      print("Entrada invalida")


main()

