# Course: Curso de Python 3 do básico ao avançado - com projetos reais | Udemy


Uma coisa comum de ocorrer quando trabalhamos com o bs4.BeautifulSoup. é problemas com caracteres. Isso ocorre devido a uma falha na detecção do encoding.

Eu explico mais sobre codificação de caracteres no artigo abaixo:

[https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/](https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/)

Caso queira mudar a codificação de caracteres, envie os bytes diretamente para o BeautifulSoup e passe o valor da codificação de caracteres no atributo "from\_encoding". Exemplo (para utf-8):

```python
    BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
```

Perceba que troquei "response.text" para "response.content" para obter os bytes ao invés da string.

Nesse caso, nosso código completo das aulas anteriores ficaria assim:

```python
import re
    
import requests
from bs4 import BeautifulSoup
    
url = 'http://127.0.0.1:3333/'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
    
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
    
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
```

Assumindo que a codificação de caracteres da página é utf-8.

Você pode detectar isso no HTML pela tag meta charset dentro da `<head>`:

```html
<meta charset="UTF-8">
```

## Recursos para esta aula

[Código](https://github.com/luizomf/cursopython2023/commit/d2280a46aa2357879bad34176171acd236f8d0e2)