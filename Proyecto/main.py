from clasehorarios import SistemaHorarios

def menuprincipal():
  print("-------------------------")
  print("Sistema de Horarios")
  print("-------------------------")
  print("1. Crear listas en blanco")
  print("2. Descargar los datos de la API en Github")
  print("3. Cargar un horario en CSV")
  print("4. Salir del programa")

def modulos():
  print("-------------------------")
  print("Modulos")
  print("-------------------------")
  print("1. Modulo de Profesores")
  print("2. Modulo de Materias")
  print("3. Generacion de Horarios")
  print("4. Modificacion de Horarios")
  print("5. Volver al menu principal")

def validarentrada(entrada):
  val=input(entrada)
  while True:
    inp=input(entrada)
    if val.isdigit():
      option=int(val)
      return option
    else:
      print("Entrada invalida")

def menuprofesores(sistema):
  while True:
    print("-------------------------")
    print("Modulo Profesores")
    print("-------------------------")
    print("1. Ver lista de profesores")
    print("2. Agregar un profesor")
    print("3. Eliminar un profesor")
    print("4. Modificar materias de un profesor")
    print("5. Volver a menu de modulos")
    option=validarentrada("Seleccione una opcion (1-5)")
    if option==1:
      print("\n---------Lista de Profesores---------")
      if not sistema.profesores:
        print("No hay profesores registrados en el sistema")
      else:
        for p in sistema.profesores:
          print(p)
          print(f"Materias que dicta: {p.materias}")
    
    elif option==2:
      print("\n---------Agregar Profesor---------")
      ci=input("Ingrese la cedula del profesor: ")
      if sistema.buscarprofesor(ci) is not None:
        print("Ya existe un profesor con esta cedula")
      else:
        nombre=input("Ingrese el nombre del profesor: ")
        correo=input("Ingrese el correo del profesor")
        limit=validarentrada("Ingrese el limite de materias permitidas (numero): ")
        nuevoprof=Profesor(nombre,cedula,correo,limite)
        sistema.profesores.append(nuevoprof)
        print(f"El profesor, {nombre}, ha sido agregado")
    
    elif option==3:
      print("\n---------Eliminar Profesor---------")
      ci=input("Ingrese la cedula del profesor: ")
      profe=sistema.buscarprofesor(ci)
      if profe is not None:
        sistema.profesores.remove(profe)
        print(f"El profesor, {profe.nombre}, ha sido eliminado")
      else:
        print("No hay profesor con esta cedula registrada")

    elif option==4:
      print("\n---------Modificar Materias de Profesor---------")
      ci=input("Ingrese la cedula del profesor: ")
      profe=sistema.buscarprofesor(ci)
      if profe is not None:
        print(f"El profesor seleccionado es: {profe.nombre}")
        print(f"Materias actuales: {profe.materias}")
        next=validarentrada("1. Agregar materia | 2. Eliminar materia")
        if next==1:
          codigo=input("Ingrese el codigo de la materia a agregar: ")
          if profe.agregarmateria(codigo):
            print("Materia agregada")
          else:
            print("El profesor ya tiene esta materia asignada")
        elif next==2:
          codigo=input("Ingrese el codigo de la materia a eliminar: ")
          if profe.eliminarmateria(codigo):
            print("Materia eliminada")
          else:
            print("El profesor no tenia esta materia asignada")
        else:
          print("Opcion invalida")
      else:
        print("No se hay registro de la cedula ingresada")
    
    elif option==5:
      print("Regresando al menu de modulos")
      break
    
    else:
      print("Entrada invalida, se debe ingresar un numero del 1 al 5")

def menumaterias(sistema):
  while True:
    print("-------------------------")
    print("Modulo Materias")
    print("-------------------------")
    print("1. Ver lista de materias")
    print("2. Agregar una materia")
    print("3. Eliminar una materia")
    print("4. Modificar cantidad de secciones")
    print("5. Volver al menu de modulos")
    option=validarentrada("Seleccione una opcion (1-5): ")

    if option==1:
      print(\n---------Lista de Materias---------)
      if not sistema.materias:
        print("No hay materias registradas")
      else:
        for m in sistema.materias:
          print(m)
    
    elif option==2:
      print(\n---------Agregar Materias---------)
      codigo=input("Ingrese el codigo de la materia: ")
      if sistema.buscarmateriascodigo(codigo) is not None:
        print("Ya existe una materia con este codigo")
      else:
        nombre=input("Ingresar nombre de la materia: ")
        secciones=validarentrada("Ingrese la cantidad de secciones necesarias (numero): ")
        nuevamateria=Materia(codigo,nombre,secciones)
        sistema.materias.append(nuevamateria)

    elif option==3:
      print(\n---------Eliminar Materias---------)
      codigo=input("Ingrese el codigo de la materia: ")
      materiaobj=sistema.buscarmateriacodigo(codigo)
      if materiaobj is not None:
        sistema.materias.remove(materiaobj)
        print(f"La materia: {materiaobj} ha sido eliminada")
      else:
        print("No hay registro de esa materia")
    
    elif option==4:
      print(\n---------Modificar Seccion de Materias---------)
      codigo=input("Ingrese el codigo de la materia: ")
      materiaobj=sistema.buscarmateriacodigo(codigo)
      if materiaobj is not None:
        print(f"Materia seleccionada: {materiaobj.nombre} ({materiaobj.codigo})")
        print(f"Secciones actuales: {materiaobj.seccion}")
        nuevaseccion=validarentrada("Ingrese la nueva cantidad de secciones: ")
        materiaobj.modificar(nuevaseccion)
        print("Cantidad de secciones actualizada exitosamente")
      else:
        print("No se encuentra alguna materia con ese codigo")
    
    elif option==5:
      print("Volviendo al menu de modulos")
      break
    
    else:
      print("Entrada debe ser un numero del 1 al 5")


def menumodulos(sistema):
  while True:
    modulos()
    option=validarentrada("Seleccione un modulo (1-5)")
    if option==1:
      menuprofesores(sistema)
    elif option==2:
      menumaterias(sistema)
    elif option==3:
      print("Horarios")
    elif option==4:
      print("Modificar Horarios")
    elif option==5:
      print("Volviendo al menu principal")
      break     
    else:
      print("Entrada invalida")

def main():
  sistema=SistemaHorarios()
  while True:
    menuprincipal()
    option=validarentrada("Seleccione una opcion (1-4)")
    if option==1:
      print("Lista en Blanco")
      sistema.profesores=[]
      sistema.materias=[]
      sistema.secciones=[]
      menumodulos(sistema)
    
    elif option==2:
      print("GitHub")
      if sistema.cargardatosapi():
        menumodulos(sistema)

    elif option==3:
      print("CSV")

    elif option==4:
      print("Saliendo")
      break
    
    else:
      print("Entrada invalida")


main()
