import requests

class APIHandler:
    url="https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/main"

    @staticmethod
    def descargardatos():
        urlprofesores = APIHandler.url + "/profesores.json"
        archivosmaterias=["/materias2425-3.json", "/materias2526-1.json", "/materias2526-2.json"]
    
        try:
            resprofesores = requests.get(urlprofesores)
            if resprofesores.status_code!=200:
                print("Error al descargar profesores")
                return None, None
            
            datosprofesores = resprofesores.json()

            datosmaterias=[]
            codigosvistos=[]
            for nombrearchivo in archivosmaterias:
                urlmaterias=APIHandler.url+nombrearchivo
                reply=requests.get(urlmaterias)
                if reply.status_code==200:
                    materiasdelarchivo=respuesta.json()
                    for m in materiasdelarchivo:
                        codigoact=m["codigo"]
                        if codigoact not in codigvistos:
                            datosmaterias.append(m)
                            codigosvistos.append(codigo act)
                else:
                    print(f"No se pudo acceder a: {nombrearchivo}")
                    return None, None
            return datosprofesores, datosmaterias

        except Exception as error:
            print("\n Hubo un problema de conexion o lectura de datos")
            print(error)
            return None, None
