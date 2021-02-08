import requests
import json
# link do conteudo explicando https://www.alura.com.br/artigos/consumindo-a-api-do-github-em-python
# esse código serve para visualizar o que tem no git de alguém 

class ListaDeRepositorios():

    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)


repositorios = ListaDeRepositorios('NahLima') #alteramos o nome aqui 
repositorios.imprime_repositorios()

