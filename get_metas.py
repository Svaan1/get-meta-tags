from bs4 import BeautifulSoup
import requests
import json

def get_metas(url):
    requested_url = requests.get(url) # Acessa a URL
    parsed_html = BeautifulSoup(requested_url.content, 'html.parser') # Deixa o HTML mais organizado
    meta_tags = parsed_html.find_all('meta') # Procura todas as Meta tags no HTML

    json_array = []
    for tag in meta_tags:
        if 'name' in tag.attrs.keys():
            json_array.append({'name':tag.attrs['name'], 'content':tag.attrs['content']}) # Adiciona ao Array todas as tags que
                                                                            #tenham nome em um dicionario junto ao seu conteúdo

    return json.dumps(json_array) # Retorna uma string formatada no padrão JSON

def main():
    pass
if __name__ == "__main__":
    main()
