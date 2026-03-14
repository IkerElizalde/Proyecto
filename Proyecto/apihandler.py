import requests

class APIHandler:
    url="https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/main"

    @staticmethod
    def descargardatos():
        url_profesores = APIHandler.url + "/profesores.json"
        url_materias = APIHandler.url + "/materias.json"

        try:
            respuesta_profesores = requests.get(url_profesores)
            respuesta_profesores.raise_for_status()
            datos_profesores = respuesta_profesores.json()

            respuesta_materias = requests.get(url_materias)
            respuesta_materias.raise_for_status()
            datos_materias = respuesta_materias.json()

            return datos_profesores, datos_materias

        except Exception as error:
            print("Hubo un problema al descargar los datos de GitHub:")
            print(error)
            return None, None
