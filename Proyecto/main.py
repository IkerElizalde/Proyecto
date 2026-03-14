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

def validarentrada(entrada)
  while True:
    in=input(entrada)
    if entrada.isdigit():
      opcion=int(entrada)
      return opcion
    else:
      print("Entrada invalida")

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
