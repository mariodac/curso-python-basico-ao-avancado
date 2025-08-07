# Corrigindo o erro 403 - Verificação CSRF falhou. Pedido cancelado

Depois de gravar as nossas últimas aulas acima, percebi que nosso servidor estava com erros em todos os formulários.

O erro que ocorre é:

```
Proibido (403)Verificação CSRF falhou. Pedido cancelado.
```

Isso ocorre porque existe uma divergência de chamadas `http` e `https` para o Django e ele não tem como saber que nossas chamadas agora são feitas via `https`. Portanto, a validação de CSRF falha porque http://django.otaviomiranda.com é diferente de https://django.otaviomiranda.com.

Perceba essa configuração da _location_ em nosso nosso arquivo: `/etc/nginx/sites-available/agendadomainssl`

```
location / {  proxy_pass http://unix:/run/agenda.socket;  proxy_http_version 1.1;  proxy_set_header Upgrade $http_upgrade;  proxy_set_header Connection 'upgrade';  proxy_set_header Host $host;  proxy_cache_bypass $http_upgrade;}
```

Em nenhum momento estamos informando ao Django que a conexão vem via HTTPS. Inclusive, a chamada do Nginx para o Django é feita na primeira linha via http:

```
proxy_pass http://unix:/run/agenda.socket;
```

Isso não é um problema, visto que estamos dentro do mesmo servidor. Mas pode causar esse tipo de problema que estamos tendo.

A solução aqui é adicionar uma nova linha em nosso arquivo de configuração (vou fazer um passo-a-passo no final):

```
proxy_set_header X-Forwarded-Proto https;
```

E nosso _location_ completo ficaria assim:

```
location / {  proxy_pass http://unix:/run/agenda.socket;  proxy_http_version 1.1;  proxy_set_header Upgrade $http_upgrade;  proxy_set_header Connection 'upgrade';  proxy_set_header Host $host;  proxy_set_header X-Forwarded-Proto https; # ESSA  proxy_cache_bypass $http_upgrade;}
```

A diretiva "proxy\_set\_header X-Forwarded-Proto https;" é usada para informar o servidor de destino (neste caso, o Django) que a conexão com o cliente foi feita através do protocolo HTTPS.

Quando o Nginx atua como um proxy reverso para o servidor de destino, ele se comunica com o servidor de destino usando o protocolo HTTP, mesmo que a conexão com o cliente seja feita através do protocolo HTTPS, lembra?

```
proxy_pass http://unix:/run/agenda.socket;
```

Isso pode causar problemas com certas funcionalidades do servidor de destino que dependem do protocolo da conexão (como a validação CSRF do Django).

Ao adicionar a diretiva "proxy\_set\_header X-Forwarded-Proto https;", o Nginx adiciona um cabeçalho HTTP "X-Forwarded-Proto" com o valor "https" à solicitação HTTP que envia ao servidor de destino. O servidor de destino (neste caso, o Django) pode usar esse cabeçalho para determinar se a conexão foi feita através do protocolo HTTPS e ajustar sua configuração e comportamento de acordo.

Em resumo, a diretiva "proxy\_set\_header X-Forwarded-Proto https;" ajuda a garantir que o servidor de destino esteja ciente de que a conexão com o cliente foi feita através do protocolo HTTPS, mesmo que a comunicação entre o Nginx e o servidor de destino seja feita através do protocolo HTTP.

**Passo a passo para corrigir o problema:**

**Observação importante:** se você copiou o arquivo nginx-https.txt final no nosso repositório, já fiz as alterações necessárias. Então você não precisa fazer isso.

**Passo 1:** para limpar o arquivo todo em /etc/nginx/sites-available/agendadomainssl, digite o comando abaixo.

```
echo | sudo tee /etc/nginx/sites-available/agendadomainssl
```

Agora o arquivo não terá mais nenhum conteúdo:

**Passo 2:** faça as alterações necessárias no arquivo nginx-https.txt (substitua as variáveis). Este arquivo está em recursos nessa mesma aula,

**Passo 3:** cole as alterações no arquivo que configuramos HTTPS nas aulas anteriores. Para isso abra o arquivo com o nano.

```
sudo nano /etc/nginx/sites-available/agendadomainssl
```

E é só colar seu novo conteúdo vindo do nginx-https.txt (recursos da aula).

CTRL + O (Salvar)  
CTRL + X (Sair)

**Passo 4:** reinicie tudo com os comandos abaixo.

```
sudo systemctl restart agendasudo systemctl restart nginx
```

Agora é só testar seus formulários.

**Outra observação:** adicionei mais alguns cabeçalhos que julguei úteis também.