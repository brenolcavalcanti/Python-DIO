import requests

def retorna_dados_cep (cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print (response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep

def retorna_dados_pokemon (pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # response = retorna_response('https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-tipo-de-participante-ptBR.asp')
    # print (response)
    # retorna_dados_cep(52040020)
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])

