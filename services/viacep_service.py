import requests

def buscar_endereco_por_cep(cep: str):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        data = response.json()
        return {
            "logradouro": data.get("logradouro"),
            "cidade": data.get("localidade")
        }
    else:
        raise Exception("Erro ao buscar CEP")
