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
      print("---------Lista de Profesores---------")
      if not sistema.profesores:
        print("No hay profesores registrados en el sistema")
      else:
        for p in sistema.profesores:
          print(p)
          print(f"Materias que dicta: {p.materias}")
    
    elif option==2:
      print("---------Agregar Profesor---------")
      ci=input("Ingrese la cedula del profesor: ")
      if sistema.buscarprofesor(ci) is not None:
        print("Ya existe un profesor con esta cedula")
      else:
        nombre=input("Ingrese el nombre del profesor: ")
        correo=input("Ingrese el correo del profesor")
        limit=validarentrada("Ingrese el limite de materias permitidas (numero): ")
        nuevoprof=Profesor(nombre,cedula,correo,limite)


def menumodulos(sistema):
  while True:
    modulos()
    option=validarentrada("Seleccione un modulo (1-5)")
    if option==1:
      print("Profesores")
    elif option==2:
      print("Materias")
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
