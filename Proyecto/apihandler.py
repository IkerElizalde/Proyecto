import requests

class APIHandler:
    url="https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/main"

    @staticmethod
    def descargardatos():
        urlprofesores = APIHandler.url + "/profesores.json"
        urlmaterias = APIHandler.url + "/materias2526-2.json"

        try:
            resprofesores = requests.get(urlprofesores)
            resprofesores.raise_for_status()
            datosprofesores = resprofesores.json()

            respmaterias = requests.get(urlmaterias)
            respmaterias.raise_for_status()
            datosmaterias = respmaterias.json()

            return datosprofesores, datosmaterias

        except Exception as error:
            print("Hubo un problema al descargar los datos de GitHub:")
            print(error)
            return None, None
