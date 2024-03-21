import requests 
import json 
def consulta_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

    print(resp['nome'], resp['fantasia'], resp['cnpj'], resp['email'], resp['telefone'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'])

consulta_cnpj('47960950000121')