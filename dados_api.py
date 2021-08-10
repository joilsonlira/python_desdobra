
import requests
import manager_db as db
import json

#dados obrigatorios
token = "3umgtsxAsEcSCvU" #Data de expiração: 24/08/2021
loteria = ["megasena","quina","lotofacil","lotomania"] #,"duplasena","timemania","diadesorte","federal","loteca","lotogol","supersete"

#dados opcionais
concurso = 2398
data = "" #Formato dd/MM/yyyy
def buscar_dados():
    request = requests.get("https://apiloterias.com.br/app/resultado?loteria="+loteria[0]+"&token="+ token)
    
    obj = request.json()

    print(obj)
    
if __name__ == '__main__':
    buscar_dados()